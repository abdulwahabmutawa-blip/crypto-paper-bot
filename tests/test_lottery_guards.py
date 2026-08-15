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
    # book cap blocks BOTH sides once the book outgrows the lottery
    why = bl.guard("BUY", "PEPEUSDT", {"USDT": 25.0}, None)
    assert why and "BOOK CAP" in why, why
    why = bl.guard("SELL", "PEPEUSDT", {"USDT": 25.0}, None)
    assert why and "BOOK CAP" in why, "cap must block an over-cap book entirely"

    # dust: below the exchange minimum there is nothing to do
    why = bl.guard("BUY", "PEPEUSDT", {"USDT": 3.0}, None)
    assert why and "DUST" in why, why

    # the real ~$11 book passes
    assert bl.guard("BUY", "PEPEUSDT", {"USDT": 11.0}, None) is None

    # the bot's book is its OWN units, not the owner's whole holding of the
    # same coin. Owner holds 1,000,000 PEPE; the bot bought 100. Valuing the
    # free balance would price the book at the owner's stack and trip the cap
    # (and, worse, imply the bot may sell it).
    orig_price = bl.price
    bl.price = lambda sym: 0.00002        # PEPE-ish
    try:
        bals = {"USDT": 1.0, "PEPE": 1_000_000.0}
        assert bl.managed_value(bals, "PEPEUSDT", units=100.0) < 2.0, \
            "book must count only the bot's units"
        assert bl.managed_value(bals, "PEPEUSDT") > 20.0, \
            "sanity: the whole free balance really is over the cap"
        # with units passed, a normal cycle is allowed; without, it trips
        assert bl.guard("SELL", "PEPEUSDT", bals, "PEPEUSDT", 100.0) is None
        assert "BOOK CAP" in (bl.guard("SELL", "PEPEUSDT", bals, "PEPEUSDT") or "")
    finally:
        bl.price = orig_price

    # kill switch beats everything
    tmp_ks.write_text("stop")
    why = bl.guard("BUY", "PEPEUSDT", {"USDT": 11.0}, None)
    assert why and "KILL SWITCH" in why, why
finally:
    bl.KILL_SWITCH = orig_ks
    for k in ("BINANCE_LIVE_API_KEY", "BINANCE_LIVE_API_SECRET", "LOTTERY_LIVE"):
        os.environ.pop(k, None)

# --- tripwires: these asserts fail any casual edit that widens the blast
# radius. Changing them is a deliberate reviewed act, which is the point.
assert bl.BOOK_CAP_USD == 20.0, "book cap moved — that is a reviewed decision"
assert bl.BASE.startswith("https://api.binance.com"), "mainnet host changed"
assert "testnet.binance.vision" in binance_broker.BASE, \
    "the shadow broker must stay on testnet"

print("test_lottery_guards: ALL PASS")
