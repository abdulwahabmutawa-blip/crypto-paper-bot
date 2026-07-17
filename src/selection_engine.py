"""Generic single-position paper-trading engine for fleet bots.

A bot supplies a SPEC dict; the engine handles state, live quotes, trades,
mark-to-market, and dashboard rendering (shared fleet template).

SPEC = {
  "key": "meanrev",                # file prefix for state/dashboard
  "universe": [...tickers...],
  "bench": "SPY",
  "signal": fn(close_df, holding) -> (pick_or_CASH, board_rows, board_title),
  "meta": {title, badge, bench_label, board_note},
  "strategy": {name, rule, backtest_cagr, backtest_maxdd, note},
}
board_rows: [{sym, price, line, tag, on(bool), fill(-50..50)}] for the screen.
PAPER MONEY ONLY. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config


def _fetch_daily(universe, bench):
    tickers = sorted(set(universe) | {bench})
    raw = yf.download(tickers, period="15mo", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    return close.dropna(how="all").ffill()


def _fetch_live(universe, bench):
    tickers = sorted(set(universe) | {bench})
    raw = yf.download(tickers, period="5d", interval="5m", auto_adjust=True,
                      progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    close = close.ffill()
    last = close.iloc[-1]
    ts = close.index[-1]
    ts = ts.tz_convert("UTC") if ts.tzinfo else ts.tz_localize("UTC")
    return ({t: float(last[t]) for t in tickers if t in close.columns
             and pd.notna(last[t])}, ts.isoformat(timespec="seconds"))


def run(spec, start_cash=1000.0):
    key = spec["key"]
    state_path = config.DATA / f"{key}_state.json"
    close = _fetch_daily(spec["universe"], spec["bench"])
    live, live_ts = _fetch_live(spec["universe"], spec["bench"])
    for t, p in live.items():
        if t in close.columns:
            close.iloc[-1, close.columns.get_loc(t)] = p

    st = json.loads(state_path.read_text()) if state_path.exists() else None
    holding = st["holding"] if st else "CASH"
    pick, board, board_title = spec["signal"](close, holding)

    # Sentinel override (default on; All-Weather doesn't use this engine and
    # stays deliberately unwired as the control group).
    if spec.get("risk_gate", True):
        import sentinel_gate
        is_severe, why = sentinel_gate.severe()
        if is_severe and pick != "CASH":
            print(f"[{key}] {why} -> forcing CASH")
            pick = "CASH"

    last = close.iloc[-1]
    asof = str(close.index[-1].date())
    now = datetime.now(timezone.utc)

    if st is None:
        st = {"created": asof, "starting_cash": start_cash, "holding": "CASH",
              "units": 0.0, "cash": start_cash,
              "bench_units": start_cash / float(last[spec["bench"]]),
              "trades": [], "history": [], "intraday": []}
        print(f"[{key}] NEW sim {asof}")

    if pick != st["holding"]:
        value = st["cash"] if st["holding"] == "CASH" else st["units"] * float(last[st["holding"]])
        if st["holding"] != "CASH":
            st["trades"].append({"date": asof, "action": "SELL",
                                 "ticker": st["holding"],
                                 "price": round(float(last[st["holding"]]), 2),
                                 "units": round(st["units"], 4),
                                 "value": round(value, 2), "reason": "Signal flip"})
        if pick == "CASH":
            st["holding"], st["units"], st["cash"] = "CASH", 0.0, value
            st["trades"].append({"date": asof, "action": "TO CASH", "ticker": "—",
                                 "price": 0, "units": 0, "value": round(value, 2),
                                 "reason": spec.get("cash_reason", "No qualifying signal")})
        else:
            p = float(last[pick])
            st["holding"], st["units"], st["cash"] = pick, value / p, 0.0
            st["trades"].append({"date": asof, "action": "BUY", "ticker": pick,
                                 "price": round(p, 2),
                                 "units": round(st["units"], 4),
                                 "value": round(value, 2),
                                 "reason": spec.get("buy_reason", "New signal pick")})

    val = st["cash"] if st["holding"] == "CASH" else st["units"] * float(last[st["holding"]])
    bench = st["bench_units"] * float(last[spec["bench"]])
    st["history"] = sorted([h for h in st["history"] if h["date"] != asof]
                           + [{"date": asof, "value": round(val, 2),
                               "bench": round(bench, 2), "holding": st["holding"]}],
                           key=lambda h: h["date"])
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["intraday"] = [p for p in st.get("intraday", [])
                      if p["ts"] != st["last_updated_utc"]][-1499:] + [
        {"ts": st["last_updated_utc"], "value": round(val, 2),
         "bench": round(bench, 2), "holding": st["holding"]}]
    state_path.write_text(json.dumps(st, indent=2))

    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": st["starting_cash"], "live_ts": live_ts,
        "current": st["history"][-1], "board": board,
        "board_title": board_title, "meta": spec["meta"],
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"], "strategy": spec["strategy"],
    }
    (config.REPORTS / f"{key}_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "fleet_dashboard_template.html").read_text(
        encoding="utf-8")
    html = template.replace("/*__DATA__*/", json.dumps(payload)).replace(
        "__DATAFILE__", f"{key}_dashboard_data.json")
    (config.REPORTS / f"{key}_dashboard.html").write_text(html, encoding="utf-8")

    print(f"[{key}] {asof} holding {st['holding']} value ${val:,.2f} "
          f"vs {spec['bench']} ${bench:,.2f}")
    return st
