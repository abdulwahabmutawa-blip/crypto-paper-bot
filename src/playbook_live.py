"""PLAYBOOK book — second Binance account, the Explosion Playbook stack.

BOOK ISOLATION IS THE PRIME DIRECTIVE. This module has its OWN keys
(PLAYBOOK_API_KEY / PLAYBOOK_API_SECRET), its OWN arming flag
(PLAYBOOK_LIVE=1), its OWN state (data/playbook_state.json) and ledger
(data/playbook_ledger.jsonl). It never imports account #1's signed-call
path; the only things borrowed from binance_live are PURE functions
(late_entry, fuel_verdict, book_floor_reason) that touch no keys and no
state. On the VPS each book runs as its own systemd service with its own
env file, so neither process ever even sees the other's secrets.

HARDENED 08-21 after a 15-agent adversarial review (12 confirmed findings,
5 critical) — every rule below exists because the review proved its absence
reachable:
  * ledger reconciliation every cycle (crash between fill and state save
    must never orphan a real position or leave a phantom seat);
  * unknown balances NEVER fire a sell (missing key defaults to 0.0, a
    failed account read skips the exit decision entirely);
  * disarming with a live position HOLDS it untouched — dry-run never
    mutates position state, in either direction;
  * rejected (definitive exchange error) vs unconfirmed (client timeout)
    orders are distinguished; unconfirmed BUYs are re-checked against the
    account before the seat is trusted either way;
  * climax/terminal-dip judge POST-ENTRY candles only, each folded once;
  * KILL_SWITCH file blocks every order, same as book #1;
  * min-notional guards on both legs; dust seats are closed as dust.

STRATEGY (distilled from trading-research/explosion_anatomy/
PLAYBOOK_2026-08-21.md; single-wave-week calibration, ~+11-15% median
capture per winner is the honest expectation):

ENTRY — gated trigger, never a bare threshold: wave regime on (fleet
breadth.json fresh+wave) → hygiene (24h qv >= $1M) → two consecutive
closed 1h candles each >= +4% on >= 3x pre-move median volume breaking the
prior 48h high → account #1's late-entry guard family. Budget 3/day +1 on
wave days; 3h per-coin cooldown; all-in USDT (percentages only).

EXIT — priority order, first trigger wins (the tape ends trades, not
clocks): 1 CLIMAX (red 1h close on move-max volume, lower-half close);
2 TERMINAL DIP (3h post-entry close drawdown >= 12% from high-water);
3 RATCHET (arm +10% MFE, floor = entry + 50% of peak gain); 4 FUEL GONE
(quiet fades); 5 STOP -6%; 6 TIME CAP 48h. Calendar-expiry exits are v2.

BOOK GUARDRAILS: drawdown floor (no entries below 62.5% of book peak),
sell only recorded units, unknown data never fires an order.

DRY RUN: with PLAYBOOK_LIVE != 1 the cycle scans, judges, and logs every
order it WOULD place as event "dry_run" — but posts nothing and mutates no
position state.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

import config
from binance_live import late_entry, fuel_verdict, book_floor_reason, \
    FUEL_MIN_CLOSED_H, climax_verdict, CLIMAX_FALLBACK_MULT  # noqa: F401
# climax_verdict lives in binance_live since 08-23 (owner promoted the
# climax exit to book #1 too; one pure-function home, two books share it)

KEY = "playbook"
STATE = config.DATA / "playbook_state.json"
LEDGER = config.DATA / "playbook_ledger.jsonl"
BREADTH = config.DATA / "breadth.json"
KILL_SWITCH = config.DATA / "KILL_SWITCH"

DATA_HOSTS = ("https://data-api.binance.vision", "https://api.binance.com")
TRADE_HOST = "https://api.binance.com"

# ---- strategy constants (playbook §6; single-wave-week calibration) --------
MIN_QV_24H = 1_000_000.0     # hygiene: thinner books printed unfillable wicks
TRIG_CLOSE_GAIN = 0.04
TRIG_VOL_SURGE = 3.0
TRIG_BREAK_H = 48
# CLIMAX_FALLBACK_MULT imported from binance_live (08-23)
TERMINAL_DIP = 0.12
RATCHET_ARM = 0.10
RATCHET_LOCK = 0.50
STOP_PCT = -0.06
MAX_HOLD_H = 48.0
BASE_ENTRIES = 3
WAVE_BONUS = 1
COOLDOWN_H = 3.0
MAX_CANDIDATES = 40
MIN_ORDER_USD = 10.0         # below this a BUY cannot pay for itself and
                             # Binance rejects sub-notional orders anyway
MIN_SELL_NOTIONAL = 5.0      # exchange minimum; below it the seat is DUST
PENDING_BUY_TTL_S = 1800     # unconfirmed BUY: recheck window before we
                             # conclude the order truly never happened

LAST_ERROR: dict = {}


# ---- own keys, own arming, own ledger — full isolation ---------------------
def _keys() -> tuple[str, str] | None:
    k = os.environ.get("PLAYBOOK_API_KEY", "").strip()
    s = os.environ.get("PLAYBOOK_API_SECRET", "").strip()
    return (k, s) if k and s else None


def armed() -> bool:
    """Live only when the owner set BOTH the keys and PLAYBOOK_LIVE=1."""
    return os.environ.get("PLAYBOOK_LIVE", "").strip() == "1" \
        and _keys() is not None


def log(entry: dict) -> None:
    entry = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             **entry}
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _public(path: str, params: dict | None = None) -> dict | list | None:
    """Unsigned market data; mirror-first. NEVER sends a key header."""
    qs = urllib.parse.urlencode(params or {})
    for host in DATA_HOSTS:
        try:
            return json.load(urllib.request.urlopen(
                f"{host}/api/v3{path}" + (f"?{qs}" if qs else ""),
                timeout=15))
        except Exception:
            continue
    return None


def _signed(method: str, path: str, params: dict | None = None
            ) -> dict | list | None:
    keys = _keys()
    if not keys:
        return None
    params = dict(params or {})
    params["timestamp"] = int(time.time() * 1000)
    params["recvWindow"] = 10_000
    qs = urllib.parse.urlencode(params)
    params["signature"] = hmac.new(keys[1].encode(), qs.encode(),
                                   hashlib.sha256).hexdigest()
    qs = urllib.parse.urlencode(params)
    url = f"{TRADE_HOST}/api/v3{path}" + (f"?{qs}" if method == "GET" else "")
    data = qs.encode() if method != "GET" else None
    req = urllib.request.Request(url, method=method, data=data,
                                 headers={"X-MBX-APIKEY": keys[0]})
    LAST_ERROR.clear()
    try:
        return json.load(urllib.request.urlopen(req, timeout=20))
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:200]
        try:
            parsed = json.loads(body)
            LAST_ERROR.update({"http": e.code, "code": parsed.get("code"),
                               "msg": parsed.get("msg", "")})
        except Exception:
            LAST_ERROR.update({"http": e.code, "code": None, "msg": body})
        print(f"[{KEY}] {method} {path} -> HTTP {e.code}: {body}")
        log({"event": "api_error", "path": path, "code": e.code,
             "body": body})
        return None
    except Exception as e:
        # network/timeout: the exchange MAY have accepted the request —
        # callers must treat this as UNKNOWN, never as "did not happen"
        LAST_ERROR.update({"http": None, "code": None, "msg": str(e)})
        print(f"[{KEY}] {method} {path} failed: {e}")
        return None


# ---- pure verdict functions (tested in tests/test_playbook_guards.py) ------
def terminal_dip_verdict(closes_3h: list[float], hwm: float) -> str | None:
    """Rule 2: 3h close drawdown >= 12% from high-water. Caller must pass
    POST-ENTRY closes only (review 08-21: pre-entry candles here judged the
    coin's past, not our position)."""
    if len(closes_3h) < 3 or not hwm or hwm <= 0:
        return None
    dd = min(closes_3h) / hwm - 1
    if dd <= -TERMINAL_DIP:
        return (f"TERMINAL DIP — {dd:.1%} off the high-water on closes: "
                f"82% of dips this deep were the top, not a shakeout")
    return None


def ratchet_floor(entry: float, hwm: float) -> float | None:
    """Rule 3: arms at +10% MFE; floor keeps 50% of the peak gain."""
    if not entry or not hwm or entry <= 0:
        return None
    gain = hwm / entry - 1
    if gain < RATCHET_ARM:
        return None
    return entry * (1 + gain * RATCHET_LOCK)


def sell_sizing(owned: float, free_balance: float | None) -> float:
    """How much a SELL may move: never more than recorded units, never on
    unknown data. A MISSING balance is 0.0, not `owned` (review 08-21
    critical: defaulting to owned let a sell fire on zero information and,
    after a crash window, liquidate the owner's personal holding)."""
    if owned <= 0 or free_balance is None:
        return 0.0
    return min(owned, free_balance)


def entry_trigger(kl: list) -> tuple[bool, str]:
    """Gate 3 on CLOSED 1h klines (>= 52 rows): two consecutive +4% closes
    on >=3x pre-move median volume, breaking the prior 48h high."""
    if not kl or len(kl) < 52:
        return False, "insufficient history"
    closes = [float(r[4]) for r in kl]
    highs = [float(r[2]) for r in kl]
    qvs = [float(r[7]) for r in kl]
    pre = sorted(qvs[:-2])[len(qvs[:-2]) // 2]
    g1 = closes[-1] / closes[-2] - 1
    g2 = closes[-2] / closes[-3] - 1
    if g1 < TRIG_CLOSE_GAIN or g2 < TRIG_CLOSE_GAIN:
        return False, "closes not consecutive +4%"
    if pre <= 0 or qvs[-1] < TRIG_VOL_SURGE * pre \
            or qvs[-2] < TRIG_VOL_SURGE * pre:
        return False, "volume not 3x pre-move median"
    if closes[-1] < max(highs[-(TRIG_BREAK_H + 2):-2]):
        return False, "did not break the prior 48h high"
    return True, "trigger met"


def wave_fresh() -> bool:
    """Market pulse gate; stale/missing breadth reads as no-wave (fails
    CLOSED for entries)."""
    try:
        bd = json.loads(BREADTH.read_text(encoding="utf-8"))
        hist = bd.get("history") or []
        fresh = hist and (datetime.now(timezone.utc) - datetime.fromisoformat(
            hist[-1]["ts"])).total_seconds() < 2700
        return bool(fresh and bd.get("wave"))
    except Exception:
        return False


def orders_blocked() -> str | None:
    """KILL_SWITCH parity with book #1: the owner's file stops every order
    on BOTH books (review 08-21: playbook ignored it entirely)."""
    if KILL_SWITCH.exists():
        return "KILL_SWITCH present — all orders blocked"
    return None


# ---- state -----------------------------------------------------------------
def _load() -> dict:
    st = {}
    if STATE.exists():
        try:
            st = json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            st = {}
    # normalize: a hand-restored file missing a key must never KeyError a
    # cycle mid-trade (review 08-21: direct indexing died AFTER the fill)
    st.setdefault("created",
                  datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    for k in ("held_symbol", "entry_price", "entry_time", "hwm",
              "book_hwm_usd", "wave_bonus_date", "pending_buy"):
        st.setdefault(k, None)
    st.setdefault("units", 0.0)
    st.setdefault("move_max_qv", 0.0)
    st.setdefault("move_qv_sum", 0.0)
    st.setdefault("move_qv_n", 0)
    st.setdefault("last_qv_ms", 0)
    st.setdefault("entries", {})
    st.setdefault("stopped", {})
    st.setdefault("realized", [])
    return st


def _save(st: dict) -> None:
    # prune unbounded dicts (review: state grew forever)
    cutoff = (datetime.now(timezone.utc).timestamp() - 14 * 86400)
    for d, parse in (("stopped", True), ("entries", False)):
        for k in list(st.get(d, {})):
            try:
                ts = datetime.fromisoformat(st[d][k]).timestamp() if parse \
                    else datetime.strptime(k, "%Y-%m-%d").timestamp()
                if ts < cutoff:
                    del st[d][k]
            except Exception:
                pass
    STATE.write_text(json.dumps(st, indent=1, sort_keys=True,
                                ensure_ascii=False),
                     encoding="utf-8", newline="\n")


def _price(sym: str) -> float | None:
    d = _public("/ticker/price", {"symbol": sym})
    try:
        return float(d["price"])
    except Exception:
        return None


def _balances() -> dict[str, float] | None:
    """None = UNREADABLE (skip decisions), {} = readable and empty.
    (Review 08-21 critical: conflating the two let sells fire blind.)"""
    acct = _signed("GET", "/account")
    if not isinstance(acct, dict) or "balances" not in acct:
        return None
    out = {}
    for b in acct.get("balances", []):
        try:
            free = float(b.get("free", 0) or 0)
        except Exception:
            free = 0.0
        if free > 0:
            out[b["asset"]] = free
    return out


def _ledger_tail(n: int = 500) -> list[dict]:
    if not LEDGER.exists():
        return []
    rows = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines()[-n:]:
        if line.strip():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def reconcile(st: dict, bals: dict[str, float] | None) -> None:
    """Crash-window healing, the lesson book #1 paid for (review 08-21
    critical: without this, a death between fill and state-save orphans a
    real position forever, and a stale seat double-sells).

    1. PHANTOM SEAT: state says held, but the ledger's latest event for
       that symbol is a SELL fill/exit -> clear the seat.
    2. ORPHANED BUY: state flat, but the ledger shows a BUY fill with no
       later SELL fill/exit for that symbol -> restore the seat from the
       fill row (price, qty, ts).
    3. UNCONFIRMED BUY: an order POST timed out client-side (no fill row,
       no rejection code). If the base asset now shows in balances, adopt
       the position at the recorded intent; if it never appears within the
       TTL, conclude the order really didn't happen and clear the flag.
    """
    rows = [r for r in _ledger_tail() if r.get("event") in
            ("fill", "exit")]

    def last_open_buy() -> dict | None:
        open_buy = None
        for r in rows:
            if r.get("event") == "fill" and r.get("action") == "BUY":
                open_buy = r
            elif open_buy and r.get("symbol") == open_buy.get("symbol") \
                    and (r.get("event") == "exit"
                         or (r.get("event") == "fill"
                             and r.get("action") == "SELL")):
                open_buy = None
        return open_buy

    ob = last_open_buy()
    if st.get("held_symbol"):
        sym = st["held_symbol"]
        if not ob or ob.get("symbol") != sym:
            log({"event": "reconciled_phantom_seat", "symbol": sym,
                 "note": "ledger says this seat was already sold; state "
                         "file was stale (crash window)"})
            print(f"[{KEY}] RECONCILED: clearing stale seat {sym}")
            for k in ("held_symbol", "entry_price", "entry_time", "hwm"):
                st[k] = None
            st["units"] = 0.0
            st["move_max_qv"] = st["move_qv_sum"] = 0.0
            st["move_qv_n"] = 0
            st["last_qv_ms"] = 0
    if not st.get("held_symbol") and ob:
        st["held_symbol"] = ob["symbol"]
        st["entry_price"] = ob.get("price")
        st["units"] = float(ob.get("qty") or 0.0)
        st["entry_time"] = ob.get("ts")
        st["hwm"] = ob.get("price")
        st["move_max_qv"] = st["move_qv_sum"] = 0.0
        st["move_qv_n"] = 0
        st["last_qv_ms"] = 0
        log({"event": "recovered_from_ledger", "symbol": ob["symbol"],
             "units": st["units"]})
        print(f"[{KEY}] recovered unfinished seat {ob['symbol']} from ledger")

    pb = st.get("pending_buy")
    if pb and not st.get("held_symbol"):
        base = str(pb.get("symbol", ""))[:-4]
        age = None
        try:
            age = (datetime.now(timezone.utc)
                   - datetime.fromisoformat(pb["ts"])).total_seconds()
        except Exception:
            age = PENDING_BUY_TTL_S + 1
        if bals is not None and bals.get(base, 0.0) > 0:
            p = _price(pb["symbol"])
            if p:
                st["held_symbol"] = pb["symbol"]
                st["entry_price"] = p     # honest approximation, flagged
                st["units"] = bals[base]
                st["entry_time"] = pb.get("ts")
                st["hwm"] = p
                st["pending_buy"] = None
                log({"event": "adopted_unconfirmed_buy",
                     "symbol": pb["symbol"], "units": bals[base],
                     "note": "POST timed out but the coins arrived; entry "
                             "price approximated at adoption"})
                print(f"[{KEY}] adopted unconfirmed BUY {pb['symbol']}")
        elif age > PENDING_BUY_TTL_S:
            st["pending_buy"] = None
            log({"event": "pending_buy_expired", "symbol": pb.get("symbol"),
                 "note": "order never appeared in balances — treating the "
                         "timed-out POST as not executed"})
    elif pb and st.get("held_symbol"):
        st["pending_buy"] = None


def _order(action: str, symbol: str, quote_qty: float | None = None,
           qty: float | None = None, st: dict | None = None) -> dict | None:
    """One market order — or a dry-run log line when not armed. Inert-by-
    default enforced HERE (defense in depth, same as account #1)."""
    blocked = orders_blocked()
    if blocked:
        log({"event": "refused", "action": action, "symbol": symbol,
             "reason": blocked})
        print(f"[{KEY}] {blocked}")
        return None
    if not armed():
        log({"event": "dry_run", "action": action, "symbol": symbol,
             "quote_qty": quote_qty, "qty": qty,
             "note": "PLAYBOOK_LIVE != 1 — no order sent"})
        print(f"[{KEY}] DRY RUN: would {action} {symbol} "
              f"({quote_qty or qty})")
        return None
    params = {"symbol": symbol, "side": action, "type": "MARKET"}
    if action == "BUY":
        # floor to the cent (book #1 lesson: rounding up got -2010 x5)
        params["quoteOrderQty"] = f"{int((quote_qty or 0.0) * 100) / 100:.2f}"
    else:
        params["quantity"] = f"{qty:.8f}".rstrip("0").rstrip(".")
    resp = _signed("POST", "/order", params)
    if resp is None:
        if LAST_ERROR.get("code") is not None:
            # definitive exchange rejection: the order did NOT happen
            log({"event": "order_rejected", "action": action,
                 "symbol": symbol, "code": LAST_ERROR.get("code"),
                 "msg": LAST_ERROR.get("msg", "")[:120]})
        else:
            # client-side timeout: UNKNOWN — the exchange may have filled
            # it. Flag for reconcile(); never assume either way.
            log({"event": "order_unconfirmed", "action": action,
                 "symbol": symbol})
            if action == "BUY" and st is not None:
                st["pending_buy"] = {
                    "symbol": symbol,
                    "ts": datetime.now(timezone.utc).isoformat(
                        timespec="seconds")}
        return None
    if not resp.get("fills"):
        log({"event": "order_no_fills", "action": action, "symbol": symbol})
        return None
    fills = resp["fills"]
    q = sum(float(f["qty"]) for f in fills)
    px = sum(float(f["price"]) * float(f["qty"]) for f in fills) / q
    log({"event": "fill", "action": action, "symbol": symbol,
         "price": px, "qty": q, "order_id": str(resp.get("orderId", "")),
         "commission": sum(float(f.get("commission", 0)) for f in fills),
         "commission_asset": (fills[0].get("commissionAsset") if fills
                              else None)})
    return {"price": px, "qty": q}


# ---- the cycle -------------------------------------------------------------
def _exit_position(st: dict, now: datetime,
                   bals: dict[str, float] | None) -> None:
    held = st.get("held_symbol")
    entry = st.get("entry_price")
    if not held or not entry:
        return
    if not armed():
        # a REAL position while disarmed is held untouched — dry-run must
        # never mutate position state (review 08-21 critical: the old path
        # wiped a live seat from state the first time a verdict fired)
        print(f"[{KEY}] disarmed with open position {held} — holding "
              f"untouched; re-arm to manage it")
        return
    entry_ms = None
    try:
        entry_ms = int(datetime.fromisoformat(
            st["entry_time"]).timestamp() * 1000)
    except Exception:
        pass
    kl = _public("/klines", {"symbol": held, "interval": "1h", "limit": 56})
    p = _price(held)
    if not kl or not p or not entry_ms:
        return                             # unknown data never fires a sell
    now_ms = time.time() * 1000
    # POST-ENTRY closed candles only (review: pre-entry candles judged the
    # coin's past, not our position), each folded exactly once
    move = [r for r in kl
            if float(r[6]) < now_ms and float(r[0]) >= entry_ms]
    prior_max = float(st.get("move_max_qv") or 0.0)
    prior_avg = (float(st.get("move_qv_sum") or 0.0)
                 / st["move_qv_n"]) if st.get("move_qv_n") else 0.0
    fresh = [r for r in move if float(r[0]) > float(st.get("last_qv_ms")
                                                    or 0)]
    st["hwm"] = max(float(st.get("hwm") or p), p)
    hwm = st["hwm"]
    held_h = (now_ms - entry_ms) / 3.6e6
    avg_qv = prior_avg

    why = None
    if fresh:
        # judge the newest candle against statistics that EXCLUDE it
        newest = fresh[-1]
        stats_max, stats_sum, stats_n = prior_max, \
            float(st.get("move_qv_sum") or 0.0), int(st.get("move_qv_n")
                                                     or 0)
        for r in fresh[:-1]:
            qv = float(r[7])
            stats_max = max(stats_max, qv)
            stats_sum += qv
            stats_n += 1
        stats_avg = (stats_sum / stats_n) if stats_n else 0.0
        if stats_n >= 1:
            why = climax_verdict(newest, stats_max, stats_avg)
        # fold everything (including the newest) exactly once
        for r in fresh:
            qv = float(r[7])
            st["move_max_qv"] = max(float(st.get("move_max_qv") or 0.0), qv)
            st["move_qv_sum"] = float(st.get("move_qv_sum") or 0.0) + qv
            st["move_qv_n"] = int(st.get("move_qv_n") or 0) + 1
        st["last_qv_ms"] = int(float(fresh[-1][0]))
        avg_qv = (st["move_qv_sum"] / st["move_qv_n"]) if st["move_qv_n"] \
            else 0.0
    if not why:
        why = terminal_dip_verdict([float(r[4]) for r in move[-3:]], hwm)
    if not why:
        floor = ratchet_floor(entry, hwm)
        if floor and p <= floor:
            why = (f"RATCHET ({p / entry - 1:+.1%} vs peak "
                   f"{hwm / entry - 1:+.1%}) — keeps half the peak gain")
    if not why and held_h >= FUEL_MIN_CLOSED_H and len(move) >= \
            FUEL_MIN_CLOSED_H:
        before = [float(r[7]) for r in kl if float(r[6]) <= entry_ms]
        surge = None
        if len(before) >= 6:
            base_qv = sorted(before)[len(before) // 2]
            surge = (float(move[-1][7]) / base_qv) if base_qv > 0 else None
        why = fuel_verdict(surge, p / entry - 1, wave_fresh())
    if not why and p / entry - 1 <= STOP_PCT:
        why = f"STOP ({p / entry - 1:.1%} from entry)"
    if not why and held_h >= MAX_HOLD_H:
        why = f"MAX HOLD ({held_h:.0f}h) — safety net, tape should have fired"
    if not why:
        return

    if bals is None:
        # exchange account unreadable: deciding to sell on zero information
        # is exactly what the review banned. Try again next cycle.
        log({"event": "exit_deferred", "symbol": held, "reason": why[:60],
             "note": "balances unreadable — no order on unknown data"})
        print(f"[{KEY}] exit wanted ({why[:40]}) but balances unreadable — "
              f"deferred")
        return
    base = held[:-4]
    sellable = sell_sizing(float(st.get("units") or 0.0),
                           bals.get(base, 0.0))
    info = _public("/exchangeInfo", {"symbol": held})
    step = min_qty = 0.0
    for f in ((info or {}).get("symbols") or [{}])[0].get("filters", []):
        if f.get("filterType") == "LOT_SIZE":
            step = float(f.get("stepSize", 0) or 0)
            min_qty = float(f.get("minQty", 0) or 0)
    qty = int(sellable / step) * step if step > 0 else sellable
    if qty <= 0 or qty < min_qty or qty * p < MIN_SELL_NOTIONAL:
        # nothing sellable at exchange minimums: the seat is DUST. Close it
        # in the books rather than looping a doomed sell forever.
        log({"event": "dust_closed", "symbol": held,
             "units": st.get("units"), "value_usd": round(qty * p, 4),
             "reason": why[:80]})
        print(f"[{KEY}] {held} seat is dust (${qty * p:.2f}) — closed in "
              f"the books")
        st["stopped"][held] = now.isoformat(timespec="seconds")
        for k in ("held_symbol", "entry_price", "entry_time", "hwm"):
            st[k] = None
        st["units"] = 0.0
        st["move_max_qv"] = st["move_qv_sum"] = 0.0
        st["move_qv_n"] = 0
        st["last_qv_ms"] = 0
        return
    fill = _order("SELL", held, qty=qty, st=st)
    if not fill:
        return          # rejection/timeout logged; state untouched, retry
    exit_px = fill["price"]
    got = exit_px * fill["qty"]
    spent = entry * fill["qty"]
    rec = {"symbol": held, "source": "playbook",
           "entry_time": st.get("entry_time"),
           "exit_time": now.isoformat(timespec="seconds"),
           "entry_price": entry, "exit_price": exit_px,
           "units": round(fill["qty"], 8),
           "pnl_pct": round((exit_px / entry - 1) * 100, 2),
           "pnl_usd": round(got - spent, 4),
           "reason": why, "date": now.strftime("%Y-%m-%d")}
    st["realized"].append(rec)
    log({"event": "exit", "symbol": held, "reason": why,
         "pnl_pct": rec["pnl_pct"], "pnl_usd": rec["pnl_usd"]})
    print(f"[{KEY}] EXIT {held} {rec['pnl_pct']:+.2f}% — {why[:60]}")
    st["stopped"][held] = now.isoformat(timespec="seconds")
    for k in ("held_symbol", "entry_price", "entry_time", "hwm"):
        st[k] = None
    st["units"] = 0.0
    st["move_max_qv"] = st["move_qv_sum"] = 0.0
    st["move_qv_n"] = 0
    st["last_qv_ms"] = 0


def _try_enter(st: dict, now: datetime,
               bals: dict[str, float] | None) -> None:
    today = now.strftime("%Y-%m-%d")
    wave = wave_fresh()
    if wave and st.get("wave_bonus_date") != today:
        st["wave_bonus_date"] = today
        print(f"[{KEY}] WAVE DAY — entry budget +1")
    budget = BASE_ENTRIES + (WAVE_BONUS if st.get("wave_bonus_date") == today
                             else 0)
    if st.get("entries", {}).get(today, 0) >= budget:
        return
    if not wave:
        return          # v1 hunts wave-beta only; calendar class is v2
    if st.get("held_symbol") or st.get("pending_buy"):
        return          # one seat; never stack on an unconfirmed order
    if armed():
        if bals is None:
            print(f"[{KEY}] balances unreadable — no entries this cycle")
            return
        spend = bals.get("USDT", 0.0)
        if spend < MIN_ORDER_USD:
            # sub-notional buys are doomed -1013s (review: zero-spend BUY)
            return
        val = spend
        if val > 0:
            st["book_hwm_usd"] = round(
                max(float(st.get("book_hwm_usd") or 0.0), val), 4)
        floor_why = book_floor_reason(val, st.get("book_hwm_usd"))
        if floor_why:
            log({"event": "floor", "reason": floor_why})
            return
    else:
        spend = 0.0

    tickers = _public("/ticker/24hr") or []
    cands = []
    for t in tickers:
        sym = t.get("symbol", "")
        if not sym.endswith("USDT"):
            continue
        try:
            qv = float(t.get("quoteVolume", 0))
            chg = float(t.get("priceChangePercent", 0))
        except Exception:
            continue
        if qv < MIN_QV_24H:
            continue                      # hygiene
        cands.append((chg, sym))
    cands.sort(reverse=True)

    dry_logged = False
    for _chg, sym in cands[:MAX_CANDIDATES]:
        if st.get("held_symbol") or st.get("pending_buy"):
            break
        cool = st.get("stopped", {}).get(sym)
        if cool:
            try:
                if (now - datetime.fromisoformat(cool)
                        ).total_seconds() < COOLDOWN_H * 3600:
                    continue
            except Exception:
                continue    # corrupt timestamp: fail toward still-cooling
        kl = _public("/klines", {"symbol": sym, "interval": "1h",
                                 "limit": 56})
        now_ms = time.time() * 1000
        closed = [r for r in (kl or []) if float(r[6]) < now_ms]
        ok, _note = entry_trigger(closed)
        if not ok:
            continue
        t24 = _public("/ticker/24hr", {"symbol": sym})
        k5 = _public("/klines", {"symbol": sym, "interval": "5m",
                                 "limit": 24})
        runup = rng = chg1 = dd2 = None
        try:
            last, low, high = (float(t24["lastPrice"]),
                               float(t24["lowPrice"]),
                               float(t24["highPrice"]))
            if low > 0:
                runup, rng = last / low - 1, high / low - 1
            c5 = [float(r[4]) for r in k5]
            h5 = [float(r[2]) for r in k5]
            if len(c5) >= 13:
                chg1 = c5[-1] / c5[-13] - 1
            if max(h5) > 0:
                dd2 = c5[-1] / max(h5) - 1
        except Exception:
            pass
        guard = late_entry(runup, chg1, dd2, rng)
        if guard:
            log({"event": "refused", "symbol": sym, "reason": guard})
            print(f"[{KEY}] refused {sym}: {guard[:60]}")
            continue
        fill = _order("BUY", sym, quote_qty=spend, st=st)
        if fill:
            st["held_symbol"] = sym
            st["entry_price"] = fill["price"]
            st["units"] = fill["qty"]
            st["entry_time"] = now.isoformat(timespec="seconds")
            st["hwm"] = fill["price"]
            st["move_max_qv"] = st["move_qv_sum"] = 0.0
            st["move_qv_n"] = 0
            st["last_qv_ms"] = 0
            st.setdefault("entries", {})[today] = \
                st.get("entries", {}).get(today, 0) + 1
            print(f"[{KEY}] ENTER {sym} @ {fill['price']:.8g}")
        elif not armed() and not dry_logged:
            # dry run: count at most ONE intended entry per cycle-day so
            # the budget stays realistic without burning 4 slots before
            # breakfast (review: once per 5-min cycle drained the budget)
            if st.get("entries", {}).get(today, 0) < budget:
                st.setdefault("entries", {})[today] = \
                    st.get("entries", {}).get(today, 0) + 1
            dry_logged = True
            break
        elif st.get("pending_buy"):
            break          # unknown outcome: reconcile owns the next step


def run() -> None:
    now = datetime.now(timezone.utc)
    st = _load()
    mode = "LIVE" if armed() else "DRY RUN"
    print(f"[{KEY}] cycle {now.isoformat(timespec='seconds')} [{mode}]")
    bals = _balances() if armed() else None
    if armed():
        reconcile(st, bals)
        _save(st)          # persist any healing before trading on it
    _exit_position(st, now, bals)
    _try_enter(st, now, bals)
    _save(st)


if __name__ == "__main__":
    run()
