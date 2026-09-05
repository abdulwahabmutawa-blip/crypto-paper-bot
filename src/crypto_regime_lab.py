"""Crypto regime switcher lab — which rule change would have helped?

Owner 2026-09-05: "reinstate crypto but make it better; figure out what it
did wrong and right." Live attribution (data/crypto_state.json, 52 days):
the book lost to BTC in exactly two ways: (1) sat in a flat alt (XRP,
08-10..08-19) or in CASH while BTC ran, because TREND's fallback is CASH and
nothing compares the alt with BTC; (2) bought alts at the top of a 7-day
spike (SOL +16% mom on 08-27, LINK +23% on 08-19) — short-lookback momentum
in majors mean-reverts. This lab replays the bot's daily logic over ~2
years of Kraken closes with those two levers changed, same fee model, and
reports vs BTC buy-and-hold. Pure research, no state touched.

Usage: python src/crypto_regime_lab.py   -> reports/crypto_regime_lab.md
"""
from __future__ import annotations

import itertools
import math
import sys

import pandas as pd

import config
import crypto_prices
from crypto_tracker import (COINS, BENCH, MA_N, Z_N, Z_ENTRY, Z_EXIT, MOM_EXIT,
                            HYST, MOM_MARGIN, Z_HYST, STOP_PCT)

OUT = config.REPORTS / "crypto_regime_lab.md"
FEE = 0.0025          # paper model: 25 bps per side


def run(close: pd.DataFrame, mom_n: int = 7, fallback: str = "CASH",
        rel_btc: bool = False, fee: float = FEE, trend_btc_only: bool = False) -> dict:
    """Daily replay of crypto_tracker's decision stack.
    fallback: what TREND holds when no alt qualifies ('CASH' or BENCH).
    rel_btc:  in TREND an alt must beat BTC's momentum by MOM_MARGIN to take
              the seat, else the seat is BTC (relative strength)."""
    ma = close.rolling(MA_N).mean()
    mom = close.pct_change(mom_n) * 100
    z = (close - close.rolling(Z_N).mean()) / close.rolling(Z_N).std()
    eq, held, entry, seat_regime = 1.0, "CASH", None, None
    trades, curve, stopped = 0, [], None
    idx = close.index
    for i in range(MA_N, len(idx) - 1):
        d = idx[i]
        regime = "TREND" if close.at[d, BENCH] > ma.at[d, BENCH] else "CHOP"
        row_m, row_z = mom.loc[d], z.loc[d]
        if regime == "TREND" and trend_btc_only:
            pick = BENCH                      # the tide itself, no alt picking
        elif regime == "TREND":
            top = row_m.idxmax()
            pick = top if row_m[top] > 0 else fallback
            if rel_btc and pick not in ("CASH", BENCH):
                # an alt must lead BTC by MOM_MARGIN points, else BTC is the seat
                if row_m[pick] < row_m[BENCH] + MOM_MARGIN:
                    pick = BENCH if row_m[BENCH] > 0 else fallback
        else:
            top = row_z.idxmin()
            pick = top if row_z[top] < Z_ENTRY else "CASH"
        # swap brake
        if held not in ("CASH",) and pick not in ("CASH", held):
            if regime == "TREND":
                if row_m[held] > MOM_EXIT:
                    bar = max(HYST * row_m[held], row_m[held] + MOM_MARGIN)
                    if row_m[pick] < bar:
                        pick = held
            else:
                if row_z[held] < Z_EXIT and row_z[pick] > row_z[held] - Z_HYST:
                    pick = held
        # exit brake
        if pick == "CASH" and held != "CASH":
            if (seat_regime == "TREND" and row_m[held] > MOM_EXIT) or \
               (seat_regime == "CHOP" and row_z[held] < Z_EXIT):
                pick = held
        # failure stop + re-entry guard
        if held != "CASH" and entry and close.at[d, held] <= entry * (1 + STOP_PCT / 100):
            pick = "CASH"; stopped = (held, d)
        if stopped:
            if row_z[stopped[0]] >= Z_EXIT and d > stopped[1]:
                stopped = None
            elif pick == stopped[0]:
                pick = held
        # execute at today's close, earn tomorrow's move
        if pick != held:
            if held != "CASH":
                eq *= 1 - fee; trades += 1
            if pick != "CASH":
                eq *= 1 - fee; entry = close.at[d, pick]; seat_regime = regime
            else:
                entry = seat_regime = None
            held = pick
        nxt = idx[i + 1]
        if held != "CASH":
            eq *= close.at[nxt, held] / close.at[d, held]
        curve.append((nxt, eq))
    s = pd.Series(dict(curve))
    return {"curve": s, "trades": trades, "final": s.iloc[-1],
            "maxdd": float((s / s.cummax() - 1).min()),
            "last90": float(s.iloc[-1] / s.iloc[-91] - 1) if len(s) > 91 else float("nan")}


def cagr(final: float, days: int) -> float:
    return final ** (365 / max(days, 1)) - 1


def main() -> int:
    close = crypto_prices.daily(COINS)
    if close is None or len(close) < MA_N + 100:
        print("not enough Kraken history"); return 1
    close = close.ffill().dropna()
    n_days = (close.index[-1] - close.index[MA_N]).days
    btc = close[BENCH].iloc[MA_N + 1:] / close[BENCH].iloc[MA_N]
    rows = []
    for mom_n, fallback, rel in itertools.product((7, 14, 30), ("CASH", BENCH), (False, True)):
        r = run(close, mom_n, fallback, rel)
        rows.append({"mom": mom_n, "fallback": fallback.replace("-USD", ""), "rel_btc": rel, **r})
    r = run(close, 7, BENCH, False, trend_btc_only=True)
    rows.append({"mom": "TREND=BTC + CHOP dip brain", "fallback": "", "rel_btc": False, **r})
    # simplest competitors: BTC-only tide timing (hold BTC above its MA, cash
    # below) and equal-weight all 8 in TREND / cash in CHOP, same fees
    ma = close.rolling(MA_N).mean()
    for label, weights in (("BTC-only MA200 timing", {BENCH: 1.0}),
                           ("equal-weight 8 in TREND", {c: 1 / len(COINS) for c in COINS})):
        eq, inpos, sw, curve = 1.0, False, 0, []
        for i in range(MA_N, len(close.index) - 1):
            d, nxt = close.index[i], close.index[i + 1]
            want = close.at[d, BENCH] > ma.at[d, BENCH]
            if want != inpos:
                eq *= 1 - FEE; sw += 1; inpos = want
            if inpos:
                eq *= sum(w * close.at[nxt, c] / close.at[d, c] for c, w in weights.items())
            curve.append((nxt, eq))
        s = pd.Series(dict(curve))
        rows.append({"mom": label, "fallback": "", "rel_btc": False, "curve": s, "trades": sw,
                     "final": float(s.iloc[-1]), "maxdd": float((s / s.cummax() - 1).min()),
                     "last90": float(s.iloc[-1] / s.iloc[-91] - 1)})
    bench = {"final": float(btc.iloc[-1]), "maxdd": float((btc / btc.cummax() - 1).min()),
             "last90": float(btc.iloc[-1] / btc.iloc[-91] - 1), "trades": 0}
    lines = [f"# Crypto regime switcher lab", "",
             f"Kraken daily closes {close.index[0].date()} to {close.index[-1].date()}, "
             f"{len(close)} rows, 8 coins, decisions at close, {FEE*1e4:.0f} bps per side. "
             f"Replay window {n_days} days after the 200-day warm-up. Current live rule = "
             f"mom 7 / fallback CASH / rel_btc False.", "",
             "| mom | TREND fallback | rel. to BTC | CAGR | vs BTC B&H | max DD | last 90d | last 90d vs BTC | switches |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: -r["final"]):
        lines.append(f"| {r['mom']} | {r['fallback']} | {('yes' if r['rel_btc'] else 'no') if r['fallback'] else ''} | "
                     f"{cagr(r['final'], n_days):+.1%} | {r['final']/bench['final']-1:+.1%} | "
                     f"{r['maxdd']:.1%} | {r['last90']:+.1%} | {r['last90']-bench['last90']:+.1%} | {r['trades']} |")
    lines.append(f"| BTC buy & hold | | | {cagr(bench['final'], n_days):+.1%} | 0 | "
                 f"{bench['maxdd']:.1%} | {bench['last90']:+.1%} | 0 | 0 |")
    lines += ["", "Read: a variant earns its place only if it beats BTC over the full window "
              "AND the last 90 days, with a drawdown no worse than the current rule. "
              "Switch counts x 50 bps are the fee bill."]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
