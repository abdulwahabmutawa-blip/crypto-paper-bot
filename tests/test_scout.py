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

# --- RULESET v2: the 08-16 log-autopsy rules ---------------------------------
# breakout must not chase a blow-off: the two chased entries (+18.5%/h and
# +8.8%/h) were the book's worst scout losses (-18.8%, -5.6% at 4h)
assert sc.score_breakout(F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7,
                           chg_1h=0.185, chg_24h=0.269,
                           range_pos=0.98)) is None, \
    "REDUSDT class: +18.5% in an hour is a blow-off, not an entry"
assert sc.score_breakout(F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7,
                           chg_1h=0.05, chg_24h=0.30,
                           range_pos=0.9)) is None, \
    "a day that already paid +30% is late, not 'about to'"
assert sc.score_breakout(F(vol_surge=6.0, trade_surge=5.0, taker_buy_frac=0.7,
                           chg_1h=0.05, chg_24h=0.15, range_pos=0.9)), \
    "a moderate, confirmed move must still fire"

# the range floor: pegged/tracker assets (XAUT, QQQB, U...) sail through
# every volume filter and can never pay the round trip — 9 of the first 48
# picks were exactly this
assert not sc.universe_ok({"symbol": "XAUTUSDT", "quoteVolume": "9000000",
                           "count": "9000", "highPrice": "3400.1",
                           "lowPrice": "3399.0", "bidPrice": "3399.5",
                           "askPrice": "3399.6"}), \
    "a peg must not enter the universe"
assert sc.universe_ok({"symbol": "AAAUSDT", "quoteVolume": "9000000",
                       "count": "9000", "highPrice": "1.10",
                       "lowPrice": "1.00", "bidPrice": "1.04",
                       "askPrice": "1.0401"}), \
    "a liquid coin that actually moves must pass"

# --- the gate: probation -> earned -> benched --------------------------------
ok, why = sc.signal_actionable({"signals": {}}, "ignition")
assert not ok and "probation" in why, "no record under current rules = probation"
ok, _ = sc.signal_actionable({"signals": {"ignition": {
    "n_4h": 30, "hit_rate_4h": 0.55, "mean_ret_4h": 0.012}}}, "ignition")
assert ok, "a signal that beats fees over a real sample must arm"
ok, why = sc.signal_actionable({"signals": {"ignition": {
    "n_4h": 30, "hit_rate_4h": 0.24, "mean_ret_4h": -0.0007}}}, "ignition")
assert not ok and "benched" in why, \
    "the live 08-16 record (24% hit, negative mean) must NOT be tradeable"

# --- re-signal cooldown: one event, one log row ------------------------------
hist = [{"ts": "2026-08-15T12:00:00+00:00", "symbol": "BICOUSDT",
         "signal": "reversion"}]
t0 = datetime(2026, 8, 15, 12, 40, tzinfo=timezone.utc)
assert sc.recently_flagged(hist, "BICOUSDT", "reversion", t0), \
    "40 minutes later is the same event"
t1 = datetime(2026, 8, 15, 16, 0, tzinfo=timezone.utc)
assert not sc.recently_flagged(hist, "BICOUSDT", "reversion", t1), \
    "4 hours later is a fresh look"
assert not sc.recently_flagged(hist, "BICOUSDT", "ignition", t0), \
    "a different signal type is a different claim"

# --- ruleset segregation: old rules' outcomes must not feed the new card -----
tmp_dir = Path(tempfile.mkdtemp())
orig_log, orig_card = sc.LOG, sc.SCORECARD
sc.LOG, sc.SCORECARD = tmp_dir / "log.jsonl", tmp_dir / "card.json"
try:
    old = {"ts": "2026-08-15T10:00:00+00:00", "symbol": "AUSDT",
           "signal": "ignition", "price": 1.0,
           "ret_1h": 0.05, "ret_4h": 0.05, "ret_24h": 0.05}   # no ruleset tag
    new = {"ts": "2026-08-16T10:00:00+00:00", "symbol": "BUSDT",
           "signal": "ignition", "price": 1.0, "ruleset": sc.RULESET,
           "ret_1h": -0.05, "ret_4h": -0.05, "ret_24h": -0.05}
    sc.LOG.write_text("\n".join([json.dumps(old)] * 20
                                + [json.dumps(new)] * 3) + "\n")
    card, rows = sc.resolve_outcomes(datetime(2026, 8, 18, 11, 0,
                                              tzinfo=timezone.utc))
    ign = card["signals"]["ignition"]
    assert ign["n_4h"] == 3 and ign["hit_rate_4h"] == 0.0, \
        f"20 old-ruleset wins must not launder the new rules' record: {ign}"
    assert len(rows) == 23, "resolve must still return the full history"
finally:
    sc.LOG, sc.SCORECARD = orig_log, orig_card

# --- REVIVAL: the explosion-study profile (n=109), day one only --------------
REV = dict(age_ok=True, chg_24h=0.05, week_chg=-0.15, med_pre_qv=400_000.0,
           today_qv=2_000_000.0, runup_30d=0.08, wave=False)
assert sc.revival_verdict(dict(REV)), "the textbook study profile must fire"
# was not beaten down last week -> wrong species (58/73 exploders fell first)
assert sc.revival_verdict(dict(REV, week_chg=-0.02)) is None
# was not quiet -> the crowd was already here
assert sc.revival_verdict(dict(REV, med_pre_qv=3_000_000.0)) is None
# volume has not actually arrived (under 3x its own week)
assert sc.revival_verdict(dict(REV, today_qv=700_000.0)) is None
# already +30% off the 30d low -> not day one, this is the chase the
# retention data punishes (-29% median for peak buyers)
assert sc.revival_verdict(dict(REV, runup_30d=0.30)) is None
# not turning today (flat) or already gone (+20% day) -> outside the window
assert sc.revival_verdict(dict(REV, chg_24h=0.005)) is None
assert sc.revival_verdict(dict(REV, chg_24h=0.20)) is None
# young listing -> different trade (bStocks class), excluded by design
assert sc.revival_verdict(dict(REV, age_ok=False)) is None
# a wave day makes the same profile louder, never quieter
s_calm, _ = sc.revival_verdict(dict(REV))
s_wave, why_wave = sc.revival_verdict(dict(REV, wave=True, wave_count=80,
                                           wave_base=30.0))
assert s_wave > s_calm and "WAVE DAY" in why_wave
# the serial-exploder prior: history is the strongest single regularity in
# the 2y study (87% of exploders repeated; TUT's +1,990% was its ninth)
s_serial, why_serial = sc.revival_verdict(dict(REV, serial_n=9))
assert s_serial > s_calm and "serial exploder: 9 runs" in why_serial
s_once, _ = sc.revival_verdict(dict(REV, serial_n=1))
assert s_once == s_calm, "a single prior event is not yet a habit"

# --- breadth: no wave calls without a baseline, 2x median = wave -------------
ok, base = sc.wave_call(100, [30] * 5)
assert not ok and base is None, "short history must never call a wave"
ok, base = sc.wave_call(65, [30, 28, 33, 30, 29, 31, 30, 32, 28, 30, 31, 29])
assert ok and base == 30.0, (ok, base)
ok, _ = sc.wave_call(45, [30, 28, 33, 30, 29, 31, 30, 32, 28, 30, 31, 29])
assert not ok, "1.5x the baseline is a breeze, not a wave"

# --- revival volume must be a RATE, not a partial-day total (bug 08-20) ------
# comparing a partial day against full days demanded a 9x pace at 08:00 UTC;
# revival logged ZERO candidates in 3 days while other signals logged 389
assert sc.prorated_day_volume(1_000_000, 0.5) == 2_000_000,     "half a day at 1M projects a 2M full-day rate"
assert sc.prorated_day_volume(500_000, 1.0/24) is None,     "under 2h elapsed there is no honest rate"
assert sc.prorated_day_volume(0.0, 0.5) == 0.0

# --- the gate demands MEANINGFULLY beating fees (3x round trip) --------------
ok, why = sc.signal_actionable({"signals": {"ignition": {
    "n_4h": 30, "hit_rate_4h": 0.60, "mean_ret_4h": 0.004}}}, "ignition")
assert not ok and "round trip" in why,     "a mean that only matches fees is trading for nothing"

# --- revival is judged on its OWN clock (24h), not the sprint clock ----------
assert "revival" in sc.SIGNAL_TYPES
card24 = {"signals": {"revival": {
    "n_4h": 30, "hit_rate_4h": 0.10, "mean_ret_4h": -0.02,      # bad sprint
    "n_24h": 30, "hit_rate_24h": 0.55, "mean_ret_24h": 0.03}}}  # good marathon
ok, _ = sc.signal_actionable(card24, "revival")
assert ok, "a grind signal with a winning 24h record must arm despite 4h noise"
ok, why = sc.signal_actionable({"signals": {"revival": {
    "n_4h": 30, "hit_rate_4h": 0.9, "mean_ret_4h": 0.05}}}, "revival")
assert not ok and "24h" in why, \
    "4h samples alone must not arm a signal judged at 24h"

print("test_scout: ALL PASS")
