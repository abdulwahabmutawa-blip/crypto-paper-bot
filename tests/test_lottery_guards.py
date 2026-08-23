"""Lottery-book guards — the lines that keep a $11 slot machine a $11 slot
machine. Offline: no network, no real keys, no data/ writes."""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import binance_live as bl  # noqa: E402
import binance_broker      # noqa: E402

# --- arming takes BOTH the keys and the explicit flag ----------------------
for k in ("BINANCE_LIVE_API_KEY", "BINANCE_LIVE_API_SECRET", "LOTTERY_LIVE"):
    os.environ.pop(k, None)
assert not bl.armed()
os.environ["LOTTERY_LIVE"] = "1"
assert not bl.armed(), "flag alone must not arm"
os.environ.pop("LOTTERY_LIVE")
os.environ["BINANCE_LIVE_API_KEY"] = "k"
os.environ["BINANCE_LIVE_API_SECRET"] = "s"
assert not bl.armed(), "keys alone must not arm"
os.environ["LOTTERY_LIVE"] = "1"
assert bl.armed(), "keys + flag = armed"
os.environ["LOTTERY_LIVE"] = "0"
assert not bl.armed(), "flag off must disarm even with keys present"

# --- guards ---------------------------------------------------------------
tmp_ks = Path(tempfile.mkdtemp()) / "KILL_SWITCH"
orig_ks = bl.KILL_SWITCH
bl.KILL_SWITCH = tmp_ks
try:
    # no book cap (owner decision 2026-08-16): a large free balance no
    # longer blocks a BUY — the bot spends whatever USDT is actually there
    assert bl.guard("BUY", "PEPEUSDT", {"USDT": 25.0}, None) is None, \
        "no cap: a large balance must not block a BUY"
    assert bl.guard("SELL", "PEPEUSDT", {"USDT": 25.0}, None) is None, \
        "a de-risking SELL must always be allowed"

    # dust: below the exchange minimum there is nothing to do
    why = bl.guard("BUY", "PEPEUSDT", {"USDT": 3.0}, None)
    assert why and "DUST" in why, why

    # the real ~$11 book passes
    assert bl.guard("BUY", "PEPEUSDT", {"USDT": 11.0}, None) is None

    # the bot's book is its OWN units, not the owner's whole holding of the
    # same coin. Owner holds 1,000,000 PEPE; the bot bought 100. Valuing the
    # free balance would price the book at the owner's stack (and, worse,
    # imply the bot may sell it) — this must stay true even with no cap to
    # trip, since managed_value() still drives the dashboard's book value.
    orig_price = bl.price
    bl.price = lambda sym: 0.00002        # PEPE-ish
    try:
        bals = {"USDT": 10.0, "PEPE": 1_000_000.0}
        assert bl.managed_value(bals, "PEPEUSDT", units=100.0) < 11.0, \
            "book must count only the bot's units"
        assert bl.managed_value(bals, "PEPEUSDT") > 20.0, \
            "sanity: the whole free balance really is that large"
        assert bl.guard("SELL", "PEPEUSDT", bals, "PEPEUSDT", 100.0) is None
        assert bl.guard("BUY", "PEPEUSDT", bals, "PEPEUSDT") is None, \
            "no cap: even the owner's whole PEPE stack must not block a BUY"
    finally:
        bl.price = orig_price

    # kill switch beats everything — including a de-risking SELL
    tmp_ks.write_text("stop")
    why = bl.guard("BUY", "PEPEUSDT", {"USDT": 11.0}, None)
    assert why and "KILL SWITCH" in why, why
    why = bl.guard("SELL", "PEPEUSDT", {"USDT": 11.0}, "PEPEUSDT", 100.0)
    assert why and "KILL SWITCH" in why, "kill switch must stop everything"
finally:
    bl.KILL_SWITCH = orig_ks
    for k in ("BINANCE_LIVE_API_KEY", "BINANCE_LIVE_API_SECRET", "LOTTERY_LIVE"):
        os.environ.pop(k, None)

# --- 2026-08-17: the three real trades, with MEASURED context --------------
# CHIP 09:21 — the bad one. The guard refused it three times as it fell
# (-7.8%, -6.6%, -5.9% on the hour) then bought when the crash bar aged out
# of the 60-minute window. Measured -7.60% below its 2h high at that entry.
why = bl.late_entry(0.11, 0.001, -0.076, 0.202)
assert why and "ROLLED OVER" in why, f"the 09:21 CHIP entry must be refused: {why}"
# ...and it must stay refused even when the hourly window reads POSITIVE,
# which is exactly the artifact that let it through
why = bl.late_entry(0.11, 0.02, -0.076, 0.202)
assert why and "ROLLED OVER" in why, "a rolled-over coin must not be rescued by a green hour"

# LTC 10:47 — clean entry, but its whole 24h range was 1.67%: a round trip
# costs ~0.2% and a burst seat closes within 8h, so it could not pay.
why = bl.late_entry(0.01, 0.002, -0.002, 0.0167)
assert why and "NO ROOM" in why, f"the LTC entry must be refused: {why}"

# SNDKB 05:46 — process-correct (drawdown -0.86%, range 10.26%). It must
# still be allowed: the fix targets the two bad trades, not all trading.
assert bl.late_entry(0.05, 0.005, -0.0086, 0.1026) is None, \
    "the SNDKB entry was defensible and must stay allowed"

# --- late-entry guard: the book's real trades, as fixtures -----------------
# Measured as RUN-UP FROM THE 24H LOW — close-to-close decays as a pump
# rolls over, which is how CHIP's second entry dodged the first cap.
# COW (watcher): +37.6% off its low, -2.3% in the hour, bought 9h after its
# top -> -11.2%. BOTH rules must catch it.
why = bl.late_entry(0.376, -0.023, -0.02, 0.40)
assert why and "LATE" in why, "the COW entry must be refused"
# CHIP round 1 (watcher): +29.2% off its low, bought AT the local top ->
# -7.7%. The run-up cap alone must catch it.
why = bl.late_entry(0.292, 0.057, -0.005, 0.30)
assert why and "LATE" in why, "the CHIP entry must be refused"
# CHIP round 2 (watcher, the 15:30 whipsaw re-buy 6.4% above its own exit):
# day-change had decayed under the old cap, but run-up off the low had not.
# THIS fixture is why the guard measures from the low.
why = bl.late_entry(0.274, 0.001, -0.02, 0.28)
assert why and "LATE" in why, "the CHIP re-buy must be refused"
# LINK: +8.0% off its low, flat hour -> the book's only winner. Must pass.
assert bl.late_entry(0.080, 0.001, -0.01, 0.10) is None, \
    "the LINK entry was fine and must stay allowed"
# early-stage move: modestly up, accelerating -> the target trade
assert bl.late_entry(0.10, 0.03, -0.005, 0.12) is None
# below the run-up cap but red on the hour: hype arrived after the top. The
# drawdown here (-2%) is inside the floor, so it is the HOURLY rule being
# tested, not the new one.
why = bl.late_entry(0.10, -0.01, -0.02, 0.12)
assert why and "rolling over" in why
# unknown price context: this book goes all-in per entry — never buy blind.
# Every input is required; any missing one refuses.
for args in ((None, 0.02, -0.01, 0.12), (0.10, None, -0.01, 0.12),
             (0.10, 0.02, None, 0.12), (0.10, 0.02, -0.01, None)):
    why = bl.late_entry(*args)
    assert why and "blind" in why, args

# --- per-seat exit clocks (explosion study: grinds take a median 11 DAYS) ---
g = bl.exit_params("scout:revival")
assert g["kind"] == "grind" and g["stall_h"] is None, \
    "a grind's early days LOOK stalled — it must not have a stall clock"
assert g["max_hold_h"] == 672.0, \
    "2y median grind is 26 DAYS — a shorter clock amputates the winners"

# progressive trail: the bigger the gain, the tighter the leash
assert bl.trail_pct(0.0) == -0.15 and bl.trail_pct(None) == -0.15
assert bl.trail_pct(0.6) == -0.10, "past +50% the leash tightens"
assert bl.trail_pct(1.5) == -0.08, "past +100% tighter still (+500% events " \
    "kept only -58% at 30d — big gains die most completely)"
b = bl.exit_params("scout:ignition")
# ignition earned the day-scale clock: its own scorecard shows +4.67% mean
# at 24h (90% hit, n=30) vs +1.47% at 4h - an 8h clock exited at hour 5
# of a 24-hour edge (the sentiment bot lesson, calibrated by our numbers)
# REVAMP 08-23: 24h -> 48h (tournament: 24h cap captured +7.16% median,
# >half-move only 10.6%; the tape exits fire first, the cap is a net)
assert b["kind"] == "burst" and b["max_hold_h"] == 48.0 \
    and b["stall_h"] == 4.0 and b["stop_pct"] == -0.06
# breakout gets 24h (from 8h), not ignition's 48h: its 24h record is weak
bb = bl.exit_params("scout:breakout")
assert bb["max_hold_h"] == 24.0 and bb["stall_h"] == 2.0
h = bl.exit_params("watcher")
assert h["kind"] == "hype" and h["max_hold_h"] == 24.0 \
    and h["stall_h"] == 6.0
assert bl.exit_params(None)["kind"] == "hype", \
    "an unknown seat gets the strictest familiar clock, never the longest"

# --- owner-accepted finish lines + wave rule (08-20 review) ------------------
# floor: below $25 no new entries; unknown value must NOT halt by itself
# percentage floor (owner decision 08-21): 62.5% of the book's peak value,
# scale-free — deposits move the peak, so the protection never drifts
why = bl.book_floor_reason(24.99, 40.0)          # 62.4% of peak -> breach
assert why and "FLOOR" in why and "post-mortem" in why
assert bl.book_floor_reason(25.01, 40.0) is None  # 62.6% of peak -> fine
assert bl.book_floor_reason(49.9, 80.0) is not None, \
    "the same -37.5%% drawdown must trip at ANY capital scale"
assert bl.book_floor_reason(50.1, 80.0) is None
assert bl.book_floor_reason(None, 40.0) is None, \
    "a failed value read is a data problem, not a stop signal"
assert bl.book_floor_reason(30.0, None) is None, \
    "no recorded peak yet must not halt the book"
# wave bonus: base 3, +1 on a breadth wave-day
assert bl.entry_budget(False) == 3
assert bl.entry_budget(True) == 4

# --- momentum exit is per-thesis (bug fix 08-20) -----------------------------
# The entry guard demands a coin that has NOT already run far; judging a
# fresh breakout seat by 24h leaderboards therefore ejected it minutes
# after entry, every time (ASTER -1.09% and CHIP -0.67% inside 6 minutes,
# same morning). Only seats whose THESIS is 24h leadership carry that exit.
assert bl.exit_params("scout:breakout").get("momentum_exit") is False,     "a breakout seat must never be judged by the daily leaderboard"
assert bl.exit_params("scout:ignition").get("momentum_exit") is False
assert bl.exit_params("scout:revival").get("momentum_exit") is False
assert bl.exit_params("watcher").get("momentum_exit") is False,     "watcher rides are judged by scans, not rank (pre-existing rule)"
assert bl.exit_params("gainer").get("momentum_exit") is True
assert bl.exit_params("adopted").get("momentum_exit") is True

# --- profit ratchet (REVAMP 08-23: ONE tier, arm +10%, keep 50%) -----------
# The 08-19 two-tier ratchet (+4% -> entry+0.5%; +8% -> half peak) was the
# book's first honest fix and it saved COW/ACE-class round-trips on paper.
# But the 245-explosion tournament replayed it on real paths: the early
# arm / tight lock was shaken out on the FIRST ordinary pullback in 240 of
# 245 moves, realizing a median 15% of the move; resumed pullbacks were
# median -6.5% deep. So the breakeven tier is retired and the -6% stop plus
# the progressive trailing leash own everything under +10% MFE.
assert bl.ratchet_stop(1.0, 1.018) is None
assert bl.ratchet_stop(None, 1.1) is None and bl.ratchet_stop(1.0, None) is None
# COW peaked +4.3%: UNARMED now (the stop, not the ratchet, owns that case)
assert bl.ratchet_stop(0.1391, 0.1391 * 1.043) is None
# DEXE peaked +7.6%: still unarmed
assert bl.ratchet_stop(1.852, 1.852 * 1.076) is None
# AXS-class: peak +12.2% -> floor keeps half = +6.1%
f = bl.ratchet_stop(1.005, 1.005 * 1.122)
assert f is not None and abs(f / 1.005 - 1.061) < 1e-6, f
# peak +10% exactly arms: floor +5%
f = bl.ratchet_stop(1.0, 1.10)
assert abs(f - 1.05) < 1e-9, f
# the floor NEVER loosens as hwm rises (monotone in hwm)
assert bl.ratchet_stop(1.0, 1.20) > bl.ratchet_stop(1.0, 1.10)

# --- watcher earn-in (owner decision 08-19: 0-for-7, -$10.95) ---------------
# pairing: the twin's actual sequence at the time of the order
twin = [
    {"action": "BUY", "ticker": "GPS-USD", "price": 0.016370},
    {"action": "SELL", "ticker": "GPS-USD", "price": 0.018210},   # +11.24%
    {"action": "BUY", "ticker": "TUT-USD", "price": 0.043870},
    {"action": "SELL", "ticker": "TUT-USD", "price": 0.043060},   # -1.85%
    {"action": "BUY", "ticker": "ACE-USD", "price": 0.226900},
    {"action": "SELL", "ticker": "ACE-USD", "price": 0.206100},   # -9.17%
]
rts = bl.twin_round_trips(twin)
assert len(rts) == 3 and abs(rts[0] - 0.1124) < 0.002, rts
ok, why = bl.watcher_earned(rts)
assert not ok and "unproven" in why,     "3 resolved trips is not a record — the watcher stays benched"
# a SELL with no matching BUY must not crash or count
assert bl.twin_round_trips([{"action": "SELL", "ticker": "X", "price": 1}]) == []
# a qualifying record arms it — mechanically, no human in the loop
# REVAMP 08-23: n >= 10 and the MEDIAN trip must pay too (n=6 with one
# outlier win armed the lane for two real XRP losses; 0-for-9 lifetime)
good = [0.11, -0.02, 0.05, -0.01, 0.08, 0.03, 0.02, -0.01, 0.03, 0.01]
ok, why = bl.watcher_earned(good)                      # 7/10 wins, median > 0
assert ok and "earned" in why, why
ok, why = bl.watcher_earned(good[:6])
assert not ok and "unproven" in why, "six trips is no longer a record"
# enough trips but a losing record stays benched
bad = [0.11, -0.05, -0.06, -0.04, -0.09, -0.02, -0.01, -0.03, -0.02, 0.0]
ok, why = bl.watcher_earned(bad)
assert not ok and "does not justify" in why, why
# mean carried by a single outlier while the median is negative: benched
outlier = [0.30, -0.02, -0.01, -0.03, -0.01, -0.02, 0.01, -0.01, -0.02, 0.0]
ok, _ = bl.watcher_earned(outlier)
assert not ok, "one big win must not carry the lane over the bar"
# only the rolling window counts: ancient wins cannot carry a rotten present
stale_glory = [0.5] * 10 + [-0.05] * 10
ok, _ = bl.watcher_earned(stale_glory)
assert not ok, "ten old wins must not arm a signal that lost its last ten"

# --- fuel-gone verdict (08-21, replaced the stall clock): three concrete
# conditions, ALL required, no elapsed-time input --------------------------
# dead fuel + never paid + no wave -> exit
assert bl.fuel_verdict(0.8, 0.01, False) is not None
assert "FUEL GONE" in bl.fuel_verdict(0.8, 0.01, False)
# any single condition alive -> hold
assert bl.fuel_verdict(2.0, 0.01, False) is None, "surge alive must hold"
assert bl.fuel_verdict(0.8, 0.04, False) is None, "a paying seat must hold"
assert bl.fuel_verdict(0.8, 0.01, True) is None, "a wave regime must hold"
# unknown must never fire a sell
assert bl.fuel_verdict(None, 0.01, False) is None
assert bl.fuel_verdict(0.8, None, False) is None
# boundary: exactly at the floors -> hold (floors are alive, not dead)
assert bl.fuel_verdict(bl.FUEL_MIN_SURGE, 0.01, False) is None
assert bl.fuel_verdict(0.8, bl.FUEL_MIN_GAIN, False) is None
# a losing-but-fueled seat holds: the stop-loss owns that exit, not fuel
assert bl.fuel_verdict(3.0, -0.04, False) is None

# --- climax verdict (08-23, promoted from the playbook): red close on
# move-max volume in the lower half of the range = distribution ----------
def _bar(o, h, low, c, qv):
    return [0, o, h, low, c, 0, 0, qv]
assert bl.climax_verdict(_bar(100, 110, 90, 94, 500), 400, 100) is not None
assert bl.climax_verdict(_bar(100, 110, 90, 106, 500), 400, 100) is None, \
    "green candle is never a climax"
assert bl.climax_verdict(_bar(100, 110, 90, 94, 120), 400, 100) is None, \
    "small volume is not a climax"
assert bl.climax_verdict(_bar(100, 110, 90, 104, 500), 400, 100) is None, \
    "red but closed in the upper half — the bid held"
assert bl.climax_verdict(_bar(100, 110, 90, 94, 500), 0, 90) is not None, \
    "5x move-average fallback must qualify when the max is unseeded"
assert bl.climax_verdict([], 400, 100) is None, "garbage candle judges nothing"

# --- REVAMP 08-23: ratchet one-tier (+10% arm, keep 50% of peak) ---------
assert bl.ratchet_stop(100.0, 104.0) is None,     "the +4% breakeven tier is gone (shaken out 240/245 in the study)"
assert bl.ratchet_stop(100.0, 109.9) is None
_f = bl.ratchet_stop(100.0, 120.0)
assert _f is not None and abs(_f - 110.0) < 1e-9, "keeps half of a +20% peak"
assert bl.ratchet_stop(None, 120.0) is None

# --- terminal dip (review-corrected 08-23): the last 3 post-entry CLOSES all
# >=12% under the high-water of the EARLIER post-entry closes ------------------
# a flat base then a breakout tick must NOT fire (the bug the review caught)
assert bl.terminal_dip_verdict([100.0, 100.0, 100.0, 114.0]) is None,     "a peak inside the judged window is a breakout, not a dip"
assert bl.terminal_dip_verdict([100.0, 112.0, 114.0, 115.0]) is None
# a real terminal dip: peak close 115, then three closes all <= 101
assert bl.terminal_dip_verdict([100.0, 115.0, 101.0, 100.0, 99.0]) is not None
# one deep close among two recovered closes: NOT all three under -> hold
assert bl.terminal_dip_verdict([100.0, 115.0, 99.0, 112.0, 113.0]) is None
assert bl.terminal_dip_verdict([100.0, 115.0, 101.0]) is None,     "fewer than 4 post-entry closes must judge nothing"
assert bl.terminal_dip_verdict([]) is None

# --- circuit breaker: 2 losing exits OR -10% of peak in a UTC day --------
assert bl.circuit_breaker_reason([], 50.0) is None
assert bl.circuit_breaker_reason([{"pnl_usd": -0.5, "pnl_pct": -1.2}],
                                 50.0) is None
assert bl.circuit_breaker_reason([{"pnl_usd": -0.5, "pnl_pct": -1.2},
                                  {"pnl_usd": -0.2, "pnl_pct": -1.5}],
                                 50.0) is not None, "2 material losses trip"
# dust/fee scratches are NOT losses (review 08-23: +1.6% winners priced as
# -$0.02 rows would have tripped the breaker 7 of 9 live days)
assert bl.circuit_breaker_reason([{"pnl_usd": -0.02, "pnl_pct": 1.63},
                                  {"pnl_usd": -0.19, "pnl_pct": -0.43}],
                                 50.0) is None, "scratches must not trip"
assert bl.circuit_breaker_reason([{"pnl_usd": -5.5, "pnl_pct": -10.5}],
                                 50.0) is not None,     "-11% of peak trips it on one loss"
assert bl.circuit_breaker_reason([{"pnl_usd": 3.0, "pnl_pct": 6.0},
                                  {"pnl_usd": -1.0, "pnl_pct": -2.0},
                                  {"pnl_usd": 2.0, "pnl_pct": 4.0}],
                                 50.0) is None
assert bl.circuit_breaker_reason([{"pnl_usd": -5.5, "pnl_pct": -10.5}],
                                 None) is None,     "no recorded peak -> only the loss-count line applies"

# --- depth gate: the exit side must absorb the seat --------------------------
assert bl.depth_gate(50.0, None, None) is not None, "unknown book: refuse"
assert bl.depth_gate(50.0, 10_000.0, 500_000.0) is not None, "thin bids"
assert bl.depth_gate(50.0, 100_000.0, 100_000.0) is None
assert bl.depth_gate(10_000.0, 100_000.0, 100_000.0) is not None,     "an order that is 10% of the 5% bid depth is too big for the book"

# --- unlock veto: >=1x ADV cliff within 7 days refuses -----------------------
assert bl.unlock_veto(3.0, 1.5) is not None
assert bl.unlock_veto(3.0, 0.4) is None, "small unlock: no veto"
assert bl.unlock_veto(20.0, 5.0) is None, "far unlock: no veto"
assert bl.unlock_veto(None, 5.0) is None and bl.unlock_veto(3.0, None) is None

# --- regime gate: revival stands down on wave days ---------------------------
assert bl.regime_allows("revival", True) is not None
assert bl.regime_allows("revival", False) is None
assert bl.regime_allows("ignition", True) is None

# --- api burst: >=3 api_errors in 10 min freezes entries ---------------------
from datetime import datetime as _dt, timezone as _tz, timedelta as _td
_now = _dt.now(_tz.utc)
def _err(mins_ago, code=503):
    return {"event": "api_error", "code": code, "body": "",
            "ts": (_now - _td(minutes=mins_ago)).isoformat(timespec="seconds")}
assert bl.api_burst_reason([_err(1), _err(2)], _now) is None
assert bl.api_burst_reason([_err(1), _err(2), _err(3)], _now) is not None
assert bl.api_burst_reason([_err(1), _err(2), _err(30)], _now) is None,     "an old error does not count toward the burst"
# client-side 400s (our bad symbol probes) are not venue failures
assert bl.api_burst_reason([_err(1, 400), _err(2, 400), _err(3, 400)],
                           _now) is None, "400 -1121 probes are our query"
# rate limits ARE venue pressure
_rl = {"event": "api_error", "code": 429, "body": '{"code":-1003}',
       "ts": _now.isoformat(timespec="seconds")}
assert bl.api_burst_reason([_rl, _rl, _rl], _now) is not None
assert bl.api_burst_reason([{"event": "fill", "ts": _now.isoformat()}] * 5,
                           _now) is None

# --- exchange announcements (08-23): delisting exit + entry vetoes ---------
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import announcement_watch as aw  # noqa: E402
assert aw.parse_delist("Binance Will Delist ICX, SCRT, STORJ on 2026-09-03") \
    == (["ICX", "SCRT", "STORJ"], "2026-09-03")
assert aw.parse_delist("Notice of Removal of Spot Trading Pairs - 2026-08-21") \
    == ([], None), "pair-removal notices name no coin in the title"
assert aw.parse_listing("Binance Will List Foo Protocol (FOO) ...") == ["FOO"]
assert aw.parse_listing("Binance Futures Will Launch UNITREEUSDT ...") == []
_ann = {"delist": {"SCRTUSDT": {"title": "Binance Will Delist ICX, SCRT, "
                                "STORJ on 2026-09-03",
                                "effective": "2026-09-03",
                                "released_utc": "2026-08-20T12:00:06+00:00"}},
        "listing": {"NEWUSDT": {"title": "Binance Will List New (NEW)",
                                "released_utc": _now.isoformat(
                                    timespec="seconds")}}}
assert bl.delisting_exit("SCRTUSDT", _ann) is not None
assert bl.delisting_exit("AXSUSDT", _ann) is None
assert bl.delisting_exit("SCRTUSDT", None) is None, "no file = no notice"
assert bl.announcement_veto("SCRTUSDT", _ann, _now) is not None
assert bl.announcement_veto("NEWUSDT", _ann, _now) is not None, \
    "a 0h-old listing is a listing open"
assert bl.announcement_veto("AXSUSDT", _ann, _now) is None
assert bl.announcement_veto("NEWUSDT", None, _now) is None

# --- tripwires: these asserts fail any casual edit that widens the blast
# radius. Changing them is a deliberate reviewed act, which is the point.
assert not hasattr(bl, "BOOK_CAP_USD"), \
    "BOOK_CAP_USD reappeared — removing it was a reviewed decision (2026-08-16)"
assert bl.BASE.startswith("https://api.binance.com"), "mainnet host changed"
assert "testnet.binance.vision" in binance_broker.BASE, \
    "the shadow broker must stay on testnet"

print("test_lottery_guards: ALL PASS")
