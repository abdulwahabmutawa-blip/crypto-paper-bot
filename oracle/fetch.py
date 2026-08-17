"""Public Binance reads. No keys, no signing, no order endpoints.

Deliberately self-contained rather than importing src/binance_data.py: the
"this package cannot trade" guarantee is much easier to audit when the whole
network surface of the Oracle is one 60-line file that only ever issues
unauthenticated GETs to two market-data paths.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

import oracle.config as config

# The only endpoints this package may ever touch.
ALLOWED_PATHS = ("/api/v3/exchangeInfo", "/api/v3/ticker/24hr",
                 "/api/v3/klines")


def _get(path: str, params: dict | None = None, retries: int = 3):
    if path not in ALLOWED_PATHS:
        raise ValueError(f"oracle.fetch refuses non-market-data path: {path}")
    qs = urllib.parse.urlencode(params or {})
    url = f"{config.BINANCE_HOST}{path}" + (f"?{qs}" if qs else "")
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": config.USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))
    return None


def exchange_info() -> dict:
    return _get("/api/v3/exchangeInfo") or {}


def tickers_24h() -> list[dict]:
    d = _get("/api/v3/ticker/24hr")
    return d if isinstance(d, list) else []


def klines(symbol: str, interval: str = "1d", limit: int = 500,
           start_ms: int | None = None, end_ms: int | None = None
           ) -> list[list]:
    """Raw klines. Rows are [open_time, o, h, l, c, vol, close_time,
    quote_vol, trades, taker_base, taker_quote, ignore]."""
    p = {"symbol": symbol, "interval": interval, "limit": limit}
    if start_ms is not None:
        p["startTime"] = int(start_ms)
    if end_ms is not None:
        p["endTime"] = int(end_ms)
    d = _get("/api/v3/klines", p)
    return d if isinstance(d, list) else []
