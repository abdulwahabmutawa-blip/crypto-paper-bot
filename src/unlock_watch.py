"""Unlock-proximity watcher — record-only calendar intelligence.

WHY (owner decision 08-23, signal-leaderboard research): token-unlock
cliffs are the only well-documented signal with WEEKS of lead time —
~90% of 16k+ tracked unlocks were negative within 30 days, and the
threshold that mattered was cliff size vs daily volume (~1.5-2.4x ADV).
For a long-only book, avoidance is free expectancy.

RECORD-ONLY, like every unproven signal in this repo: this module writes
data/unlocks.json and the Oracle snapshots it as covariates so the
09-16+ scoring can judge whether unlock proximity actually predicts
(non-)explosions in OUR universe. No book trades on it until it earns
that, per SCORING_PLAN.md's promotion gate.

Source: DefiLlama's free public dataset mirror (emissionsIndex, ~22MB).
The paid api.llama.fi/emissions endpoints are NOT used. Self-throttled:
refetches at most every 6h; between refreshes the committed file rides.
Symbol mapping is name/token-symbol uppercased + validated against
Binance's live USDT pairs — unmatched protocols are simply skipped
(missing coverage is fine for a record-only lens; wrong joins are not).
"""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from datetime import datetime, timezone

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "unlocks.json"

INDEX_URL = "https://defillama-datasets.llama.fi/emissionsIndex"
BINANCE = ("https://data-api.binance.vision", "https://api.binance.com")
REFRESH_H = 6.0
HORIZON_D = 60          # record cliffs up to 60d out (front-running starts ~30d)
MIN_PCT_SUPPLY = 0.001  # ignore dust events (<0.1% of max supply)


def _get(url: str, timeout: int = 60):
    req = urllib.request.Request(url, headers={"User-Agent": "unlock-watch/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def _binance(path: str):
    for host in BINANCE:
        try:
            return _get(f"{host}/api/v3{path}", timeout=30)
        except Exception:
            continue
    return None


def fresh_enough() -> bool:
    try:
        d = json.loads(OUT.read_text(encoding="utf-8"))
        age = (datetime.now(timezone.utc) - datetime.fromisoformat(
            d["generated_utc"])).total_seconds() / 3600.0
        return age < REFRESH_H
    except Exception:
        return False


def upcoming_events(proto: dict, now_s: float) -> list[dict]:
    """Future events within the horizon, sized as a share of max supply."""
    out = []
    max_supply = float(proto.get("maxSupply") or 0) or \
        float(proto.get("circSupply") or 0)
    for ev in proto.get("events") or []:
        ts = ev.get("timestamp")
        if not ts or ts <= now_s or ts > now_s + HORIZON_D * 86400:
            continue
        toks = ev.get("noOfTokens") or []
        try:
            amount = max(float(t) for t in toks) if toks else 0.0
        except Exception:
            amount = 0.0
        if amount <= 0 or max_supply <= 0:
            continue
        pct = amount / max_supply
        if pct < MIN_PCT_SUPPLY:
            continue
        out.append({"ts": int(ts), "tokens": amount,
                    "pct_supply": round(pct, 5),
                    "unlock_type": ev.get("unlockType"),
                    "category": ev.get("category")})
    return out


def run() -> None:
    if fresh_enough():
        print("[unlocks] fresh enough — skip")
        return
    now = datetime.now(timezone.utc)
    now_s = now.timestamp()
    idx = _get(INDEX_URL, timeout=120)
    protos = (idx or {}).get("data") or []
    print(f"[unlocks] index: {len(protos)} protocols")

    # one call for the whole exchange: symbols + price + 24h quote volume
    tickers = _binance("/ticker/24hr") or []
    by_base = {}
    for t in tickers:
        s = t.get("symbol", "")
        if s.endswith("USDT"):
            by_base[s[:-4]] = t

    events: dict[str, dict] = {}
    for p in protos:
        sym = str(p.get("name") or "").upper().strip()
        t = by_base.get(sym)
        if not t:
            continue
        evs = upcoming_events(p, now_s)
        if not evs:
            continue
        # nearest CLIFF outranks nearest linear tick; fall back to nearest
        cliffs = [e for e in evs if e.get("unlock_type") == "cliff"]
        nxt = min(cliffs or evs, key=lambda e: e["ts"])
        try:
            price = float(t.get("lastPrice") or 0)
            qv24 = float(t.get("quoteVolume") or 0)
        except Exception:
            price = qv24 = 0.0
        unlock_usd = nxt["tokens"] * price
        events[f"{sym}USDT"] = {
            "next_unlock_utc": datetime.fromtimestamp(
                nxt["ts"], tz=timezone.utc).isoformat(timespec="seconds"),
            "days_to_unlock": round((nxt["ts"] - now_s) / 86400, 1),
            "unlock_type": nxt.get("unlock_type"),
            "pct_supply": nxt["pct_supply"],
            "unlock_usd": round(unlock_usd, 0),
            # the literature's decision variable: cliff size vs daily volume
            "adv_ratio": round(unlock_usd / qv24, 2) if qv24 > 0 else None,
            "n_events_60d": len(evs),
        }

    OUT.write_text(json.dumps(
        {"generated_utc": now.isoformat(timespec="seconds"),
         "horizon_days": HORIZON_D, "source": "defillama emissionsIndex",
         "n_symbols": len(events), "events": events},
        indent=1, sort_keys=True), encoding="utf-8", newline="\n")
    big = sorted(events.items(),
                 key=lambda kv: -(kv[1].get("adv_ratio") or 0))[:5]
    print(f"[unlocks] {len(events)} Binance symbols with upcoming events; "
          f"largest vs ADV: "
          + ", ".join(f"{s} {v['adv_ratio']}x in {v['days_to_unlock']}d"
                      for s, v in big if v.get("adv_ratio")))


if __name__ == "__main__":
    try:
        run()
    except Exception as e:   # record-only: must never take the fleet down
        print(f"[unlocks] non-fatal: {e}")
        sys.exit(0)
