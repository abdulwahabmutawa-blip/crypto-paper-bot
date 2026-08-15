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
        "units": 0.0, "entry_scan_ts": None, "entry_source": None,
        "stopped": {}, "entries": {}, "realized": []}

    bals = binance_live.balances()
    if not bals:
        print(f"[{KEY}] could not read balances — cycle skipped")
        return

    # Crash recovery, from the LEDGER — never from the balance sheet.
    #
    # The first version scanned every non-USDT balance and adopted the
    # largest as its seat. On a dedicated account that is harmless; on the
    # owner's real account (23 assets: PEPE, SOL, SUI, STRK...) it would
    # have adopted coins the bot never bought and then sold them on a hype
    # exit. THE BOT MANAGES ONLY WHAT THE BOT BOUGHT. The ledger is the
    # record of that, so recovery reads the ledger: a fill BUY with no
    # later exit for the same symbol is a genuinely orphaned seat.
    if not st["held_symbol"] and binance_live.LEDGER.exists():
        last_buy = None
        for line in binance_live.LEDGER.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("event") == "fill" and e.get("action") == "BUY":
                last_buy = e
            elif e.get("event") == "exit" and last_buy \
                    and e.get("symbol") == last_buy.get("symbol"):
                last_buy = None
        if last_buy:
            st["held_symbol"] = last_buy["symbol"]
            st["entry_price"] = last_buy.get("price")
            st["units"] = last_buy.get("qty", 0.0)
            st["entry_scan_ts"], st["entry_source"] = scan_ts, "recovered"
            binance_live.log({"event": "recovered_from_ledger",
                              "symbol": st["held_symbol"],
                              "units": st["units"]})
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
        st["units"] = 0.0
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
                    # exact filled quantity: the ONLY amount this bot may
                    # ever sell back (the account holds other coins)
                    st["units"] = fill["qty"]
                    st["entry_scan_ts"], st["entry_source"] = scan_ts, source
                    st.setdefault("entries", {})
                    st["entries"] = {d: c for d, c in st["entries"].items()
                                     if d >= today}
                    st["entries"][today] = entries_today + 1

    val = binance_live.managed_value(binance_live.balances() or bals,
                                     st["held_symbol"], st.get("units"))
    st["last_value_usd"] = round(val, 2)
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    STATE.write_text(json.dumps(st, indent=2))
    print(f"[{KEY}] {today} seat={st['held_symbol'] or 'CASH'} "
          f"book ${val:.2f} (cap ${binance_live.BOOK_CAP_USD:.0f}) — "
          f"ticket odds printed in the docstring")


if __name__ == "__main__":
    main()
