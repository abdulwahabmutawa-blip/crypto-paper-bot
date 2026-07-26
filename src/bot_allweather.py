"""All-Weather Control bot — the fleet's boring benchmark-with-a-seatbelt.

Fixed allocation (30% SPY / 40% TLT / 15% GLD / 7.5% DBC / 7.5% BIL),
rebalanced on the first cycle of each month. No signals, no forecasts —
the control group every fancy bot must justify itself against.
Lab: only +7.5%/yr since 2010, but max drawdown -22% ever, -6.6% since 2024.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config
import market_hours

W = {"SPY": 0.30, "TLT": 0.40, "GLD": 0.15, "DBC": 0.075, "BIL": 0.075}
BENCH = "SPY"
KEY = "allweather"
START_CASH = 1000.0
STATE = config.DATA / f"{KEY}_state.json"


def quotes():
    tickers = sorted(set(W) | {BENCH})
    raw = yf.download(tickers, period="5d", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    close = market_hours.trim_incomplete_bars(close).ffill()
    last = close.iloc[-1]
    return {t: float(last[t]) for t in tickers}, str(close.index[-1].date())


def main():
    px, asof = quotes()
    now = datetime.now(timezone.utc)
    st = json.loads(STATE.read_text()) if STATE.exists() else None

    if st is None:
        st = {"created": asof, "starting_cash": START_CASH,
              "units": {t: START_CASH * w / px[t] for t, w in W.items()},
              "last_rebalance_month": asof[:7],
              "bench_units": START_CASH / px[BENCH],
              "trades": [{"date": asof, "action": "ALLOCATE", "ticker": t,
                          "price": round(px[t], 2),
                          "units": round(START_CASH * w / px[t], 4),
                          "value": round(START_CASH * w, 2),
                          "reason": f"Initial allocation {w:.1%}"}
                         for t, w in W.items()],
              "history": [], "intraday": []}
        print(f"[{KEY}] NEW sim {asof}")

    val = sum(u * px[t] for t, u in st["units"].items())

    # monthly rebalance back to target weights
    if asof[:7] != st["last_rebalance_month"]:
        for t, w in W.items():
            target_units = val * w / px[t]
            delta = target_units - st["units"][t]
            if abs(delta * px[t]) >= 1:
                st["trades"].append({"date": asof,
                                     "action": "REBAL+" if delta > 0 else "REBAL-",
                                     "ticker": t, "price": round(px[t], 2),
                                     "units": round(abs(delta), 4),
                                     "value": round(abs(delta) * px[t], 2),
                                     "reason": f"Monthly rebalance to {w:.1%}"})
            st["units"][t] = target_units
        st["last_rebalance_month"] = asof[:7]
        print(f"[{KEY}] monthly rebalance done")

    bench = st["bench_units"] * px[BENCH]
    st["history"] = sorted([h for h in st["history"] if h["date"] != asof]
                           + [{"date": asof, "value": round(val, 2),
                               "bench": round(bench, 2), "holding": "5 assets"}],
                           key=lambda h: h["date"])
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["intraday"] = [p for p in st.get("intraday", [])
                      if p["ts"] != st["last_updated_utc"]][-1499:] + [
        {"ts": st["last_updated_utc"], "value": round(val, 2),
         "bench": round(bench, 2), "holding": "5 assets"}]
    STATE.write_text(json.dumps(st, indent=2))

    board = []
    for t, w in W.items():
        cur_w = st["units"][t] * px[t] / val
        board.append({"sym": t, "price": round(px[t], 2),
                      "line": f"target {w:.1%} · now {cur_w:.1%} · "
                              f"${st['units'][t]*px[t]:,.0f}",
                      "tag": "held", "on": True, "pick": False,
                      "fill": min(50, cur_w * 100)})

    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": START_CASH, "live_ts": st["last_updated_utc"],
        "current": st["history"][-1], "board": board,
        "board_title": "Fixed allocation, rebalanced monthly",
        "meta": {
            "title": "All-Weather Control — $1,000 Challenge",
            "badge": "PAPER SIM · CONTROL GROUP",
            "bench_label": "SPY benchmark ($1,000 same day)",
            "board_note": "No signals, no forecasts, no cleverness — the "
                          "diversified do-nothing portfolio every other bot "
                          "has to beat to justify its complexity.",
        },
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"],
        "strategy": {
            "name": "All-Weather Control (Dalio-style)",
            "rule": "30% stocks / 40% long bonds / 15% gold / 7.5% "
                    "commodities / 7.5% T-bills, rebalanced monthly",
            "backtest_cagr": "+7.5%/yr since 2010 · +11.5%/yr 2024+",
            "backtest_maxdd": "-22% worst ever · only -6.6% since 2024",
        },
    }
    (config.REPORTS / f"{KEY}_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "fleet_dashboard_template.html").read_text(
        encoding="utf-8")
    html = template.replace("/*__DATA__*/", json.dumps(payload)).replace(
        "__DATAFILE__", f"{KEY}_dashboard_data.json")
    (config.REPORTS / f"{KEY}_dashboard.html").write_text(html, encoding="utf-8")
    print(f"[{KEY}] {asof} value ${val:,.2f} vs SPY ${bench:,.2f}")


if __name__ == "__main__":
    main()
