"""Scout signal logic — deterministic, offline, no network.
Feeds synthetic feature dicts through the scorers so each rule is pinned."""
import json
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import binance_scout as sc  # noqa: E402


def F(**over):
    """A neutral coin: nothing unusual anywhere."""
    base = {"price": 1.0, "chg_24h": 0.0, "vol_surge": 1.0, "trade_surge": 1.0,
            "chg_15m": 0.0, "chg_1h": 0.0, "drawdown_24h": -0.02,
            "range_pos": 0.5, "green_streak": 0, "quote_vol_24h": 9e6,
            "taker_buy_frac": 0.5, "burst_usd": 200_000.0,
            "xs_bottom_decile": False, "liq_rank_pct": 0.5}
    base.update(over)
    return base


# --- nothing fires on a quiet coin -------------------------------------------
q = F()
assert sc.score_ignition(q) is None
assert sc.score_breakout(q) is None
assert sc.score_reversion(q) is None

# --- IGNITION: trades AND volume detonate, price has NOT moved yet -----------
# Thresholds are the published ones: 5x volume (arXiv 2503.08692), trade
# arrival as the PRIMARY feature (La Morgia RF Gini), taker-buy >= 0.60.
ign = F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7, chg_1h=0.01,
        range_pos=0.55)
assert sc.score_ignition(ign), "textbook ignition must fire"
# 2x volume is FOLKLORE — no study uses it standalone, and it must not fire
assert sc.score_ignition(F(vol_surge=2.0, trade_surge=5.0,
                           taker_buy_frac=0.7, chg_1h=0.01)) is None
# one whale printing size is not a crowd: notional up, trade count flat
assert sc.score_ignition(F(vol_surge=9.0, trade_surge=1.2,
                           taker_buy_frac=0.7, chg_1h=0.01)) is None
# balanced flow is not accumulation — buyers must be lifting offers
assert sc.score_ignition(F(vol_surge=6.0, trade_surge=5.0,
                           taker_buy_frac=0.45, chg_1h=0.01)) is None
# a 5x ratio on a dead book is arithmetically free; the absolute floor stops it
assert sc.score_ignition(F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7,
                           chg_1h=0.01, burst_usd=8_000)) is None
# price already ran -> that is a breakout, not an ignition
assert sc.score_ignition(F(vol_surge=6.0, trade_surge=5.0,
                           taker_buy_frac=0.7, chg_1h=0.09)) is None
# already pinned at the 24h high -> the move happened; not an early catch
assert sc.score_ignition(F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7,
                           chg_1h=0.01, range_pos=0.95)) is None
# bleeding out on heavy volume is distribution, not accumulation
assert sc.score_ignition(F(vol_surge=6.0, trade_surge=5.0,
                           taker_buy_frac=0.7, chg_1h=-0.05)) is None

# --- BREAKOUT: volume AND price moving, near the high ------------------------
brk = F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7, chg_1h=0.08,
        range_pos=0.9)
assert sc.score_breakout(brk), "textbook breakout must fire"
# price up but on NO extra volume = a thin drift, not a breakout
assert sc.score_breakout(F(vol_surge=1.1, trade_surge=5.0, chg_1h=0.08,
                           taker_buy_frac=0.7, range_pos=0.9)) is None
# up big earlier but stalled this hour -> the pump already died (the live
# COWUSDT case: +49% on the day, -6.5% in the hour, volume below average)
assert sc.score_breakout(F(vol_surge=0.7, chg_1h=-0.065, range_pos=0.51)) is None
# mid-range means it is not breaking anything out
assert sc.score_breakout(F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7,
                           chg_1h=0.08, range_pos=0.55)) is None

# --- REVERSION: cross-sectional bottom decile, now turning up ----------------
rev = F(chg_24h=-0.20, xs_bottom_decile=True, chg_15m=0.01, green_streak=3,
        liq_rank_pct=0.4)
assert sc.score_reversion(rev), "textbook reversion must fire"
# NOT in the market's bottom decile -> not the published sort, no trade
assert sc.score_reversion(F(chg_24h=-0.20, xs_bottom_decile=False,
                            chg_15m=0.01, green_streak=3)) is None
# THE KNIFE FILTER: catastrophic collapse is an exploit/unlock, not a dip
# (the live NFPUSDT case: -66% on the day with a green flicker)
assert sc.score_reversion(F(chg_24h=-0.66, xs_bottom_decile=True,
                            chg_15m=0.023, green_streak=3)) is None
# the reversal premium is an ILLIQUIDITY premium and reverses sign in the
# largest coins (Zaremba) — fading a mega-cap trades against the evidence
assert sc.score_reversion(F(chg_24h=-0.20, xs_bottom_decile=True,
                            chg_15m=0.01, green_streak=3,
                            liq_rank_pct=0.97)) is None
# still falling: no green candles yet
assert sc.score_reversion(F(chg_24h=-0.20, xs_bottom_decile=True,
                            chg_15m=-0.01, green_streak=0)) is None
# barely down is not oversold, even if it is technically the bottom decile
assert sc.score_reversion(F(chg_24h=-0.03, xs_bottom_decile=True,
                            chg_15m=0.01, green_streak=3)) is None

# --- learning weights --------------------------------------------------------
# below the sample floor the scorecard must not move the needle at all
assert sc.signal_weight({"signals": {"ignition": {"n_4h": 5,
                                                  "hit_rate_4h": 1.0}}},
                        "ignition") == 1.0, "small samples are not evidence"
# with enough samples, a good signal is amplified and a bad one is muted
hot = sc.signal_weight({"signals": {"ignition": {"n_4h": 200,
                                                 "hit_rate_4h": 0.8}}}, "ignition")
cold = sc.signal_weight({"signals": {"ignition": {"n_4h": 200,
                                                  "hit_rate_4h": 0.1}}}, "ignition")
assert hot > 1.0 > cold, (hot, cold)
assert sc.WEIGHT_FLOOR <= cold and hot <= sc.WEIGHT_CEIL

# --- market-wide surge: the zero-cost all-market detector --------------------
now = datetime(2026, 8, 15, 12, 0, tzinfo=timezone.utc)
tmp = Path(tempfile.mkdtemp()) / "snap.json"
orig = sc.SNAPSHOT
sc.SNAPSHOT = tmp
try:
    # first call has no history -> no ratios, but it must seed the snapshot
    t0 = [{"symbol": "AAAUSDT", "quoteVolume": "144000", "count": "1440"}]
    assert sc.market_wide_surge(t0, now - timedelta(minutes=10)) == {}
    assert tmp.exists()
    # 10 minutes later the coin traded 10x its own average slice
    # (24h volume 144000 -> expected 1000 per 10 min; it did 10000)
    t1 = [{"symbol": "AAAUSDT", "quoteVolume": "154000", "count": "1600"}]
    out = sc.market_wide_surge(t1, now)
    assert 9.0 < out["AAAUSDT"] < 11.0, out
    # a stale snapshot (server was down for hours) must be ignored, not
    # treated as one enormous surge
    far = sc.market_wide_surge(t1, now + timedelta(hours=3))
    assert far == {}, far
finally:
    sc.SNAPSHOT = orig

print("test_scout: ALL PASS")
