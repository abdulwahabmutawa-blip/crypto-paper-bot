"""binance_broker offline checks — mapping, lot math, signing, no-op safety.
Plain script, no pytest, no network: everything here runs without keys."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import binance_broker as bb  # noqa: E402

# symbol mapping
assert bb.to_symbol("BTC-USD") == "BTCUSDT"
assert bb.to_symbol("doge-usd") == "DOGEUSDT"
assert bb.base_asset("XRP-USD") == "XRP"

# lot flooring: down to the step grid, never up
assert bb.lot_floor(0.123456, 0.001) == 0.123
assert bb.lot_floor(5.0, 0.0) == 5.0          # no filter -> unchanged
assert bb.lot_floor(0.0009, 0.001) == 0.0     # below one step -> zero

# HMAC signature — known vector (Binance docs example secret/params shape)
sig = bb.sign("testsecret", {"symbol": "BTCUSDT", "side": "BUY"})
import hashlib, hmac as h
expect = h.new(b"testsecret", b"symbol=BTCUSDT&side=BUY",
               hashlib.sha256).hexdigest()
assert sig == expect, sig

# testnet lock: base URL must be the testnet host — this assert is the tripwire
# against anyone "just switching the URL" to mainnet in place
assert "testnet.binance.vision" in bb.BASE

# no keys -> enabled False and shadow_fill is a silent no-op
for k in ("BINANCE_TESTNET_API_KEY", "BINANCE_TESTNET_API_SECRET"):
    os.environ.pop(k, None)
assert not bb.enabled()
assert bb.shadow_fill("BUY", "BTC-USD", 100.0) is None
assert bb.shadow_fill("SELL", "ETH-USD", 100.0) is None
# non-crypto ticker -> no-op even with keys present
os.environ["BINANCE_TESTNET_API_KEY"] = "x"
os.environ["BINANCE_TESTNET_API_SECRET"] = "y"
assert bb.shadow_fill("BUY", "SPY", 100.0) is None
for k in ("BINANCE_TESTNET_API_KEY", "BINANCE_TESTNET_API_SECRET"):
    os.environ.pop(k, None)

# fee model: 10bps + half default spread on $325
import risk_common
f = risk_common.binance_fee(325.0)
assert abs(f - 325.0 * (10.0 + 8.0 / 2) / 10_000.0) < 1e-9, f

print("test_binance_broker: ALL PASS")
