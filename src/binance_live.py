"""Binance MAINNET adapter — LOTTERY BOOK ONLY. Real money, tiny by law.

This is the deliberate, reviewed mainnet module that binance_broker.py's
testnet lock pointed to — built 2026-08-15 for exactly ONE purpose: the
owner's explicitly-sacrificial ~$11 lottery book. It is NOT the Track C
pilot and is engineered so it cannot quietly become it:

  * BOOK CAP $20, hard-coded: if the account's managed value (free USDT +
    tracked position) exceeds the cap, the module HALTS every order and
    writes a red-flag ledger entry. Raising the cap is a reviewed human
    commit — "the slot machine paid once, add the rent money" is the exact
    failure this line exists to stop.
  * ARMING is a double deliberate act by the OWNER, never default-on:
    repo secrets BINANCE_LIVE_API_KEY / BINANCE_LIVE_API_SECRET, AND repo
    variable LOTTERY_LIVE="1". Missing either -> inert no-op.
  * Key hygiene (owner-side, documented in BINANCE_LOTTERY_SETUP.md):
    spot-trade-only API key, WITHDRAWALS DISABLED. A leaked trade-only key
    can lose the $11 on bad trades; it cannot drain the account.
  * KILL SWITCH: the same data/KILL_SWITCH file live_guard honors blocks
    every mainnet order here too.
  * Every order and every refusal is appended to data/lottery_ledger.jsonl
    (committed by the loop) — the book's full honest history.

Expected outcome, stated where it can't be unseen: the documented base rate
for small-account pump-chasing is loss of principal. This module makes the
attempt honest, capped, and auditable — it does not make it a good idea.
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
from datetime import datetime, timezone

import config

HOST = "https://api.binance.com"
BASE = HOST + "/api"          # spot trading endpoints (/v3/...)
# key-permission endpoints live under /sapi and are passed as full paths
BOOK_CAP_USD = 20.0
MIN_ORDER_USDT = 5.0          # Binance spot minimum notional (typical pairs)
LEDGER = config.DATA / "lottery_ledger.jsonl"
KILL_SWITCH = config.DATA / "KILL_SWITCH"

# Last API error, so callers can diagnose precisely instead of guessing.
# Binance's error codes are specific and each points at a different fix;
# a generic "check your key or IP" message sent the first real setup
# chasing the wrong problem.
LAST_ERROR: dict = {}


def _keys() -> tuple[str, str] | None:
    k = os.environ.get("BINANCE_LIVE_API_KEY", "").strip()
    s = os.environ.get("BINANCE_LIVE_API_SECRET", "").strip()
    return (k, s) if k and s else None


def armed() -> bool:
    """Live only when the owner set BOTH the keys and LOTTERY_LIVE=1."""
    return os.environ.get("LOTTERY_LIVE", "").strip() == "1" and _keys() is not None


def log(entry: dict) -> None:
    entry = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             **entry}
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def _call(method: str, path: str, params: dict | None = None,
          signed: bool = False) -> dict | list | None:
    keys = _keys()
    if signed and not keys:
        return None
    params = dict(params or {})
    headers = {"X-MBX-APIKEY": keys[0]} if keys else {}
    if signed:
        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 10_000
        qs = urllib.parse.urlencode(params)
        params["signature"] = hmac.new(keys[1].encode(), qs.encode(),
                                       hashlib.sha256).hexdigest()
    qs = urllib.parse.urlencode(params)
    root = HOST if path.startswith("/sapi") else BASE
    url = f"{root}{path}" + (f"?{qs}" if qs and method == "GET" else "")
    data = qs.encode() if method != "GET" and qs else None
    req = urllib.request.Request(url, method=method, data=data, headers=headers)
    try:
        return json.load(urllib.request.urlopen(req, timeout=20))
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:200]
        try:
            parsed = json.loads(body)
            LAST_ERROR.clear()
            LAST_ERROR.update({"http": e.code, "code": parsed.get("code"),
                               "msg": parsed.get("msg", "")})
        except Exception:
            LAST_ERROR.clear()
            LAST_ERROR.update({"http": e.code, "code": None, "msg": body})
        print(f"[lottery-live] {method} {path} -> HTTP {e.code}: {body}")
        log({"event": "api_error", "path": path, "code": e.code, "body": body})
        return None
    except Exception as e:
        print(f"[lottery-live] {method} {path} failed: {e}")
        return None


def balances() -> dict[str, float]:
    """{'USDT': 11.0, 'PEPE': 12345.0, ...} free balances > 0."""
    acct = _call("GET", "/v3/account", signed=True)
    out = {}
    for b in (acct or {}).get("balances", []):
        free = float(b.get("free", 0) or 0)
        if free > 0:
            out[b["asset"]] = free
    return out


def price(symbol: str) -> float | None:
    d = _call("GET", "/v3/ticker/price", {"symbol": symbol})
    try:
        return float(d["price"])
    except Exception:
        return None


def managed_value(bals: dict[str, float], held_symbol: str | None,
                  units: float | None = None) -> float:
    """Free USDT + the value of the units THIS BOT holds. `units` matters on
    an account that also holds the owner's own coins: valuing the whole free
    balance of the same asset would count their holdings as the bot's book."""
    v = bals.get("USDT", 0.0)
    if held_symbol:
        base = held_symbol[:-4]
        qty = bals.get(base, 0.0) if units is None else min(units, bals.get(base, 0.0))
        if qty > 0:
            p = price(held_symbol)
            if p:
                v += qty * p
    return v


def guard(action: str, symbol: str, bals: dict, held_symbol: str | None,
          units: float | None = None) -> str | None:
    """Returns a refusal reason, or None = clear to proceed."""
    if KILL_SWITCH.exists():
        return "KILL SWITCH file present"
    val = managed_value(bals, held_symbol, units)
    # The cap blocks BUYs only (audit 08-15): a SELL of an over-cap book
    # REDUCES exposure, and blocking it would kill every protective exit at
    # the exact moment a position pumps past $20 — stop, trail and stall
    # would all go dead at peak profit. "The lottery can never become the
    # pilot" needs new money blocked, not old money trapped.
    if action == "BUY" and val > BOOK_CAP_USD:
        return (f"BOOK CAP — managed value ${val:.2f} > ${BOOK_CAP_USD:.0f}. "
                f"This is the lottery book, not the pilot; raising the cap "
                f"is a reviewed commit (GO_LIVE_PLAN Track C guards real "
                f"capital)")
    if action == "BUY" and bals.get("USDT", 0.0) < MIN_ORDER_USDT:
        return (f"DUST — free USDT ${bals.get('USDT', 0.0):.2f} below the "
                f"${MIN_ORDER_USDT:.0f} exchange minimum; book effectively "
                f"burned, nothing to do")
    return None


def market(action: str, symbol: str, quote_qty: float | None = None,
           qty: float | None = None) -> dict | None:
    """One real market order. Caller passes quoteOrderQty for BUY (spend
    USDT) or quantity for SELL. Returns avg-fill dict or None."""
    # Defense in depth (audit 08-15): arming enforced HERE, not only by the
    # caller. With keys present but LOTTERY_LIVE!=1 this function must be
    # inert no matter who imports it or what future code calls it.
    if not armed():
        log({"event": "refused", "action": action.upper(), "symbol": symbol,
             "reason": "not armed (LOTTERY_LIVE != 1) — market() is inert"})
        print(f"[lottery-live] market() called while not armed — refused")
        return None
    params = {"symbol": symbol, "side": action.upper(), "type": "MARKET"}
    if action.upper() == "BUY":
        params["quoteOrderQty"] = round(min(quote_qty or 0.0, BOOK_CAP_USD), 2)
    else:
        params["quantity"] = f"{qty:.8f}".rstrip("0").rstrip(".")
    resp = _call("POST", "/v3/order", params, signed=True)
    if resp is None:
        # The order may have EXECUTED with the response lost in transit
        # (timeout after the exchange accepted it). Leave a loud marker so
        # the next cycle's ledger reconciliation looks for an untracked
        # position instead of trusting the void.
        log({"event": "order_unconfirmed", "action": action.upper(),
             "symbol": symbol,
             "note": "POST returned nothing — order MAY have filled; "
                     "reconcile against balances next cycle"})
        return None
    fills = resp.get("fills") or []
    tq = sum(float(f["qty"]) for f in fills)
    if tq <= 0:
        log({"event": "order_no_fill", "action": action, "symbol": symbol,
             "resp": bool(resp)})
        return None
    avg = sum(float(f["price"]) * float(f["qty"]) for f in fills) / tq
    commission = sum(float(f.get("commission", 0) or 0) for f in fills)
    out = {"price": avg, "qty": tq, "order_id": str(resp.get("orderId", "")),
           "commission": commission,
           "commission_asset": (fills[0].get("commissionAsset", "")
                                if fills else "")}
    log({"event": "fill", "action": action.upper(), "symbol": symbol, **out})
    print(f"[lottery-live] REAL {action.upper()} {symbol} "
          f"{tq} @ {avg:.10g}")
    return out
