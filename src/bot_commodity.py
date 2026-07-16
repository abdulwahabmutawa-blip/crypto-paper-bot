"""Commodity Trend bot — the fleet's 4th asset class.

Hold the strongest (90d momentum) of gold/silver/oil/broad-commodities while
it's above its own 200d MA; else T-bills. Lab: best NEW idea in the current
regime (+33.8%/yr since 2024, beat SPY).
"""
from __future__ import annotations

import pandas as pd

import selection_engine

COMMOD = ["GLD", "SLV", "USO", "DBC"]
NAMES = {"GLD": "Gold", "SLV": "Silver", "USO": "Oil", "DBC": "Broad basket"}


def signal(close: pd.DataFrame, holding: str):
    u = close[COMMOD]
    ma = u.rolling(200).mean().iloc[-1]
    mom = u.pct_change(90).iloc[-1]
    last = close.iloc[-1]

    elig = [c for c in COMMOD if pd.notna(ma[c]) and last[c] > ma[c]
            and pd.notna(mom[c])]
    pick = max(elig, key=lambda c: mom[c]) if elig else "CASH"

    board = []
    for c in sorted(COMMOD, key=lambda c: -(mom[c] if pd.notna(mom[c]) else -9)):
        gap = (float(last[c]) / float(ma[c]) - 1) * 100 if pd.notna(ma[c]) else 0
        m = float(mom[c]) * 100 if pd.notna(mom[c]) else 0
        board.append({
            "sym": c, "price": round(float(last[c]), 2),
            "line": f"{NAMES[c]} · mom90 {m:+.1f}% · MA gap {gap:+.1f}%",
            "tag": "HELD" if c == pick else ("eligible" if c in elig else "below MA"),
            "on": c in elig, "pick": c == pick,
            "fill": max(-50, min(50, m)),
        })
    return pick, board, "4 commodity ETFs ranked by 90-day momentum"


SPEC = {
    "key": "commodity",
    "universe": COMMOD,
    "bench": "SPY",
    "signal": signal,
    "cash_reason": "No commodity above its 200-day MA — in T-bill-style cash",
    "buy_reason": "Strongest commodity above its 200-day MA",
    "meta": {
        "title": "Commodity Trend — $1,000 Challenge",
        "badge": "PAPER SIM · 4TH ASSET CLASS",
        "bench_label": "SPY benchmark ($1,000 same day)",
        "board_note": "Commodities often trend when stocks and crypto chop — "
                      "this bot rides whichever of gold/silver/oil/basket is "
                      "trending, or stands aside.",
    },
    "strategy": {
        "name": "Commodity Trend Rotation",
        "rule": "Hold the strongest 90-day-momentum commodity ETF above its "
                "own 200-day MA (GLD/SLV/USO/DBC); none above -> cash",
        "backtest_cagr": "+8.7%/yr since 2010 · +33.8%/yr 2024+ (beat SPY)",
        "backtest_maxdd": "-63% (2010s commodity winter) · -47% recent",
    },
}

if __name__ == "__main__":
    selection_engine.run(SPEC)
