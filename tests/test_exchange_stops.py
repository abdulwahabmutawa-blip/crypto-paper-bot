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

# --- INERT UNLESS LIVE; ON BY DEFAULT ONCE LIVE (opt-out since 2026-09-02) --
assert not bl.exchange_stops_armed(), "nothing set must not arm"
os.environ["LOTTERY_EXCHANGE_STOPS"] = "1"
assert not bl.exchange_stops_armed(), "its own flag must not arm live trading"
os.environ["BINANCE_LIVE_API_KEY"] = "k"
os.environ["BINANCE_LIVE_API_SECRET"] = "s"
os.environ["LOTTERY_LIVE"] = "1"
assert bl.armed()
assert bl.exchange_stops_armed(), "keys + live + own flag = armed"
os.environ.pop("LOTTERY_EXCHANGE_STOPS", None)
assert bl.exchange_stops_armed(), \
    "a live book with nothing set rests its floor at the exchange (default ON)"
os.environ["LOTTERY_EXCHANGE_STOPS"] = "0"
assert bl.armed() and not bl.exchange_stops_armed(), \
    "an explicit 0 keeps the poll-only path"
# and while disarmed, placement is inert without touching the network
assert bl.place_protective_stop("AXSUSDT", 10.0, 1.0) is None

# --- THE FLOOR MIRRORS THE POLL RULES ------------------------------------
e = 1.005
assert bl.protective_floor(None, None, -0.10) is None
assert bl.protective_floor(0, None, -0.10) is None
# no peak yet -> the hard stop, and the hard stop is per-seat
assert abs(bl.protective_floor(e, None, -0.10) - e * 0.90) < 1e-9
assert abs(bl.protective_floor(e, None, -0.06) - e * 0.94) < 1e-9

# 2026-09-03: ONLY the hard stop rests at the exchange (a resting ratchet
# wicked ZEC out of a +31% ride at +6% in the replay); the poll path keeps
# the ratchet and the 10% trail.
for mfe in (0.0, 0.02, 0.04, 0.08, 0.12, 0.5, 1.2):
    f = bl.protective_floor(e, e * (1 + mfe), -0.10)
    assert abs(f - e * 0.90) < 1e-9, "resting floor must be the hard stop only"
assert bl.trail_pct(0.05) == -0.15 and bl.trail_pct(0.10) == -0.10 and bl.trail_pct(1.5) == -0.10

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
