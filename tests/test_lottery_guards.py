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

# --- late-entry guard: the book's real trades, as fixtures -----------------
# Measured as RUN-UP FROM THE 24H LOW — close-to-close decays as a pump
# rolls over, which is how CHIP's second entry dodged the first cap.
# COW (watcher): +37.6% off its low, -2.3% in the hour, bought 9h after its
# top -> -11.2%. BOTH rules must catch it.
why = bl.late_entry(0.376, -0.023)
assert why and "LATE" in why, "the COW entry must be refused"
# CHIP round 1 (watcher): +29.2% off its low, bought AT the local top ->
# -7.7%. The run-up cap alone must catch it.
why = bl.late_entry(0.292, 0.057)
assert why and "LATE" in why, "the CHIP entry must be refused"
# CHIP round 2 (watcher, the 15:30 whipsaw re-buy 6.4% above its own exit):
# day-change had decayed under the old cap, but run-up off the low had not.
# THIS fixture is why the guard measures from the low.
why = bl.late_entry(0.274, 0.001)
assert why and "LATE" in why, "the CHIP re-buy must be refused"
# LINK: +8.0% off its low, flat hour -> the book's only winner. Must pass.
assert bl.late_entry(0.080, 0.001) is None, \
    "the LINK entry was fine and must stay allowed"
# early-stage move: modestly up, accelerating -> the target trade
assert bl.late_entry(0.10, 0.03) is None
# below the run-up cap but red on the hour: hype arrived after the top
why = bl.late_entry(0.10, -0.01)
assert why and "rolling over" in why
# unknown price context: this book goes all-in per entry — never buy blind
why = bl.late_entry(None, 0.02)
assert why and "blind" in why
why = bl.late_entry(0.10, None)
assert why and "blind" in why

# --- per-seat exit clocks (explosion study: grinds take a median 11 DAYS) ---
g = bl.exit_params("scout:revival")
assert g["kind"] == "grind" and g["stall_h"] is None, \
    "a grind's early days LOOK stalled — it must not have a stall clock"
assert g["max_hold_h"] == 336.0, "a 24h clock force-sells every 11-day grind"
b = bl.exit_params("scout:ignition")
assert b["kind"] == "burst" and b["max_hold_h"] == 8.0 \
    and b["stop_pct"] == -0.06
h = bl.exit_params("watcher")
assert h["kind"] == "hype" and h["max_hold_h"] == 24.0 \
    and h["stall_h"] == 6.0
assert bl.exit_params(None)["kind"] == "hype", \
    "an unknown seat gets the strictest familiar clock, never the longest"

# --- tripwires: these asserts fail any casual edit that widens the blast
# radius. Changing them is a deliberate reviewed act, which is the point.
assert not hasattr(bl, "BOOK_CAP_USD"), \
    "BOOK_CAP_USD reappeared — removing it was a reviewed decision (2026-08-16)"
assert bl.BASE.startswith("https://api.binance.com"), "mainnet host changed"
assert "testnet.binance.vision" in binance_broker.BASE, \
    "the shadow broker must stay on testnet"

print("test_lottery_guards: ALL PASS")
