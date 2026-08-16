"""Lottery Live — the owner's explicitly-sacrificial real-money book.

Bot #13, and deliberately NOT the pilot: real Binance spot, one seat,
armed only by the owner's keys + LOTTERY_LIVE=1. Pre-registered 2026-08-15
with the owner's stated intent verbatim: "explode or burn — mostly
explode". The documented base rate says burn; this file makes the attempt
mechanical and honest. NO BOOK CAP as of 2026-08-16 (owner decision): every
BUY spends the account's full free USDT balance — see binance_live.py.

Selector (mechanical, no discretion anywhere):
  1. Watcher's euphoric CRYPTO symbols (same source as the hypecrypto paper
     twin), freshest scan only (<= 9h);
  2. fallback when the Watcher lists none: Binance's top 24h USDT gainer
     with > $20M quote volume (stables excluded) — "buy what is already
     exploding", the maximal-variance mechanical rule.

Exits run EVERY cycle (~10 min) off live Binance prices, because Grok scans
land at most every 8h and anything gated on a fresh scan reacts long after
a pump has rolled over. Price is free, instant and 24/7, so price owns the
fast exits and the Watcher owns the slow qualitative ones:
  1. -10% hard stop from entry
  2. -15% trailing stop from the high-water mark  <- the anti-crash exit
  3. stalled: 6h in and under +3% — the pump never came
  4. max hold 24h — hype has a half-life, never marry a coin
  5. momentum gone: no longer a top-25 24h mover
  6. Watcher SEVERE, or scans stale > 24h (a blind risk officer grounds it)
  7. hype faded on a NEWER scan (Watcher-sourced entries)
Up to 3 entries per UTC day, any day — crypto trades 24/7. Full-balance
sizing: this book YOLOs its whole balance by design.

THE BOT MANAGES ONLY WHAT THE BOT BOUGHT. This runs on the owner's real
account, which already holds ~23 other coins; the bot records the exact
filled quantity of its own seat and can never sell more than that, and it
never adopts a balance it did not buy. Crash recovery reads the LEDGER (a
BUY fill with no matching exit), not the balance sheet.
REAL MONEY. Not investment advice — the opposite: the odds are printed on
the ticket.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import config
import binance_live
from sentinel_trader import scan_age_hours, scan_is_stale
from hype_crypto_tracker import crypto_candidates, ENTRY_FRESH_H

STATE = config.DATA / "lottery_state.json"
SENTINEL = config.DATA / "sentinel_state.json"
STOP_PCT = -0.10        # hard stop from entry (Watcher-sourced hype rides)
TRAIL_PCT = -0.15       # from the high-water mark: gives back at most this
MAX_HOLD_H = 24.0       # hype has a half-life; do not marry a coin
STALL_H = 6.0           # flat-to-down this long = the pump is over
STALL_MIN_GAIN = 0.03   # ...unless it is at least this far ahead
# Scout-sourced entries are volume events, and the research is unambiguous
# that those resolve in MINUTES to a few hours, not days — a burst that has
# not paid quickly is noise being held for no stated reason. So scout trades
# run on a faster clock than Watcher hype rides:
SCOUT_STOP_PCT = -0.06
SCOUT_STALL_H = 2.0
SCOUT_MAX_HOLD_H = 8.0
# Re-entry cooldown after ANY protective exit (audit 08-15: the old
# blacklist was keyed on the Watcher's scan_ts — meaningless for scout
# entries, and only the hard stop set it, so a trailing-stopped coin could
# be rebought the very next 5-minute cycle while still crashing).
COOLDOWN_H = 3.0
# Crypto trades 24/7 — the weekday-only rule was inherited from a book whose
# universe collapsed to crypto-only at weekends while equities were shut.
# That reasoning does not transfer to a crypto-native book: weekend hype is
# real hype, and every exit already runs 24/7 anyway.
WEEKEND_ENTRIES = True
MAX_ENTRIES_PER_DAY = 3
STABLES = {"USDC", "FDUSD", "TUSD", "DAI", "EUR", "USDP", "BUSD"}
KEY = "lottery"


def scout_candidates(max_age_min: float = 30.0) -> list[dict]:
    """The Scout's ranked opinion, if it is fresh enough to act on.

    Read-only handoff through a file: the Scout cannot trade and this book
    cannot scan, so neither can break the other. A stale signals file (the
    Scout crashed, or the cycle is running without it) yields an empty list
    rather than a stale trade — the same rule the Watcher gets."""
    p = config.DATA / "scout_signals.json"
    if not p.exists():
        return []
    try:
        d = json.loads(p.read_text())
        age = (datetime.now(timezone.utc)
               - datetime.fromisoformat(d["ts"])).total_seconds() / 60.0
    except Exception:
        return []
    if age > max_age_min:
        print(f"[{KEY}] scout signals {age:.0f}min old — ignoring")
        return []
    return d.get("candidates") or []


def top_gainer() -> tuple[str, float] | None:
    """Fallback selector: top 24h USDT gainer, > $20M volume, no stables.
    Public data endpoint — works unarmed too."""
    d = binance_live._call("GET", "/v3/ticker/24hr")
    if not isinstance(d, list):
        return None
    best = None
    for t in d:
        s = t.get("symbol", "")
        if not s.endswith("USDT") or s[:-4] in STABLES:
            continue
        if float(t.get("quoteVolume", 0) or 0) < 20_000_000:
            continue
        chg = float(t.get("priceChangePercent", 0) or 0)
        if best is None or chg > best[1]:
            best = (s, chg)
    return best


def in_top_gainers(symbol: str, n: int = 10) -> bool:
    d = binance_live._call("GET", "/v3/ticker/24hr")
    if not isinstance(d, list):
        return True   # feed failure must not force a panic exit
    ranked = sorted(
        (t for t in d if t.get("symbol", "").endswith("USDT")
         and t["symbol"][:-4] not in STABLES
         and float(t.get("quoteVolume", 0) or 0) > 20_000_000),
        key=lambda t: float(t.get("priceChangePercent", 0) or 0), reverse=True)
    return symbol in {t["symbol"] for t in ranked[:n]}


def main():
    now = datetime.now(timezone.utc)
    today = str(now.date())

    if not binance_live.armed():
        print(f"[{KEY}] not armed (needs BINANCE_LIVE keys + LOTTERY_LIVE=1) "
              f"— skipping")
        return

    sent = json.loads(SENTINEL.read_text()) if SENTINEL.exists() else {"scans": []}
    scan = sent["scans"][-1] if sent["scans"] else None
    scan_ts = scan["ts"] if scan else ""
    age_h = scan_age_hours(scan)
    stale = scan_is_stale(scan)
    fresh = age_h is not None and age_h <= ENTRY_FRESH_H
    severe = bool(scan and scan.get("risk_level") == "severe")

    st = json.loads(STATE.read_text()) if STATE.exists() else {
        "created": today, "held_symbol": None, "entry_price": None,
        "units": 0.0, "entry_scan_ts": None, "entry_source": None,
        "stopped": {}, "entries": {}, "realized": []}

    bals = binance_live.balances()
    if not bals:
        print(f"[{KEY}] could not read balances — cycle skipped")
        return

    # LEDGER RECONCILIATION, every cycle — never from the balance sheet.
    #
    # THE BOT MANAGES ONLY WHAT THE BOT BOUGHT (the account holds ~23 other
    # coins). The ledger is the record of that. Audit 08-15 rewrote this
    # from a recover-only-when-stateless scan into a full reconciliation,
    # closing two critical holes:
    #   * a SELL whose "fill" line landed but whose "exit" line (or the
    #     state write) was lost to a crash left the old scan re-adopting an
    #     ALREADY-SOLD seat — whose next exit would sell the owner's own
    #     holding of that coin up to `units`. A SELL fill now closes the
    #     seat in the scan, and a state seat the ledger says is closed is
    #     cleared loudly (the phantom-seat self-heal).
    #   * an unconfirmed order (POST timed out after the exchange accepted
    #     it) is surfaced as a marker the owner can see in the ledger.
    ledger_open = None          # last BUY fill with no closing SELL/exit
    if binance_live.LEDGER.exists():
        for line in binance_live.LEDGER.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("event") == "fill" and e.get("action") == "BUY":
                ledger_open = e
            elif ledger_open and e.get("symbol") == ledger_open.get("symbol") \
                    and (e.get("event") == "exit"
                         or (e.get("event") == "fill"
                             and e.get("action") == "SELL")):
                ledger_open = None
    if st["held_symbol"] and (not ledger_open
                              or ledger_open.get("symbol") != st["held_symbol"]):
        binance_live.log({"event": "reconciled_closed_seat",
                          "symbol": st["held_symbol"],
                          "note": "ledger says this seat was already sold; "
                                  "state file was stale (crash window)"})
        print(f"[{KEY}] RECONCILED: ledger says {st['held_symbol']} was "
              f"already closed — clearing the stale seat")
        st["held_symbol"] = st["entry_price"] = st["entry_scan_ts"] = None
        st["entry_source"] = None
        st["units"] = 0.0
        st["spent_usd"] = None
        st.pop("hwm", None)
        st.pop("entry_time", None)
    if not st["held_symbol"] and ledger_open:
        st["held_symbol"] = ledger_open["symbol"]
        st["entry_price"] = ledger_open.get("price")
        st["units"] = ledger_open.get("qty", 0.0)
        st["hwm"] = ledger_open.get("price")
        st["entry_time"] = ledger_open.get("ts")
        st["entry_scan_ts"], st["entry_source"] = scan_ts, "recovered"
        binance_live.log({"event": "recovered_from_ledger",
                          "symbol": st["held_symbol"], "units": st["units"]})
        print(f"[{KEY}] recovered unfinished seat {st['held_symbol']} "
              f"from the ledger (state file had lost it)")

    held = st["held_symbol"]

    def sell(reason: str) -> bool:
        base = held[:-4]
        qty_free = bals.get(base, 0.0)
        # Sell ONLY what this bot bought. Selling the whole free balance
        # would liquidate coins the owner already held in the same account
        # (they hold 23 assets) — the bot's units are the ceiling, the
        # exchange balance only caps it lower if something is missing.
        owned = float(st.get("units") or 0.0)
        sellable = min(owned, qty_free) if owned > 0 else 0.0
        if owned <= 0:
            print(f"[{KEY}] no recorded units for {held} — refusing to sell "
                  f"a balance this bot did not buy")
            return False
        # mainnet lot steps (binance_broker's cache is testnet's — different)
        info = binance_live._call("GET", "/v3/exchangeInfo", {"symbol": held})
        step = 0.0
        for f in ((info or {}).get("symbols") or [{}])[0].get("filters", []):
            if f.get("filterType") == "LOT_SIZE":
                step = float(f.get("stepSize", 0) or 0)
        qty = int(sellable / step) * step if step > 0 else sellable
        if qty <= 0:
            print(f"[{KEY}] nothing sellable in {base} — skip")
            return False
        why = binance_live.guard("SELL", held, bals, held, owned)
        if why:
            binance_live.log({"event": "refused", "action": "SELL",
                              "symbol": held, "reason": why})
            print(f"[{KEY}] SELL refused: {why}")
            return False
        fill = binance_live.market("SELL", held, qty=qty)
        if not fill:
            return False
        entry_px = st.get("entry_price")
        exit_px = fill["price"]
        u = float(st.get("units") or 0.0)
        pnl = ((exit_px / entry_px - 1) * 100) if entry_px else None
        spent = round(entry_px * u, 4) if entry_px else None
        got = round(exit_px * fill["qty"], 4)
        pnl_usd = round(got - spent, 4) if spent is not None else None
        rec = {"symbol": held,
               "entry_time": st.get("entry_time"),
               "exit_time": now.isoformat(timespec="seconds"),
               "entry_price": entry_px, "exit_price": exit_px,
               "units": round(u, 8), "spent_usd": spent, "got_usd": got,
               "pnl_pct": round(pnl, 2) if pnl is not None else None,
               "pnl_usd": pnl_usd, "reason": reason,
               "date": today, "exit": exit_px, "entry": entry_px}
        st["realized"].append(rec)
        binance_live.log({"event": "exit", "symbol": held, "reason": reason,
                          "entry_price": entry_px, "exit_price": exit_px,
                          "pnl_pct": rec["pnl_pct"], "pnl_usd": pnl_usd})
        st["held_symbol"] = st["entry_price"] = st["entry_scan_ts"] = None
        st["entry_source"] = None
        st["units"] = 0.0
        st["spent_usd"] = None
        st.pop("hwm", None)
        st.pop("entry_time", None)
        return True

    # ---- exits ----
    # These run EVERY cycle (~10 min) off live Binance prices, deliberately
    # not off the Watcher: Grok scans arrive at most every 8h, so anything
    # gated on a new scan reacts hours after a pump has already rolled over.
    # Price is free, instant, and 24/7 — so price carries the fast exits and
    # the Watcher carries the slow, qualitative ones.
    if held:
        p = binance_live.price(held)
        entry = st.get("entry_price")
        is_scout = str(st.get("entry_source") or "").startswith("scout:")
        stop_pct = SCOUT_STOP_PCT if is_scout else STOP_PCT
        stall_h = SCOUT_STALL_H if is_scout else STALL_H
        max_hold = SCOUT_MAX_HOLD_H if is_scout else MAX_HOLD_H

        # high-water mark, updated live
        if p:
            st["hwm"] = max(float(st.get("hwm") or p), p)
        hwm = float(st.get("hwm") or 0)
        held_h = None
        if st.get("entry_time"):
            try:
                held_h = (now - datetime.fromisoformat(
                    st["entry_time"])).total_seconds() / 3600.0
            except Exception:
                held_h = None

        if p and entry and p / entry - 1 <= stop_pct:
            st["stopped"][held] = now.isoformat(timespec="seconds")
            if sell(f"STOP-LOSS ({(p / entry - 1):.1%} from entry) — "
                    f"hype that bleeds gets cut"):
                held = None
        # trailing stop: the pump gave back too much of its peak. THIS is the
        # exit that gets the book out before a hype crash instead of after.
        if held and p and hwm and p / hwm - 1 <= TRAIL_PCT:
            st["stopped"][held] = now.isoformat(timespec="seconds")
            if sell(f"TRAILING STOP ({(p / hwm - 1):.1%} off the "
                    f"{hwm:.8g} peak) — riding it down is not the strategy"):
                held = None
        # stall: hours in, still not meaningfully ahead. Hype that has not
        # paid by now is decay, and every hour held is a hour of exposure.
        if held and p and entry and held_h is not None and held_h >= stall_h \
                and p / entry - 1 < STALL_MIN_GAIN:
            st["stopped"][held] = now.isoformat(timespec="seconds")
            if sell(f"STALLED ({held_h:.1f}h in, only "
                    f"{(p / entry - 1):+.1%}) — the pump never came"):
                held = None
        # hard time cap: never marry a coin
        if held and held_h is not None and held_h >= max_hold:
            if sell(f"MAX HOLD ({held_h:.0f}h) — hype has a half-life"):
                held = None
        # Momentum decay — ONLY for entries whose thesis was "it is a top
        # mover" (gainer/adopted/scout:breakout). An ignition entry has by
        # definition NOT moved yet, so judging it by top-25 membership would
        # sell it one cycle after buying, every time; its stall clock covers
        # the fizzle case. Watcher hype rides are judged by scans, not rank.
        src = str(st.get("entry_source") or "")
        if held and (src in ("gainer", "adopted") or src == "scout:breakout") \
                and not in_top_gainers(held, n=25):
            if sell("MOMENTUM GONE — no longer a top-25 24h mover"):
                held = None
        if held and severe:
            if sell("Watcher SEVERE — lottery closes in a crisis"):
                held = None
        if held and stale:
            if sell(f"Grok scans stale "
                    f"({'?' if age_h is None else f'{age_h:.0f}'}h) — "
                    f"risk officer blind, book grounded"):
                held = None
        if held and st.get("entry_source") == "watcher" and not stale \
                and scan_ts and st.get("entry_scan_ts") \
                and scan_ts > st["entry_scan_ts"]:
            hype_now = {c.replace("-USD", "") + "USDT"
                        for c in crypto_candidates(scan)}
            if held not in hype_now:
                if sell("Hype faded — coin off a newer euphoric scan"):
                    held = None

    # ---- entry ----
    bals = binance_live.balances() or bals
    entries_today = st.get("entries", {}).get(today, 0)
    can_enter = (held is None and not (severe or stale)
                 and (WEEKEND_ENTRIES or now.weekday() < 5)
                 and entries_today < MAX_ENTRIES_PER_DAY)
    if can_enter:
        # time-based cooldown: a coin exited by ANY protective rule stays
        # untouchable for COOLDOWN_H regardless of which source re-suggests
        # it — and expired entries are pruned so the dict cannot grow forever
        def _in_cooldown(ts_str) -> bool:
            try:
                return (now - datetime.fromisoformat(ts_str)
                        ).total_seconds() / 3600.0 < COOLDOWN_H
            except Exception:
                return False    # legacy scan_ts values: not parseable = expired
        st["stopped"] = {s: ts for s, ts in st.get("stopped", {}).items()
                         if _in_cooldown(ts)}
        blacklisted = set(st["stopped"])

        pick, source = None, None
        if fresh:
            for c in crypto_candidates(scan):
                sym = c.replace("-USD", "") + "USDT"
                if sym not in blacklisted and binance_live.price(sym):
                    pick, source = sym, "watcher"
                    break
        # The Scout: fast, quantitative, every cycle across all ~670 pairs.
        # It supersedes the old naive top-24h-gainer fallback, which happily
        # bought a coin that pumped six hours ago and was already rolling
        # over (the live COWUSDT case: +49% on the day, -6.5% in the hour, on
        # BELOW-average volume). The Scout requires the move to be alive now.
        if pick is None:
            for c in scout_candidates():
                if c["symbol"] in blacklisted:
                    continue
                if binance_live.price(c["symbol"]):
                    pick = c["symbol"]
                    source = f"scout:{c['signal']}"
                    print(f"[{KEY}] scout says {c['symbol']} "
                          f"({c['signal']}, score {c.get('score')}): "
                          f"{c.get('why', '')}")
                    break
        if pick:
            why = binance_live.guard("BUY", pick, bals, None)
            if why:
                binance_live.log({"event": "refused", "action": "BUY",
                                  "symbol": pick, "reason": why})
                print(f"[{KEY}] BUY refused: {why}")
            else:
                spend = bals.get("USDT", 0.0)
                fill = binance_live.market("BUY", pick, quote_qty=spend)
                if fill:
                    st["held_symbol"], st["entry_price"] = pick, fill["price"]
                    # exact filled quantity: the ONLY amount this bot may
                    # ever sell back (the account holds other coins)
                    st["units"] = fill["qty"]
                    st["spent_usd"] = round(fill["price"] * fill["qty"], 4)
                    # seeds the trailing stop and the hold clock
                    st["hwm"] = fill["price"]
                    st["entry_time"] = now.isoformat(timespec="seconds")
                    st["entry_scan_ts"], st["entry_source"] = scan_ts, source
                    st.setdefault("entries", {})
                    st["entries"] = {d: c for d, c in st["entries"].items()
                                     if d >= today}
                    st["entries"][today] = entries_today + 1

    val = binance_live.managed_value(binance_live.balances() or bals,
                                     st["held_symbol"], st.get("units"))
    st["last_value_usd"] = round(val, 2)
    st["last_updated_utc"] = now.isoformat(timespec="seconds")

    # live snapshot of the OPEN position for the dashboard: what it cost, what
    # it is worth now, and the unrealized P/L — the numbers the owner asked to
    # see on their phone
    if st.get("held_symbol"):
        cur = binance_live.price(st["held_symbol"])
        u = float(st.get("units") or 0.0)
        # fall back to entry_price * units for seats opened before spent_usd
        # was recorded (pre-08-15 fills, or ledger-recovered ones)
        spent = st.get("spent_usd")
        if spent is None and st.get("entry_price") and u:
            spent = round(st["entry_price"] * u, 4)
        now_val = round(cur * u, 4) if cur else None
        st["open_position"] = {
            "symbol": st["held_symbol"], "entry_time": st.get("entry_time"),
            "entry_price": st.get("entry_price"), "current_price": cur,
            "units": round(u, 8), "spent_usd": spent, "value_usd": now_val,
            "pnl_usd": (round(now_val - spent, 4)
                        if (now_val is not None and spent is not None) else None),
            "pnl_pct": (round((cur / st["entry_price"] - 1) * 100, 2)
                        if (cur and st.get("entry_price")) else None),
            "source": st.get("entry_source"),
        }
    else:
        st["open_position"] = None
    STATE.write_text(json.dumps(st, indent=2))
    print(f"[{KEY}] {today} seat={st['held_symbol'] or 'CASH'} "
          f"book ${val:.2f} (no cap) — "
          f"ticket odds printed in the docstring")


if __name__ == "__main__":
    main()
