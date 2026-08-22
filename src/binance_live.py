"""Binance MAINNET adapter — LOTTERY BOOK ONLY. Real money.

This is the deliberate, reviewed mainnet module that binance_broker.py's
testnet lock pointed to — built 2026-08-15 for the owner's sacrificial
lottery book.

  * NO BOOK CAP (owner decision 2026-08-16): every BUY spends the account's
    full free USDT balance. The original hard-coded $20 ceiling has been
    removed on purpose — read the git history for `BOOK_CAP_USD` if you
    need the old, capped behavior back. Whatever real USDT sits in this
    account is what the lottery bot will risk.
  * ARMING is a double deliberate act by the OWNER, never default-on:
    repo secrets BINANCE_LIVE_API_KEY / BINANCE_LIVE_API_SECRET, AND repo
    variable LOTTERY_LIVE="1". Missing either -> inert no-op.
  * Key hygiene (owner-side, documented in BINANCE_LOTTERY_SETUP.md):
    spot-trade-only API key, WITHDRAWALS DISABLED. A leaked trade-only key
    can lose the full USDT balance on bad trades; it cannot withdraw.
  * KILL SWITCH: the same data/KILL_SWITCH file live_guard honors blocks
    every mainnet order here too.
  * Every order and every refusal is appended to data/lottery_ledger.jsonl
    (committed by the loop) — the book's full honest history.

Expected outcome, stated where it can't be unseen: the documented base rate
for small-account pump-chasing is loss of principal. This module makes the
attempt honest and auditable — it does not make it a good idea.
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

HOST = "https://api.binance.com"
BASE = HOST + "/api"          # spot trading endpoints (/v3/...)
# key-permission endpoints live under /sapi and are passed as full paths
MIN_ORDER_USDT = 5.0          # Binance spot minimum notional (typical pairs)
LEDGER = config.DATA / "lottery_ledger.jsonl"
KILL_SWITCH = config.DATA / "KILL_SWITCH"

# Last API error, so callers can diagnose precisely instead of guessing.
# Binance's error codes are specific and each points at a different fix;
# a generic "check your key or IP" message sent the first real setup
# chasing the wrong problem.
LAST_ERROR: dict = {}


def _keys() -> tuple[str, str] | None:
    k = os.environ.get("BINANCE_LIVE_API_KEY", "").strip()
    s = os.environ.get("BINANCE_LIVE_API_SECRET", "").strip()
    return (k, s) if k and s else None


def armed() -> bool:
    """Live only when the owner set BOTH the keys and LOTTERY_LIVE=1."""
    return os.environ.get("LOTTERY_LIVE", "").strip() == "1" and _keys() is not None


def log(entry: dict) -> None:
    entry = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             **entry}
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def _call(method: str, path: str, params: dict | None = None,
          signed: bool = False) -> dict | list | None:
    keys = _keys()
    if signed and not keys:
        return None
    params = dict(params or {})
    headers = {"X-MBX-APIKEY": keys[0]} if keys else {}
    if signed:
        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 10_000
        qs = urllib.parse.urlencode(params)
        params["signature"] = hmac.new(keys[1].encode(), qs.encode(),
                                       hashlib.sha256).hexdigest()
    qs = urllib.parse.urlencode(params)
    root = HOST if path.startswith("/sapi") else BASE
    url = f"{root}{path}" + (f"?{qs}" if qs and method == "GET" else "")
    data = qs.encode() if method != "GET" and qs else None
    req = urllib.request.Request(url, method=method, data=data, headers=headers)
    try:
        return json.load(urllib.request.urlopen(req, timeout=20))
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:200]
        try:
            parsed = json.loads(body)
            LAST_ERROR.clear()
            LAST_ERROR.update({"http": e.code, "code": parsed.get("code"),
                               "msg": parsed.get("msg", "")})
        except Exception:
            LAST_ERROR.clear()
            LAST_ERROR.update({"http": e.code, "code": None, "msg": body})
        print(f"[lottery-live] {method} {path} -> HTTP {e.code}: {body}")
        log({"event": "api_error", "path": path, "code": e.code, "body": body})
        return None
    except Exception as e:
        print(f"[lottery-live] {method} {path} failed: {e}")
        return None


def balances() -> dict[str, float]:
    """{'USDT': 11.0, 'PEPE': 12345.0, ...} free balances > 0."""
    acct = _call("GET", "/v3/account", signed=True)
    out = {}
    for b in (acct or {}).get("balances", []):
        free = float(b.get("free", 0) or 0)
        if free > 0:
            out[b["asset"]] = free
    return out


def balances_valuation(held_symbol: str | None) -> dict[str, float]:
    """Free balances, PLUS the locked units of the held seat's base asset.
    VALUATION ONLY -- never feed this to a sell path, which may only ever
    spend free balance.

    Exists because balances() is free-only: the moment a protective stop
    rests on the exchange it locks the position's units, they vanish from
    free, and managed_value() prices the seat at $0 -- a phantom -100% that
    trips book_floor_reason and freezes entries on a book that never lost
    anything.

    Only the held base asset picks up its locked side, never USDT and never
    the owner's other 22 assets: this account is shared, and their own
    resting orders lock quote and base balances that are none of the book's
    business. The bot's own protective stop locks exactly one thing -- the
    seat it is protecting -- so that is exactly what this restores.
    """
    acct = _call("GET", "/v3/account", signed=True)
    if not acct:
        return {}
    base = held_symbol[:-4] if held_symbol else None
    out: dict[str, float] = {}
    for b in (acct or {}).get("balances", []):
        asset = b.get("asset")
        free = float(b.get("free", 0) or 0)
        val = free + (float(b.get("locked", 0) or 0) if asset == base else 0.0)
        if val > 0:
            out[asset] = val
    return out


def price(symbol: str) -> float | None:
    d = _call("GET", "/v3/ticker/price", {"symbol": symbol})
    try:
        return float(d["price"])
    except Exception:
        return None


def managed_value(bals: dict[str, float], held_symbol: str | None,
                  units: float | None = None) -> float:
    """Free USDT + the value of the units THIS BOT holds. `units` matters on
    an account that also holds the owner's own coins: valuing the whole free
    balance of the same asset would count their holdings as the bot's book."""
    v = bals.get("USDT", 0.0)
    if held_symbol:
        base = held_symbol[:-4]
        qty = bals.get(base, 0.0) if units is None else min(units, bals.get(base, 0.0))
        if qty > 0:
            p = price(held_symbol)
            if p:
                v += qty * p
    return v


def guard(action: str, symbol: str, bals: dict, held_symbol: str | None,
          units: float | None = None) -> str | None:
    """Returns a refusal reason, or None = clear to proceed."""
    if KILL_SWITCH.exists():
        return "KILL SWITCH file present"
    if action == "BUY" and bals.get("USDT", 0.0) < MIN_ORDER_USDT:
        return (f"DUST — free USDT ${bals.get('USDT', 0.0):.2f} below the "
                f"${MIN_ORDER_USDT:.0f} exchange minimum; book effectively "
                f"burned, nothing to do")
    return None


# ---- repeat-loser memory (trade autopsy 2026-08-22) -------------------------
# st["stopped"] is a 3-HOUR COOLDOWN, not a memory: nothing in the book ever
# remembered that a coin had already taken money. CHIPUSDT was bought five
# separate times over five days -- four losses, net -$5.72, 73% of the book's
# entire drawdown -- because each re-entry looked fresh to the scanner.
#
# What this rule can and cannot do: it engages only AFTER a symbol has proved
# itself, so it never prevents the first loss, and on CHIP the first two were
# the big ones. Replayed on the real 23-trade tape it recovers +$2.25, not
# the -$5.72 headline. Worth having as a guard; not a fix for the drawdown.
#
# Threshold is a FRACTION of the book's high-water value, never a dollar
# amount -- same discipline as BOOK_FLOOR_FRAC (owner decision 2026-08-21:
# "amount of money should not matter"), so it rescales when the owner
# deposits. 0.05 sits mid-plateau: 3%, 5% and 8% all recover the same +$2.25
# on the tape and only 10% degrades it, so the number is not knife-edge fitted.
REPEAT_LOSS_FRAC = 0.05   # a symbol that has cost 5% of the book is retired
REPEAT_LOSS_MAX = 2       # ...as is one that has lost this many round trips


def retired_symbols(realized: list[dict] | None,
                    hwm_usd: float | None) -> dict[str, str]:
    """Symbols this book has stopped paying to re-learn, with the reason.

    Retirement is for the life of the experiment, not a cooldown: the point
    is that the coin has already answered the question. Cleared only by the
    owner editing state, which is deliberate -- an automatic expiry would
    reopen the exact door CHIP walked through five times.
    """
    out: dict[str, str] = {}
    if not realized:
        return out
    losses: dict[str, int] = {}
    cum: dict[str, float] = {}
    for t in realized:
        sym = t.get("symbol")
        pnl = t.get("pnl_usd")
        if not sym or pnl is None:
            continue
        pnl = float(pnl)
        cum[sym] = cum.get(sym, 0.0) + pnl
        if pnl < 0:
            losses[sym] = losses.get(sym, 0) + 1
    # A missing/zero high-water mark disables only the fraction test; the
    # count test still stands, so an unreadable book value cannot silently
    # switch the whole guard off.
    line = -REPEAT_LOSS_FRAC * hwm_usd if hwm_usd else None
    for sym in set(losses) | set(cum):
        n, c = losses.get(sym, 0), cum.get(sym, 0.0)
        if line is not None and c <= line:
            out[sym] = (f"RETIRED — has cost this book ${-c:.2f}, past "
                        f"{REPEAT_LOSS_FRAC:.0%} of its ${hwm_usd:.2f} peak; "
                        f"it has already answered the question")
        elif n >= REPEAT_LOSS_MAX:
            out[sym] = (f"RETIRED — {n} losing round trips "
                        f"(net ${c:+.2f}); it has already answered the question")
    return out


# ---- late-entry guard (trade autopsy 2026-08-16, all 4 real trades) ---------
# The book's only real losses were LATE entries into already-run hype, both
# from the WATCHER path, which had no price checks at all: COW bought +37%
# into its day, NINE HOURS after its local top, falling -2.3%/h at entry
# (-11.2%); CHIP bought +28% into its day AT the local top (-7.8% within
# 90min). Grok's "euphoric" is inherently trailing — crowd noise peaks after
# price — so lateness must be enforced mechanically at the moment of
# purchase, for EVERY source. The scout's paper record agrees: REDUSDT +27%
# on the day at entry, -18.8% after.
MAX_RUNUP_24H_AT_ENTRY = 0.15  # [EVIDENCE] measured from the 24h LOW, not
                               # close-to-close: CHIP's second entry (15:30)
                               # dodged a close-to-close cap because the
                               # price FALLING after the pump shrank the day
                               # change — exactly when the coin was most
                               # spent. Run-up from the low doesn't decay:
                               # COW +37.6%, CHIP +29.2% then +27% — all
                               # losers, all refused. LINK +8.0% — the one
                               # winner — passes.
                               # TIGHTENED 0.25 -> 0.15 (owner-directed
                               # post-mortem 08-20, all 18 real trades vs
                               # their actual price paths): every entry
                               # >15% off its 24h low lost money except
                               # EDEN — the seven of them total -$9.13 —
                               # while the nine entries <=10% off the low
                               # total +$1.16. ACE +24.6% and GPS +23.5%
                               # slid UNDER the old 25% cap and delivered
                               # -$3.05 and a +9% post-exit rebound we
                               # sold into. The "sold too early" trades
                               # the owner flagged were these same seats:
                               # bought spent moves, shaken out on the
                               # pullback, coin bounced after. Late entry
                               # was the disease; early exit the symptom.
MIN_CHG_1H_AT_ENTRY = 0.0      # [EVIDENCE] COW was FALLING at entry
                               # (-2.3%/1h). An explosion's current hour is
                               # green; buying a red hour is riding down.
                               # Kept at 0.0, not higher: a genuinely early
                               # (ignition-style) entry has a flat hour by
                               # definition, and the run-up cap above does
                               # the heavy lifting.
MAX_DRAWDOWN_2H = -0.04        # [EVIDENCE — 08-17 CHIP] chg_1h compares two
                               # ENDPOINTS of a rolling window, so a crash
                               # bar simply ages out of it. The guard
                               # refused CHIP three times as it fell
                               # (-7.8%, -6.6%, -5.9%) and then bought it at
                               # 09:21 when the drop rolled past the 60-min
                               # edge — the coin had not recovered, the
                               # measurement just stopped seeing the fall.
                               # Distance below the recent HIGH has no such
                               # cliff: it decays gradually instead of
                               # flipping. CHIP was -7.6% below its 2h high
                               # at that entry; the two trades that were
                               # process-correct sat at -0.9% and -0.2%.
MIN_RANGE_24H_AT_ENTRY = 0.05  # [EVIDENCE — 08-17 LTC] a round trip costs
                               # ~0.2% in fees plus spread, and a burst seat
                               # is closed within 8h. LTC was bought with a
                               # 1.67% 24h range: even a perfect exit could
                               # not pay for the trade, and it closed -$0.06
                               # on a 2h stall. The other two entries had
                               # 20.2% and 10.3% of room. This is a
                               # necessary condition, not a sufficient one.


# ---- owner-accepted finish lines and wave rule (2026-08-20) -----------------
# Pre-committed by the owner at the 08-20 review, so that 2am after a red
# candle never gets to decide:
#   * FLOOR: if the book's managed value is below $25, NO new entries — the
#     experiment stops and gets a full post-mortem instead of a slow bleed.
#     Exits still run: a floor breach must never trap an open seat.
#   * WAVE BONUS: a breadth wave-day grants ONE extra daily entry. The
#     08-20 wave found the budget already spent on scratch trades hours
#     before breadth fired; explosions cluster on wave days (64% within a
#     day of a mass-trough in the 2y study), so the scarcest resource must
#     not be exhaustible by the quietest hours. Pre-registered at the
#     review, not invented mid-wave.
# PERCENTAGE FLOOR (owner decision 2026-08-21, replaces BOOK_FLOOR_USD=25):
# "amount of money should not matter — we are focusing on creating a
# successful strategy." The $25 line was $25-of-$40 = a 37.5% max drawdown
# in disguise, and it silently loosened every time the owner deposited
# (at $80 of capital the same $25 meant tolerating -69%). The floor is now
# expressed as what it always meant: a maximum drawdown from the book's
# high-water value. Deposits raise the high-water mark naturally, so the
# guardrail rescales itself and NO rule in this system references a dollar
# amount any more. 0.625 = the original 25/40 ratio, unchanged protection.
BOOK_FLOOR_FRAC = 0.625      # no entries below 62.5% of the book's peak
BASE_ENTRIES_PER_DAY = 3
WAVE_BONUS_ENTRIES = 1


def book_floor_reason(value_usd: float | None,
                      hwm_usd: float | None) -> str | None:
    """Refusal reason when the owner's pre-committed drawdown floor is
    breached: value below BOOK_FLOOR_FRAC of the book's high-water value."""
    if value_usd is None or not hwm_usd:
        return None          # unknown value must not halt the book by itself
    line = hwm_usd * BOOK_FLOOR_FRAC
    if value_usd < line:
        return (f"BOOK FLOOR — value ${value_usd:.2f} is below "
                f"{BOOK_FLOOR_FRAC:.1%} of the book's ${hwm_usd:.2f} peak "
                f"(line ${line:.2f}, drawdown "
                f"{value_usd / hwm_usd - 1:.1%}): no new entries; "
                f"post-mortem due")
    return None


def entry_budget(wave_active_today: bool) -> int:
    """Daily entry allowance: base, plus one on a breadth wave-day."""
    return BASE_ENTRIES_PER_DAY + (WAVE_BONUS_ENTRIES if wave_active_today
                                   else 0)


def exit_params(source: str | None) -> dict:
    """Seat policy by entry source — the explosion study (08-16, n=109)
    split the prey into species with incompatible clocks:

      hype spikes  — fast, half-life measured in hours: 24h max hold,
                     6h stall. (Watcher/heat/adopted seats.)
      scout bursts — volume events that resolve in minutes-to-hours:
                     8h max, 2h stall, tighter stop.
      grinds       — the study's actual money: median 11 DAYS trough to
                     peak, 67/109 took 10+. A 24h clock structurally
                     cannot hold one; the old exits would have force-sold
                     every grind on day one. 14d max hold, NO stall clock
                     (a grind's early days LOOK stalled by design), the
                     trailing stop is the primary exit.
    """
    src = source or ""
    # momentum_exit: does this seat die when the coin is no longer a top-25
    # 24h mover? ONLY for seats whose entry thesis WAS 24h leadership (the
    # legacy gainer path and adopted/recovered seats of unknown thesis).
    # BUG FIX 2026-08-20: scout:breakout was on this list, but the entry
    # guard demands a coin that has NOT already run far — so breakout seats
    # almost never rank top-25 and were being bought and ejected 6 minutes
    # later (ASTER -1.09%, CHIP -0.67%, both same morning): a structural
    # buy-high-sell-lower machine. A breakout seat's thesis is a fresh
    # intraday event; it is judged by its own burst clocks, stops and the
    # ratchet, not by daily leaderboards.
    momentum_exit = src in ("gainer", "adopted")
    if src == "scout:revival":
        # 28d: the 2y study (n=1,908) put the MEDIAN grind at 26 days
        # trough->peak — the first 14d cap would still have amputated
        # half the winners it was built to hold
        return {"kind": "grind", "stop_pct": -0.10, "stall_h": None,
                "max_hold_h": 672.0, "momentum_exit": momentum_exit}
    if src == "scout:ignition":
        # Ignition's OWN scorecard: +1.47% mean at 4h but +4.67% at 24h
        # (90% hit, n=30) — the edge lives at the day scale, and the old
        # 8h clock exited at hour 5 of a 24-hour move (DEXE stalled out at
        # +2.9% of what its cohort averages +4.7%). The sentiment equities
        # bot — the fleet's top earner — holds while its thesis holds;
        # this is that lesson, calibrated by our own numbers. Breakout
        # does NOT get this: its 24h record is NEGATIVE (-3.79%).
        return {"kind": "burst", "stop_pct": -0.06, "stall_h": 4.0,
                "max_hold_h": 24.0, "momentum_exit": momentum_exit}
    if src.startswith("scout:"):
        return {"kind": "burst", "stop_pct": -0.06, "stall_h": 2.0,
                "max_hold_h": 8.0, "momentum_exit": momentum_exit}
    return {"kind": "hype", "stop_pct": -0.10, "stall_h": 6.0,
            "max_hold_h": 24.0, "momentum_exit": momentum_exit}


# ---- watcher earn-in (OWNER DECISION 2026-08-19: "fix it. I don't want
# this to happen") ------------------------------------------------------------
# The Watcher's real-money record at the moment of the order: 0 wins in 7
# entries, -$10.95 — every dollar this book has ever lost. Every scout
# signal must EARN actionability on a resolved record; the Watcher was the
# one path trading on trust. No longer: watcher ENTRIES are benched until
# the PAPER TWIN (hypecrypto — the same signal, unguarded, $1,000 paper)
# shows a rolling record that beats the bar below. Re-arming is mechanical
# and automatic in both directions; neither fear nor hope gets a vote.
# The Watcher keeps its risk-officer roles (SEVERE exits, staleness
# grounding, hype-faded exits) — only its power to OPEN real positions is
# gated.
WATCHER_EARN_WINDOW = 10       # judge the twin's last N round trips
WATCHER_EARN_MIN_N = 6         # fewer resolved trips = unproven = benched
WATCHER_EARN_MIN_WINS = 0.40   # same bar the scout gate uses


def twin_round_trips(trades: list[dict]) -> list[float]:
    """Pair the twin's BUY->SELL rows per ticker, in order, into realized
    round-trip returns (fractions). Unmatched rows are ignored."""
    open_pos: dict = {}
    out: list[float] = []
    for t in trades or []:
        try:
            if t.get("action") == "BUY":
                open_pos[t["ticker"]] = float(t["price"])
            elif t.get("action") == "SELL" and t.get("ticker") in open_pos:
                buy = open_pos.pop(t["ticker"])
                if buy > 0:
                    out.append(float(t["price"]) / buy - 1.0)
        except Exception:
            continue
    return out


def watcher_earned(round_trips: list[float]) -> tuple[bool, str]:
    """(armed, reason). Armed only when the twin's rolling record clears
    the bar; unproven or failing records stay benched."""
    window = round_trips[-WATCHER_EARN_WINDOW:]
    n = len(window)
    if n < WATCHER_EARN_MIN_N:
        return False, (f"benched — twin has {n}/{WATCHER_EARN_MIN_N} "
                       f"resolved round trips; unproven signals do not "
                       f"spend real money (owner decision 08-19)")
    wins = sum(1 for r in window if r > 0)
    mean = sum(window) / n
    if wins / n < WATCHER_EARN_MIN_WINS or mean <= 0:
        return False, (f"benched — twin last {n}: {wins} wins, "
                       f"mean {mean:+.2%}; the paper record does not "
                       f"justify real money")
    return True, (f"earned — twin last {n}: {wins} wins, mean {mean:+.2%}")


# ---- FUEL-GONE exit (owner-directed 2026-08-21, replaces the stall clock) ---
# The exit-timing audit (reports/exit_timing.md) found the book's signature
# error is EARLY exits, and every one of them was the STALL CLOCK: stalls
# surrendered only +1.6% of their in-hold peak on average, then the coins ran
# +5.5% within 24h of the sell. Meanwhile the 08-15..08-21 rally made BTC
# +22% while this book made -7% — with the scout's own flagged coins at a
# median +18%: signal detection was fine, the clock was selling correctly
# identified moves 2-4h into a 24-48h resolution. A clock knows nothing about
# a thesis. This check does: an ignition/breakout entry IS a volume event, so
# the position dies when the VOLUME dies (and it never paid, and the market
# pulse is not in a wave regime where coins re-ignite). The stop-loss,
# ratchet, trailing stop and max-hold cap all remain untouched above it.
FUEL_MIN_SURGE = 1.5     # thesis alive while the last closed hour still runs
                         # >=1.5x the pre-entry hourly-volume baseline
FUEL_MIN_CLOSED_H = 2    # need >=2 fully closed post-entry hours to judge —
                         # a measurement floor, not a stall clock: one hourly
                         # candle is noise, and judging on the partial
                         # forming hour would eject every fresh entry
FUEL_MIN_GAIN = 0.03     # a seat >=+3% is paying; the ratchet/trailing
                         # leash manage winners, fuel-gone only judges duds


def fuel_surge(symbol: str, entry_ms: int) -> float | None:
    """Last closed post-entry hourly quote volume vs the pre-entry baseline.

    Baseline = median hourly quote volume of the closed hours BEFORE entry
    (needs >=6 to mean anything). None = cannot judge yet, which refuses to
    exit — unknown must never fire a sell."""
    k = _call("GET", "/v3/klines",
              {"symbol": symbol, "interval": "1h", "limit": 30})
    try:
        now_ms = time.time() * 1000
        closed = [r for r in k if float(r[6]) < now_ms]
        before = [float(r[7]) for r in closed if float(r[6]) <= entry_ms]
        after = [r for r in closed if float(r[0]) >= entry_ms]
        if len(before) < 6 or len(after) < FUEL_MIN_CLOSED_H:
            return None
        base = sorted(before)[len(before) // 2]
        if base <= 0:
            return None
        return float(after[-1][7]) / base
    except Exception:
        return None


def fuel_verdict(surge: float | None, pnl_frac: float | None,
                 wave_active: bool) -> str | None:
    """Pure verdict: exit reason iff the thesis is measurably dead.

    Three concrete conditions, ALL required — no elapsed-time input:
      1. the volume surge is gone (fuel below FUEL_MIN_SURGE x baseline)
      2. the seat never paid (under FUEL_MIN_GAIN)
      3. the market pulse is not in a breadth wave (waves re-ignite coins;
         the stop/ratchet/trailing leash carry the downside meanwhile)
    """
    if surge is None or pnl_frac is None:
        return None
    if wave_active:
        return None
    if pnl_frac >= FUEL_MIN_GAIN:
        return None
    if surge >= FUEL_MIN_SURGE:
        return None
    return (f"FUEL GONE — hourly volume {surge:.1f}x its pre-entry baseline "
            f"(floor {FUEL_MIN_SURGE}x) and only {pnl_frac:+.1%}: the surge "
            f"this entry bought is over and it never paid")


def trail_pct(gain: float | None) -> float:
    """Progressive trailing stop: the more a ride has paid, the tighter it
    is held. The 2y study's retention gradient is monotonic — +50-100%
    events kept -24% at 30d, +500%+ kept -58%: the bigger the pump, the
    more completely it dies, so protecting a big gain matters more than
    stretching for its tail. gain = high-water-mark / entry - 1."""
    g = gain or 0.0
    if g >= 1.0:
        return -0.08
    if g >= 0.5:
        return -0.10
    return -0.15


# ---- profit ratchet (exit audit 2026-08-19, all 14 real trades) --------------
# The book's winners peak between +4% and +8% (MFE: COW +4.3, CHIP +4.5,
# EDEN +6.0, ACE +6.1, DEXE +7.6) — and then round-trip, because the
# trailing leash (-15%) only tightens after gains of +50% that never
# happen at this horizon. Result: avg win +1.72% vs avg loss -3.42%, and
# three trades that were UP +4-6% mid-ride ended -7.9% to -11.2%.
# The ratchet closes that hole: once a ride has paid, it is never again
# allowed to go red; once it has paid well, half the peak is locked.
RATCHET_ARM = 0.04       # MFE >= +4%: lock breakeven-plus-fees
RATCHET_LOCK = 0.005     # ...at entry +0.5% (covers the round trip)
RATCHET_ARM2 = 0.08      # MFE >= +8%: lock half the peak gain
RATCHET_KEEP2 = 0.5


def ratchet_stop(entry: float | None, hwm: float | None) -> float | None:
    """Price floor earned by the ride so far, or None if not armed.
    Applied on top of (never instead of) the hard stop and trailing stop.

    Replayed on the actual record: COW (-11.2%) exits +0.5%, CHIP-1 (-7.7%)
    exits +0.5%, ACE (-7.9%) exits +0.5%, DEXE (+2.9%) exits ~+3.8%. Small
    sample, fitted in hindsight — which is why the ledger tags these exits
    RATCHET so the rule builds its own attributable record.
    """
    if not entry or not hwm or entry <= 0:
        return None
    mfe = hwm / entry - 1.0
    if mfe >= RATCHET_ARM2:
        return entry * (1.0 + mfe * RATCHET_KEEP2)
    if mfe >= RATCHET_ARM:
        return entry * (1.0 + RATCHET_LOCK)
    return None


def late_entry(runup_24h: float | None, chg_1h: float | None,
               dd_2h: float | None, range_24h: float | None) -> str | None:
    """Pure verdict: refusal reason if this entry is chasing a spent move or
    reaching for one too small to pay for itself.

    Every input is required. None means the data could not be fetched, and
    this book goes all-in per entry — 'unknown' is not a number it can
    afford, so unknown refuses."""
    if runup_24h is None or chg_1h is None or dd_2h is None \
            or range_24h is None:
        return "LATE-ENTRY GUARD — price context unavailable; not buying blind"
    if range_24h < MIN_RANGE_24H_AT_ENTRY:
        return (f"NO ROOM — 24h range is only {range_24h:.1%} (floor "
                f"{MIN_RANGE_24H_AT_ENTRY:.0%}): a round trip costs ~0.2% "
                f"and this cannot pay for itself inside the hold")
    if runup_24h > MAX_RUNUP_24H_AT_ENTRY:
        return (f"LATE — already {runup_24h:+.1%} off its 24h low (cap "
                f"{MAX_RUNUP_24H_AT_ENTRY:+.0%}): the pump this hype "
                f"describes has already happened")
    if dd_2h <= MAX_DRAWDOWN_2H:
        return (f"ROLLED OVER — {dd_2h:+.1%} below its 2h high (floor "
                f"{MAX_DRAWDOWN_2H:+.0%}): it just fell, and an hourly "
                f"window would lose that as the drop ages out")
    if chg_1h < MIN_CHG_1H_AT_ENTRY:
        return (f"LATE — {chg_1h:+.1%} in the last hour: the move is rolling "
                f"over, hype arrived after the top")
    return None


def late_entry_check(symbol: str) -> str | None:
    """Fetch the four numbers late_entry() judges. Two public GETs."""
    runup_24h = range_24h = None
    t = _call("GET", "/v3/ticker/24hr", {"symbol": symbol})
    try:
        last = float(t["lastPrice"])
        low, high = float(t["lowPrice"]), float(t["highPrice"])
        if low > 0:
            runup_24h = last / low - 1.0
            range_24h = high / low - 1.0
    except Exception:
        pass
    chg_1h = dd_2h = None
    # 24 five-minute bars = 2 hours: the last 13 give the hourly change, the
    # whole window gives the distance below the recent high
    k = _call("GET", "/v3/klines",
              {"symbol": symbol, "interval": "5m", "limit": 24})
    try:
        closes = [float(r[4]) for r in k]
        highs = [float(r[2]) for r in k]
        last = closes[-1]
        if len(closes) >= 13:
            chg_1h = last / closes[-13] - 1.0
        peak = max(highs)
        if peak > 0:
            dd_2h = last / peak - 1.0
    except Exception:
        pass
    return late_entry(runup_24h, chg_1h, dd_2h, range_24h)


# ---- exchange-side protective stop (trade autopsy 2026-08-22) ---------------
# The book defends its floors by POLLING every ~5 min and then selling at
# market. On 08-22 that cost real money: AXSUSDT peaked +11.8%, so
# ratchet_stop set a floor at +5.9% -- and the fill came back at +1.29%. The
# price fell through the floor between two cycles and the bot sold at
# whatever it saw next. 4.6 points, gone to polling granularity, on an asset
# class that moves 5% in minutes.
#
# A resting STOP_LOSS_LIMIT sits AT the exchange and triggers in the gap
# between our cycles. Three rules keep this safe:
#   1. ADDITIVE, NEVER REPLACING. Every poll-based exit (hard stop, ratchet,
#      trailing, fuel, momentum, hype) keeps running untouched. If placement
#      fails for any reason the book degrades to exactly today's behaviour,
#      never to unprotected -- the one failure mode worth engineering against.
#   2. Off by default (LOTTERY_EXCHANGE_STOPS != 1). This is the order path
#      on a real-money account; it earns its way on with the owner watching.
#   3. A resting order locks the units, so valuation must use
#      balances_valuation() or the seat prices at $0. See that function.
STOP_LIMIT_SLIP = 0.015   # limit this far under the trigger, so a fast
                          # crash still fills instead of leaving a stranded
                          # stop-limit above a collapsing bid
STOP_REPLACE_EPS = 0.005  # only re-place when the floor moves >0.5%: the
                          # floor creeps up every cycle a winner rises, and
                          # cancel/replace on each tick is pure API churn


def exchange_stops_armed() -> bool:
    """Both the live-trading arm AND its own opt-in. Neither implies the other."""
    return armed() and os.getenv("LOTTERY_EXCHANGE_STOPS", "") == "1"


def symbol_filters(symbol: str) -> dict:
    """{'tick': float, 'step': float} -- price and quantity increments.

    Binance rejects any order off-increment (-1013), and a rejected stop is
    a stop that silently is not there, so this is not optional politeness.
    """
    info = _call("GET", "/v3/exchangeInfo", {"symbol": symbol})
    out = {"tick": 0.0, "step": 0.0}
    for f in ((info or {}).get("symbols") or [{}])[0].get("filters", []):
        if f.get("filterType") == "PRICE_FILTER":
            out["tick"] = float(f.get("tickSize", 0) or 0)
        elif f.get("filterType") == "LOT_SIZE":
            out["step"] = float(f.get("stepSize", 0) or 0)
    return out


def _down_to(value: float, increment: float) -> float:
    """Round DOWN onto an increment. Down, always: rounding a sell stop up
    could place it above the market and be rejected outright."""
    if not increment or increment <= 0:
        return value
    return int(value / increment) * increment


def protective_floor(entry: float | None, hwm: float | None,
                     stop_pct: float) -> float | None:
    """The single highest price floor the poll-based rules would defend --
    hard stop, profit ratchet and trailing stop resolved into one number a
    resting order can carry. Mirrors the poll logic; it never invents a
    floor the polling path would not also enforce.

    stop_pct is per-seat (exit_params(): -0.06 burst, -0.10 grind/hype), so
    it is passed in rather than assumed -- a resting order built on the wrong
    species' stop would sit 4 points from where the poll path defends.
    """
    if not entry or entry <= 0:
        return None
    floors = [entry * (1.0 + stop_pct)]
    if hwm and hwm > 0:
        floors.append(hwm * (1.0 + trail_pct(hwm / entry - 1.0)))
        r = ratchet_stop(entry, hwm)
        if r:
            floors.append(r)
    return max(floors)


def resting_stop(symbol: str) -> dict | None:
    """The bot's live protective order on this symbol, if one is resting."""
    if not armed():
        return None
    orders = _call("GET", "/v3/openOrders", {"symbol": symbol}, signed=True)
    for o in orders or []:
        if o.get("side") == "SELL" and "STOP" in str(o.get("type", "")):
            return o
    return None


def order_status(symbol: str, order_id: str) -> dict | None:
    if not armed() or not order_id:
        return None
    return _call("GET", "/v3/order",
                 {"symbol": symbol, "orderId": order_id}, signed=True)


def cancel_stop(symbol: str, order_id: str) -> bool:
    """Cancel a resting stop. Must run before ANY bot-initiated sell: leaving
    it behind would hold units the market order needs, or fire later against
    a seat the book has already closed."""
    if not armed() or not order_id:
        return False
    r = _call("DELETE", "/v3/order",
              {"symbol": symbol, "orderId": order_id}, signed=True)
    ok = bool(r)
    log({"event": "stop_cancelled" if ok else "stop_cancel_failed",
         "symbol": symbol, "order_id": str(order_id),
         "code": LAST_ERROR.get("code"), "msg": LAST_ERROR.get("msg", "")})
    return ok


def place_protective_stop(symbol: str, qty: float,
                          stop_price: float) -> dict | None:
    """Rest a STOP_LOSS_LIMIT sell at stop_price. Returns the order or None.

    Returning None is a normal, survivable outcome -- the caller keeps its
    poll-based exits either way -- so every failure here is logged and
    swallowed rather than raised.
    """
    if not exchange_stops_armed():
        return None
    f = symbol_filters(symbol)
    stop = _down_to(stop_price, f["tick"])
    limit = _down_to(stop * (1.0 - STOP_LIMIT_SLIP), f["tick"])
    q = _down_to(qty, f["step"])
    if stop <= 0 or limit <= 0 or q <= 0:
        log({"event": "stop_not_placed", "symbol": symbol,
             "reason": f"non-positive after increment rounding "
                       f"(stop={stop}, limit={limit}, qty={q})"})
        return None
    # A stop at or above the market triggers instantly -- that is a market
    # sell wearing a stop's clothes, and not what any caller asked for.
    p = price(symbol)
    if p and stop >= p:
        log({"event": "stop_not_placed", "symbol": symbol,
             "reason": f"floor {stop} is at or above market {p}; the "
                       f"poll-based exit owns this case"})
        return None
    LAST_ERROR.clear()
    resp = _call("POST", "/v3/order",
                 {"symbol": symbol, "side": "SELL", "type": "STOP_LOSS_LIMIT",
                  "timeInForce": "GTC",
                  "quantity": f"{q:.8f}".rstrip("0").rstrip("."),
                  "stopPrice": f"{stop:.10f}".rstrip("0").rstrip("."),
                  "price": f"{limit:.10f}".rstrip("0").rstrip(".")},
                 signed=True)
    if not resp:
        log({"event": "stop_not_placed", "symbol": symbol,
             "reason": "exchange rejected or did not answer",
             "code": LAST_ERROR.get("code"), "msg": LAST_ERROR.get("msg", "")})
        return None
    out = {"order_id": str(resp.get("orderId", "")), "stop": stop,
           "limit": limit, "qty": q}
    log({"event": "stop_placed", "symbol": symbol, **out})
    print(f"[lottery-live] protective stop resting on {symbol} @ {stop}")
    return out


def market(action: str, symbol: str, quote_qty: float | None = None,
           qty: float | None = None) -> dict | None:
    """One real market order. Caller passes quoteOrderQty for BUY (spend
    USDT) or quantity for SELL. Returns avg-fill dict or None."""
    # Defense in depth (audit 08-15): arming enforced HERE, not only by the
    # caller. With keys present but LOTTERY_LIVE!=1 this function must be
    # inert no matter who imports it or what future code calls it.
    if not armed():
        log({"event": "refused", "action": action.upper(), "symbol": symbol,
             "reason": "not armed (LOTTERY_LIVE != 1) — market() is inert"})
        print(f"[lottery-live] market() called while not armed — refused")
        return None
    params = {"symbol": symbol, "side": action.upper(), "type": "MARKET"}
    if action.upper() == "BUY":
        # FLOOR to the cent, never round: an all-in BUY passes the exact
        # free balance, and round() half-up asked Binance for more than the
        # account held (free 9.2995 -> order 9.30 -> five straight -2010
        # rejections, 08-16). Flooring leaves at most one cent behind.
        params["quoteOrderQty"] = f"{int((quote_qty or 0.0) * 100) / 100:.2f}"
    else:
        params["quantity"] = f"{qty:.8f}".rstrip("0").rstrip(".")
    LAST_ERROR.clear()
    resp = _call("POST", "/v3/order", params, signed=True)
    if resp is None:
        if LAST_ERROR.get("code") is not None:
            # Binance answered with a definitive error code: the order was
            # REJECTED, full stop. Logging these as "may have filled" sent
            # the 08-16 digest hunting phantom positions five times over.
            log({"event": "order_rejected", "action": action.upper(),
                 "symbol": symbol, "code": LAST_ERROR.get("code"),
                 "msg": LAST_ERROR.get("msg", "")})
            return None
        # No response and no error body — the order may have EXECUTED with
        # the response lost in transit (timeout after the exchange accepted
        # it). Leave a loud marker so the next cycle's ledger reconciliation
        # looks for an untracked position instead of trusting the void.
        log({"event": "order_unconfirmed", "action": action.upper(),
             "symbol": symbol,
             "note": "POST returned nothing — order MAY have filled; "
                     "reconcile against balances next cycle"})
        return None
    fills = resp.get("fills") or []
    tq = sum(float(f["qty"]) for f in fills)
    if tq <= 0:
        log({"event": "order_no_fill", "action": action, "symbol": symbol,
             "resp": bool(resp)})
        return None
    avg = sum(float(f["price"]) * float(f["qty"]) for f in fills) / tq
    commission = sum(float(f.get("commission", 0) or 0) for f in fills)
    out = {"price": avg, "qty": tq, "order_id": str(resp.get("orderId", "")),
           "commission": commission,
           "commission_asset": (fills[0].get("commissionAsset", "")
                                if fills else "")}
    log({"event": "fill", "action": action.upper(), "symbol": symbol, **out})
    print(f"[lottery-live] REAL {action.upper()} {symbol} "
          f"{tq} @ {avg:.10g}")
    return out
