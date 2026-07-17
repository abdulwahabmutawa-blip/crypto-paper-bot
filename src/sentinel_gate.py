"""Shared read-only gate: is the Grok Sentinel currently calling SEVERE risk?

Every bot (except the All-Weather control, which stays deliberately deaf to
preserve the experiment's baseline) checks this before taking risk. SEVERE is
reserved for crisis-level events; ordinary 'caution' days change nothing.
Reading the file costs nothing — only the Sentinel ever spends API credits.
"""
from __future__ import annotations

import json

import config

VERDICT = config.DATA / "sentinel_verdict.json"


def severe() -> tuple[bool, str]:
    """Returns (is_severe, short_reason)."""
    try:
        v = json.loads(VERDICT.read_text())
    except Exception:
        return False, ""
    if v.get("risk_level") != "severe":
        return False, ""
    alerts = v.get("risk_alerts") or []
    head = alerts[0].get("headline", "unspecified event") if alerts else "unspecified event"
    return True, f"Watcher SEVERE ({v.get('ts','')[:16]}): {head}"
