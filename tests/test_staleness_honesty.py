"""Staleness honesty — the 08-07..08-13 silent-open family.
1. sentinel_trader.scan_is_stale: dead/old scans read as stale, fresh don't.
2. analyst_agent._watcher: a stale verdict reports UNKNOWN, never its last
   risk_level (the 96h-stale 'caution' the agent cited on 08-11).
Plain script, no pytest. Never touches data/ — paths are monkeypatched."""
import json
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import sentinel_trader  # noqa: E402
import sentinel_gate    # noqa: E402
import analyst_agent    # noqa: E402


def iso_hours_ago(h):
    return (datetime.now(timezone.utc) - timedelta(hours=h)).isoformat()


# --- scan_is_stale ----------------------------------------------------------
assert sentinel_trader.scan_is_stale(None), "no scan must read stale"
assert sentinel_trader.scan_is_stale({}), "unreadable ts must read stale"
assert sentinel_trader.scan_is_stale({"ts": iso_hours_ago(30)}), "30h is stale"
assert not sentinel_trader.scan_is_stale({"ts": iso_hours_ago(2)}), "2h is fresh"

# --- _watcher honesty -------------------------------------------------------
tmp = Path(tempfile.mkdtemp())
orig = sentinel_gate.VERDICT
try:
    # fresh caution -> reported as-is with real keys
    sentinel_gate.VERDICT = tmp / "sentinel_verdict.json"
    sentinel_gate.VERDICT.write_text(json.dumps(
        {"ts": iso_hours_ago(2), "risk_level": "caution",
         "risk_alerts": [{"headline": "x"}]}))
    w = analyst_agent._watcher()
    assert w["risk_level"] == "caution" and "risk_alerts" in w and "ts" in w, w

    # 96h stale caution -> UNKNOWN with the last-known verdict quarantined
    sentinel_gate.VERDICT.write_text(json.dumps(
        {"ts": iso_hours_ago(96), "risk_level": "caution"}))
    w = analyst_agent._watcher()
    assert w["risk_level"] == "unknown", f"stale must be unknown, got {w}"
    assert "not calm" in w["note"], w
    assert w["last_known"]["risk_level"] == "caution", w

    # missing file -> unknown
    sentinel_gate.VERDICT = tmp / "nope.json"
    w = analyst_agent._watcher()
    assert w["risk_level"] == "unknown", w
finally:
    sentinel_gate.VERDICT = orig

# --- receipt check ----------------------------------------------------------
d = {"action": "buy", "ticker": "SPY", "conviction": "low",
     "reasoning": "Watcher remains caution, trend up", "falsifier": "x"}
_, _, tag = analyst_agent.apply_guardrails(d, "CASH", 1000.0, False, ())
assert "UNRECEIPTED WATCHER CLAIM" in tag, tag
_, _, tag = analyst_agent.apply_guardrails(d, "CASH", 1000.0, False,
                                           ("read_watcher",))
assert "UNRECEIPTED" not in tag, tag
d2 = {**d, "reasoning": "SPY above 50-day, no macro event this week"}
_, _, tag = analyst_agent.apply_guardrails(d2, "CASH", 1000.0, False, ())
assert "UNRECEIPTED" not in tag, tag

print("test_staleness_honesty: ALL PASS")
