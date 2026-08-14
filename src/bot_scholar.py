"""The Scholar (العالِم) — the fleet's synthesis bot, born at the v2 review.

Built ONLY from ingredients that survived our own research (full provenance
and honest caveats: reports/scholar_spec.md, registered launch day):
vol-adjusted momentum (Hunter's score concept), mom90 + MA200 standard params
(commodity bot / stats-lab lesson 3), positive-momentum requirement, 1.25x
switch hysteresis (anti-churn, lesson 4), vol-targeted sizing instead of
all-in (Turtle concept; the 20% number is a NEW choice, not inherited), 10%
trailing stop + 5-CALENDAR-day cooldown (the parked v2 risk overlay), no
leveraged ETFs (lesson 5: TQQQ = beta drag, not edge).

Signals run on each asset's NATIVE trading calendar (signal_frame="raw"):
crypto trades 365 days/yr, equities 252 — union-calendar rolling windows
would silently shrink every equity's MA200 to ~137 trading days and NaN-mask
eligibility (found by the 2026-07-31 pre-launch adversarial review, which
invalidated the first backtest for exactly this).
"""
from __future__ import annotations

import json

import pandas as pd

import config
import selection_engine

UNIV = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT",
        "GLD", "SLV", "USO", "DBC", "BTC-USD", "ETH-USD"]
NAMES = {"SPY": "S&P 500", "QQQ": "Nasdaq 100", "IWM": "US small caps",
         "EFA": "Developed intl", "EEM": "Emerging mkts", "TLT": "Long bonds",
         "GLD": "Gold", "SLV": "Silver", "USO": "Oil", "DBC": "Broad commodities",
         "BTC-USD": "Bitcoin", "ETH-USD": "Ethereum"}
HYST = 1.25


def asset_stats(raw: pd.DataFrame):
    """Per-asset {sym: (last, ma200, mom90, vol90_ann, score)} on NATIVE calendars."""
    out = {}
    for c in raw.columns:
        s = raw[c].dropna()
        if len(s) < 201:
            continue
        last = float(s.iloc[-1])
        ma = float(s.rolling(200).mean().iloc[-1])
        mom = float(s.pct_change(90).iloc[-1])
        vol = float(s.pct_change().rolling(90).std().iloc[-1]) \
            * (selection_engine._ann_factor(c) ** 0.5)
        if not (pd.notna(ma) and pd.notna(mom) and pd.notna(vol)) or vol <= 0:
            continue
        out[c] = (last, ma, mom, vol, mom / vol)
    return out


def signal(raw: pd.DataFrame, holding: str):
    stats = asset_stats(raw[[c for c in UNIV if c in raw.columns]])
    elig = [c for c, (last, ma, mom, vol, sc) in stats.items()
            if last > ma and mom > 0]
    top = max(elig, key=lambda c: stats[c][4]) if elig else None

    if holding == "CASH" or holding not in elig:
        pick = top or "CASH"
    elif top and top != holding and stats[top][4] > HYST * stats[holding][4]:
        pick = top
    else:
        pick = holding

    # Fleet review 2026-08-10: evidence capture, not more trading. Persist the
    # challenger-vs-holding score each day so the 1.25x hysteresis can be
    # judged from the bot's own record at the 90-day review. Each ~13-min run
    # overwrites today's row (converges to end-of-day state); bot.yml commits
    # data/ wholesale. Any I/O failure is inert — trading logic untouched.
    try:
        d = str(raw.index[-1].date())
        p = config.DATA / "scholar_signal_log.json"
        log = json.loads(p.read_text()) if p.exists() else {}
        log[d] = {"holding": holding, "pick": pick, "top": top,
                  "top_score": round(stats[top][4], 4) if top else None,
                  "held_score": round(stats[holding][4], 4)
                  if holding in stats else None}
        p.write_text(json.dumps(log))
    except Exception:
        pass

    board = []
    for c in sorted(stats, key=lambda c: -stats[c][4]):
        last, ma, mom, vol, sc = stats[c]
        board.append({
            "sym": c, "price": round(last, 2),
            "line": f"{NAMES[c]} · score {sc:+.2f} · mom90 {mom*100:+.1f}% "
                    f"· MA gap {(last/ma-1)*100:+.1f}%",
            "tag": "HELD" if c == pick else ("eligible" if c in elig else "not eligible"),
            "on": c in elig, "pick": c == pick,
            "fill": max(-50, min(50, sc * 25)),
        })
    return pick, board, "12 instruments ranked by momentum-per-unit-risk"


SPEC = {
    "key": "scholar",
    "universe": UNIV,
    "bench": "SPY",
    "signal": signal,
    "signal_frame": "raw",
    "risk": {"trailing": 0.10, "cooldown_days": 5},
    "vol_target": 0.20,
    # Live-pilot candidate (GO_LIVE_PLAN 08-14 A5): the fee-fit template —
    # ~1 trade/mo ≈ 0.6%/mo at IBKR's $1 minimum. Dry-run intents only.
    "live_pilot": True,
    "cash_reason": "Nothing in a confirmed uptrend — standing aside in cash",
    "buy_reason": "Best momentum-per-unit-risk in a confirmed uptrend",
    "meta": {
        "title": "The Scholar — $1,000 Challenge",
        "badge": "PAPER SIM · SYNTHESIS BOT",
        "bench_label": "SPY benchmark ($1,000 same day)",
        "board_note": "Every rule in this bot was earned by an earlier "
                      "experiment: vol-adjusted momentum, trend gate as crash "
                      "protection, vol-sized positions, trailing stop, and a "
                      "switch threshold that fights churn. The synthesis on trial.",
    },
    "strategy": {
        "name": "The Scholar — cross-asset synthesis",
        "rule": "Hold the best mom90/vol score of 12 unleveraged assets in "
                "confirmed uptrends (price > MA200, mom90 > 0); switch only on "
                "a 1.25x better score; position sized to 20% ann. vol; 10% "
                "trailing stop + 5-calendar-day cooldown; nothing qualifies -> cash",
        # numbers restated 2026-07-31 after the adversarial review invalidated
        # the first backtest (it had silently tested BTC/ETH only) — see
        # reports/scholar_spec.md and the lab header for the full story.
        "backtest_cagr": "+10.9%/yr 2017+ (LAGGED SPY's +15.0%) · +16.9%/yr "
                         "2020+ · +23.3%/yr 2024+ (SPY +20.5%) — mixed, "
                         "honestly reported",
        "backtest_maxdd": "-29.0% vs SPY -33.7% (2017+) but -27.6% vs SPY "
                          "-18.8% in 2024+ · 0.1%/side costs included",
        "note": "Expectation after the McLean-Pontiff decay haircut: roughly "
                "SPY-like return with lower drawdown is the honest hope. "
                "Judged by kill_criteria.md like every other bot.",
    },
}

if __name__ == "__main__":
    selection_engine.run(SPEC)
