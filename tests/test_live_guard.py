"""live_guard rules — every unwaivable rule fails this file if weakened.
Plain script (fleet convention), no pytest. Pure-function core: state, kill
switch, and watcher freshness are injected; data/ is never touched."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import live_guard  # noqa: E402

FRESH = dict(state={"start_equity": 325.0, "frozen": None, "orders": {}},
             kill_switch_exists=False, watcher_ok=True)


def check(action="BUY", ticker="IWM", value=300.0, units=1.0, equity=325.0,
          **over):
    kw = {**FRESH, **over}
    return live_guard.check(action, ticker, value, units, equity, **kw)


# kill switch blocks everything, even liquidation
ok, why = check(kill_switch_exists=True)
assert not ok and "KILL SWITCH" in why, why
ok, why = check(action="SELL", kill_switch_exists=True)
assert not ok, "kill switch must block sells too"

# frozen book never trades again
ok, why = check(state={"start_equity": 325.0,
                       "frozen": {"date": "2026-08-14", "rule": "floor"},
                       "orders": {}})
assert not ok and "FROZEN" in why, why

# floor: equity at 75% of start blocks BUY but allows the liquidating SELL
ok, why = check(equity=243.0)
assert not ok and "FLOOR" in why, why
ok, why = check(action="SELL", equity=243.0)
assert ok, f"liquidation must pass at the floor: {why}"

# stale watcher blocks entries only
ok, why = check(watcher_ok=False)
assert not ok and "Watcher" in why, why
ok, why = check(action="SELL", watcher_ok=False)
assert ok, f"exits must never be blocked by a dead feed: {why}"

# throttle: 2 orders/day
from datetime import datetime, timezone
today = str(datetime.now(timezone.utc).date())
ok, why = check(state={"start_equity": 325.0, "frozen": None,
                       "orders": {today: 2}})
assert not ok and "throttle" in why, why

# fee cap: sub-$100 orders die at IBKR's $1 minimum (>1%)
ok, why = check(value=80.0, units=0.5)
assert not ok and "fee cap" in why, why
# a full-book pilot order passes
ok, why = check(value=300.0, units=1.5)
assert ok, why

# record_order: seeds start equity, counts the day, freezes after a
# floor-breach SELL — exercised against a temp file, never data/
import tempfile, json
tmp = Path(tempfile.mkdtemp()) / "guard_state.json"
st = live_guard.record_order("BUY", "IWM", 325.0, path=tmp)
assert st["start_equity"] == 325.0 and st["orders"][today] == 1
st = live_guard.record_order("SELL", "IWM", 240.0, path=tmp)
assert st["frozen"], "floor-breach SELL must freeze the book"
assert json.loads(tmp.read_text())["frozen"]

print("test_live_guard: ALL PASS")
