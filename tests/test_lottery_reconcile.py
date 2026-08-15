"""Lottery ledger-reconciliation logic — the money-safety audit fixes.
Pure: no network, no keys, no real state files. Exercises the reconciliation
scan and cooldown pruning as standalone logic mirrors."""
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))


def reconcile(ledger_lines):
    """Mirror of lottery_live's ledger scan: last BUY fill with no closing
    SELL/exit is the open seat; None if flat."""
    ledger_open = None
    for e in ledger_lines:
        if e.get("event") == "fill" and e.get("action") == "BUY":
            ledger_open = e
        elif ledger_open and e.get("symbol") == ledger_open.get("symbol") \
                and (e.get("event") == "exit"
                     or (e.get("event") == "fill" and e.get("action") == "SELL")):
            ledger_open = None
    return ledger_open


# BUY then nothing -> open seat
assert reconcile([{"event": "fill", "action": "BUY", "symbol": "AAAUSDT",
                   "price": 1.0, "qty": 10}])["symbol"] == "AAAUSDT"

# BUY then exit -> flat (the critical fix: old code ignored the close and
# would re-adopt AAAUSDT, then sell the owner's own AAA on the next exit)
assert reconcile([
    {"event": "fill", "action": "BUY", "symbol": "AAAUSDT", "price": 1.0, "qty": 10},
    {"event": "exit", "symbol": "AAAUSDT", "reason": "stop"},
]) is None

# BUY then a SELL FILL whose exit line was lost to a crash -> still flat
assert reconcile([
    {"event": "fill", "action": "BUY", "symbol": "AAAUSDT", "price": 1.0, "qty": 10},
    {"event": "fill", "action": "SELL", "symbol": "AAAUSDT", "price": 1.1, "qty": 10},
]) is None

# full round trip then a new BUY -> the new seat is open
o = reconcile([
    {"event": "fill", "action": "BUY", "symbol": "AAAUSDT", "price": 1.0, "qty": 10},
    {"event": "exit", "symbol": "AAAUSDT"},
    {"event": "fill", "action": "BUY", "symbol": "BBBUSDT", "price": 2.0, "qty": 5},
])
assert o["symbol"] == "BBBUSDT"

# a SELL for a DIFFERENT symbol must not close the open seat
o = reconcile([
    {"event": "fill", "action": "BUY", "symbol": "AAAUSDT", "price": 1.0, "qty": 10},
    {"event": "fill", "action": "SELL", "symbol": "ZZZUSDT", "price": 9, "qty": 1},
])
assert o and o["symbol"] == "AAAUSDT"


def prune_cooldown(stopped, now, cooldown_h=3.0):
    """Mirror of the time-based cooldown prune."""
    def _in(ts):
        try:
            return (now - datetime.fromisoformat(ts)).total_seconds() / 3600.0 < cooldown_h
        except Exception:
            return False
    return {s: ts for s, ts in stopped.items() if _in(ts)}


now = datetime(2026, 8, 15, 18, 0, tzinfo=timezone.utc)
recent = (now - timedelta(hours=1)).isoformat()
old = (now - timedelta(hours=5)).isoformat()
kept = prune_cooldown({"AAAUSDT": recent, "BBBUSDT": old, "CCCUSDT": "garbage"}, now)
assert "AAAUSDT" in kept, "1h-old stop is still in cooldown"
assert "BBBUSDT" not in kept, "5h-old stop has expired"
assert "CCCUSDT" not in kept, "unparseable legacy scan_ts value expires"

print("test_lottery_reconcile: ALL PASS")
