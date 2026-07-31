"""Scholar backtest — validation of the registered spec (reports/scholar_spec.md).

One variant only, parameters fixed before results were seen. No grid. Costs
included (0.1% per SIDE). Fills at the signal day's close (documented
optimism: up to one bar vs the live engine's market-hours gate).

REWRITTEN 2026-07-31 after the pre-launch adversarial review invalidated v1:
v1 ran rolling windows on the union equity+crypto calendar without ffill, so
every equity's MA200 was permanently NaN and the "12-asset" backtest silently
tested a BTC/ETH-only rotation. v2: signals on each asset's NATIVE calendar
(crypto annualized at 365d, equities 252d), aligned to the union calendar by
carrying the last computed value forward (never lookahead); fills/marks from
the ffilled price frame; equity legs trade only on weekday rows (mirrors the
live market-hours gate); stop -> CASH and calendar-day cooldown exactly as
the live engine implements them.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import yfinance as yf

UNIVERSE = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT",
            "GLD", "SLV", "USO", "DBC", "BTC-USD", "ETH-USD"]
BENCH = "SPY"
MA_N, MOM_N, VOL_N = 200, 90, 90
HYST = 1.25          # challenger must score > 1.25x holder
VOL_TARGET = 0.20    # annualized, for position sizing
TRAIL = 0.10         # trailing stop
COOLDOWN = 5         # calendar days (matches the live engine)
COST = 0.001         # 0.1% per side


def load():
    raw = yf.download(sorted(set(UNIVERSE) | {BENCH}), period="max",
                      auto_adjust=True, progress=False)["Close"]
    return raw.dropna(how="all")


def can_trade(sym, day):
    return sym == "CASH" or sym.endswith("-USD") or day.weekday() < 5


def run(close: pd.DataFrame, start: str):
    close = close[close.index >= pd.Timestamp("2000-01-01")]
    sig = {}
    for c in UNIVERSE:
        if c not in close.columns:
            continue
        s = close[c].dropna()
        ann = 365.0 if c.endswith("-USD") else 252.0
        df = pd.DataFrame({
            "ma": s.rolling(MA_N).mean(),
            "mom": s.pct_change(MOM_N),
            "vol": s.pct_change().rolling(VOL_N).std() * np.sqrt(ann),
            "px": s,
        })
        df["score"] = df["mom"] / df["vol"]
        sig[c] = df.reindex(close.index).ffill()
    fill_px = close.ffill()

    idx = close.index[close.index >= pd.Timestamp(start)]
    cash, units, holding = 1000.0, 0.0, "CASH"
    hwm, stopped_sym, stopped_day = None, None, None
    legs = 0
    buys = {}   # per-symbol fill count — the "which assets did this ACTUALLY
    eq = []     # trade" sanity check (2026-07-31 lesson: v1 traded only crypto)

    for d in idx:
        row = {c: sig[c].loc[d] for c in sig}
        elig = [c for c, r in row.items()
                if pd.notna(r["px"]) and pd.notna(r["ma"]) and pd.notna(r["score"])
                and r["px"] > r["ma"] and r["mom"] > 0]
        top = max(elig, key=lambda c: row[c]["score"]) if elig else None

        pick = holding
        if holding == "CASH" or holding not in elig:
            pick = top or "CASH"
        elif top and top != holding \
                and row[top]["score"] > HYST * row[holding]["score"]:
            pick = top

        # trailing stop: overrides the signal, exits to CASH (as live)
        stop_fired = False
        if holding != "CASH" and pd.notna(fill_px.loc[d, holding]):
            p = float(fill_px.loc[d, holding])
            hwm = max(hwm or p, p)
            if p <= hwm * (1 - TRAIL):
                pick, stop_fired = "CASH", True

        # cooldown blocks RE-ENTRY into the stopped ticker only (as live)
        if pick not in ("CASH", holding) and pick == stopped_sym \
                and (d - stopped_day).days < COOLDOWN:
            pick = holding

        # equity legs fill only on weekday rows (mirrors market-hours gate)
        if pick != holding and not (can_trade(pick, d) and can_trade(holding, d)):
            pick = holding

        if pick != holding:
            sell_px = fill_px.loc[d, holding] if holding != "CASH" else None
            buy_px = fill_px.loc[d, pick] if pick != "CASH" else None
            if (holding != "CASH" and pd.isna(sell_px)) or \
                    (pick != "CASH" and pd.isna(buy_px)):
                pick = holding          # never fill at a NaN price
            else:
                if holding != "CASH":
                    cash += units * float(sell_px) * (1 - COST)
                    units, legs = 0.0, legs + 1
                    if stop_fired:
                        stopped_sym, stopped_day = holding, d
                if pick != "CASH":
                    v = row[pick]["vol"]
                    frac = min(1.0, VOL_TARGET / float(v)) \
                        if pd.notna(v) and v > 0 else 1.0
                    spend = cash * frac
                    units = spend * (1 - COST) / float(buy_px)
                    cash -= spend
                    hwm = float(buy_px)
                    legs += 1
                    buys[pick] = buys.get(pick, 0) + 1
                holding = pick

        mark = fill_px.loc[d, holding] if holding != "CASH" else 0.0
        eq.append(cash + (units * float(mark) if holding != "CASH" else 0.0))

    eq = pd.Series(eq, index=idx)
    # start date can be a weekend/market holiday (union calendar): normalize
    # the bench at its first real close in the window — flat span, no trade
    bench_px = close[BENCH].reindex(idx).ffill()
    first = bench_px.first_valid_index()
    bench = 1000 * bench_px.ffill().bfill() / bench_px.loc[first]
    years = (idx[-1] - idx[0]).days / 365.25

    def stats(s, base=1000.0):
        cagr = (s.iloc[-1] / base) ** (1 / years) - 1
        dd = (s / s.cummax() - 1).min()
        return s.iloc[-1], cagr, dd

    e, ec, edd = stats(eq)
    b, bc, bdd = stats(bench)
    print(f"{start}+  scholar ${e:>9,.0f}  cagr {ec:+7.1%}  maxDD {edd:6.1%}  "
          f"legs {legs:3d}  |  SPY ${b:>9,.0f}  cagr {bc:+7.1%}  maxDD {bdd:6.1%}")
    print(f"          buys by symbol: "
          f"{dict(sorted(buys.items(), key=lambda kv: -kv[1]))}")
    return eq


if __name__ == "__main__":
    close = load()
    for start in ["2017-01-01", "2020-01-01", "2024-01-01"]:
        run(close, start)
