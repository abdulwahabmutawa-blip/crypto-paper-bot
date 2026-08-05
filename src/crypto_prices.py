"""Crypto prices from a real exchange (Kraken public API), yfinance fallback.

Why (audit 2026-08-05): all 10 bots hang off yfinance — an unofficial Yahoo
scraper whose stale/undelivered bars caused all three ledger restatements.
Crypto is the easy escape: exchanges publish real bars for free, no key.
Kraken chosen over Binance because GitHub Actions runners are US-hosted and
api.binance.com geo-blocks US IPs.

Public rate limit ~1 req/s: daily() makes one OHLC call per coin with a
polite sleep (8 coins ≈ 9s per cycle — the cycle runs every ~13 min).
Any failure returns None; callers fall back to yfinance so a Kraken outage
degrades to the status quo, never to a dead bot.
"""
from __future__ import annotations

import json
import time
import urllib.request

import pandas as pd

BASE = "https://api.kraken.com/0/public"
# Kraken quirks: BTC is XBT, DOGE is XDG
PAIRS = {"BTC-USD": "XBTUSD", "ETH-USD": "ETHUSD", "SOL-USD": "SOLUSD",
         "DOGE-USD": "XDGUSD", "AVAX-USD": "AVAXUSD", "LINK-USD": "LINKUSD",
         "ADA-USD": "ADAUSD", "XRP-USD": "XRPUSD"}


def _get(url: str) -> dict | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "paper-bot/1.0"})
        d = json.load(urllib.request.urlopen(req, timeout=30))
        if d.get("error"):
            print(f"[kraken] API error: {d['error']}")
            return None
        return d.get("result") or None
    except Exception as e:
        print(f"[kraken] request failed: {e}")
        return None


def daily(coins: list[str]) -> pd.DataFrame | None:
    """Daily close frame (UTC dates, columns = '-USD' tickers), ~720 days.
    None on any failure — caller must fall back."""
    cols = {}
    for c in coins:
        pair = PAIRS.get(c)
        if not pair:
            return None
        res = _get(f"{BASE}/OHLC?pair={pair}&interval=1440")
        if not res:
            return None
        rows = next((v for k, v in res.items() if k != "last"), None)
        if not rows:
            return None
        # OHLC row: [time, open, high, low, close, vwap, volume, count]
        s = pd.Series({pd.Timestamp(r[0], unit="s"): float(r[4]) for r in rows})
        cols[c] = s
        time.sleep(1.1)  # public rate limit
    df = pd.DataFrame(cols).sort_index()
    df.index = pd.DatetimeIndex(df.index.date)
    return df if not df.empty else None


def live(coins: list[str]) -> tuple[dict, dict] | None:
    """One Ticker call -> ({coin: last price}, {coin: full spread in bps}).
    The spread is a real, measured execution cost — half of it is charged on
    every fill (risk_common.fee). None on failure."""
    pairs = [PAIRS[c] for c in coins if c in PAIRS]
    if len(pairs) != len(coins):
        return None
    res = _get(f"{BASE}/Ticker?pair={','.join(pairs)}")
    if not res:
        return None
    # response keys are Kraken's internal names and their order is NOT
    # guaranteed — match by normalized pair name instead
    def norm(k: str) -> str:
        return k.replace("XXBT", "XBT").replace("XXDG", "XDG").replace(
            "ZUSD", "USD").replace("XETH", "ETH").replace("XXRP", "XRP")
    by_pair = {norm(k): v for k, v in res.items()}
    prices, spreads = {}, {}
    for c in coins:
        v = by_pair.get(PAIRS[c])
        if not v:
            return None
        last = float(v["c"][0])   # c = [last trade price, lot volume]
        prices[c] = last
        try:
            bid, ask = float(v["b"][0]), float(v["a"][0])
            mid = (bid + ask) / 2.0
            spreads[c] = max(0.0, (ask - bid) / mid * 10_000.0) if mid > 0 else None
        except Exception:
            spreads[c] = None
        if spreads[c] is None:
            spreads.pop(c)
    return prices, spreads
