"""Shared read-only gate: is the Grok Sentinel currently calling SEVERE risk?

Every bot (except the All-Weather control, which stays deliberately deaf to
preserve the experiment's baseline) checks this before taking risk. SEVERE is
reserved for crisis-level events; ordinary 'caution' days change nothing.
Reading the file costs nothing — only the Sentinel ever spends API credits.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import config

VERDICT = config.DATA / "sentinel_verdict.json"
MAX_AGE_H = 24.0  # older than this = the Watcher is effectively offline


def _age_hours(v: dict) -> float | None:
    try:
        ts = datetime.fromisoformat(str(v.get("ts", "")).replace("Z", "+00:00"))
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - ts).total_seconds() / 3600.0
    except Exception:
        return None


def status() -> tuple[str, str]:
    """('ok'|'stale'|'missing', detail). A dead Grok API used to fail
    silent-open forever — 42/42 scans said 'caution' and nothing would have
    noticed if they stopped arriving at all (audit 2026-08-05)."""
    try:
        v = json.loads(VERDICT.read_text())
    except Exception:
        return "missing", "no verdict file — Watcher has never reported"
    age = _age_hours(v)
    if age is None:
        return "stale", "verdict has no readable timestamp"
    if age > MAX_AGE_H:
        return "stale", (f"newest Watcher verdict is {age:.1f}h old "
                         f"(> {MAX_AGE_H:.0f}h) — treat risk as UNKNOWN")
    return "ok", f"verdict {age:.1f}h old"


def severe() -> tuple[bool, str]:
    """Returns (is_severe, short_reason). A stale verdict is never SEVERE —
    but callers should surface status() so silence is visible, not mistaken
    for calm."""
    try:
        v = json.loads(VERDICT.read_text())
    except Exception:
        return False, ""
    age = _age_hours(v)
    if age is not None and age > MAX_AGE_H:
        print(f"[gate] WARNING: {status()[1]}")
        return False, ""
    if v.get("risk_level") != "severe":
        return False, ""
    alerts = v.get("risk_alerts") or []
    head = alerts[0].get("headline", "unspecified event") if alerts else "unspecified event"
    return True, f"Watcher SEVERE ({v.get('ts','')[:16]}): {head}"
