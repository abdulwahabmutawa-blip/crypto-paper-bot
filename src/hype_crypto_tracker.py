"""Hype Crypto Trader — bot #12 ($1,000 paper + Binance testnet shadow).

PRE-REGISTERED SPEC (written 2026-08-15, BEFORE any results — amendments are
human commits). Hypothesis: the sentiment bot's mechanical hype pattern
(buy fresh euphoria, exit the moment it fades from scans; 10/13 winners over
28 days on equities) transfers to crypto, where Binance's percentage-only
fees don't punish a small book the way IBKR's $1 minimum does.

Rules (all mechanical, none waivable):
  * Universe: crypto only — Watcher euphoric symbols that map to USDT pairs.
  * ENTRY: top euphoric crypto from the LATEST scan, and only while that scan
    is fresh (<= 9h old): stale hype is not hype. Max ONE new entry per UTC
    day (fee math: worst case ~30 sides/month ≈ 4%/month at Binance tier).
    No weekend entries (the SHIB Saturday lesson was a crypto lesson).
  * EXIT, in priority order: hard stop -10% from entry (any time, 24/7);
    Watcher SEVERE -> flat; scans stale >24h -> flat (flying blind is not a
    strategy); symbol absent from the euphoric list of a scan NEWER than the
    entry scan -> rotate or cash. No exit on the entry scan itself — one
    scan, one opinion, no same-scan flip-flop.
  * Stopped coin is blacklisted until a NEWER scan lists it euphoric again.
  * R1 kill floor $750, code-enforced, permanent freeze (risk_common).
  * Fees: Binance spot tier (10bps + half-spread) on every side — the
    venue-of-intent's real price, not the Kraken model.
  * Every fill is shadowed to the Binance SPOT TESTNET (binance_broker) —
    plumbing realism from day one.

Benchmark: $1,000 BTC buy-and-hold (crypto book, crypto bar).
Promotion to real money: Track C gate only (GO_LIVE_PLAN_2026-08-14.md) —
4+ weeks, net-positive after fees, ahead of benchmark, zero silent failures.
PAPER MONEY. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config
import market_hours
import risk_common
import sentinel_gate
from sentinel_trader import CRYPTO, scan_age_hours, scan_is_stale, to_ticker

STATE = config.DATA / "hypecrypto_state.json"
SENTINEL = config.DATA / "sentinel_state.json"
BENCH = "BTC-USD"
START_CASH = 1000.0
STOP_PCT = -0.10
ENTRY_FRESH_H = 9.0          # entries only on a genuinely fresh scan
MAX_ENTRIES_PER_DAY = 1
KEY = "hypecrypto"


def crypto_candidates(scan: dict | None) -> list[str]:
    """Euphoric crypto candidates, most explosive first.

    Preferred source: the Watcher's DEDICATED crypto_hype section (added
    2026-08-15) — its symbols are coins by construction, so no whitelist
    filter applies and a memecoin outside the CRYPTO set still qualifies.
    Fallback for older scans: euphoric entries of the mixed hype list that
    match the known-coin set. Tradability is enforced downstream by each
    consumer's own price source (yfinance for the paper twin, Binance for
    the lottery), never here."""
    out = []
    for h in (scan or {}).get("crypto_hype", []):
        if h.get("mood") != "euphoric":
            continue
        s = str(h.get("symbol", "")).upper().lstrip("$").replace("-USD", "")
        if s and s.isalnum():
            out.append(f"{s}-USD")
    if out:
        return out
    for h in (scan or {}).get("hype", []):
        if h.get("mood") != "euphoric":
            continue
        s = str(h.get("symbol", "")).upper().lstrip("$")
        if s in CRYPTO:
            out.append(f"{s}-USD")
    return out


def quotes(tickers):
    tickers = sorted(set(tickers) | {BENCH})
    raw = yf.download(tickers, period="5d", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    if isinstance(close, pd.Series):
        close = close.to_frame(tickers[0])
    close = market_hours.trim_incomplete_bars(close)
    filled = close.ffill()
    last = filled.iloc[-1]
    return ({t: float(last[t]) for t in tickers
             if t in filled.columns and pd.notna(last[t])}, close)


def main():
    now = datetime.now(timezone.utc)
    today = str(now.date())

    sent = json.loads(SENTINEL.read_text()) if SENTINEL.exists() else {"scans": []}
    scan = sent["scans"][-1] if sent["scans"] else None
    scan_ts = scan["ts"] if scan else ""
    age_h = scan_age_hours(scan)
    stale = scan_is_stale(scan)
    fresh = age_h is not None and age_h <= ENTRY_FRESH_H
    severe = bool(scan and scan.get("risk_level") == "severe")
    cands = crypto_candidates(scan)

    st = json.loads(STATE.read_text()) if STATE.exists() else None
    if st is None:
        px0, _ = quotes([])
        if BENCH not in px0:
            print(f"[{KEY}] no benchmark price — cannot initialize")
            return
        st = {"created": today, "starting_cash": START_CASH, "holding": "CASH",
              "units": 0.0, "cash": START_CASH, "entry_price": None,
              "entry_scan_ts": None, "bench_units": START_CASH / px0[BENCH],
              "stopped": {}, "entries": {}, "trades": [], "history": [],
              "intraday": []}
        print(f"[{KEY}] NEW sim {today}")

    px, rawc = quotes(cands + ([st["holding"]] if st["holding"] != "CASH" else []))
    tradeable = [t for t in cands if t in px]

    def sell(reason) -> bool:
        p = px.get(st["holding"])
        if p is None:
            print(f"[{KEY}] held {st['holding']} has no quote — sale deferred")
            return False
        gross = st["units"] * p
        f = risk_common.binance_fee(gross)
        st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
        st["trades"].append({"date": today, "action": "SELL",
                             "ticker": st["holding"], "price": round(p, 8),
                             "units": round(st["units"], 6),
                             "value": round(gross, 2), "fee": round(f, 2),
                             "reason": reason})
        import binance_broker
        bf = binance_broker.shadow_fill("SELL", st["holding"], gross)
        if bf:
            st["trades"][-1]["testnet_fill"] = round(bf["price"], 8)
            st["trades"][-1]["fill_gap_bps"] = round((bf["price"] / p - 1) * 10_000, 2)
        st["cash"], st["holding"], st["units"] = gross - f, "CASH", 0.0
        st["entry_price"], st["entry_scan_ts"] = None, None
        return True

    # 1) hard stop — crypto fills 24/7, no market-hours wait
    if st["holding"] != "CASH" and st["holding"] in px and st["entry_price"]:
        chg = px[st["holding"]] / st["entry_price"] - 1
        if chg <= STOP_PCT:
            st["stopped"][st["holding"]] = scan_ts
            sell(f"STOP-LOSS ({chg:.1%} from entry) — hype that bleeds gets cut")

    # 2) severe -> flat, no exceptions
    if severe and st["holding"] != "CASH":
        sell("Watcher SEVERE — no hype positions in a crisis")

    # 3) stale scans -> flat (the 08-07..08-13 lesson, inherited at birth)
    if stale and st["holding"] != "CASH":
        sell(f"Grok scans stale ({age_h:.0f}h) — hype unverifiable, exiting")

    # 4) hype faded — only judged by a scan NEWER than the entry scan
    if (st["holding"] != "CASH" and not stale and scan_ts
            and st.get("entry_scan_ts") and scan_ts > st["entry_scan_ts"]
            and st["holding"] not in tradeable):
        sell("Hype faded — coin dropped off a newer euphoric scan")

    # 5) R1 kill floor
    r1_hit = False
    if not st.get("frozen"):
        hp = px.get(st["holding"]) if st["holding"] != "CASH" else None
        cur_val = st["cash"] if st["holding"] == "CASH" \
            else (st["units"] * hp if hp is not None else None)
        if cur_val is not None and risk_common.r1_breached(cur_val):
            r1_hit = True
            print(f"[{KEY}] {risk_common.r1_reason(cur_val)}")
            if st["holding"] != "CASH":
                sell(risk_common.r1_reason(cur_val))
            if st["holding"] == "CASH":
                st["frozen"] = {"date": today,
                                "rule": "R1 kill floor (kill_criteria.md)"}
                print(f"[{KEY}] book FROZEN — un-freezing is a human decision")

    # 6) entry — one per day, fresh scan only, weekdays only, not blacklisted
    blacklisted = {t for t, ts in st["stopped"].items() if ts == scan_ts}
    entries_today = st.get("entries", {}).get(today, 0)
    can_enter = (st["holding"] == "CASH" and not (severe or stale or r1_hit)
                 and not st.get("frozen") and fresh
                 and now.weekday() < 5
                 and entries_today < MAX_ENTRIES_PER_DAY)
    if can_enter:
        avail = [t for t in tradeable if t not in blacklisted]
        if avail:
            pick = avail[0]
            p = px[pick]
            base = pick.replace("-USD", "")
            h = next((h for h in (scan.get("crypto_hype", [])
                                  + scan.get("hype", []))
                      if str(h.get("symbol", "")).upper().lstrip("$")
                      .replace("-USD", "") == base),
                     {"symbol": base, "note": ""})
            f = risk_common.binance_fee(st["cash"])
            invest = st["cash"] - f
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
            st["units"], st["cash"] = invest / p, 0.0
            st["holding"], st["entry_price"] = pick, p
            st["entry_scan_ts"] = scan_ts
            st.setdefault("entries", {})
            st["entries"] = {d: c for d, c in st["entries"].items() if d >= today}
            st["entries"][today] = entries_today + 1
            st["trades"].append({"date": today, "action": "BUY", "ticker": pick,
                                 "price": round(p, 8),
                                 "units": round(st["units"], 6),
                                 "value": round(invest, 2), "fee": round(f, 2),
                                 "reason": f"Grok: {h['symbol']} euphoric — "
                                           f"{h.get('note','')} (scan {scan_ts[:16]})"})
            import binance_broker
            bf = binance_broker.shadow_fill("BUY", pick, invest)
            if bf:
                st["trades"][-1]["testnet_fill"] = round(bf["price"], 8)
                st["trades"][-1]["fill_gap_bps"] = round(
                    (bf["price"] / p - 1) * 10_000, 2)

    # 7) mark to market — crypto has a bar every day; guard missing quotes
    if st["holding"] != "CASH" and st["holding"] not in px:
        print(f"[{KEY}] held {st['holding']} has no quote — mark skipped")
        STATE.write_text(json.dumps(st, indent=2))
        return
    val = st["cash"] if st["holding"] == "CASH" else st["units"] * px[st["holding"]]
    bench = st["bench_units"] * px[BENCH]
    priced = BENCH if st["holding"] == "CASH" else st["holding"]
    asof = market_hours.last_real_date(rawc, priced) or today
    newest = st["history"][-1]["date"] if st["history"] else ""
    if asof < newest:
        print(f"[{KEY}] STALE BAR {asof} < {newest} — mark skipped")
    else:
        st["history"] = sorted(
            [h for h in st["history"] if h["date"] != asof]
            + [{"date": asof, "value": round(val, 2), "bench": round(bench, 2),
                "holding": st["holding"]}], key=lambda h: h["date"])
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["intraday"] = [p_ for p_ in st.get("intraday", [])
                      if p_["ts"] != st["last_updated_utc"]][-1499:] + [
        {"ts": st["last_updated_utc"], "value": round(val, 2),
         "bench": round(bench, 2), "holding": st["holding"]}]
    STATE.write_text(json.dumps(st, indent=2))

    # 8) dashboard (shared fleet template)
    board = []
    board_src = (scan or {}).get("crypto_hype") or (scan or {}).get("hype", [])
    for h in board_src:
        s = str(h.get("symbol", "")).upper().lstrip("$").replace("-USD", "")
        t = f"{s}-USD" if (scan or {}).get("crypto_hype") else to_ticker(s)
        if not t.endswith("-USD"):
            continue
        mood = h.get("mood", "mixed")
        board.append({
            "sym": str(h.get("symbol", "")).upper(), "price": round(px.get(t, 0), 4),
            "line": f"{mood} · {h.get('note','')[:40]}",
            "tag": "HELD" if t == st["holding"] else
                   ("stopped" if t in blacklisted else
                    ("candidate" if mood == "euphoric" and t in px else mood)),
            "on": mood == "euphoric", "pick": t == st["holding"],
            "fill": 40 if mood == "euphoric" else (-40 if mood == "fearful" else 0),
        })
    stale_note = ("" if not stale else
                  f" · ⚠️ STALE {age_h:.0f}h — trading suspended" if age_h is not None
                  else " · ⚠️ NO SCAN — trading suspended")
    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": START_CASH, "live_ts": st["last_updated_utc"],
        "current": st["history"][-1], "board": board,
        "board_title": f"Grok's crypto hype read (scan {scan_ts[:16] or 'pending'})"
                       + stale_note,
        "meta": {
            "title": "Hype Crypto — $1,000 Challenge",
            "badge": "PAPER + TESTNET SHADOW · CRYPTO HYPE ON TRIAL",
            "bench_label": "BTC buy & hold ($1,000 same day)",
            "board_note": "Crypto-only twin of the Hype Trader: buys the "
                          "loudest fresh euphoria (one entry/day, weekdays), "
                          "cuts at -10%, exits when a newer scan stops being "
                          "euphoric — and pays Binance-tier fees on every fill.",
        },
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"], "costs_paid": st.get("costs_paid", 0.0),
        "frozen": st.get("frozen"),
        "thoughts": (
            (f"⚠️ Scans are {'missing' if age_h is None else f'{age_h:.0f}h old'} — "
             f"no fresh hype exists, so I hold nothing and buy nothing.\n\n"
             if stale else "")
            + (f"I'm riding {st['holding'].replace('-USD','')} from the "
               f"{str(st.get('entry_scan_ts',''))[:16]} scan. My exit is "
               f"mechanical: a newer scan without it, -10% from entry, or a "
               f"blind/severe Watcher — whichever comes first."
               if st["holding"] != "CASH" else
               "I'm in cash. I buy only the freshest euphoric crypto (scan "
               "under 9h old), one entry a day, never on weekends — lukewarm "
               "or aging hype is how small accounts bleed out in fees.")),
        "strategy": {
            "name": "Hype Crypto — sentiment pattern, crypto venue, on trial",
            "rule": "Top euphoric crypto from a fresh Watcher scan; 1 entry/"
                    "day max; -10% hard stop; exit on newer scan without the "
                    "coin, stale scans, or SEVERE; Binance-tier fees",
            "backtest_cagr": "NONE — pre-registered live test; the sentiment "
                             "bot's 28-day equity record is the only prior",
            "backtest_maxdd": "unknown · stop caps single-trade loss at ~10%",
        },
    }
    (config.REPORTS / f"{KEY}_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "fleet_dashboard_template.html").read_text(
        encoding="utf-8")
    (config.REPORTS / f"{KEY}_dashboard.html").write_text(
        template.replace("/*__DATA__*/", json.dumps(payload)).replace(
            "__DATAFILE__", f"{KEY}_dashboard_data.json"), encoding="utf-8")
    print(f"[{KEY}] {today} holding {st['holding']} value ${val:,.2f} "
          f"vs BTC ${bench:,.2f} | crypto euphoric: "
          f"{[c.replace('-USD','') for c in cands] or 'none'}"
          f"{' | SCANS STALE' if stale else ''}")


if __name__ == "__main__":
    main()
