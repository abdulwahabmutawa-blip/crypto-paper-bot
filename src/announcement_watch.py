"""Binance announcements watcher — delistings and listings, no key needed.

WHY (owner decision 08-23, signal leaderboard + Binance bots review):
exchange operational notices are the one "news" source with documented,
usable lead time — and the delisting notice is a documented instant
drawdown (-16% to -33% within hours; peer-reviewed event study). Two
verified uses:
  * DELISTING INSTANT-EXIT: a held coin whose symbol appears in a
    delisting notice is sold on the next cycle, ahead of every other rule.
  * ENTRY VETO: never open a seat in a coin under a delisting notice, and
    never buy a listing open (2024 Binance listings averaged -22.7% at 3
    months; the tradeable edge is before the public sees it).
The calendar-squeeze class (ONG/ONT/SCRT-type notices days ahead) is
recorded here for the Oracle and for a future owner decision; this module
flags, the books' rules decide.

Source: Binance's public CMS article endpoint (the same JSON the
announcements page renders) — catalog 161 (Delisting), 48 (New Listing).
Self-throttled to 10 minutes; parse titles only (no article bodies),
conservative symbol extraction, fail-soft: a missing file means "no
notices known", never a crash.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "announcements.json"
API = ("https://www.binance.com/bapi/composite/v1/public/cms/article/"
       "list/query?type=1&pageNo=1&pageSize=20&catalogId={cat}")
CATALOGS = {"delist": 161, "listing": 48}
REFRESH_MIN = 10.0
KEEP_DAYS = 45

_DELIST_RX = re.compile(r"Binance Will Delist\s+(.+?)\s+on\s+(\d{4}-\d{2}-\d{2})",
                        re.I)
_LIST_RX = re.compile(r"\(([A-Z0-9]{2,12})\)")


def _get(url: str):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 Chrome/124 Safari/537.36",
        "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fresh_enough() -> bool:
    try:
        d = json.loads(OUT.read_text(encoding="utf-8"))
        age = (datetime.now(timezone.utc) - datetime.fromisoformat(
            d["generated_utc"])).total_seconds() / 60.0
        return age < REFRESH_MIN
    except Exception:
        return False


def parse_delist(title: str) -> tuple[list[str], str | None]:
    """'Binance Will Delist ICX, SCRT, STORJ on 2026-09-03' ->
    (['ICX','SCRT','STORJ'], '2026-09-03'). Pure, tested."""
    m = _DELIST_RX.search(title or "")
    if not m:
        return [], None
    syms = [s.strip().upper() for s in re.split(r",|\band\b", m.group(1))]
    syms = [s for s in syms if re.fullmatch(r"[A-Z0-9]{2,12}", s)]
    return syms, m.group(2)


def parse_listing(title: str) -> list[str]:
    """'Binance Will List Foo (FOO) ...' -> ['FOO']. Tickers in parentheses
    only — conservative on purpose."""
    if not re.search(r"Binance Will List|Binance Lists|Will Add", title or "",
                     re.I):
        return []
    return sorted(set(_LIST_RX.findall(title or "")))


def run() -> None:
    if fresh_enough():
        print("[announcements] fresh enough — skip")
        return
    now = datetime.now(timezone.utc)
    prev = {}
    try:
        prev = json.loads(OUT.read_text(encoding="utf-8"))
    except Exception:
        prev = {}
    delist = dict(prev.get("delist") or {})
    listing = dict(prev.get("listing") or {})
    notices = list(prev.get("notices") or [])[-200:]
    seen_ids = {n.get("id") for n in notices}

    for kind, cat in CATALOGS.items():
        try:
            d = _get(API.format(cat=cat))
            arts = (((d or {}).get("data") or {}).get("catalogs") or [{}])[0] \
                .get("articles") or []
        except Exception as e:
            print(f"[announcements] {kind} fetch failed: {e}")
            continue
        for a in arts:
            aid = a.get("id")
            title = a.get("title") or ""
            rel = a.get("releaseDate")
            rel_iso = datetime.fromtimestamp(rel / 1000, tz=timezone.utc
                                             ).isoformat(timespec="seconds") \
                if rel else None
            if aid not in seen_ids:
                notices.append({"id": aid, "kind": kind, "title": title,
                                "released_utc": rel_iso})
                seen_ids.add(aid)
            if kind == "delist":
                syms, eff = parse_delist(title)
                for s in syms:
                    delist[f"{s}USDT"] = {"title": title, "effective": eff,
                                          "released_utc": rel_iso}
            else:
                for s in parse_listing(title):
                    listing[f"{s}USDT"] = {"title": title,
                                           "released_utc": rel_iso}

    # prune: delistings past their effective date + KEEP_DAYS; listings
    # older than KEEP_DAYS (the listing-open veto only matters for days)
    cutoff = now.timestamp() - KEEP_DAYS * 86400
    for sym in list(delist):
        try:
            if datetime.fromisoformat(delist[sym]["released_utc"]
                                      ).timestamp() < cutoff:
                del delist[sym]
        except Exception:
            pass
    for sym in list(listing):
        try:
            if datetime.fromisoformat(listing[sym]["released_utc"]
                                      ).timestamp() < cutoff:
                del listing[sym]
        except Exception:
            pass

    OUT.write_text(json.dumps(
        {"generated_utc": now.isoformat(timespec="seconds"),
         "delist": delist, "listing": listing, "notices": notices[-200:]},
        indent=1, sort_keys=True, ensure_ascii=False),
        encoding="utf-8", newline="\n")
    print(f"[announcements] delist symbols: {sorted(delist)[:12]}"
          f"{'...' if len(delist) > 12 else ''} | listings: "
          f"{len(listing)} | notices kept: {len(notices[-200:])}")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:   # record-only: must never take a cycle down
        print(f"[announcements] non-fatal: {e}")
        sys.exit(0)
