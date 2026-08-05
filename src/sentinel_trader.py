"""Sentinel Hype Trader — bot #7's trading book ($1,000 paper).

Trades the Grok Sentinel's own scans (data/sentinel_state.json — no extra API
cost). Fully mechanical:
  * Candidates = symbols Grok marked "euphoric" in the LATEST scan, in order.
  * Hold the first tradeable candidate; KEEP holding while it stays euphoric.
  * Hype faded (symbol gone) -> rotate to the new top candidate, else cash.
  * HARD STOP: -10% from entry -> cash, and that symbol is blacklisted until
    a fresh scan arrives. First bot in the fleet with a stop-loss.
  * Sentinel risk_level == "severe" -> no buying; existing position is sold.
Benchmark: $1,000 SPY. Honest note: sentiment-chasing is the weakest-evidence
strategy in the fleet — that is WHY it carries the strictest guards.
PAPER MONEY ONLY. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config
import market_hours
import risk_common

STATE = config.DATA / "sentiment_state.json"
SENTINEL = config.DATA / "sentinel_state.json"
BENCH = "SPY"
START_CASH = 1000.0
STOP_PCT = -0.10
KEY = "sentiment"

CRYPTO = set(("BTC ETH SOL DOGE XRP ADA AVAX LINK RUNE SHIB PEPE BNB TON "
              "SUI APT ARB OP LTC BCH DOT NEAR").split())


def to_ticker(sym: str) -> str:
    s = sym.upper().lstrip("$")
    return f"{s}-USD" if s in CRYPTO else s


def quotes(tickers):
    """Returns (prices, raw_frame). The caller dates its mark off the raw
    (pre-ffill) frame via market_hours.last_real_date: a mark must be filed
    under the session it reflects, and this book mixes crypto (which has
    weekend bars) with an equity benchmark (which does not)."""
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
    severe = bool(scan and scan.get("risk_level") == "severe")
    hype = (scan or {}).get("hype", [])
    euphoric = [h for h in hype if h.get("mood") == "euphoric"]

    st = json.loads(STATE.read_text()) if STATE.exists() else None
    if st is None:
        px0, _ = quotes([])
        st = {"created": today, "starting_cash": START_CASH, "holding": "CASH",
              "units": 0.0, "cash": START_CASH, "entry_price": None,
              "bench_units": START_CASH / px0[BENCH],
              "stopped": {}, "trades": [], "history": [], "intraday": []}
        print(f"[{KEY}] NEW sim {today}")

    cand_map = {to_ticker(h["symbol"]): h for h in euphoric}
    px, rawc = quotes(list(cand_map)
                      + ([st["holding"]] if st["holding"] != "CASH" else []))
    tradeable = [t for t in cand_map if t in px]

    def sell(reason) -> bool:
        """Returns True only if the sale actually filled. A missing quote
        used to liquidate silently AT ENTRY PRICE with no trade record —
        P/L erased, $0 wipe if entry_price was unset (audit 2026-08-05).
        Now: no quote, no trade, position held, loud log."""
        p = px.get(st["holding"])
        if p is None:
            print(f"[{KEY}] held {st['holding']} has no quote — sale deferred, "
                  f"position kept, nothing recorded")
            return False
        gross = st["units"] * p
        f = risk_common.fee(st["holding"], gross)
        st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
        st["trades"].append({"date": today, "action": "SELL",
                             "ticker": st["holding"], "price": round(p, 8),
                             "units": round(st["units"], 4),
                             "value": round(gross, 2), "fee": round(f, 2),
                             "reason": reason})
        st["cash"], st["holding"], st["units"] = gross - f, "CASH", 0.0
        st["entry_price"] = None
        return True

    import market_hours

    # 1) hard stop-loss (fills only when the holding's market is open —
    #    a closed market has no tradable price, so the stop waits for one)
    if st["holding"] != "CASH" and st["holding"] in px and st["entry_price"] \
            and market_hours.can_fill(st["holding"]):
        chg = px[st["holding"]] / st["entry_price"] - 1
        if chg <= STOP_PCT:
            st["stopped"][st["holding"]] = scan_ts
            sell(f"STOP-LOSS hit ({chg:.1%} from entry) — hype that bleeds gets cut")

    # 2) severe risk -> flat, no exceptions (as soon as a fill is possible)
    if severe and st["holding"] != "CASH" and market_hours.can_fill(st["holding"]):
        sell("Watcher risk verdict SEVERE — no hype positions in a crisis")

    # 2.5) R1 kill floor, code-enforced (audit 2026-08-05)
    r1_hit = False
    if not st.get("frozen"):
        hp = px.get(st["holding"]) if st["holding"] != "CASH" else None
        cur_val = st["cash"] if st["holding"] == "CASH" \
            else (st["units"] * hp if hp is not None else None)
        if cur_val is not None and risk_common.r1_breached(cur_val):
            r1_hit = True
            print(f"[{KEY}] {risk_common.r1_reason(cur_val)}")
            if st["holding"] != "CASH" and market_hours.can_fill(st["holding"]):
                sell(risk_common.r1_reason(cur_val))
            if st["holding"] == "CASH":
                st["frozen"] = {"date": today,
                                "rule": "R1 kill floor (kill_criteria.md)"}
                print(f"[{KEY}] book FROZEN — un-freezing is a human decision")

    # 3) decide desired holding
    blacklisted = {t for t, ts in st["stopped"].items() if ts == scan_ts}
    if severe or r1_hit or st.get("frozen"):
        desired = "CASH"
    elif st["holding"] != "CASH" and st["holding"] in tradeable:
        desired = st["holding"]                     # hype still alive -> ride it
    else:
        avail = [t for t in tradeable if t not in blacklisted]
        desired = avail[0] if avail else "CASH"

    sell_ok = st["holding"] == "CASH" or market_hours.can_fill(st["holding"])
    buy_ok = desired == "CASH" or market_hours.can_fill(desired)
    if desired != st["holding"] and not (sell_ok and buy_ok):
        print(f"[{KEY}] rotation {st['holding']} -> {desired} deferred — "
              f"US market closed, will fill at the open")
    if desired != st["holding"] and sell_ok and buy_ok:
        rotated = True
        if st["holding"] != "CASH":
            rotated = sell("Hype faded — symbol dropped off Grok's euphoric list")
        if rotated and desired != "CASH":
            p = px[desired]
            h = cand_map[desired]
            f = risk_common.fee(desired, st["cash"])
            invest = st["cash"] - f
            st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
            st["units"] = invest / p
            st["cash"] = 0.0
            st["holding"] = desired
            st["entry_price"] = p
            st["trades"].append({"date": today, "action": "BUY",
                                 "ticker": desired, "price": round(p, 8),
                                 "units": round(st["units"], 4),
                                 "value": round(invest, 2), "fee": round(f, 2),
                                 "reason": f"Grok: {h['symbol']} euphoric — "
                                           f"{h.get('note','')} (scan {scan_ts[:16]})"})

    # 4) mark to market (guard: never mark a holding that has no quote)
    if st["holding"] != "CASH" and st["holding"] not in px:
        print(f"[{KEY}] held {st['holding']} has no quote — mark skipped, "
              f"state saved unchanged")
        STATE.write_text(json.dumps(st, indent=2))
        return
    val = st["cash"] if st["holding"] == "CASH" else st["units"] * px[st["holding"]]
    bench = st["bench_units"] * px[BENCH]
    # date the mark by the asset that determines its value (crypto trades
    # weekends; the equity bench does not), never by the wall clock
    priced = BENCH if st["holding"] == "CASH" else st["holding"]
    asof = market_hours.last_real_date(rawc, priced) or str(now.date())
    bench_asof = market_hours.last_real_date(rawc, BENCH)
    newest = st["history"][-1]["date"] if st["history"] else ""
    if asof < newest:
        print(f"[{KEY}] STALE BAR {asof} < newest mark {newest} — "
              f"mark skipped (feed served an old bar)")
    else:
        row = {"date": asof, "value": round(val, 2),
               "bench": round(bench, 2), "holding": st["holding"]}
        if bench_asof and bench_asof != asof:
            row["bench_asof"] = bench_asof      # bench ffilled to reach here
        st["history"] = sorted([h for h in st["history"] if h["date"] != asof]
                               + [row], key=lambda h: h["date"])
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["intraday"] = [p_ for p_ in st.get("intraday", [])
                      if p_["ts"] != st["last_updated_utc"]][-1499:] + [
        {"ts": st["last_updated_utc"], "value": round(val, 2),
         "bench": round(bench, 2), "holding": st["holding"]}]
    STATE.write_text(json.dumps(st, indent=2))

    # 5) dashboard (shared fleet template)
    board = []
    for h in hype:
        t = to_ticker(h["symbol"])
        mood = h.get("mood", "mixed")
        board.append({
            "sym": h["symbol"].upper(), "price": round(px.get(t, 0), 2),
            "line": f"{mood} · {h.get('note','')[:40]}",
            "tag": "HELD" if t == st["holding"] else
                   ("stopped" if t in blacklisted else
                    ("candidate" if mood == "euphoric" and t in px else mood)),
            "on": mood == "euphoric", "pick": t == st["holding"],
            "fill": 40 if mood == "euphoric" else (-40 if mood == "fearful" else 0),
        })
    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": START_CASH, "live_ts": st["last_updated_utc"],
        "current": st["history"][-1], "board": board,
        "board_title": f"Grok's latest hype read (scan {scan_ts[:16] or 'pending'}, "
                       f"risk {scan.get('risk_level') if scan else '—'})",
        "meta": {
            "title": "Hype Trader — $1,000 Challenge",
            "badge": "PAPER SIM · SENTIMENT ON TRIAL",
            "bench_label": "SPY benchmark ($1,000 same day)",
            "board_note": "Buys the crowd's loudest euphoria, rides it while "
                          "it lasts, cuts it at -10%, and refuses to trade "
                          "in a severe-risk tape. Weakest-evidence strategy "
                          "in the fleet — hence the strictest guards.",
        },
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"],
        "costs_paid": st.get("costs_paid", 0.0),
        "frozen": st.get("frozen"),
        "thoughts": (
            (f"I'm riding {st['holding'].replace('-USD','')} because the Watcher's "
             f"latest scan of X and the news says the crowd is most excited about "
             f"it right now. I know hype is the weakest evidence there is — so my "
             f"rules are the strictest in the fleet: the moment the excitement "
             f"fades from the scans I sell, and if I'm down 10% from my buy price "
             f"I sell no matter what."
             if st["holding"] != "CASH" else
             "I'm in cash. The crowd isn't truly excited about anything on the "
             "latest scan — and I only ever buy genuine euphoria. Chasing "
             "lukewarm hype is how sentiment traders lose; I wait for a loud one.")),
        "strategy": {
            "name": "Hype Trader — rides the Watcher's reads, on trial",
            "rule": "Hold the top euphoric symbol from the Watcher's 8-hour "
                    "Grok scans while it stays euphoric; -10% hard stop; "
                    "Watcher severe verdict -> cash",
            "backtest_cagr": "NONE — sentiment can't be backtested honestly; "
                             "this live run IS the test",
            "backtest_maxdd": "unknown · stop-loss caps single-trade loss at ~10%",
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
          f"vs SPY ${bench:,.2f} | euphoric candidates: "
          f"{[h['symbol'] for h in euphoric] or 'none'}")


if __name__ == "__main__":
    main()
