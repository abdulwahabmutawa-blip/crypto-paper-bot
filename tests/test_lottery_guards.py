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
assert b["kind"] == "burst" and b["max_hold_h"] == 8.0 \
    and b["stop_pct"] == -0.06
h = bl.exit_params("watcher")
assert h["kind"] == "hype" and h["max_hold_h"] == 24.0 \
    and h["stall_h"] == 6.0
assert bl.exit_params(None)["kind"] == "hype", \
    "an unknown seat gets the strictest familiar clock, never the longest"

# --- profit ratchet: a ride that paid never goes red (exit audit 08-19) -----
# below +4% MFE: unarmed — a scratch may still become a stop-loss (LINK
# peaked +1.8%; ratcheting there would churn every wiggle)
assert bl.ratchet_stop(1.0, 1.018) is None
assert bl.ratchet_stop(None, 1.1) is None and bl.ratchet_stop(1.0, None) is None
# COW peaked +4.3% then fell to -11.2%. Armed: floor = entry +0.5%.
f = bl.ratchet_stop(0.1391, 0.1391 * 1.043)
assert f is not None and abs(f / 0.1391 - 1.005) < 1e-6,     "COW must exit at +0.5%, not -11.2%"
# ACE peaked +6.1% then fell to -7.9%. Same lock.
f = bl.ratchet_stop(0.2241, 0.2241 * 1.061)
assert f is not None and abs(f / 0.2241 - 1.005) < 1e-6
# DEXE peaked +7.6%: still stage-1 (under +8%)
f = bl.ratchet_stop(1.852, 1.852 * 1.076)
assert abs(f / 1.852 - 1.005) < 1e-6
# past +8% MFE, half the peak is locked: peak +10% -> floor +5%
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
good = [0.11, -0.02, 0.05, -0.01, 0.08, 0.03]          # 4/6 wins, mean > 0
ok, why = bl.watcher_earned(good)
assert ok and "earned" in why, why
# enough trips but a losing record stays benched
bad = [0.11, -0.05, -0.06, -0.04, -0.09, -0.02]        # 1/6 wins
ok, why = bl.watcher_earned(bad)
assert not ok and "does not justify" in why, why
# only the rolling window counts: ancient wins cannot carry a rotten present
stale_glory = [0.5] * 10 + [-0.05] * 10
ok, _ = bl.watcher_earned(stale_glory)
assert not ok, "ten old wins must not arm a signal that lost its last ten"

# --- tripwires: these asserts fail any casual edit that widens the blast
# radius. Changing them is a deliberate reviewed act, which is the point.
assert not hasattr(bl, "BOOK_CAP_USD"), \
    "BOOK_CAP_USD reappeared — removing it was a reviewed decision (2026-08-16)"
assert bl.BASE.startswith("https://api.binance.com"), "mainnet host changed"
assert "testnet.binance.vision" in binance_broker.BASE, \
    "the shadow broker must stay on testnet"

print("test_lottery_guards: ALL PASS")
