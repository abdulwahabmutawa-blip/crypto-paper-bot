"""Pure-function guards of the playbook book. Run: python tests/test_playbook_guards.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
os.environ.pop("PLAYBOOK_LIVE", None)
os.environ.pop("PLAYBOOK_API_KEY", None)
os.environ.pop("PLAYBOOK_API_SECRET", None)

import playbook_live as pb

# --- arming: inert without BOTH keys and the flag --------------------------
assert not pb.armed()
os.environ["PLAYBOOK_LIVE"] = "1"
assert not pb.armed(), "flag without keys must stay inert"
os.environ["PLAYBOOK_API_KEY"] = "k"
os.environ["PLAYBOOK_API_SECRET"] = "s"
assert pb.armed()
os.environ["PLAYBOOK_LIVE"] = "0"
assert not pb.armed(), "keys without flag must stay inert"
for v in ("PLAYBOOK_LIVE", "PLAYBOOK_API_KEY", "PLAYBOOK_API_SECRET"):
    os.environ.pop(v, None)

# --- isolation: this module must never read account #1's env names ----------
src = open(os.path.join(os.path.dirname(__file__), "..", "src",
                        "playbook_live.py"), encoding="utf-8").read()
assert "BINANCE_LIVE_API" not in src, "book #2 must never touch book #1 keys"
assert "LOTTERY_LIVE" not in src, "book #2 must never read book #1's arming"
assert "lottery_state" not in src and "lottery_ledger" not in src, \
    "book #2 must never touch book #1 state files"

# --- climax verdict ---------------------------------------------------------
# kline row: [open_time, open, high, low, close, vol, close_time, quote_vol]
def bar(o, h, low, c, qv):
    return [0, o, h, low, c, 0, 0, qv]

# red close on move-max volume, closed in lower half -> exit
assert pb.climax_verdict(bar(100, 110, 90, 94, 500), 400, 100) is not None
# green candle never a climax
assert pb.climax_verdict(bar(100, 110, 90, 106, 500), 400, 100) is None
# red but small volume -> hold
assert pb.climax_verdict(bar(100, 110, 90, 94, 120), 400, 100) is None
# red on big volume but closed in UPPER half (bid held) -> hold
assert pb.climax_verdict(bar(100, 110, 90, 104, 500), 400, 100) is None
# fallback path: 5x move average qualifies even below running max
assert pb.climax_verdict(bar(100, 110, 90, 94, 500), 0, 90) is not None

# --- terminal dip ------------------------------------------------------------
assert pb.terminal_dip_verdict([88.0, 87.9, 88.2], 100.0) is not None  # -12%
assert pb.terminal_dip_verdict([92.0, 91.0, 93.0], 100.0) is None      # -9%
assert pb.terminal_dip_verdict([], 100.0) is None
assert pb.terminal_dip_verdict([88.0], None) is None

# --- ratchet -----------------------------------------------------------------
assert pb.ratchet_floor(100.0, 105.0) is None, "must not arm below +10%"
f = pb.ratchet_floor(100.0, 120.0)
assert f is not None and abs(f - 110.0) < 1e-9, "keeps 50% of a +20% peak"
assert pb.ratchet_floor(None, 120.0) is None

# --- entry trigger -----------------------------------------------------------
# --- sell sizing: unknown balances never fire (review 08-21 critical) ------
assert pb.sell_sizing(100.0, None) == 0.0, \
    "unreadable balance must sell NOTHING, never default to owned"
assert pb.sell_sizing(100.0, 0.0) == 0.0, \
    "missing asset means 0 sellable, not full recorded units"
assert pb.sell_sizing(100.0, 40.0) == 40.0, "exchange balance caps the sell"
assert pb.sell_sizing(100.0, 500.0) == 100.0, \
    "never sell more than the bot bought (owner holds other coins)"
assert pb.sell_sizing(0.0, 500.0) == 0.0

# --- terminal dip: needs 3 POST-ENTRY closes (review: pre-entry data) -------
assert pb.terminal_dip_verdict([88.0, 87.9], 100.0) is None, \
    "fewer than 3 post-entry closes must never judge the position"

# --- climax stats must EXCLUDE the judged candle (review off-by-one):
# a red bar on volume equal to the prior max STILL fires (>= prior max)...
def bar2(o, h, low, c, qv):
    return [0, o, h, low, c, 0, 0, qv]
assert pb.climax_verdict(bar2(100, 110, 90, 94, 400), 400, 100) is not None
# ...which is exactly why the caller must not fold it in first: folded-in,
# prior_max becomes its own qv and the rule still fires here — the caller-
# side contract is asserted in the source comment and exercised in dry runs.

def rows(prices, qvs):
    out = []
    for i, (p, q) in enumerate(zip(prices, qvs)):
        out.append([i, p, p * 1.001, p * 0.999, p, 0, i, q])
    return out

flat = [100.0] * 52
quiet = [100.0] * 52
ok, note = pb.entry_trigger(rows(flat, quiet))
assert not ok
# two +4% closes on 3x volume breaking the base
prices = [100.0] * 50 + [104.5, 109.0]
qvs = [100.0] * 50 + [400.0, 420.0]
ok, note = pb.entry_trigger(rows(prices, qvs))
assert ok, note
# same closes but volume only 2x -> refuse
qvs2 = [100.0] * 50 + [200.0, 210.0]
ok, _ = pb.entry_trigger(rows(prices, qvs2))
assert not ok
# +4% closes under a higher old high (no breakout) -> refuse
prices3 = [100.0] * 25 + [130.0] + [100.0] * 24 + [104.5, 109.0]
ok, _ = pb.entry_trigger(rows(prices3, qvs))
assert not ok
assert pb.entry_trigger([]) == (False, "insufficient history")

print("test_playbook_guards: ALL PASS")
