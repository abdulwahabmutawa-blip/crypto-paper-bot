"""Grok Sentinel — the fleet's risk officer + sentiment recorder (bot #7).

Every SCAN_INTERVAL_H hours (self-throttled; the workflow runs far more often
but this script only spends money when due), asks Grok — with live X + web
search — two questions:
  1. RISK: did anything happen that should worry the fleet? (exchange
     collapse, war outbreak, emergency Fed action, market halts...)
  2. HYPE: which tickers/coins have unusual chatter, and what's the mood?

It OBSERVES AND RECORDS ONLY — it places no trades and (for now) does not
override the other bots. The risk verdict is written to
data/sentinel_verdict.json so future bot versions can consume it (v2 agenda).

Budget guards: 8h throttle (~3 scans/day) + hard cap of MONTHLY_CAP scans per
calendar month + your prepaid xAI credits as the final wall.
Requires XAI_API_KEY in the environment (GitHub secret); skips gracefully
without it. PAPER PROJECT. Not investment advice.
"""
from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone

import config

BASE = "https://api.x.ai/v1"
MODEL = "grok-4.5"
SCAN_INTERVAL_H = 8
MONTHLY_CAP = 100
STATE = config.DATA / "sentinel_state.json"
VERDICT = config.DATA / "sentinel_verdict.json"

PROMPT = """Search live X posts and the web from the last 24 hours about
financial markets (stocks + crypto). Then answer ONLY with a JSON object,
no prose before or after, in exactly this shape:

{
 "risk_level": "none" | "caution" | "severe",
 "risk_alerts": [{"headline": "...", "markets": ["crypto"|"stocks"|"both"], "severity": "caution"|"severe"}],
 "hype": [{"symbol": "TICKER", "mood": "euphoric"|"fearful"|"mixed", "note": "under 12 words"}],
 "overall_mood": "one sentence on overall market mood"
}

Rules: "severe" is reserved for events like a major exchange collapse, war
outbreak involving major powers, emergency central-bank action, or trading
halts — not ordinary volatility. List at most 5 hype entries, most unusual
chatter first. Empty risk_alerts list is a perfectly good answer."""


def call_grok() -> str:
    key = os.environ.get("XAI_API_KEY", "").strip()
    req = urllib.request.Request(
        BASE + "/responses",
        data=json.dumps({
            "model": MODEL,
            "input": [{"role": "user", "content": PROMPT}],
            "tools": [{"type": "x_search"}, {"type": "web_search"}],
        }).encode(),
        headers={"Authorization": f"Bearer {key}",
                 "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.load(r)
    if isinstance(data.get("output_text"), str) and data["output_text"]:
        return data["output_text"]
    parts = []
    for item in data.get("output", []):
        for c in item.get("content", []) or []:
            if isinstance(c, dict) and c.get("text"):
                parts.append(c["text"])
    return "\n".join(parts)


def parse_scan(raw: str) -> dict:
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        return {"risk_level": "unparsed", "risk_alerts": [], "hype": [],
                "overall_mood": raw[:300]}
    try:
        d = json.loads(m.group(0))
        d.setdefault("risk_level", "unparsed")
        d.setdefault("risk_alerts", [])
        d.setdefault("hype", [])
        d.setdefault("overall_mood", "")
        return d
    except Exception:
        return {"risk_level": "unparsed", "risk_alerts": [], "hype": [],
                "overall_mood": raw[:300]}


def render(st: dict) -> None:
    latest = st["scans"][-1] if st["scans"] else None
    payload = {
        "latest": latest, "scans": st["scans"][-30:],
        "scan_count_month": st["month_count"].get(
            datetime.now(timezone.utc).strftime("%Y-%m"), 0),
        "monthly_cap": MONTHLY_CAP, "interval_h": SCAN_INTERVAL_H,
    }
    template = (config.ROOT / "src" / "sentinel_template.html").read_text(
        encoding="utf-8")
    (config.REPORTS / "sentinel_dashboard.html").write_text(
        template.replace("/*__DATA__*/", json.dumps(payload)),
        encoding="utf-8")
    print("[sentinel] dashboard rendered")


def main():
    now = datetime.now(timezone.utc)
    st = json.loads(STATE.read_text()) if STATE.exists() else \
        {"scans": [], "month_count": {}, "last_scan_utc": None}

    if not os.environ.get("XAI_API_KEY", "").strip():
        print("[sentinel] XAI_API_KEY not set — skipping scan (add the repo "
              "secret to activate). Rendering last known state.")
        render(st)
        return

    mkey = now.strftime("%Y-%m")
    due = True
    if st["last_scan_utc"]:
        last = datetime.fromisoformat(st["last_scan_utc"])
        hours = (now - last).total_seconds() / 3600
        due = hours >= SCAN_INTERVAL_H
    if st["month_count"].get(mkey, 0) >= MONTHLY_CAP:
        print(f"[sentinel] monthly cap ({MONTHLY_CAP}) reached — skipping.")
        render(st)
        return
    if not due:
        print("[sentinel] not due yet (throttle) — no credits spent.")
        render(st)
        return

    try:
        raw = call_grok()
    except urllib.error.HTTPError as e:
        print(f"[sentinel] xAI HTTP {e.code}: "
              f"{e.read().decode(errors='replace')[:300]}")
        render(st)
        return
    scan = parse_scan(raw)
    scan["ts"] = now.isoformat(timespec="seconds")
    st["scans"] = (st["scans"] + [scan])[-90:]
    st["last_scan_utc"] = scan["ts"]
    st["month_count"][mkey] = st["month_count"].get(mkey, 0) + 1
    STATE.write_text(json.dumps(st, indent=2))
    VERDICT.write_text(json.dumps({
        "ts": scan["ts"], "risk_level": scan["risk_level"],
        "risk_alerts": scan["risk_alerts"],
        "note": "advisory only — no bot consumes this yet (v2 agenda)",
    }, indent=2))
    render(st)
    print(f"[sentinel] scan done — risk {scan['risk_level']}, "
          f"{len(scan['hype'])} hype entries, "
          f"{st['month_count'][mkey]}/{MONTHLY_CAP} scans this month")


if __name__ == "__main__":
    main()
