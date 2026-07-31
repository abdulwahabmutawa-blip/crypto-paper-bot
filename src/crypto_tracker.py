"""LIVE crypto $1,000 paper sim — YOLO 2.0 momentum rotation, 8 coins.

Rule (user choice, lesson from the grid in test_absmom.py applied):
Always 100% in the coin with the hottest 7-day momentum — but never hold a
falling one. If all 8 have negative weekly momentum, sit in cash until
something rises. Live quotes, 24/7 market.

State: data/crypto_state.json.  Screen: reports/crypto_dashboard.html.
Run any time:  python src/crypto_tracker.py
PAPER MONEY ONLY. Not investment advice.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf

import config

STATE = config.DATA / "crypto_state.json"
COINS = ["BTC-USD", "ETH-USD", "SOL-USD", "DOGE-USD", "AVAX-USD",
         "LINK-USD", "ADA-USD", "XRP-USD"]
BENCH = "BTC-USD"          # benchmark: $1,000 of BTC held from day one
START_CASH = 1000.0
# REGIME SWITCHER (v3 of the bot, 2026-07-16): two brains, picked daily by
# BTC vs its 200-day MA (crypto's tide gauge).
#   TREND (BTC > MA): momentum brain — hottest 7d coin, only while rising.
#   CHOP  (BTC < MA): reversion brain — most oversold coin (z20 < -1.25),
#                     harvesting bounces; nothing oversold -> cash.
# Only tested variant profitable in the 2024+ chop (+9.2%/yr).
MA_N, MOM_N, Z_N, Z_ENTRY = 200, 7, 20, -1.25


def fetch() -> pd.DataFrame:
    raw = yf.download(COINS, period="15mo", auto_adjust=True, progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    return close.dropna(how="all").ffill()


def fetch_live() -> tuple[dict, str]:
    """Latest intraday quote per coin (Yahoo 5-minute bars, near-real-time
    for crypto). Returns ({coin: price}, iso_timestamp_utc)."""
    raw = yf.download(COINS, period="1d", interval="5m", auto_adjust=True,
                      progress=False)
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    close = close.ffill()
    last = close.iloc[-1]
    ts = close.index[-1]
    ts = ts.tz_convert("UTC") if ts.tzinfo else ts.tz_localize("UTC")
    return ({c: float(last[c]) for c in COINS if pd.notna(last[c])},
            ts.isoformat(timespec="seconds"))


def signal(close: pd.DataFrame) -> tuple[str, dict, str]:
    """Regime switcher. Returns (pick, board, regime).
    TREND: hottest 7d coin if rising. CHOP: most oversold coin (z < Z_ENTRY)."""
    last = close.iloc[-1]
    ma = close.rolling(MA_N).mean().iloc[-1]
    mom = close.pct_change(MOM_N).iloc[-1]
    z20 = ((close - close.rolling(Z_N).mean())
           / close.rolling(Z_N).std()).iloc[-1]
    regime = "TREND" if last["BTC-USD"] > ma["BTC-USD"] else "CHOP"

    board = {}
    for c in COINS:
        board[c] = {
            "price": round(float(last[c]), 4),
            "ma200": round(float(ma[c]), 4),
            "gap_pct": round((float(last[c]) / float(ma[c]) - 1) * 100, 2),
            "mom_pct": round(float(mom[c]) * 100, 2),
            "z": round(float(z20[c]), 2),
            "above_ma": bool(last[c] > ma[c]),
        }
    # rank by the metric the active brain uses
    if regime == "TREND":
        ranked = sorted(COINS, key=lambda c: board[c]["mom_pct"], reverse=True)
        top = ranked[0]
        pick = top if board[top]["mom_pct"] > 0 else "CASH"
    else:
        ranked = sorted(COINS, key=lambda c: board[c]["z"])
        top = ranked[0]
        pick = top if board[top]["z"] < Z_ENTRY else "CASH"
    for i, c in enumerate(ranked):
        board[c]["rank"] = i + 1
    return pick, board, regime


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else None


def init_state(close, pick, board) -> dict:
    asof = str(close.index[-1].date())
    st = {
        "created": asof, "starting_cash": START_CASH,
        "holding": "CASH", "units": 0.0, "cash": START_CASH,
        "bench_units": START_CASH / board[BENCH]["price"],
        "trades": [], "history": [],
    }
    if pick != "CASH":
        px = board[pick]["price"]
        st["holding"], st["units"], st["cash"] = pick, START_CASH / px, 0.0
        st["trades"].append({"date": asof, "action": "BUY", "ticker": pick,
                             "price": px, "units": round(st["units"], 6),
                             "value": START_CASH,
                             "reason": f"Initial entry — strongest eligible coin "
                                       f"({board[pick]['mom_pct']:+.1f}% 7d momentum)"})
    else:
        st["trades"].append({"date": asof, "action": "HOLD CASH", "ticker": "—",
                             "price": 0, "units": 0, "value": START_CASH,
                             "reason": "All 8 coins falling on the week — cash until one rises"})
    return st


def update(st, close, pick, board) -> dict:
    asof = str(close.index[-1].date())
    # value before any switch
    cur_px = board[st["holding"]]["price"] if st["holding"] != "CASH" else None

    if pick != st["holding"]:
        # liquidate current
        value = st["cash"] if st["holding"] == "CASH" else st["units"] * cur_px
        if st["holding"] != "CASH":
            st["trades"].append({"date": asof, "action": "SELL",
                                 "ticker": st["holding"], "price": cur_px,
                                 "units": round(st["units"], 6),
                                 "value": round(value, 2),
                                 "reason": "Signal flip"})
        if pick == "CASH":
            st["holding"], st["units"], st["cash"] = "CASH", 0.0, value
            st["trades"].append({"date": asof, "action": "TO CASH", "ticker": "—",
                                 "price": 0, "units": 0, "value": round(value, 2),
                                 "reason": "All 8 coins falling on the week — cash until one rises"})
        else:
            px = board[pick]["price"]
            st["holding"], st["units"], st["cash"] = pick, value / px, 0.0
            st["trades"].append({"date": asof, "action": "BUY", "ticker": pick,
                                 "price": px, "units": round(st["units"], 6),
                                 "value": round(value, 2),
                                 "reason": f"Strongest eligible coin "
                                           f"({board[pick]['mom_pct']:+.1f}% 7d momentum)"})

    val = st["cash"] if st["holding"] == "CASH" else st["units"] * board[st["holding"]]["price"]
    bench = st["bench_units"] * board[BENCH]["price"]
    row = {"date": asof, "value": round(val, 2), "bench": round(bench, 2),
           "holding": st["holding"]}
    st["history"] = sorted([h for h in st["history"] if h["date"] != asof] + [row],
                           key=lambda h: h["date"])
    st["last_updated_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    # live intraday equity stream (rolling ~48h at 2-min cadence)
    st.setdefault("intraday", [])
    st["intraday"] = [p for p in st["intraday"]
                      if p["ts"] != st["last_updated_utc"]]
    st["intraday"].append({"ts": st["last_updated_utc"],
                           "value": round(val, 2), "bench": round(bench, 2),
                           "holding": st["holding"]})
    st["intraday"] = st["intraday"][-1500:]
    return st


def emit(st, board, pick, live_ts="", regime="") -> None:
    payload = {
        "generated_utc": st["last_updated_utc"], "created": st["created"],
        "starting_cash": st["starting_cash"], "live_ts": live_ts,
        "current": st["history"][-1], "board": board, "pick": pick,
        "regime": regime,
        "intraday": st.get("intraday", []),
        "trades": st["trades"][-20:], "history": st["history"],
        "thoughts": (
            ("Right now I'm in TREND mode: Bitcoin is above its 200-day average, "
             "which historically means crypto is in an uptrend — so my rule is to "
             "ride whichever coin has climbed the most this week. "
             if "TREND" in (regime or "").upper() else
             "Right now I'm in CHOP mode: Bitcoin is below its 200-day average, "
             "which means the market is directionless — chasing momentum here "
             "loses money, so instead I look for a coin that fell unusually hard "
             "and try to catch its bounce back. ")
            + (f"That's why I'm holding {st['holding'].replace('-USD', '')}."
               if st["holding"] != "CASH" else
               "Nothing qualifies at this moment, so I'm in cash — in crypto, "
               "sitting out is often the smartest trade.")),
        "strategy": {
            "name": "Regime Switcher — two brains, one bot",
            "rule": "BTC above its 200-day MA = TREND: ride the hottest "
                    "rising 7-day-momentum coin. Below = CHOP: buy the most "
                    "oversold coin (z20 < -1.25) and harvest the bounce; "
                    "nothing qualifies -> cash",
            "backtest_cagr": "+50%/yr since 2017 · +9%/yr in the 2024+ chop",
            "backtest_maxdd": "-93% (2017 era) · experimental — parameters are soft",
        },
    }
    (config.REPORTS / "crypto_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "crypto_dashboard_template.html").read_text(
        encoding="utf-8")
    out = config.REPORTS / "crypto_dashboard.html"
    out.write_text(template.replace("/*__DATA__*/", json.dumps(payload)),
                   encoding="utf-8")
    print(f"[dash] rendered {out.name}")


def main():
    close = fetch()
    # Override today's row with LIVE quotes so momentum, ranking, and trade
    # prices all reflect right now, not yesterday's close.
    live, live_ts = fetch_live()
    for c, p in live.items():
        close.iloc[-1, close.columns.get_loc(c)] = p
    pick, board, regime = signal(close)
    import sentinel_gate
    is_severe, why = sentinel_gate.severe()
    if is_severe and pick != "CASH":
        print(f"[crypto-live] {why} -> forcing CASH")
        pick = "CASH"
    st = load_state()
    if st is None:
        st = init_state(close, pick, board)
        print(f"[crypto-live] NEW sim {st['created']} — opening position: {pick}")
    st = update(st, close, pick, board)
    STATE.write_text(json.dumps(st, indent=2))
    emit(st, board, pick, live_ts, regime)
    print(f"[crypto-live] regime: {regime}")
    print(f"[crypto-live] live quotes as of {live_ts}")

    cur = st["history"][-1]
    print(f"[crypto-live] {cur['date']}  holding {cur['holding']}  "
          f"value ${cur['value']:,.2f}  vs BTC ${cur['bench']:,.2f}  pick={pick}")
    for c in sorted(COINS, key=lambda c: board[c]["rank"]):
        b = board[c]
        print(f"  #{b['rank']} {c:<9} ${b['price']:>10,.2f}  "
              f"mom7 {b['mom_pct']:+7.2f}%  gap-to-MA {b['gap_pct']:+7.2f}%")


if __name__ == "__main__":
    main()
