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


def quotes(tickers) -> dict:
    tickers = sorted(set(tickers) | {BENCH})
    raw = yf.download(tickers, period="5d", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    if isinstance(close, pd.Series):
        close = close.to_frame(tickers[0])
    close = close.ffill()
    last = close.iloc[-1]
    return {t: float(last[t]) for t in tickers
            if t in close.columns and pd.notna(last[t])}


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
        px0 = quotes([])
        st = {"created": today, "starting_cash": START_CASH, "holding": "CASH",
              "units": 0.0, "cash": START_CASH, "entry_price": None,
              "bench_units": START_CASH / px0[BENCH],
              "stopped": {}, "trades": [], "history": [], "intraday": []}
        print(f"[{KEY}] NEW sim {today}")

    cand_map = {to_ticker(h["symbol"]): h for h in euphoric}
    px = quotes(list(cand_map) + ([st["holding"]] if st["holding"] != "CASH" else []))
    tradeable = [t for t in cand_map if t in px]

    def sell(reason):
        p = px.get(st["holding"])
        if p is None:
            st["cash"], st["holding"], st["units"] = st["units"] * (st["entry_price"] or 0), "CASH", 0.0
            return
        val = st["units"] * p
        st["trades"].append({"date": today, "action": "SELL",
                             "ticker": st["holding"], "price": round(p, 2),
                             "units": round(st["units"], 4),
                             "value": round(val, 2), "reason": reason})
        st["cash"], st["holding"], st["units"] = val, "CASH", 0.0
        st["entry_price"] = None

    # 1) hard stop-loss
    if st["holding"] != "CASH" and st["holding"] in px and st["entry_price"]:
        chg = px[st["holding"]] / st["entry_price"] - 1
        if chg <= STOP_PCT:
            st["stopped"][st["holding"]] = scan_ts
            sell(f"STOP-LOSS hit ({chg:.1%} from entry) — hype that bleeds gets cut")

    # 2) severe risk -> flat, no exceptions
    if severe and st["holding"] != "CASH":
        sell("Sentinel risk verdict SEVERE — no hype positions in a crisis")

    # 3) decide desired holding
    blacklisted = {t for t, ts in st["stopped"].items() if ts == scan_ts}
    if severe:
        desired = "CASH"
    elif st["holding"] != "CASH" and st["holding"] in tradeable:
        desired = st["holding"]                     # hype still alive -> ride it
    else:
        avail = [t for t in tradeable if t not in blacklisted]
        desired = avail[0] if avail else "CASH"

    if desired != st["holding"]:
        if st["holding"] != "CASH":
            sell("Hype faded — symbol dropped off Grok's euphoric list")
        if desired != "CASH":
            p = px[desired]
            h = cand_map[desired]
            invest = st["cash"]
            st["units"] = invest / p
            st["cash"] = 0.0
            st["holding"] = desired
            st["entry_price"] = p
            st["trades"].append({"date": today, "action": "BUY",
                                 "ticker": desired, "price": round(p, 2),
                                 "units": round(st["units"], 4),
                                 "value": round(invest, 2),
                                 "reason": f"Grok: {h['symbol']} euphoric — "
                                           f"{h.get('note','')} (scan {scan_ts[:16]})"})

    # 4) mark to market
    val = st["cash"] if st["holding"] == "CASH" else st["units"] * px[st["holding"]]
    bench = st["bench_units"] * px[BENCH]
    st["history"] = sorted([h for h in st["history"] if h["date"] != today]
                           + [{"date": today, "value": round(val, 2),
                               "bench": round(bench, 2), "holding": st["holding"]}],
                           key=lambda h: h["date"])
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
            "title": "Sentinel Hype Trader — $1,000 Challenge",
            "badge": "PAPER SIM · SENTIMENT ON TRIAL",
            "bench_label": "SPY benchmark ($1,000 same day)",
            "board_note": "Buys the crowd's loudest euphoria, rides it while "
                          "it lasts, cuts it at -10%, and refuses to trade "
                          "in a severe-risk tape. Weakest-evidence strategy "
                          "in the fleet — hence the strictest guards.",
        },
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"],
        "strategy": {
            "name": "Hype Rider — sentiment as a signal, on trial",
            "rule": "Hold the top euphoric symbol from the Sentinel's 8-hour "
                    "Grok scans while it stays euphoric; -10% hard stop; "
                    "severe risk verdict -> cash",
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
