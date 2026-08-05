"""Offline verification of selection_engine v2 features (fake feed, temp state).

Covers: vol-target sizing + cash cushion, mark = cash + position, trailing
stop, cooldown, legacy all-in bots unchanged, crypto-aware deferral.
"""
import json
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import config
import market_hours
import risk_common
import selection_engine

# Tests 1-9 predate the fee model and assert exact zero-fee cash math;
# they run with fees off. Tests 10-11 turn them back on and test them.
risk_common.EQUITY_BPS = 0.0
risk_common.CRYPTO_BPS = 0.0

TMP = Path(tempfile.mkdtemp())
config.DATA = TMP / "data"; config.DATA.mkdir()
config.REPORTS = TMP / "reports"; config.REPORTS.mkdir()
market_hours.us_equities_open = lambda now=None: True

FRAME = {"df": None}
selection_engine._fetch_daily = lambda u, b: (FRAME["df"].ffill(), FRAME["df"])
# 3-tuple since 2026-08-04: (prices, ts, raw 5m frame used for honest dating)
selection_engine._fetch_live = lambda u, b: ({}, "2026-07-31T00:00:00+00:00", None)


def mk_frame(days, aaa_path, spy=500.0):
    """AAA follows aaa_path (list of closes); SPY flat; BBB-USD flat 100."""
    idx = pd.bdate_range("2025-01-01", periods=days)
    aaa = list(aaa_path) + [aaa_path[-1]] * (days - len(aaa_path))
    return pd.DataFrame({"AAA": aaa[:days], "BBB-USD": 100.0, "SPY": spy}, index=idx)


def spec(key, pick_fn, **extra):
    s = {"key": key, "universe": ["AAA", "BBB-USD"], "bench": "SPY",
         "signal": lambda close, holding: (pick_fn(close, holding), [], "t"),
         "risk_gate": False,
         "meta": {"title": "t", "badge": "t", "bench_label": "t", "board_note": "t"},
         "strategy": {"name": "t", "rule": "t", "backtest_cagr": "t",
                      "backtest_maxdd": "t"}}
    s.update(extra)
    return s


def state(key):
    return json.loads((config.DATA / f"{key}_state.json").read_text())


# ---- 1. vol sizing: high-vol asset gets a fractional position + cash cushion
rng = np.random.default_rng(7)
path = list(100 * np.cumprod(1 + rng.normal(0, 0.04, 250)))  # ~63% ann vol
FRAME["df"] = mk_frame(250, path)
s = spec("t1", lambda c, h: "AAA", risk={"trailing": 0.10, "cooldown_days": 5},
         vol_target=0.20)
st = selection_engine.run(s)
vol = FRAME["df"]["AAA"].pct_change().rolling(90).std().iloc[-1] * (252 ** 0.5)
frac = min(1.0, 0.20 / float(vol))
assert frac < 0.6, f"test setup: expected clearly fractional, got {frac}"
px = FRAME["df"]["AAA"].iloc[-1]
assert abs(st["units"] * px - 1000 * frac) < 1e-6, "position != frac * equity"
assert abs(st["cash"] - 1000 * (1 - frac)) < 1e-6, "cash cushion wrong"
v = st["history"][-1]["value"]
assert abs(v - 1000) < 0.01, f"mark must equal cash+position at entry, got {v}"
print(f"1. vol sizing OK (frac {frac:.0%}, cash cushion ${st['cash']:.2f})")

# ---- 2. trailing stop fires at -10% from HWM; sell banks cushion + proceeds
base = state("t1")
FRAME["df"] = mk_frame(252, path + [px * 1.05, px * 1.08])
selection_engine.run(s)                      # hwm rides to the peak (own cycle)
peak_path = path + [px * 1.05, px * 1.08, px * 1.08 * 0.89]  # then -11%
FRAME["df"] = mk_frame(253, peak_path)
selection_engine.run(s)                      # stop fires this cycle
st = state("t1")
assert st["holding"] == "CASH", "trailing stop did not fire"
assert st["trades"][-1]["reason"].startswith("TRAILING STOP"), st["trades"][-1]
assert st.get("stopped", {}).get("ticker") == "AAA", "stopped marker missing"
assert "hwm" not in st, "hwm must clear on CASH"
expected = base["cash"] + base["units"] * peak_path[-1]
assert abs(st["cash"] - expected) < 1e-6, "sell proceeds lost the cash cushion"
print(f"2. trailing stop OK (banked ${st['cash']:.2f})")

# ---- 3. cooldown blocks re-entry, then expires
FRAME["df"] = mk_frame(254, peak_path + [peak_path[-1]])
selection_engine.run(s)                      # next day: signal still says AAA
st = state("t1")
assert st["holding"] == "CASH", "cooldown failed to block re-entry"
FRAME["df"] = mk_frame(262, peak_path + [peak_path[-1]] * 9)  # +8 bdays > 5d
selection_engine.run(s)
st = state("t1")
assert st["holding"] == "AAA", "re-entry after cooldown failed"
assert "stopped" not in st, "stopped marker must clear"
print("3. cooldown OK (blocked, then expired)")

# ---- 4. legacy SPEC (no risk/vol_target): all-in, cash 0, mark unchanged
FRAME["df"] = mk_frame(250, path)
st = selection_engine.run(spec("t2", lambda c, h: "AAA"))
assert st["cash"] == 0.0 and abs(st["units"] * px - 1000) < 1e-6, "legacy sizing changed!"
print("4. legacy all-in unchanged OK")

# ---- 5. deferral: market closed -> equity switch defers, crypto proceeds
market_hours.us_equities_open = lambda now=None: False
st = selection_engine.run(spec("t3", lambda c, h: "AAA"))
assert st["holding"] == "CASH", "equity buy must defer when market closed"
st = selection_engine.run(spec("t4", lambda c, h: "BBB-USD"))
assert st["holding"] == "BBB-USD", "crypto buy must not defer"
print("5. deferral OK (equity deferred, crypto filled)")

# ---- 6. stop firing while market CLOSED must not corrupt state (review bug):
# sell defers, 'stopped' NOT persisted; after recovery, position survives
market_hours.us_equities_open = lambda now=None: True
s6 = spec("t6", lambda c, h: "AAA", risk={"trailing": 0.10, "cooldown_days": 5})
FRAME["df"] = mk_frame(250, path)
selection_engine.run(s6)                          # entry, hwm = entry px
market_hours.us_equities_open = lambda now=None: False
FRAME["df"] = mk_frame(251, path + [px * 0.85])   # -15%: stop fires, closed
selection_engine.run(s6)
st = state("t6")
assert st["holding"] == "AAA", "deferred stop must keep the position"
assert "stopped" not in st, "deferred stop must NOT persist 'stopped'"
market_hours.us_equities_open = lambda now=None: True
FRAME["df"] = mk_frame(252, path + [px * 0.85, px * 1.01])  # recovered by open
selection_engine.run(s6)
st = state("t6")
assert st["holding"] == "AAA", "recovered position must NOT be liquidated"
assert "stopped" not in st and not any(
    t["reason"].startswith("TRAILING") for t in st["trades"]), "phantom stop"
print("6. deferred stop OK (no corruption, recovery survives)")

# ---- 7. stop deferred, NO recovery: fills honestly at the open
FRAME["df"] = mk_frame(253, path + [px * 0.85, px * 1.01, px * 0.84])
selection_engine.run(s6)
st = state("t6")
assert st["holding"] == "CASH" and st.get("stopped", {}).get("ticker") == "AAA", \
    "stop must fill at the open and record 'stopped'"
print("7. open-market stop OK (fills, recorded)")

# ---- 8. held ticker with a dead (all-NaN) column: cycle freezes, no NaN state
FRAME["df"] = mk_frame(250, path)
s8 = spec("t8", lambda c, h: "AAA", vol_target=0.20)
selection_engine.run(s8)
before = state("t8")
dead = mk_frame(251, path + [path[-1]])
dead["AAA"] = np.nan
FRAME["df"] = dead
st = selection_engine.run(s8)
after = state("t8")
assert after == before, "dead-column cycle must not mutate state"
assert not any(v != v for v in [after["cash"], after["units"]]), "NaN leaked"
print("8. dead-column freeze OK")

# ---- 9. regressed feed: no trade, no history write, but STILL ALIVE
# (the 2026-08-03/04 lockups — a lagging feed took bots fully offline)
FRAME["df"] = mk_frame(250, path)
s9 = spec("t9", lambda c, h: "AAA")
selection_engine.run(s9)
before = state("t9")
assert before["holding"] == "AAA"
import time
time.sleep(1.1)                     # timestamps are second-resolution
FRAME["df"] = mk_frame(249, path[:-1])          # feed regresses one bar
st = selection_engine.run(spec("t9", lambda c, h: "BBB-USD"))
after = state("t9")
assert after["holding"] == "AAA", "must not trade on a regressed feed"
assert after["history"] == before["history"], "must not write behind newest mark"
assert after["feed_delayed"] is True, "must flag the delay"
assert after["last_updated_utc"] != before["last_updated_utc"], \
    "must still record a heartbeat — a lagging feed is not a dead bot"
assert (config.REPORTS / "t9_dashboard.html").exists(), "must still render"
payload = json.loads((config.REPORTS / "t9_dashboard_data.json").read_text())
assert "feed is running behind" in payload["thoughts"], "must say so on the page"
print("9. regressed feed OK (no trade, no bad mark, still alive + rendering)")

# ---- 10. transaction costs: every fill pays its fee, ledger records it
risk_common.EQUITY_BPS = 10.0
FRAME["df"] = mk_frame(250, path)
st = selection_engine.run(spec("t10", lambda c, h: "AAA"))
fee0 = 1000 * 10 / 10_000                      # $1 on the $1,000 entry
assert abs(st["costs_paid"] - fee0) < 1e-9, f"costs_paid {st['costs_paid']}"
assert st["trades"][-1]["fee"] == round(fee0, 2), "fee missing from trade"
assert abs(st["history"][-1]["value"] - (1000 - fee0)) < 0.01, \
    "mark must reflect the fee paid"
FRAME["df"] = mk_frame(251, path + [path[-1]])
st = selection_engine.run(spec("t10", lambda c, h: "CASH"))
assert st["costs_paid"] > fee0, "sell side must also pay a fee"
assert st["trades"][-1]["reason"] != "", "exit recorded"
print(f"10. cost model OK (fees ${st['costs_paid']:.2f} across entry+exit)")

# ---- 11. R1 kill floor: breach liquidates, freezes, and stays frozen
risk_common.EQUITY_BPS = 0.0
crash = path + [px * 0.60]                     # position falls ~40% -> < $750
FRAME["df"] = mk_frame(250, path)
selection_engine.run(spec("t11", lambda c, h: "AAA"))
FRAME["df"] = mk_frame(251, crash)
st = selection_engine.run(spec("t11", lambda c, h: "AAA"))
assert st["holding"] == "CASH", "R1 breach must liquidate"
assert st.get("frozen"), "R1 breach must freeze the book"
assert any(t["reason"].startswith("R1 KILL FLOOR") for t in st["trades"]), \
    "liquidation must carry the R1 reason"
FRAME["df"] = mk_frame(252, crash + [px])      # price fully recovers
st = selection_engine.run(spec("t11", lambda c, h: "AAA"))
assert st["holding"] == "CASH" and st.get("frozen"), \
    "frozen book must NEVER trade again, even on recovery"
print("11. R1 kill floor OK (liquidated, frozen, stays frozen)")

print("ALL PASS")
