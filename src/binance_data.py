"""Binance PUBLIC market data — no key, no auth, no account access.

One module so every book that thinks in Binance terms reads the same prices
the real order would fill against. The paper twin used Yahoo quotes, which
drift from Binance and cover a different universe; a paper book that cannot
be compared to the live book is not evidence of anything.

Read-only by construction: only GET endpoints under /api/v3 that require no
signature. This module can never place an order — that lives in
binance_live.py (mainnet, guarded) and binance_broker.py (testnet).

Rate limits: spot public endpoints share a 6000 request-weight/minute budget
(1200 on the older documented tier — we assume the lower number and stay far
under it). Every response's X-MBX-USED-WEIGHT-1M header is recorded in
USED_WEIGHT so callers can back off before Binance does it for them.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

# SPOT HOSTS, IN ORDER (fix 2026-08-17). api.binance.com answers HTTP 451 to
# US IPs and GitHub's hosted runners are US-hosted, so every spot call from
# Actions returned None — which is exactly how hype-crypto froze silently
# from 2026-08-15 (it could not price its BTC-USD benchmark, so every cycle
# skipped). data-api.binance.vision is Binance's public market-data mirror:
# same paths, same payloads, no keys, no geo-block. It leads; the main host
# is the fallback for when the mirror itself is down.
HOSTS = ("https://data-api.binance.vision", "https://api.binance.com")
HOST = HOSTS[-1]                        # kept for anything referencing it
# Futures has no public mirror. Only the scout and heat map call it, and
# both run on the VPS (not geo-blocked), so this stays as-is.
FHOST = "https://fapi.binance.com"      # USDT-M futures, also keyless
UA = "paper-bot-fleet/1.0"

# Weight budget we hold ourselves to per minute — deliberately a fraction of
# Binance's own, so a scan can never be the reason the fleet gets banned.
# Binance's own spot cap is 6000 request-weight/minute. A full scan costs
# ~100 (exchangeInfo + all-symbol ticker) + 2 per kline call, so even 90
# symbols lands near 280 — under 5% of the cap. This self-budget sits at a
# quarter of Binance's, which leaves room to widen the scan considerably
# before rate limits become the binding constraint (they are not today; the
# 10-minute cadence is).
SELF_BUDGET_1M = 1500
USED_WEIGHT = {"value": 0, "minute": 0}

# Leveraged tokens and stable/wrapped pairs are excluded from every scan:
# leveraged tokens decay by construction and stables do not pump.
LEVERAGED_SUFFIXES = ("UPUSDT", "DOWNUSDT", "BULLUSDT", "BEARUSDT")
STABLE_BASES = {"USDC", "FDUSD", "TUSD", "DAI", "USDP", "BUSD", "EUR", "GBP",
                "AEUR", "USD1", "XUSD", "PYUSD", "EURI"}


def _throttle(weight: int) -> None:
    """Self-imposed budget: pause rather than push into Binance's limiter."""
    now_min = int(time.time() // 60)
    if USED_WEIGHT["minute"] != now_min:
        USED_WEIGHT["minute"], USED_WEIGHT["value"] = now_min, 0
    if USED_WEIGHT["value"] + weight > SELF_BUDGET_1M:
        time.sleep(max(0, 60 - (time.time() % 60)) + 0.5)
        USED_WEIGHT["minute"], USED_WEIGHT["value"] = int(time.time() // 60), 0
    USED_WEIGHT["value"] += weight


def _get(path: str, params: dict | None = None, weight: int = 1,
         retries: int = 2):
    """GET a public endpoint. Returns parsed JSON or None — never raises, so
    a market-data outage can never take a book down."""
    _throttle(weight)
    qs = urllib.parse.urlencode(params or {})
    for host in HOSTS:
        url = f"{host}{path}" + (f"?{qs}" if qs else "")
        for attempt in range(retries + 1):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=20) as r:
                    used = r.headers.get("X-MBX-USED-WEIGHT-1M")
                    if used and used.isdigit():
                        USED_WEIGHT["value"] = max(USED_WEIGHT["value"],
                                                   int(used))
                    return json.load(r)
            except urllib.error.HTTPError as e:
                # 451 = geo-blocked. Not a transient fault: it will never
                # succeed from this IP, so try the next host immediately
                # rather than spending the retry budget on a legal block.
                if e.code == 451:
                    print(f"[binance-data] {host} geo-blocked (451) "
                          f"— trying next host")
                    break
                # 429 = rate limited, 418 = banned for ignoring 429. Back off
                # hard and never retry a 418 — that only lengthens the ban.
                if e.code == 418:
                    print("[binance-data] HTTP 418 — IP banned for rate "
                          "abuse; stopping this cycle")
                    return None
                if e.code == 429 and attempt < retries:
                    ra = e.headers.get("Retry-After", "5") or "5"
                    wait = int(ra) if str(ra).isdigit() else 5
                    print(f"[binance-data] 429 rate limited — backing off "
                          f"{wait}s")
                    time.sleep(min(wait, 60))
                    continue
                print(f"[binance-data] {path} HTTP {e.code}")
                return None
            except Exception as e:
                if attempt < retries:
                    time.sleep(1 + attempt)
                    continue
                print(f"[binance-data] {path} failed on {host}: {e}")
                break        # fall through to the next host
    return None


def to_symbol(ticker: str) -> str:
    """Fleet 'BTC-USD' / 'btc' -> Binance 'BTCUSDT'."""
    s = str(ticker).upper().lstrip("$").replace("-USD", "").replace("/", "")
    return s if s.endswith("USDT") else s + "USDT"


def is_tradeable_pair(symbol: str) -> bool:
    """Excludes leveraged tokens and stable-for-stable pairs."""
    if not symbol.endswith("USDT"):
        return False
    if symbol.endswith(LEVERAGED_SUFFIXES):
        return False
    return symbol[:-4] not in STABLE_BASES


def price(symbol: str) -> float | None:
    d = _get("/api/v3/ticker/price", {"symbol": symbol}, weight=2)
    try:
        return float(d["price"])
    except Exception:
        return None


def prices(symbols) -> dict[str, float]:
    """Spot prices for several symbols in one call — with a per-symbol
    fallback, because Binance 400s the ENTIRE batch (-1121) if even one
    symbol is unknown, and the symbols this fleet asks about are exactly
    the delisting-prone tail (audit 08-15: one delisted coin froze every
    price lookup, stalling the scout's whole learning loop and the paper
    twin's stop-losses)."""
    syms = [s for s in dict.fromkeys(symbols)]
    if not syms:
        return {}
    d = _get("/api/v3/ticker/price",
             {"symbols": json.dumps(syms, separators=(",", ":"))}, weight=4)
    out = {}
    if isinstance(d, list):
        for row in d:
            try:
                out[row["symbol"]] = float(row["price"])
            except Exception:
                pass
        return out
    # batch refused — resolve individually (bounded), skipping the bad ones
    for s in syms[:30]:
        p = price(s)
        if p:
            out[s] = p
    return out


def all_tickers_24h() -> list[dict]:
    """Every symbol's rolling 24h stats in one call (weight 80).

    Fields used downstream: lastPrice, openPrice, highPrice, lowPrice,
    priceChangePercent, quoteVolume (notional traded), count (number of
    trades), weightedAvgPrice.
    """
    d = _get("/api/v3/ticker/24hr", weight=80)
    return d if isinstance(d, list) else []


def klines(symbol: str, interval: str = "5m", limit: int = 60) -> list[list]:
    """Recent candles, oldest first. Weight 2 for limit <= 100.
    Each row: [openTime, open, high, low, close, volume, closeTime,
    quoteAssetVolume, numberOfTrades, ...]."""
    d = _get("/api/v3/klines",
             {"symbol": symbol, "interval": interval, "limit": limit},
             weight=2)
    return d if isinstance(d, list) else []


def _fget(path: str, params: dict | None = None, weight: int = 1):
    """GET a keyless USDT-M FUTURES public endpoint. Same never-raises
    contract as _get. Futures has its own weight bucket, so this does not
    compete with the spot scan's budget."""
    _throttle(weight)
    qs = urllib.parse.urlencode(params or {})
    url = f"{FHOST}{path}" + (f"?{qs}" if qs else "")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.load(r)
    except Exception as e:
        print(f"[binance-data] futures {path} failed: {e}")
        return None


def funding_extremes() -> dict[str, float]:
    """symbol -> last funding rate, for every USDT-M perp (one weight-1
    call). Extreme funding = crowded positioning: very positive means longs
    are paying heavily (over-eager crowd, fragile to a long squeeze), very
    negative means shorts are paying (capitulation, a reversion tailwind).
    Keys are spot-style ('BTCUSDT') so callers can join on symbol."""
    d = _fget("/fapi/v1/premiumIndex", weight=1)
    out = {}
    if isinstance(d, list):
        for row in d:
            try:
                out[row["symbol"]] = float(row["lastFundingRate"])
            except Exception:
                pass
    return out


def open_interest_drop(symbol: str) -> float | None:
    """Fraction OI has fallen from its recent peak over the last ~2h of 5m
    samples. A liquidation CASCADE clears open interest as it self-
    extinguishes (published: OI drops 25-70%, cascade decays within ~1h),
    whereas an information-driven collapse keeps OI roughly intact. So a
    LARGE positive drop here means "the forced selling is spent, a bounce is
    mechanically plausible"; a near-zero drop on a big price fall means "the
    reason is fundamental — do not catch it". None if unavailable (no perp,
    or the call failed) so the caller can treat it as unknown, not as safe.
    """
    d = _fget("/futures/data/openInterestHist",
              {"symbol": symbol, "period": "5m", "limit": 24}, weight=1)
    if not isinstance(d, list) or len(d) < 6:
        return None
    try:
        oi = [float(x["sumOpenInterest"]) for x in d]
    except Exception:
        return None
    peak = max(oi) or 1e-12
    return (peak - oi[-1]) / peak


def long_short_ratio(symbol: str) -> float | None:
    """Latest 1h global long/short ACCOUNT ratio for a USDT-M perp (free,
    keyless). >1 = more accounts long than short. Very high readings mean
    the crowd is already all-in long — late-entry fuel is spent and the
    squeeze risk points down. None if no perp exists or the call failed:
    unknown, not neutral."""
    d = _fget("/futures/data/globalLongShortAccountRatio",
              {"symbol": symbol, "period": "1h", "limit": 1}, weight=1)
    if not isinstance(d, list) or not d:
        return None
    try:
        return float(d[-1]["longShortRatio"])
    except Exception:
        return None


def candle_series(rows: list[list]) -> dict[str, list[float]]:
    """Unpack klines into named float series (empty lists if malformed)."""
    out = {"close": [], "high": [], "low": [], "volume": [], "quote": [],
           "trades": [], "taker_buy": []}
    for r in rows:
        # parse-then-commit (audit 08-15): a row that fails halfway must not
        # leave partial appends behind, or the parallel series desync and
        # every [-2] "closed bar" index reads a DIFFERENT bar per series
        try:
            vals = (float(r[2]), float(r[3]), float(r[4]), float(r[5]),
                    float(r[7]), float(r[8]),
                    # index 10 = taker buy quote volume: how much of the bar
                    # was market buyers lifting offers vs passive fills
                    float(r[10]))
        except Exception:
            continue
        out["high"].append(vals[0])
        out["low"].append(vals[1])
        out["close"].append(vals[2])
        out["volume"].append(vals[3])
        out["quote"].append(vals[4])
        out["trades"].append(vals[5])
        out["taker_buy"].append(vals[6])
    return out
