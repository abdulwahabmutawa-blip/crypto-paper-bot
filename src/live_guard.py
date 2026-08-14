"""Live-money guard — every real (or dry-run) order passes here first.

Enforced in the BROKER path, not the strategy, so no strategy can bypass it
(the 7/31 lesson: guards that live in one module protect only that module).
Pre-registered in GO_LIVE_PLAN_2026-08-14.md Track A4 BEFORE any account
exists; weakening any rule is a human commit, on purpose, with a diff.

Rules (all unwaivable in code):
  * KILL SWITCH: data/KILL_SWITCH file exists -> every order blocked. Touch
    the file, push, and the pilot is dead within one cycle. Delete = revive.
  * FLOOR: equity <= 75% of starting equity -> only liquidating SELLs pass;
    the book freezes permanently once flat (mirrors R1's $750/$1000 ratio).
  * WATCHER: gate not 'ok' (stale/missing scans) -> BUYs blocked, SELLs pass.
    Exits must never be blocked by a dead feed — that's the sentinel_trader
    silent-open bug, inverted.
  * THROTTLE: max 2 orders per UTC day. The fee wall at pilot size makes
    anything faster self-harm (research 08-13 §5).
  * FEE CAP: estimated fee > 1% of order value -> blocked. At IBKR's $1
    minimum this simply refuses orders under ~$100.

Guard state (data/live_guard_state.json) tracks start equity, daily order
counts, and the frozen flag. PAPER-SHADOW SAFE: pure function core, state
path injectable for tests.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import config
import risk_common

STATE_PATH = config.DATA / "live_guard_state.json"
KILL_SWITCH = config.DATA / "KILL_SWITCH"
FLOOR_FRAC = 0.75
MAX_ORDERS_PER_DAY = 2
MAX_FEE_FRAC = 0.01


def _load(path=None):
    p = path or STATE_PATH
    if p.exists():
        return json.loads(p.read_text())
    return {"start_equity": None, "frozen": None, "orders": {}}


def _save(st, path=None):
    (path or STATE_PATH).write_text(json.dumps(st, indent=2))


def check(action: str, ticker: str, value: float, units: float,
          equity: float, state: dict | None = None,
          kill_switch_exists: bool | None = None,
          watcher_ok: bool | None = None) -> tuple[bool, str]:
    """(allowed, reason). Pure given explicit state/kill/watcher args;
    the None defaults read the real files (production path)."""
    st = _load() if state is None else state
    if kill_switch_exists is None:
        kill_switch_exists = KILL_SWITCH.exists()
    if watcher_ok is None:
        import sentinel_gate
        watcher_ok = sentinel_gate.status()[0] == "ok"

    if kill_switch_exists:
        return False, "KILL SWITCH file present — all live orders blocked"
    if st.get("frozen"):
        return False, (f"book FROZEN since {st['frozen'].get('date')} "
                       f"({st['frozen'].get('rule')}) — un-freezing is a "
                       f"human commit")
    start = st.get("start_equity")
    if start and equity <= start * FLOOR_FRAC and action == "BUY":
        return False, (f"FLOOR — equity ${equity:,.2f} <= {FLOOR_FRAC:.0%} of "
                       f"start ${start:,.2f}; only liquidation allowed")
    if action == "BUY" and not watcher_ok:
        return False, "Watcher not fresh — no new entries on a blind risk gate"
    today = str(datetime.now(timezone.utc).date())
    if st.get("orders", {}).get(today, 0) >= MAX_ORDERS_PER_DAY:
        return False, f"throttle — {MAX_ORDERS_PER_DAY} orders already today"
    est_fee = risk_common.ibkr_fee(ticker, value, units)
    if value > 0 and est_fee / value > MAX_FEE_FRAC:
        return False, (f"fee cap — est ${est_fee:.2f} is "
                       f"{est_fee / value:.1%} of ${value:,.2f} order "
                       f"(> {MAX_FEE_FRAC:.0%}); order too small to be sane")
    return True, "ok"


def record_order(action: str, ticker: str, equity: float, path=None):
    """Called AFTER a passed order: bumps the daily count, seeds start
    equity on first ever order, freezes on floor breach after a SELL."""
    st = _load(path)
    if st.get("start_equity") is None:
        st["start_equity"] = round(equity, 2)
    today = str(datetime.now(timezone.utc).date())
    st.setdefault("orders", {})
    st["orders"] = {d: c for d, c in st["orders"].items()
                    if d >= today}  # ponytail: keep only today, history is in the ledger
    st["orders"][today] = st["orders"].get(today, 0) + 1
    start = st["start_equity"]
    if action == "SELL" and start and equity <= start * FLOOR_FRAC \
            and not st.get("frozen"):
        st["frozen"] = {"date": today,
                        "rule": f"live floor {FLOOR_FRAC:.0%} of start "
                                f"(GO_LIVE_PLAN Track A4)"}
    _save(st, path)
    return st
