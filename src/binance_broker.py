"""Binance SPOT TESTNET shadow broker — the crypto lane's execution rig.

TESTNET ONLY BY CONSTRUCTION: the base URL is hardcoded to
testnet.binance.vision, the same safety pattern as alpaca_broker's hardcoded
paper endpoint — a mainnet key pasted into the secrets still cannot reach
real markets through this module. Promoting the crypto lane to real money is
a separate, deliberate, reviewed adapter that does not exist yet and is
gated by Track C (GO_LIVE_PLAN_2026-08-14.md).

What testnet shadow fills honestly measure: order-lifecycle plumbing —
symbol mapping, LOT_SIZE/NOTIONAL filter compliance, market-order mechanics,
API error handling. What they do NOT measure: real liquidity (testnet books
are thin and fake), so fill_gap numbers here validate the machine, not the
slippage model.

Keys come from env (GitHub secrets): BINANCE_TESTNET_API_KEY,
BINANCE_TESTNET_API_SECRET — minted at testnet.binance.vision (free, fake
funds). No keys -> every call is a silent no-op; a broker outage can never
take a bot down. The sim's books remain the source of truth.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://testnet.binance.vision/api"

_FILTER_CACHE: dict[str, dict] = {}


def to_symbol(ticker: str) -> str:
    """Fleet 'BTC-USD' style -> Binance 'BTCUSDT'."""
    return ticker.upper().replace("-USD", "") + "USDT"


def base_asset(ticker: str) -> str:
    return ticker.upper().replace("-USD", "")


def _keys() -> tuple[str, str] | None:
    k = os.environ.get("BINANCE_TESTNET_API_KEY", "").strip()
    s = os.environ.get("BINANCE_TESTNET_API_SECRET", "").strip()
    return (k, s) if k and s else None


def enabled() -> bool:
    return _keys() is not None


def sign(secret: str, params: dict) -> str:
    """HMAC-SHA256 of the urlencoded query string — Binance's auth scheme."""
    qs = urllib.parse.urlencode(params)
    return hmac.new(secret.encode(), qs.encode(), hashlib.sha256).hexdigest()


def _call(method: str, path: str, params: dict | None = None,
          signed: bool = False) -> dict | list | None:
    keys = _keys()
    if signed and not keys:
        return None
    params = dict(params or {})
    headers = {}
    if keys:
        headers["X-MBX-APIKEY"] = keys[0]
    if signed:
        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 10_000
        params["signature"] = sign(keys[1], params)
    qs = urllib.parse.urlencode(params)
    url = f"{BASE}{path}" + (f"?{qs}" if qs and method == "GET" else "")
    data = qs.encode() if method != "GET" and qs else None
    req = urllib.request.Request(url, method=method, data=data, headers=headers)
    try:
        return json.load(urllib.request.urlopen(req, timeout=20))
    except urllib.error.HTTPError as e:
        print(f"[binance-testnet] {method} {path} -> HTTP {e.code}: "
              f"{e.read().decode(errors='replace')[:200]}")
        return None
    except Exception as e:
        print(f"[binance-testnet] {method} {path} failed: {e}")
        return None


def _filters(symbol: str) -> dict:
    """{'step': float, 'min_qty': float, 'min_notional': float} per symbol,
    cached per process. Missing/failed lookup returns permissive defaults —
    the order then simply succeeds or fails at the venue, loudly."""
    if symbol in _FILTER_CACHE:
        return _FILTER_CACHE[symbol]
    out = {"step": 0.0, "min_qty": 0.0, "min_notional": 0.0}
    info = _call("GET", "/v3/exchangeInfo", {"symbol": symbol})
    for f in ((info or {}).get("symbols") or [{}])[0].get("filters", []):
        if f.get("filterType") == "LOT_SIZE":
            out["step"] = float(f.get("stepSize", 0) or 0)
            out["min_qty"] = float(f.get("minQty", 0) or 0)
        if f.get("filterType") in ("NOTIONAL", "MIN_NOTIONAL"):
            out["min_notional"] = float(f.get("minNotional", 0) or 0)
    _FILTER_CACHE[symbol] = out
    return out


def lot_floor(qty: float, step: float) -> float:
    """Floor qty to the LOT_SIZE step grid (Binance rejects off-grid qty)."""
    if step <= 0:
        return qty
    return int(qty / step) * step


def _avg_fill(resp: dict) -> dict | None:
    fills = resp.get("fills") or []
    tq = sum(float(f["qty"]) for f in fills)
    if tq <= 0:
        return None
    avg = sum(float(f["price"]) * float(f["qty"]) for f in fills) / tq
    return {"price": avg, "qty": tq, "order_id": str(resp.get("orderId", ""))}


def shadow_fill(action: str, ticker: str, notional: float) -> dict | None:
    """Mirror one sim trade to the TESTNET matching engine. Returns
    {"price", "qty", "order_id"} or None. BUY spends notional USDT via
    quoteOrderQty; SELL liquidates the free base balance (floored to the
    lot grid). Never raises — sim unaffected by any failure here."""
    if not enabled() or not ticker.endswith("-USD"):
        return None
    try:
        symbol = to_symbol(ticker)
        if action.upper() == "BUY":
            resp = _call("POST", "/v3/order",
                         {"symbol": symbol, "side": "BUY", "type": "MARKET",
                          "quoteOrderQty": round(min(notional, 100_000), 2)},
                         signed=True)
        else:
            acct = _call("GET", "/v3/account", signed=True)
            free = 0.0
            for b in (acct or {}).get("balances", []):
                if b.get("asset") == base_asset(ticker):
                    free = float(b.get("free", 0) or 0)
            flt = _filters(symbol)
            qty = lot_floor(free, flt["step"])
            if qty <= 0 or qty < flt["min_qty"]:
                print(f"[binance-testnet] no sellable {base_asset(ticker)} "
                      f"balance (free={free}) — shadow sell skipped")
                return None
            resp = _call("POST", "/v3/order",
                         {"symbol": symbol, "side": "SELL", "type": "MARKET",
                          "quantity": f"{qty:.8f}".rstrip("0").rstrip(".")},
                         signed=True)
        if not resp:
            return None
        fill = _avg_fill(resp)
        if fill:
            print(f"[binance-testnet] {action} {symbol} filled "
                  f"{fill['qty']} @ {fill['price']:.6f}")
        return fill
    except Exception as e:
        print(f"[binance-testnet] shadow {action} {ticker} failed ({e}) — "
              f"sim unaffected")
        return None
