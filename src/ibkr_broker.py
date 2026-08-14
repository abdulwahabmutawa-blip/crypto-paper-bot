"""IBKR pilot broker — DRY-RUN ONLY until an account exists and the human
turns the key. Mirrors alpaca_broker's shape: strategies never import this;
the engine calls pilot_order() beside its sim fill and the sim's books stay
the source of truth.

Activation ladder (each step is a deliberate human act):
  1. default            -> completely inert, returns None instantly
  2. LIVE=1             -> DRY-RUN: order passes live_guard, intent is logged
                           to data/live_orders_dryrun.jsonl, nothing is sent
  3. LIVE=1 + IBKR_LIVE=1 -> refuses to start (raises) until a real IBKR
                           adapter is written, reviewed, and the Track C gate
                           has passed. The refusal is the safety feature: no
                           half-finished path to a real order can exist.

Kuwait note (research 08-13): equities only, cash account, fractional shares.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

import config

DRYRUN_LOG = config.DATA / "live_orders_dryrun.jsonl"


def enabled() -> bool:
    return os.environ.get("LIVE", "").strip() == "1"


def pilot_order(action: str, ticker: str, notional: float, units: float,
                equity: float) -> None:
    """Guard-check + log one intended order. Returns None always (dry-run);
    the future real adapter will return a fill dict like alpaca_broker."""
    if not enabled():
        return None
    if os.environ.get("IBKR_LIVE", "").strip() == "1":
        raise RuntimeError(
            "IBKR_LIVE=1 but no real adapter exists yet — refusing to "
            "pretend. The real order path ships only after the Track C "
            "validation gate (GO_LIVE_PLAN_2026-08-14.md).")
    if ticker.endswith("-USD"):
        return None  # no crypto lane, ever (Kuwait prohibition)
    try:
        # same contract as alpaca_broker: a broker-path failure can never
        # take a bot down — the sim's books are the source of truth
        import live_guard
        ok, why = live_guard.check(action, ticker, notional, units, equity)
        entry = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "action": action, "ticker": ticker,
                 "notional": round(notional, 2), "units": round(units, 4),
                 "equity": round(equity, 2),
                 "guard": "PASS" if ok else "BLOCKED", "reason": why}
        if ok:
            live_guard.record_order(action, ticker, equity)
        with DRYRUN_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[ibkr-dryrun] {entry['guard']} {action} {ticker} "
              f"${notional:,.2f} — {why}")
    except Exception as e:
        print(f"[ibkr-dryrun] pilot path failed ({e}) — sim unaffected")
    return None
