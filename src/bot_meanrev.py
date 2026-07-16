"""Mean-Reversion Mega-Caps bot — the anti-momentum experiment.

Buy the most oversold mega-cap (20d z-score < -1.5), hold until it recovers
to its 20d average (z >= 0), else cash. Lab verdict was MIXED (beat SPY
2020-2023, lagged 2024+) — this live run is the tiebreaker.
"""
from __future__ import annotations

import pandas as pd

import selection_engine

MEGA = ["AAPL", "MSFT", "AMZN", "GOOGL", "NVDA", "JPM", "JNJ", "XOM",
        "WMT", "PG", "UNH", "HD", "KO", "PEP", "CVX", "MRK"]
Z_ENTRY, Z_EXIT = -1.5, 0.0


def signal(close: pd.DataFrame, holding: str):
    u = close[MEGA]
    z = ((u - u.rolling(20).mean()) / u.rolling(20).std()).iloc[-1]
    last = close.iloc[-1]

    pick = holding
    if holding != "CASH" and pd.notna(z[holding]) and z[holding] >= Z_EXIT:
        pick = "CASH"                        # recovered -> take the bounce
    if pick == "CASH":
        zmin = z.min()
        if pd.notna(zmin) and zmin < Z_ENTRY:
            pick = z.idxmin()                # most oversold name

    board, ranked = [], sorted(MEGA, key=lambda c: z[c])
    for c in ranked[:10]:
        zv = float(z[c])
        board.append({
            "sym": c, "price": round(float(last[c]), 2),
            "line": f"z {zv:+.2f}",
            "tag": "HELD" if c == pick else ("oversold" if zv < Z_ENTRY else "normal"),
            "on": zv < Z_ENTRY, "pick": c == pick,
            "fill": max(-50, min(50, -zv / 3 * 50)),
        })
    return pick, board, "16 mega-caps, most oversold first (z < -1.5 = buy zone)"


SPEC = {
    "key": "meanrev",
    "universe": MEGA,
    "bench": "SPY",
    "signal": signal,
    "cash_reason": "Bounce harvested / nothing oversold — waiting in cash",
    "buy_reason": "Most oversold mega-cap (z < -1.5) — buying the dip",
    "meta": {
        "title": "Mean-Reversion Mega-Caps — $1,000 Challenge",
        "badge": "PAPER SIM · ANTI-MOMENTUM",
        "bench_label": "SPY benchmark ($1,000 same day)",
        "board_note": "Buys panic, sells relief: enter the most stretched "
                      "mega-cap below -1.5 z, exit when it recovers to average.",
    },
    "strategy": {
        "name": "Mean Reversion — buy panic in quality names",
        "rule": "Hold the most oversold of 16 mega-caps (20-day z-score < "
                "-1.5) until it recovers to its average; else cash",
        "backtest_cagr": "+13.9%/yr since 2010 · +9.7%/yr 2024+",
        "backtest_maxdd": "-57% (2010 era) · verdict MIXED — this live run decides",
    },
}

if __name__ == "__main__":
    selection_engine.run(SPEC)
