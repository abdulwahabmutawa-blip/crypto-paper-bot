"""Lottery Live — the owner's explicitly-sacrificial ~$11 real-money book.

Bot #13, and deliberately NOT the pilot: real Binance spot, one seat,
BOOK CAP $20 enforced in binance_live.py, armed only by the owner's keys +
LOTTERY_LIVE=1. Pre-registered 2026-08-15 with the owner's stated intent
verbatim: "explode or burn — mostly explode". The documented base rate says
burn; this file makes the attempt mechanical, capped, and honest.

Selector (mechanical, no discretion anywhere):
  1. Watcher's euphoric CRYPTO symbols (same source as the hypecrypto paper
     twin), freshest scan only (<= 9h);
  2. fallback when the Watcher lists none: Binance's top 24h USDT gainer
     with > $20M quote volume (stables excluded) — "buy what is already
     exploding", the maximal-variance mechanical rule.

Exits, priority order: -10% hard stop (24/7) -> Watcher SEVERE -> scans
stale > 24h (only if Watcher-sourced entry... no: a blind risk officer
grounds the whole book, fallback entries included) -> hype faded on a newer
scan (Watcher entries only; fallback entries exit when the coin drops out
of the top-10 24h gainers). One new entry per UTC day, weekdays only
(the SHIB Saturday lesson; flip WEEKEND_ENTRIES to change). Full-balance
sizing: this book YOLOs its whole (capped) balance by design.

State (data/lottery_state.json) records entries/exits; POSITION TRUTH IS
THE EXCHANGE — balances are re-read every cycle, and an untracked position
(crash between fill and state write) is adopted, never re-bought over.
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
STOP_PCT = -0.10
WEEKEND_ENTRIES = False
MAX_ENTRIES_PER_DAY = 1
STABLES = {"USDC", "FDUSD", "TUSD", "DAI", "EUR", "USDP", "BUSD"}
KEY = "lottery"


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
        "entry_scan_ts": None, "entry_source": None, "stopped": {},
        "entries": {}, "realized": []}

    bals = binance_live.balances()
    if not bals:
        print(f"[{KEY}] could not read balances — cycle skipped")
        return

    # adopt an orphan position (crash between fill and state write): largest
    # non-USDT asset worth more than the exchange minimum becomes the seat
    if not st["held_symbol"]:
        cand = None
        for asset, qty in bals.items():
            if asset in ("USDT",) or asset in STABLES:
                continue
            p = binance_live.price(asset + "USDT")
            if p and qty * p >= binance_live.MIN_ORDER_USDT:
                v = qty * p
                if cand is None or v > cand[1]:
                    cand = (asset + "USDT", v, p)
        if cand:
            st["held_symbol"], st["entry_price"] = cand[0], cand[2]
            st["entry_scan_ts"], st["entry_source"] = scan_ts, "adopted"
            binance_live.log({"event": "adopted_orphan", "symbol": cand[0],
                              "value": round(cand[1], 2)})
            print(f"[{KEY}] adopted untracked position {cand[0]} "
                  f"(${cand[1]:.2f})")

    held = st["held_symbol"]

    def sell(reason: str) -> bool:
        base = held[:-4]
        qty_free = bals.get(base, 0.0)
        # mainnet lot steps (binance_broker's cache is testnet's — different)
        info = binance_live._call("GET", "/v3/exchangeInfo", {"symbol": held})
        step = 0.0
        for f in ((info or {}).get("symbols") or [{}])[0].get("filters", []):
            if f.get("filterType") == "LOT_SIZE":
                step = float(f.get("stepSize", 0) or 0)
        qty = int(qty_free / step) * step if step > 0 else qty_free
        if qty <= 0:
            print(f"[{KEY}] nothing sellable in {base} — skip")
            return False
        why = binance_live.guard("SELL", held, bals, held)
        if why:
            binance_live.log({"event": "refused", "action": "SELL",
                              "symbol": held, "reason": why})
            print(f"[{KEY}] SELL refused: {why}")
            return False
        fill = binance_live.market("SELL", held, qty=qty)
        if not fill:
            return False
        pnl = ((fill["price"] / st["entry_price"] - 1) * 100
               if st.get("entry_price") else None)
        st["realized"].append({"date": today, "symbol": held,
                               "exit": fill["price"],
                               "entry": st.get("entry_price"),
                               "pnl_pct": round(pnl, 2) if pnl is not None else None,
                               "reason": reason})
        binance_live.log({"event": "exit", "symbol": held, "reason": reason,
                          "pnl_pct": round(pnl, 2) if pnl is not None else None})
        st["held_symbol"] = st["entry_price"] = st["entry_scan_ts"] = None
        st["entry_source"] = None
        return True

    # ---- exits ----
    if held:
        p = binance_live.price(held)
        if p and st.get("entry_price") and p / st["entry_price"] - 1 <= STOP_PCT:
            st["stopped"][held] = scan_ts
            if sell(f"STOP-LOSS ({(p / st['entry_price'] - 1):.1%}) — "
                    f"hype that bleeds gets cut"):
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
        if held and st.get("entry_source") in ("gainer", "adopted") \
                and not in_top_gainers(held):
            if sell("Momentum faded — coin out of the top-10 24h gainers"):
                held = None

    # ---- entry ----
    bals = binance_live.balances() or bals
    entries_today = st.get("entries", {}).get(today, 0)
    can_enter = (held is None and not (severe or stale)
                 and (WEEKEND_ENTRIES or now.weekday() < 5)
                 and entries_today < MAX_ENTRIES_PER_DAY)
    if can_enter:
        pick, source = None, None
        if fresh:
            blacklisted = {s for s, ts in st["stopped"].items() if ts == scan_ts}
            for c in crypto_candidates(scan):
                sym = c.replace("-USD", "") + "USDT"
                if sym not in blacklisted and binance_live.price(sym):
                    pick, source = sym, "watcher"
                    break
        if pick is None:
            tg = top_gainer()
            if tg and tg[0] not in {s for s, ts in st["stopped"].items()
                                    if ts == scan_ts}:
                pick, source = tg[0], "gainer"
        if pick:
            why = binance_live.guard("BUY", pick, bals, None)
            if why:
                binance_live.log({"event": "refused", "action": "BUY",
                                  "symbol": pick, "reason": why})
                print(f"[{KEY}] BUY refused: {why}")
            else:
                spend = min(bals.get("USDT", 0.0), binance_live.BOOK_CAP_USD)
                fill = binance_live.market("BUY", pick, quote_qty=spend)
                if fill:
                    st["held_symbol"], st["entry_price"] = pick, fill["price"]
                    st["entry_scan_ts"], st["entry_source"] = scan_ts, source
                    st.setdefault("entries", {})
                    st["entries"] = {d: c for d, c in st["entries"].items()
                                     if d >= today}
                    st["entries"][today] = entries_today + 1

    val = binance_live.managed_value(binance_live.balances() or bals,
                                     st["held_symbol"])
    st["last_value_usd"] = round(val, 2)
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    STATE.write_text(json.dumps(st, indent=2))
    print(f"[{KEY}] {today} seat={st['held_symbol'] or 'CASH'} "
          f"book ${val:.2f} (cap ${binance_live.BOOK_CAP_USD:.0f}) — "
          f"ticket odds printed in the docstring")


if __name__ == "__main__":
    main()
