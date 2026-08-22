"""Exchange-side protective stop — the floor that survives the gap between
cycles. AXSUSDT peaked +11.8%, ratchet_stop set a floor at +5.9%, and the
5-minute poll filled it at +1.29%: 4.6 points lost to polling granularity.

The safety property under test is NOT "it works" but "it cannot hurt":
disarmed it is inert, and a failure to place leaves the poll-based exits
exactly as they were.

Offline: no network, no keys, no data/ writes.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import binance_live as bl  # noqa: E402

for k in ("BINANCE_LIVE_API_KEY", "BINANCE_LIVE_API_SECRET",
          "LOTTERY_LIVE", "LOTTERY_EXCHANGE_STOPS"):
    os.environ.pop(k, None)

# --- INERT UNLESS EXPLICITLY ARMED ---------------------------------------
assert not bl.exchange_stops_armed(), "nothing set must not arm"
os.environ["LOTTERY_EXCHANGE_STOPS"] = "1"
assert not bl.exchange_stops_armed(), "its own flag must not arm live trading"
os.environ["BINANCE_LIVE_API_KEY"] = "k"
os.environ["BINANCE_LIVE_API_SECRET"] = "s"
os.environ["LOTTERY_LIVE"] = "1"
assert bl.armed()
assert bl.exchange_stops_armed(), "keys + live + own flag = armed"
os.environ["LOTTERY_EXCHANGE_STOPS"] = "0"
assert bl.armed() and not bl.exchange_stops_armed(), \
    "a live book with the feature off must stay on the poll path"
# and while disarmed, placement is inert without touching the network
assert bl.place_protective_stop("AXSUSDT", 10.0, 1.0) is None

# --- THE FLOOR MIRRORS THE POLL RULES ------------------------------------
e = 1.005
assert bl.protective_floor(None, None, -0.10) is None
assert bl.protective_floor(0, None, -0.10) is None
# no peak yet -> the hard stop, and the hard stop is per-seat
assert abs(bl.protective_floor(e, None, -0.10) - e * 0.90) < 1e-9
assert abs(bl.protective_floor(e, None, -0.06) - e * 0.94) < 1e-9

# the AXSUSDT replay: at its real +11.8% peak the floor is +5.9%
axs = bl.protective_floor(e, e * 1.118, -0.10)
assert abs(axs / e - 1 - 0.059) < 1e-6, (axs / e - 1)
# ...which is 4.6 points above where the poll actually filled it
assert axs / e - 1 > 0.0129 + 0.045

# the floor never sits below what the poll path would defend
for mfe in (0.0, 0.02, 0.04, 0.08, 0.12, 0.5, 1.2):
    hwm = e * (1 + mfe)
    f = bl.protective_floor(e, hwm, -0.10)
    assert f >= e * 0.90 - 1e-9, "never below the hard stop"
    r = bl.ratchet_stop(e, hwm)
    if r:
        assert f >= r - 1e-9, "never below the ratchet"
    assert f >= hwm * (1 + bl.trail_pct(mfe)) - 1e-9, "never below the trail"

# the floor is monotonic in the peak: a ride that climbs never loosens
prev = 0.0
for mfe in (0.0, 0.04, 0.08, 0.12, 0.30, 1.0):
    f = bl.protective_floor(e, e * (1 + mfe), -0.10)
    assert f >= prev - 1e-9, "floor must never fall as the peak rises"
    prev = f

# --- INCREMENT ROUNDING GOES DOWN, NEVER UP ------------------------------
assert bl._down_to(1.2345, 0.01) == 1.23
assert bl._down_to(1.2399, 0.01) == 1.23      # down, not nearest
assert bl._down_to(5.0, 0.0) == 5.0           # unknown increment: unchanged
assert bl._down_to(0.004, 0.01) == 0.0        # flagged by the caller

# --- REPLACEMENT HYSTERESIS ----------------------------------------------
# the floor creeps up every cycle a winner rises; only a real move re-places
assert bl.STOP_REPLACE_EPS > 0
assert abs(1.0000 - 1.0004) / 1.0 <= bl.STOP_REPLACE_EPS   # churn: skipped
assert abs(1.0000 - 1.0100) / 1.0 > bl.STOP_REPLACE_EPS    # real: replaced

# --- the limit sits UNDER the trigger so a fast crash still fills ---------
assert 0 < bl.STOP_LIMIT_SLIP < 0.10

print("test_exchange_stops: OK")
