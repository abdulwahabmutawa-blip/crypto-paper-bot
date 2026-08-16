"""Cross-source social heat — the Watcher's always-on peripheral vision.

Bot-adjacent, CANNOT TRADE: no keys, no broker imports, public GETs only.
Writes data/social_heat.json; the Scout reads it as one more signal type
(gated like every other) and the Watcher folds it into Grok's context.

Why it exists (owner decision 2026-08-16): the sentinel already fetched
CoinGecko trending, Reddit, StockTwits and Binance movers every scan — then
pasted them into a prompt and threw them away. Their value was throttled to
Grok's 2h cadence and the Actions scheduler's ~6% acceptance. This module
makes the same free sources FIRST-CLASS DATA on the VPS's 10-minute clock:

  THE ONE IDEA: a coin trending on ONE surface is noise; a coin lighting up
  on THREE INDEPENDENT surfaces at the same moment is the actual shape of
  "about to explode". Each source alone is gameable and noisy; their
  simultaneous agreement is much harder to fake and much rarer.

Surfaces counted (each contributes at most 1 to a coin's heat):
  coingecko   — trending searches (retail attention, crypto-native)
  reddit      — r/CryptoCurrency + r/SatoshiStreetBets hot titles
  stocktwits  — trending symbols (the .X crypto tickers)
  movers      — Binance 24h top gainers >$20M (price already confirming)
  watcher     — Grok's latest euphoric crypto list, if the scan is fresh
  cryptopanic — hot aggregated news, only with CRYPTOPANIC_TOKEN set
                (free developer key; absent -> surface silently skipped)

Also attached per hot coin (context, not surfaces): USDT-M perp funding
rate and the 1h global long/short account ratio — hard numbers on how
crowded the trade already is. [EVIDENCE-anchored] extreme positive funding
= over-eager longs (fragile); the Scout's knife filter already trades on
the OI half of this logic.

Reddit symbol extraction is deliberately conservative: $CASHTAGS always
count; bare words count only if they are a known Binance base AND not in
the ambiguity stoplist (ONE, GAS, HOT... real coins whose names are also
English words — a headline containing "one" is not a Harmony signal).
[JUDGEMENT] False positives that survive still have to reach 3 surfaces
and then earn the Scout's gate before a cent moves — layered skepticism is
the design, not perfect parsing.
"""
from __future__ import annotations

import json
import os
import re
import urllib.request
from datetime import datetime, timezone

import binance_data
import config

OUT = config.DATA / "social_heat.json"
SENTINEL = config.DATA / "sentinel_state.json"
UA = "paper-bot-heat/1.0"
WATCHER_FRESH_H = 9.0       # a stale euphoric list is not a live surface
MIN_MOVER_VOL = 20_000_000
TOP_MOVERS = 8
LS_CALLS_MAX = 5            # bounded futures calls for the hottest coins

# Binance bases that are also common English words / headline nouns —
# counted only as $CASHTAGS, never as bare words. [JUDGEMENT]
AMBIGUOUS = {"ONE", "GAS", "HOT", "WIN", "SUN", "FUN", "NOT", "MOVE",
             "PEOPLE", "TRUMP", "JUST", "TIME", "ACT", "OM", "RED",
             "BEAT", "HOME", "COW", "U"}


def _atomic_write(path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _get_json(url: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return json.load(urllib.request.urlopen(req, timeout=timeout))


# ---- pure helpers (unit-tested offline) -------------------------------------

def extract_symbols(titles: list[str], universe: set[str]) -> list[str]:
    """Coin bases mentioned in free text, conservatively (see docstring)."""
    found = []
    for title in titles:
        for tag in re.findall(r"\$([A-Za-z]{2,10})\b", title):
            base = tag.upper()
            if base in universe and base not in found:
                found.append(base)
        for word in re.findall(r"\b([A-Z]{2,10})\b", title):
            if word in universe and word not in AMBIGUOUS \
                    and word not in found:
                found.append(word)
    return found


def stocktwits_bases(symbols: list[str], universe: set[str]) -> list[str]:
    """StockTwits crypto tickers look like 'BTC.X'; equities have no .X and
    are not this book's universe."""
    out = []
    for s in symbols:
        if s.endswith(".X"):
            base = s[:-2].upper()
            if base in universe and base not in out:
                out.append(base)
    return out


def aggregate(sources: dict[str, list[str]]) -> list[dict]:
    """Count DISTINCT surfaces per coin. One source listing a coin twice is
    still one surface — the whole point is independence."""
    per = {}
    for src, bases in sources.items():
        for base in dict.fromkeys(bases):
            per.setdefault(base, []).append(src)
    heat = [{"symbol": b, "surfaces": len(srcs), "sources": sorted(srcs)}
            for b, srcs in per.items()]
    heat.sort(key=lambda h: (-h["surfaces"], h["symbol"]))
    return heat


# ---- fetchers (best-effort; a dead source contributes nothing) --------------

def fetch_coingecko(universe: set[str]) -> list[str]:
    try:
        d = _get_json("https://api.coingecko.com/api/v3/search/trending")
        return [c["item"]["symbol"].upper() for c in d.get("coins", [])
                if c.get("item", {}).get("symbol", "").upper() in universe]
    except Exception:
        return []


def fetch_reddit(universe: set[str]) -> list[str]:
    titles = []
    for sub in ("CryptoCurrency", "SatoshiStreetBets"):
        try:
            d = _get_json(f"https://www.reddit.com/r/{sub}/hot.json?limit=15")
            titles += [c["data"].get("title", "")
                       for c in d.get("data", {}).get("children", [])
                       if not c["data"].get("stickied")]
        except Exception:
            continue
    return extract_symbols(titles, universe)


def fetch_stocktwits(universe: set[str]) -> list[str]:
    try:
        d = _get_json("https://api.stocktwits.com/api/2/trending/symbols.json")
        return stocktwits_bases([s.get("symbol", "")
                                 for s in d.get("symbols", [])], universe)
    except Exception:
        return []


def movers_from_tickers(tickers: list[dict]) -> list[str]:
    rows = [t for t in tickers
            if float(t.get("quoteVolume", 0) or 0) > MIN_MOVER_VOL
            and float(t.get("priceChangePercent", 0) or 0) > 0]
    rows.sort(key=lambda t: -float(t["priceChangePercent"]))
    return [t["symbol"][:-4] for t in rows[:TOP_MOVERS]]


def watcher_surface(now: datetime, universe: set[str]) -> list[str]:
    """Grok's euphoric crypto list counts as one surface while fresh — X is
    a surface here like any other, no longer the only one that matters."""
    try:
        scans = json.loads(SENTINEL.read_text()).get("scans") or []
        scan = scans[-1]
        age_h = (now - datetime.fromisoformat(scan["ts"])
                 ).total_seconds() / 3600.0
        if age_h > WATCHER_FRESH_H:
            return []
        return [c.get("symbol", "").upper().replace("-USD", "")
                for c in scan.get("crypto_hype") or []
                if c.get("mood") == "euphoric"
                and c.get("symbol", "").upper() in universe]
    except Exception:
        return []


def fetch_cryptopanic(universe: set[str]) -> list[str]:
    """Hot aggregated crypto news, community-voted. Free developer token in
    CRYPTOPANIC_TOKEN; without it this surface simply does not exist."""
    token = os.environ.get("CRYPTOPANIC_TOKEN", "").strip()
    if not token:
        return []
    for url in (
        f"https://cryptopanic.com/api/developer/v2/posts/?auth_token={token}"
        f"&public=true&filter=hot",
        f"https://cryptopanic.com/api/v1/posts/?auth_token={token}"
        f"&public=true&filter=hot",
    ):
        try:
            d = _get_json(url)
            found = []
            for post in d.get("results", []):
                for cur in (post.get("currencies") or
                            post.get("instruments") or []):
                    code = str(cur.get("code", "")).upper()
                    if code in universe and code not in found:
                        found.append(code)
            return found
        except Exception:
            continue
    return []


# ---- main -------------------------------------------------------------------

def build(now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    tickers = [t for t in binance_data.all_tickers_24h()
               if binance_data.is_tradeable_pair(t.get("symbol", ""))]
    universe = {t["symbol"][:-4] for t in tickers}

    sources = {
        "coingecko": fetch_coingecko(universe),
        "reddit": fetch_reddit(universe),
        "stocktwits": fetch_stocktwits(universe),
        "movers": movers_from_tickers(tickers),
        "watcher": watcher_surface(now, universe),
        "cryptopanic": fetch_cryptopanic(universe),
    }
    heat = aggregate({k: v for k, v in sources.items() if v})

    # positioning context for the hottest names only (bounded API cost):
    # funding is one bulk call; long/short is one call per hot coin
    funding = binance_data.funding_extremes()
    for i, h in enumerate(heat):
        perp = h["symbol"] + "USDT"
        if perp in funding:
            h["funding"] = round(funding[perp], 6)
        if i < LS_CALLS_MAX and h["surfaces"] >= 2:
            ls = binance_data.long_short_ratio(perp)
            if ls is not None:
                h["long_short"] = round(ls, 2)

    out = {
        "ts": now.isoformat(timespec="seconds"),
        "sources": sources,
        "heat": heat[:20],
        "note": "READ-ONLY heat map. Surfaces are independent; agreement "
                "is the signal. The Scout's gate decides if it trades.",
    }
    _atomic_write(OUT, json.dumps(out, indent=2))
    return out


def main():
    out = build()
    hot = [h for h in out["heat"] if h["surfaces"] >= 2]
    live = [k for k, v in out["sources"].items() if v]
    print(f"[heat] {len(live)} live surfaces ({', '.join(live)}) — "
          f"{len(hot)} coins on 2+")
    for h in hot[:6]:
        extra = ""
        if h.get("funding") is not None:
            extra += f"  funding {h['funding']:+.4%}"
        if h.get("long_short") is not None:
            extra += f"  L/S {h['long_short']}"
        print(f"  {h['symbol']:<10} {h['surfaces']} surfaces "
              f"({'+'.join(h['sources'])}){extra}")


if __name__ == "__main__":
    main()
