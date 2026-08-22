"""Repeat-loser memory — the guard that stops the book paying twice to learn
the same thing. CHIPUSDT was bought five times for a net -$5.72 because
st["stopped"] is a 3h cooldown and nothing remembered the losses.

Offline: no network, no keys, no data/ writes.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import binance_live as bl  # noqa: E402


def T(sym, pnl):
    return {"symbol": sym, "pnl_usd": pnl}


HWM = 60.0          # 5% line = -$3.00

# --- the count test -------------------------------------------------------
assert bl.retired_symbols([T("A", -0.10)], HWM) == {}, "one small loss is not a verdict"
assert "A" in bl.retired_symbols([T("A", -0.10), T("A", -0.10)], HWM)
# wins do not decrement the count: two losses is two losses
assert "A" in bl.retired_symbols([T("A", -0.10), T("A", 5.0), T("A", -0.10)], HWM)

# --- the fraction test ----------------------------------------------------
# one loss, but a big one -> retired on cost alone, before a second attempt
assert "B" in bl.retired_symbols([T("B", -3.50)], HWM)
assert "B" not in bl.retired_symbols([T("B", -2.99)], HWM), "just inside the line"

# the line scales with the book, so a deposit does not loosen it
assert "B" in bl.retired_symbols([T("B", -3.50)], HWM)
assert "B" not in bl.retired_symbols([T("B", -3.50)], 200.0), \
    "on a bigger book the same loss is proportionally smaller"

# a symbol that lost then more than recovered is not retired by cost
assert "C" not in bl.retired_symbols([T("C", -5.0), T("C", 6.0)], HWM)

# --- degradation ----------------------------------------------------------
# no high-water mark: the fraction test is disabled but the COUNT still holds,
# so an unreadable book value cannot silently switch the whole guard off
assert bl.retired_symbols([T("D", -9.0)], None) == {}
assert "D" in bl.retired_symbols([T("D", -9.0), T("D", -9.0)], None)
assert bl.retired_symbols(None, HWM) == {}
assert bl.retired_symbols([], HWM) == {}
# malformed rows must not crash or poison the tally
assert bl.retired_symbols([{}, {"symbol": "E"}, T("E", -3.5)], HWM).get("E")

# --- the real tape --------------------------------------------------------
# replayed on the actual 23 trades, CHIP is retired at its FIRST entry, which
# is the whole point: the four re-entries never happen.
chip = [T("CHIPUSDT", -3.47), T("CHIPUSDT", -1.74), T("CHIPUSDT", -0.66),
        T("CHIPUSDT", 0.42), T("CHIPUSDT", -0.27)]
assert "CHIPUSDT" in bl.retired_symbols(chip[:1], 44.0), \
    "the -$3.47 first loss alone must retire it"

# and the guard is honest about what it cannot do: it never blocks trade #1
assert bl.retired_symbols([], 44.0) == {}

print("test_repeat_losers: OK")
