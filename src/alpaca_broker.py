"""Alpaca PAPER account shadow broker — execution realism, measured not modeled.

The sim decides a trade as usual; when Alpaca paper keys are present, the
same order is ALSO sent to Alpaca's paper matching engine and the real fill
price is recorded beside the sim's assumed fill. The difference IS the
execution-realism gap — measured per trade instead of argued about.

Shadow only: the sim's books remain the source of truth. Equities only
(Alpaca paper crypto needs different symbology; crypto already has real
exchange data via Kraken).

Keys come from env (GitHub secrets in CI): ALPACA_API_KEY_ID,
ALPACA_API_SECRET_KEY. No keys -> every call is a silent no-op; a broker
outage can never take a bot down. PAPER ONLY: base URL is hardcoded to the
paper endpoint so a live-account key pasted by mistake still cannot trade
real money through this module.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

BASE = "https://paper-api.alpaca.markets/v2"


def _keys() -> tuple[str, str] | None:
    k = os.environ.get("ALPACA_API_KEY_ID", "").strip()
    s = os.environ.get("ALPACA_API_SECRET_KEY", "").strip()
    return (k, s) if k and s else None


def _call(method: str, path: str, body: dict | None = None) -> dict | None:
    keys = _keys()
    if not keys:
        return None
    req = urllib.request.Request(
        BASE + path, method=method,
        data=json.dumps(body).encode() if body else None,
        headers={"APCA-API-KEY-ID": keys[0], "APCA-API-SECRET-KEY": keys[1],
                 "Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=30))
    except urllib.error.HTTPError as e:
        print(f"[alpaca] {method} {path} -> HTTP {e.code}: "
              f"{e.read().decode(errors='replace')[:200]}")
        return None
    except Exception as e:
        print(f"[alpaca] {method} {path} failed: {e}")
        return None


def enabled() -> bool:
    return _keys() is not None


def shadow_fill(action: str, ticker: str, notional: float) -> dict | None:
    """Submit a market order to the PAPER account and wait briefly for the
    fill. Returns {"price": float, "qty": float, "order_id": str} or None.
    action: "BUY" | "SELL". SELL sells the position qty if one exists
    (notional sells are rejected for shorts), BUY uses notional dollars."""
    if ticker.endswith("-USD") or not enabled():
        return None
    side = action.lower()
    order = {"symbol": ticker, "side": side, "type": "market",
             "time_in_force": "day"}
    if side == "buy":
        order["notional"] = str(round(min(notional, 200_000), 2))
    else:
        pos = _call("GET", f"/positions/{ticker}")
        if not pos or float(pos.get("qty", 0)) <= 0:
            print(f"[alpaca] no paper position in {ticker} to sell — skipped")
            return None
        order["qty"] = pos["qty"]
    placed = _call("POST", "/orders", order)
    if not placed:
        return None
    oid = placed.get("id", "")
    for _ in range(6):                      # up to ~6s for a market fill
        time.sleep(1)
        o = _call("GET", f"/orders/{oid}")
        if o and o.get("status") == "filled":
            return {"price": float(o["filled_avg_price"]),
                    "qty": float(o["filled_qty"]), "order_id": oid}
        if o and o.get("status") in ("rejected", "canceled", "expired"):
            print(f"[alpaca] order {o.get('status')}: {o.get('symbol')}")
            return None
    print(f"[alpaca] order {oid} not filled within wait window "
          f"(market closed?) — shadow fill skipped")
    return None
