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

HOST = "https://api.binance.com"
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
    url = f"{HOST}{path}" + (f"?{qs}" if qs else "")
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                used = r.headers.get("X-MBX-USED-WEIGHT-1M")
                if used and used.isdigit():
                    USED_WEIGHT["value"] = max(USED_WEIGHT["value"], int(used))
                return json.load(r)
        except urllib.error.HTTPError as e:
            # 429 = rate limited, 418 = banned for ignoring 429. Back off hard
            # and never retry a 418 — that only lengthens the ban.
            if e.code == 418:
                print("[binance-data] HTTP 418 — IP banned for rate abuse; "
                      "stopping this cycle")
                return None
            if e.code == 429 and attempt < retries:
                wait = int(e.headers.get("Retry-After", "5") or 5)
                print(f"[binance-data] 429 rate limited — backing off {wait}s")
                time.sleep(wait)
                continue
            print(f"[binance-data] {path} HTTP {e.code}")
            return None
        except Exception as e:
            if attempt < retries:
                time.sleep(1 + attempt)
                continue
            print(f"[binance-data] {path} failed: {e}")
            return None
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
    """Spot prices for several symbols in ONE call (weight 4 for a list)."""
    syms = [s for s in dict.fromkeys(symbols)]
    if not syms:
        return {}
    d = _get("/api/v3/ticker/price",
             {"symbols": json.dumps(syms, separators=(",", ":"))}, weight=4)
    if not isinstance(d, list):
        return {}
    out = {}
    for row in d:
        try:
            out[row["symbol"]] = float(row["price"])
        except Exception:
            pass
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


def candle_series(rows: list[list]) -> dict[str, list[float]]:
    """Unpack klines into named float series (empty lists if malformed)."""
    out = {"close": [], "high": [], "low": [], "volume": [], "quote": [],
           "trades": [], "taker_buy": []}
    for r in rows:
        try:
            out["high"].append(float(r[2]))
            out["low"].append(float(r[3]))
            out["close"].append(float(r[4]))
            out["volume"].append(float(r[5]))
            out["quote"].append(float(r[7]))
            out["trades"].append(float(r[8]))
            # index 10 = taker buy quote volume: the aggressive-buy share of
            # the bar, which is how much of the move was market buyers
            # lifting offers rather than passive fills
            out["taker_buy"].append(float(r[10]))
        except Exception:
            continue
    return out
