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
import risk_common

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
    # Guard (audit 2026-08-05): a NaN here used to flow silently into every
    # valuation below. Missing price = no cycle.
    px = {t: float(last[t]) for t in tickers if pd.notna(last.get(t))}
    return px, str(close.index[-1].date())


def main():
    px, asof = quotes()
    missing = (set(W) | {BENCH}) - set(px)
    if missing:
        print(f"[{KEY}] no price for {sorted(missing)} — cycle skipped")
        return
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

    # R1 kill floor (code-enforced; audit 2026-08-05). Even the control group
    # obeys the fleet's pre-registered rules: at/below $750 it liquidates to
    # cash and freezes — the experiment is over at that point anyway.
    if not st.get("frozen") and risk_common.r1_breached(val):
        print(f"[{KEY}] {risk_common.r1_reason(val)}")
        for t, u in st["units"].items():
            if u > 0:
                gross = u * px[t]
                f = risk_common.fee(t, gross)
                st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
                st["trades"].append({"date": asof, "action": "SELL", "ticker": t,
                                     "price": round(px[t], 8),
                                     "units": round(u, 4),
                                     "value": round(gross, 2), "fee": round(f, 2),
                                     "reason": risk_common.r1_reason(val)})
        st["cash_frozen"] = round(sum(
            u * px[t] - risk_common.fee(t, u * px[t])
            for t, u in st["units"].items()), 2)
        st["units"] = {t: 0.0 for t in W}
        st["frozen"] = {"date": asof, "rule": "R1 kill floor (kill_criteria.md)"}
        print(f"[{KEY}] book FROZEN — un-freezing is a human decision")
    if st.get("frozen"):
        # old frozen state without cash_frozen must not value the book at $0
        val = st.get("cash_frozen") or (st["history"][-1]["value"]
                                        if st["history"] else val)

    # monthly rebalance back to target weights (10bps per rebalance trade —
    # the audit's cost model; frozen books never rebalance). All targets are
    # computed from the SAME pre-fee value, then the total fee shrinks the
    # book proportionally — mid-loop mutation skewed later tickers' weights.
    # Strict > (fleet review 2026-08-10): a stale out-of-order bar from a
    # PRIOR month (07-31 arrived after the 08-03 rebalance) re-triggered `!=`
    # and flipped last_rebalance_month backward, causing two unscripted
    # rebalances. YYYY-MM compares correctly as strings; the control must
    # trade exactly once a month as pre-registered.
    if not st.get("frozen") and asof[:7] > st["last_rebalance_month"]:
        total_fee = 0.0
        for t, w in W.items():
            delta = val * w / px[t] - st["units"][t]
            if abs(delta * px[t]) >= 1:
                f = risk_common.fee(t, abs(delta) * px[t])
                total_fee += f
                st["costs_paid"] = round(st.get("costs_paid", 0.0) + f, 4)
                st["trades"].append({"date": asof,
                                     "action": "REBAL+" if delta > 0 else "REBAL-",
                                     "ticker": t, "price": round(px[t], 2),
                                     "units": round(abs(delta), 4),
                                     "value": round(abs(delta) * px[t], 2),
                                     "fee": round(f, 2),
                                     "reason": f"Monthly rebalance to {w:.1%}"})
        val -= total_fee
        st["units"] = {t: val * w / px[t] for t, w in W.items()}
        st["last_rebalance_month"] = asof[:7]
        print(f"[{KEY}] monthly rebalance done (fees ${total_fee:.2f})")

    bench = st["bench_units"] * px[BENCH]
    # stale-mark guard (same rule as every other book)
    newest = st["history"][-1]["date"] if st["history"] else ""
    if asof < newest:
        print(f"[{KEY}] STALE BAR {asof} < newest mark {newest} — mark skipped")
    else:
        st["history"] = sorted([h for h in st["history"] if h["date"] != asof]
                               + [{"date": asof, "value": round(val, 2),
                                   "bench": round(bench, 2),
                                   "holding": "FROZEN" if st.get("frozen")
                                   else "5 assets"}],
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
        "costs_paid": st.get("costs_paid", 0.0),
        "frozen": st.get("frozen"),
        "thoughts": "I don't think — and that's the whole point. I hold the same "
                    "diversified mix through everything (30% stocks, 40% bonds, "
                    "15% gold, 7.5% commodities, 7.5% T-bills) and once a month I "
                    "top up whatever fell and trim whatever grew, back to those "
                    "targets. I'm the control group: every clever bot in this "
                    "fleet has to beat boring old me to prove its cleverness is "
                    "worth anything.",
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
