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

# --- late-entry guard: the book's four real trades, as fixtures ------------
# COW (watcher): +37.3% on the day, -2.3% in the hour, bought 9h after its
# local top -> -11.2%. BOTH rules must catch it.
why = bl.late_entry(0.373, -0.023)
assert why and "LATE" in why, "the COW entry must be refused"
# CHIP (watcher): +27.8% on the day AT the local top, hour still green ->
# -7.8% within 90 minutes. The day-cap alone must catch it.
why = bl.late_entry(0.278, 0.057)
assert why and "LATE" in why, "the CHIP entry must be refused"
# LINK: +7.9% on the day, flat hour -> the book's only winner. Must pass.
assert bl.late_entry(0.079, 0.001) is None, \
    "the LINK entry was fine and must stay allowed"
# early-stage move: modestly up on the day, accelerating -> the target trade
assert bl.late_entry(0.10, 0.03) is None
# below the day-cap but red on the hour: hype arrived after the top
why = bl.late_entry(0.10, -0.01)
assert why and "rolling over" in why
# unknown price context: this book goes all-in per entry — never buy blind
why = bl.late_entry(None, 0.02)
assert why and "blind" in why
why = bl.late_entry(0.10, None)
assert why and "blind" in why

# --- tripwires: these asserts fail any casual edit that widens the blast
# radius. Changing them is a deliberate reviewed act, which is the point.
assert not hasattr(bl, "BOOK_CAP_USD"), \
    "BOOK_CAP_USD reappeared — removing it was a reviewed decision (2026-08-16)"
assert bl.BASE.startswith("https://api.binance.com"), "mainnet host changed"
assert "testnet.binance.vision" in binance_broker.BASE, \
    "the shadow broker must stay on testnet"

print("test_lottery_guards: ALL PASS")
