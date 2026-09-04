"""Small-wins lab — offline checks of the resolver, features and the
pre-registered break-even arithmetic. No network, no writes."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import smallwins_lab as sw  # noqa: E402

FUTURE_CLOSE = 10 ** 15     # a candle closing in the far future = still open


def candle(t, o, h, l, c, qv=1000.0, tb=600.0, close_t=None):
    return [t, o, h, l, c, 0, close_t if close_t is not None else t + 899_000, qv, 10, 0, tb, 0]


def test_resolver_target_stop_time():
    pos = {"entry": 100.0, "entry_ms": 0, "target": 0.02, "stop": 0.02, "max_h": 1}
    # target touched first
    k = [candle(900_000, 100, 102.5, 99.5, 101)]
    r = sw.resolve(pos, k)
    assert r and r[1] == "TARGET" and abs(r[0] - (0.02 - sw.COST)) < 1e-9
    # both touched in one candle -> STOP FIRST (pre-registered)
    k = [candle(900_000, 100, 103, 97, 101)]
    assert sw.resolve(pos, k)[1] == "STOP"
    # nothing touched, deadline passes -> TIME at close
    k = [candle(900_000, 100, 100.5, 99.6, 100.2), candle(3_600_000, 100.2, 100.9, 99.7, 100.4)]
    r = sw.resolve(pos, k)
    assert r[1] == "TIME" and abs(r[0] - (1.004 - 1 - sw.COST)) < 1e-9
    # still-open candle is never used
    k = [candle(900_000, 100, 105, 99, 104, close_t=FUTURE_CLOSE)]
    assert sw.resolve(pos, k) is None


def test_breakeven_arithmetic():
    # +1% target / -1% stop needs (0.01+0.0025)/0.02 = 62.5%
    assert abs(sw.breakeven(0.01, 0.01) - 0.625) < 1e-9
    # +3% / -2% needs 45%
    assert abs(sw.breakeven(0.03, 0.02) - 0.45) < 1e-9


def test_features_shape():
    k = [candle(i * 900_000, 100, 101, 99, 100 + (i % 3) * 0.1) for i in range(120)]
    b = [candle(i * 900_000, 50000, 50100, 49900, 50000) for i in range(120)]
    F = sw.features(k, b)
    assert F and set(F) >= {"px", "r1h", "r4h", "r24", "v4h", "tbs4h", "rp24", "rng24", "btc1", "btc4", "btc24"}
    assert 0.0 <= F["rp24"] <= 1.0 and 0.0 <= F["tbs4h"] <= 1.0
    assert sw.features(k[:50], b) is None
    assert sw.features(k[:99], b[:99]) is not None, "99 closed candles (a 100-limit fetch minus the open one) must work"


def test_grid_is_sane():
    for target, stop, max_h in sw.GRID:
        assert 0 < target <= 0.05 and 0 < stop <= 0.05 and 1 <= max_h <= 48
        assert sw.breakeven(target, stop) < 0.85, "a tactic nobody can clear is not a test"
