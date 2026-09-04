"""IBKR adapter for the hype trader — REAL BROKER, paper or live by port.

Talks to a running IB Gateway (see IBKR_SETUP.md) through the `ib_async`
library. The Gateway holds the login; this module holds no credentials.

Arming ladder (every rung is a deliberate act in /etc/hype_ibkr.env):
  * nothing set                -> inert: every function returns None/{}.
  * HYPE_IBKR_ARMED=1          -> orders may be placed against the Gateway
                                  on IBKR_PORT (default 4002 = PAPER money).
  * IBKR_PORT=4001 (live)      -> ALSO needs HYPE_IBKR_REAL=1 or the module
                                  refuses to connect. Two flags for real
                                  money, never one.
  * HYPE_IBKR_MAX_USD          -> hard cap per order (default 300).

Orders are dollar-sized MARKET buys (fractional shares) and share-sized
MARKET sells, US stocks only, regular hours only (enforced by the caller).
Every fill, refusal and error is appended to data/hype_ibkr_ledger.jsonl.
"""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone

import config

LEDGER = config.DATA / "hype_ibkr_ledger.jsonl"
KILL_SWITCH = config.DATA / "KILL_SWITCH"
DEFAULT_PORT_PAPER = 4002
PORT_LIVE = 4001
FILL_WAIT_S = 45
_IB = None


def log(entry: dict) -> None:
    entry = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), **entry}
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def armed() -> bool:
    return os.environ.get("HYPE_IBKR_ARMED", "").strip() == "1"


def port() -> int:
    try:
        return int(os.environ.get("IBKR_PORT", DEFAULT_PORT_PAPER))
    except Exception:
        return DEFAULT_PORT_PAPER


def is_paper() -> bool:
    return port() != PORT_LIVE


def real_allowed() -> bool:
    return os.environ.get("HYPE_IBKR_REAL", "").strip() == "1"


def max_usd() -> float:
    try:
        return float(os.environ.get("HYPE_IBKR_MAX_USD", "300"))
    except Exception:
        return 300.0


def connect():
    """Connect to the Gateway (cached). None when disarmed or unreachable.
    Refuses the LIVE port without HYPE_IBKR_REAL=1."""
    global _IB
    if not armed():
        return None
    if not is_paper() and not real_allowed():
        log({"event": "refused", "reason": "IBKR_PORT is the LIVE port but "
                                            "HYPE_IBKR_REAL is not 1"})
        return None
    if _IB is not None and _IB.isConnected():
        return _IB
    try:
        from ib_async import IB
    except Exception as e:
        log({"event": "error", "where": "import ib_async", "msg": str(e)[:200]})
        return None
    ib = IB()
    try:
        ib.connect(os.environ.get("IBKR_HOST", "127.0.0.1"), port(),
                   clientId=int(os.environ.get("IBKR_CLIENT_ID", "7")),
                   timeout=20, readonly=False)
    except Exception as e:
        log({"event": "error", "where": "connect", "port": port(), "msg": str(e)[:200]})
        return None
    _IB = ib
    return ib


def disconnect() -> None:
    global _IB
    try:
        if _IB is not None:
            _IB.disconnect()
    except Exception:
        pass
    _IB = None


def _stock(ib, ticker: str):
    from ib_async import Stock
    c = Stock(ticker, "SMART", "USD")
    try:
        ib.qualifyContracts(c)
    except Exception as e:
        log({"event": "error", "where": "qualify", "ticker": ticker, "msg": str(e)[:200]})
        return None
    return c


def account() -> dict:
    """{'settled_cash', 'net_liq', 'buying_power'} in USD, or {}."""
    ib = connect()
    if ib is None:
        return {}
    out = {}
    try:
        for v in ib.accountValues():
            if v.currency not in ("USD", "BASE"):
                continue
            if v.tag == "SettledCash":
                out["settled_cash"] = float(v.value)
            elif v.tag == "NetLiquidation":
                out["net_liq"] = float(v.value)
            elif v.tag == "BuyingPower":
                out["buying_power"] = float(v.value)
            elif v.tag == "TotalCashValue" and "settled_cash" not in out:
                out["cash"] = float(v.value)
    except Exception as e:
        log({"event": "error", "where": "account", "msg": str(e)[:200]})
    return out


def positions() -> dict[str, float]:
    """{ticker: shares} for US stocks held."""
    ib = connect()
    if ib is None:
        return {}
    out = {}
    try:
        for p in ib.positions():
            if getattr(p.contract, "secType", "") == "STK" and p.position:
                out[p.contract.symbol] = float(p.position)
    except Exception as e:
        log({"event": "error", "where": "positions", "msg": str(e)[:200]})
    return out


def quote(ticker: str) -> float | None:
    """Last/mid price from a snapshot; None if unavailable."""
    ib = connect()
    if ib is None:
        return None
    c = _stock(ib, ticker)
    if c is None:
        return None
    try:
        t = ib.reqMktData(c, "", True, False)
        for _ in range(20):
            ib.sleep(0.25)
            px = t.marketPrice()
            if px and px == px and px > 0:
                return float(px)
        last = getattr(t, "last", None) or getattr(t, "close", None)
        return float(last) if last and last == last else None
    except Exception as e:
        log({"event": "error", "where": "quote", "ticker": ticker, "msg": str(e)[:200]})
        return None


def _wait_fill(ib, trade) -> dict | None:
    deadline = time.time() + FILL_WAIT_S
    while time.time() < deadline:
        ib.sleep(0.5)
        st = trade.orderStatus.status
        if st == "Filled":
            qty = float(trade.orderStatus.filled or 0)
            avg = float(trade.orderStatus.avgFillPrice or 0)
            comm = 0.0
            try:
                comm = sum(float(f.commissionReport.commission or 0)
                           for f in trade.fills if f.commissionReport)
            except Exception:
                pass
            return {"qty": qty, "price": avg, "commission": comm,
                    "order_id": str(trade.order.orderId)}
        if st in ("Cancelled", "Inactive", "ApiCancelled"):
            return None
    try:
        ib.cancelOrder(trade.order)
    except Exception:
        pass
    return None


def market_buy(ticker: str, usd: float) -> dict | None:
    """Dollar-sized MARKET buy (fractional). Returns fill dict or None."""
    if KILL_SWITCH.exists():
        log({"event": "refused", "action": "BUY", "ticker": ticker, "reason": "KILL SWITCH"})
        return None
    usd = float(min(usd, max_usd()))
    if usd < 5:
        return None
    ib = connect()
    if ib is None:
        return None
    c = _stock(ib, ticker)
    if c is None:
        return None
    try:
        from ib_async import MarketOrder
        o = MarketOrder("BUY", 0)
        o.cashQty = round(usd, 2)
        o.tif = "DAY"
        tr = ib.placeOrder(c, o)
        fill = _wait_fill(ib, tr)
    except Exception as e:
        log({"event": "error", "where": "buy", "ticker": ticker, "msg": str(e)[:200]})
        return None
    if not fill:
        log({"event": "order_unfilled", "action": "BUY", "ticker": ticker, "usd": usd})
        return None
    log({"event": "fill", "action": "BUY", "ticker": ticker, "paper": is_paper(), **fill})
    return fill


def market_sell(ticker: str, qty: float) -> dict | None:
    if KILL_SWITCH.exists():
        log({"event": "refused", "action": "SELL", "ticker": ticker, "reason": "KILL SWITCH"})
        return None
    ib = connect()
    if ib is None or qty <= 0:
        return None
    c = _stock(ib, ticker)
    if c is None:
        return None
    try:
        from ib_async import MarketOrder
        o = MarketOrder("SELL", round(qty, 4))
        o.tif = "DAY"
        tr = ib.placeOrder(c, o)
        fill = _wait_fill(ib, tr)
    except Exception as e:
        log({"event": "error", "where": "sell", "ticker": ticker, "msg": str(e)[:200]})
        return None
    if not fill:
        log({"event": "order_unfilled", "action": "SELL", "ticker": ticker, "qty": qty})
        return None
    log({"event": "fill", "action": "SELL", "ticker": ticker, "paper": is_paper(), **fill})
    return fill
