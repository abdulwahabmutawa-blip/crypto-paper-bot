"""LIVE $1,000 paper-trading tracker — 3x leveraged trend rotation.

State lives in data/stock_state.json. Each run:
  1. Fetches latest prices (QQQ, TQQQ, BIL, SPY).
  2. Computes today's signal: QQQ close vs 200-day SMA.
  3. Executes any regime switch in the PAPER portfolio (sell/buy at latest close).
  4. Marks portfolio to market, appends to daily history.
  5. Emits reports/stock_dashboard_data.json for the dashboard screen.

Run any time:  python src/live_tracker.py
PAPER MONEY ONLY. This never touches a brokerage. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config

STATE = config.DATA / "stock_state.json"
DASH = config.REPORTS / "stock_dashboard_data.json"
START_CASH = 1000.0
RISK_TKR = "TQQQ"
SAFE_TKR = "BIL"
SIGNAL_TKR = "QQQ"
BENCH_TKR = "SPY"


def fetch() -> pd.DataFrame:
    px = yf.download([SIGNAL_TKR, RISK_TKR, SAFE_TKR, BENCH_TKR],
                     period="15mo", auto_adjust=True, progress=False)
    close = px["Close"] if isinstance(px.columns, pd.MultiIndex) else px
    return close.dropna(how="all").ffill()


def load_state() -> dict | None:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return None


def save_state(st: dict) -> None:
    STATE.write_text(json.dumps(st, indent=2))


def init_state(close: pd.DataFrame) -> dict:
    last = close.iloc[-1]
    asof = close.index[-1]
    ma200 = close[SIGNAL_TKR].rolling(200).mean().iloc[-1]
    in_market = bool(last[SIGNAL_TKR] > ma200)
    hold = RISK_TKR if in_market else SAFE_TKR
    shares = START_CASH / last[hold]
    spy_shares = START_CASH / last[BENCH_TKR]
    return {
        "created": str(asof.date()),
        "starting_cash": START_CASH,
        "holding": hold,
        "shares": shares,
        "bench_shares": spy_shares,
        "trades": [{
            "date": str(asof.date()), "action": "BUY", "ticker": hold,
            "price": round(float(last[hold]), 4),
            "shares": round(shares, 6),
            "value": START_CASH,
            "reason": f"Initial entry — QQQ {'above' if in_market else 'below'} 200-day MA",
        }],
        "history": [],
    }


def update(st: dict, close: pd.DataFrame) -> dict:
    last = close.iloc[-1]
    asof = close.index[-1]
    ma200 = close[SIGNAL_TKR].rolling(200).mean().iloc[-1]
    in_market = bool(last[SIGNAL_TKR] > ma200)
    # Sentinel override: leveraged positions and crisis tape don't mix.
    import sentinel_gate
    is_severe, why = sentinel_gate.severe()
    if is_severe and in_market:
        in_market = False
        print(f"[live] {why} -> forcing safe asset")
    target = RISK_TKR if in_market else SAFE_TKR

    # Regime switch: sell current holding, buy target at latest close.
    if target != st["holding"]:
        sell_px = float(last[st["holding"]])
        value = st["shares"] * sell_px
        st["trades"].append({
            "date": str(asof.date()), "action": "SELL", "ticker": st["holding"],
            "price": round(sell_px, 4), "shares": round(st["shares"], 6),
            "value": round(value, 2),
            "reason": f"Signal flip — QQQ crossed {'above' if in_market else 'below'} 200-day MA",
        })
        buy_px = float(last[target])
        st["holding"] = target
        st["shares"] = value / buy_px
        st["trades"].append({
            "date": str(asof.date()), "action": "BUY", "ticker": target,
            "price": round(buy_px, 4), "shares": round(st["shares"], 6),
            "value": round(value, 2),
            "reason": "Rotation target after signal flip",
        })

    # Mark to market; upsert today's history row.
    val = st["shares"] * float(last[st["holding"]])
    bench = st["bench_shares"] * float(last[BENCH_TKR])
    row = {"date": str(asof.date()), "value": round(val, 2),
           "bench": round(bench, 2), "holding": st["holding"],
           "signal_in_market": in_market,
           "qqq": round(float(last[SIGNAL_TKR]), 2),
           "ma200": round(float(ma200), 2)}
    hist = [h for h in st["history"] if h["date"] != row["date"]]
    hist.append(row)
    st["history"] = sorted(hist, key=lambda h: h["date"])
    st["last_updated_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return st


def emit_dashboard(st: dict, close: pd.DataFrame) -> None:
    last = st["history"][-1]
    ma_gap = (last["qqq"] / last["ma200"] - 1) * 100
    # 60 sessions of QQQ + MA for the signal mini-chart
    qqq = close[SIGNAL_TKR].dropna()
    ma = close[SIGNAL_TKR].rolling(200).mean()
    sig_series = [
        {"date": str(d.date()), "qqq": round(float(q), 2),
         "ma": round(float(m), 2)}
        for d, q, m in zip(qqq.index[-60:], qqq.iloc[-60:], ma.iloc[-60:])
    ]
    payload = {
        "generated_utc": st["last_updated_utc"],
        "created": st["created"],
        "starting_cash": st["starting_cash"],
        "current": last,
        "ma_gap_pct": round(ma_gap, 2),
        "trades": st["trades"][-20:],
        "history": st["history"],
        "signal_series": sig_series,
        "strategy": {
            "name": "3x Leveraged Trend Rotation",
            "rule": "Hold TQQQ while QQQ > 200-day MA; else T-bills (BIL)",
            "backtest_cagr": "31.8% (2010-2026)",
            "backtest_maxdd": "-56%",
            "risk_note": "Highest-risk strategy tested. Paper money only.",
        },
    }
    DASH.write_text(json.dumps(payload, indent=2))
    print(f"[dash] wrote {DASH.name}")

    # Render the dashboard screen: inject data into the HTML template.
    template = (config.ROOT / "src" / "stock_dashboard_template.html").read_text(
        encoding="utf-8")
    html = template.replace("/*__DATA__*/", json.dumps(payload))
    out = config.REPORTS / "stock_dashboard.html"
    out.write_text(html, encoding="utf-8")
    print(f"[dash] rendered {out.name}")


def main():
    close = fetch()
    st = load_state()
    if st is None:
        st = init_state(close)
        print(f"[live] NEW simulation started {st['created']} — "
              f"bought {st['trades'][0]['shares']:.4f} {st['holding']} "
              f"@ ${st['trades'][0]['price']:,.2f}")
    st = update(st, close)
    save_state(st)
    emit_dashboard(st, close)

    cur = st["history"][-1]
    ret = cur["value"] / st["starting_cash"] - 1
    bret = cur["bench"] / st["starting_cash"] - 1
    print(f"[live] {cur['date']}  holding {cur['holding']}  "
          f"value ${cur['value']:,.2f} ({ret:+.2%})  "
          f"vs SPY ${cur['bench']:,.2f} ({bret:+.2%})  "
          f"signal={'IN market' if cur['signal_in_market'] else 'OUT (cash)'}")


if __name__ == "__main__":
    main()
