"""Hype trader on IBKR — the sentiment paper bot's rules with real fills.

Owner request 2026-09-04, starting stake ~$300. Same thesis as
sentinel_trader.py (buy the top "euphoric" name in the latest Grok scan,
hold while it stays euphoric, rotate when it fades, -10% stop, sell on a
SEVERE verdict), re-cut for a $300 cash account at a $1-minimum broker:

  * ONE position, dollar-sized to SETTLED cash, capped by HYPE_IBKR_MAX_USD.
  * MIN HOLD 2 trading days (≈48h): a $2 round trip is 0.67% of $300, and
    a cash account cannot re-buy with unsettled proceeds (good-faith
    violations freeze the account). Hype-fade / stale-scan exits wait for
    the minimum hold; the -10% stop and SEVERE do not.
  * MAX 2 new entries per rolling 7 days.
  * US stocks only (Grok's crypto names are skipped), regular hours only.
  * Fills are sanity-checked against the live quote (±3%); anything wider
    is logged as an anomaly so an impossible fill can never inflate the
    record the way the paper bot's did.
  * Paper by default (IBKR port 4002). Real money needs IBKR_PORT=4001 AND
    HYPE_IBKR_REAL=1. KILL_SWITCH file honoured.

State: data/hype_ibkr_state.json. Ledger: data/hype_ibkr_ledger.jsonl.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone, timedelta

import config
import ibkr_live
import market_hours
import sentinel_gate
from sentinel_trader import scan_age_hours, scan_is_stale, to_ticker, CRYPTO

STATE = config.DATA / "hype_ibkr_state.json"
SENTINEL = config.DATA / "sentinel_state.json"
KEY = "hype-ibkr"
STOP_PCT = -0.10
MIN_HOLD_H = 48.0
MAX_ENTRIES_7D = 2
ENTRY_FRESH_H = 6.0        # a scan older than this is not "current euphoria"
FILL_SANITY = 0.03


def _now():
    return datetime.now(timezone.utc)


def _load():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"created": _now().isoformat(timespec="seconds"), "holding": None,
            "units": 0.0, "entry_price": None, "entry_time": None,
            "entry_scan_ts": None, "entries": [], "realized": [], "stopped": {}}


def _save(st):
    tmp = STATE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(st, indent=1), encoding="utf-8")
    tmp.replace(STATE)


def entries_last_7d(st, now) -> int:
    n = 0
    for ts in st.get("entries", []):
        try:
            if (now - datetime.fromisoformat(ts)).total_seconds() <= 7 * 86400:
                n += 1
        except Exception:
            pass
    return n


def equity_candidates(scan: dict | None) -> list[str]:
    """Euphoric US-stock tickers from the scan, in Grok's order."""
    out = []
    # Fill audit 2026-09-05: the paper twin bought "ONG" (a Binance mover) as
    # a stock. Anything the Watcher lists in crypto_hype is a coin, whatever
    # its ticker looks like — never send it to IBKR as an equity.
    coins = {str(h.get("symbol", "")).upper().lstrip("$")
             for h in (scan or {}).get("crypto_hype", []) or []} | CRYPTO
    for h in (scan or {}).get("hype", []) or []:
        if h.get("mood") != "euphoric":
            continue
        sym = str(h.get("symbol", "")).upper().lstrip("$")
        if not sym or sym in coins or not sym.isalpha() or len(sym) > 5:
            continue
        t = to_ticker(sym)
        if t.endswith("-USD"):
            continue
        out.append(t)
    return out


def fill_ok(fill_px: float | None, quote_px: float | None) -> bool:
    if not fill_px or not quote_px:
        return False
    return abs(fill_px / quote_px - 1.0) <= FILL_SANITY


def main():
    now = _now()
    st = _load()
    if not ibkr_live.armed():
        print(f"[{KEY}] not armed (HYPE_IBKR_ARMED != 1) — skipping")
        return 0
    if ibkr_live.KILL_SWITCH.exists():
        print(f"[{KEY}] KILL SWITCH present — no orders")
        return 0
    sent = json.loads(SENTINEL.read_text(encoding="utf-8")) if SENTINEL.exists() else {"scans": []}
    scan = sent["scans"][-1] if sent.get("scans") else None
    scan_ts = scan["ts"] if scan else ""
    age_h = scan_age_hours(scan)
    stale = scan_is_stale(scan)
    fresh = age_h is not None and age_h <= ENTRY_FRESH_H
    severe = bool(scan and scan.get("risk_level") == "severe")
    cands = equity_candidates(scan)

    # reconcile with the broker: the broker is the truth about what we hold
    pos = ibkr_live.positions()
    held = st.get("holding")
    if held and pos.get(held, 0.0) <= 1e-6:
        ibkr_live.log({"event": "reconciled_external_close", "ticker": held,
                       "units": st.get("units")})
        print(f"[{KEY}] {held} no longer in the account — clearing the seat")
        st.update({"holding": None, "units": 0.0, "entry_price": None,
                   "entry_time": None, "entry_scan_ts": None})
        held = None
    if held:
        st["units"] = min(float(st.get("units") or 0.0), float(pos.get(held, 0.0)))

    open_mkt = market_hours.us_equities_open(now)
    held_h = None
    if held and st.get("entry_time"):
        try:
            held_h = (now - datetime.fromisoformat(st["entry_time"])).total_seconds() / 3600.0
        except Exception:
            held_h = None

    def sell(reason: str) -> bool:
        q = ibkr_live.quote(held)
        fill = ibkr_live.market_sell(held, float(st["units"]))
        if not fill:
            return False
        if not fill_ok(fill["price"], q):
            ibkr_live.log({"event": "fill_anomaly", "action": "SELL", "ticker": held,
                           "fill": fill["price"], "quote": q})
        entry = float(st.get("entry_price") or 0)
        pnl = (fill["price"] / entry - 1.0) if entry else None
        pnl_usd = round((fill["price"] - entry) * fill["qty"] - fill.get("commission", 0.0)
                        - float(st.get("entry_fee", 0.0)), 4) if entry else None
        rec = {"ticker": held, "entry_time": st.get("entry_time"),
               "exit_time": now.isoformat(timespec="seconds"),
               "entry_price": entry, "exit_price": fill["price"], "units": fill["qty"],
               "pnl_pct": round(pnl * 100, 2) if pnl is not None else None,
               "pnl_usd": pnl_usd, "reason": reason, "paper": ibkr_live.is_paper()}
        st["realized"].append(rec)
        ibkr_live.log({"event": "exit", "ticker": held, "reason": reason,
                       "pnl_pct": rec["pnl_pct"], "pnl_usd": pnl_usd})
        st["stopped"][held] = now.isoformat(timespec="seconds")
        st.update({"holding": None, "units": 0.0, "entry_price": None,
                   "entry_time": None, "entry_scan_ts": None, "entry_fee": 0.0})
        return True

    # ---- exits (regular hours only: a market order outside hours will not fill)
    if held and open_mkt:
        q = ibkr_live.quote(held)
        entry = float(st.get("entry_price") or 0)
        if q and entry and q / entry - 1.0 <= STOP_PCT:
            if sell(f"STOP-LOSS ({q / entry - 1:.1%} from entry)"):
                held = None
        if held and severe:
            if sell("Watcher SEVERE — out in a crisis"):
                held = None
        if held and held_h is not None and held_h >= MIN_HOLD_H:
            if stale:
                if sell(f"Grok scans stale ({age_h:.0f}h) — thesis unverifiable"):
                    held = None
            elif scan_ts and st.get("entry_scan_ts") and scan_ts > st["entry_scan_ts"] \
                    and held not in cands:
                if sell("Hype faded — off the euphoric list on a newer scan"):
                    held = None
        elif held and held_h is not None and held_h < MIN_HOLD_H and (stale or held not in cands):
            print(f"[{KEY}] {held}: fade/stale seen but min hold {MIN_HOLD_H:.0f}h not reached "
                  f"({held_h:.1f}h) — holding")

    # ---- entry
    if held is None and open_mkt and fresh and not severe and not stale:
        if entries_last_7d(st, now) >= MAX_ENTRIES_7D:
            print(f"[{KEY}] entry budget spent ({MAX_ENTRIES_7D} per 7 days)")
        else:
            acct = ibkr_live.account()
            settled = float(acct.get("settled_cash", acct.get("cash", 0.0)) or 0.0)
            spend = min(settled, ibkr_live.max_usd())
            if spend < 25:
                print(f"[{KEY}] settled cash ${settled:.2f} too small — waiting for settlement")
            else:
                cool = {t for t, ts in st.get("stopped", {}).items()
                        if (now - datetime.fromisoformat(ts)).total_seconds() < 3 * 86400}
                for t in cands:
                    if t in cool:
                        continue
                    q = ibkr_live.quote(t)
                    if not q:
                        continue
                    fill = ibkr_live.market_buy(t, spend)
                    if not fill:
                        continue
                    if not fill_ok(fill["price"], q):
                        ibkr_live.log({"event": "fill_anomaly", "action": "BUY", "ticker": t,
                                       "fill": fill["price"], "quote": q})
                    st.update({"holding": t, "units": fill["qty"], "entry_price": fill["price"],
                               "entry_time": now.isoformat(timespec="seconds"),
                               "entry_scan_ts": scan_ts,
                               "entry_fee": float(fill.get("commission", 0.0))})
                    st.setdefault("entries", []).append(now.isoformat(timespec="seconds"))
                    st["entries"] = st["entries"][-20:]
                    held = t
                    print(f"[{KEY}] BOUGHT {t} {fill['qty']} @ {fill['price']:.4f} (${spend:.2f})")
                    break

    acct = ibkr_live.account() if ibkr_live.armed() else {}
    st["last_value_usd"] = acct.get("net_liq")
    st["last_updated_utc"] = now.isoformat(timespec="seconds")
    st["paper"] = ibkr_live.is_paper()
    _save(st)
    print(f"[{KEY}] {'PAPER' if ibkr_live.is_paper() else 'LIVE'} seat={held or 'CASH'} "
          f"net ${st['last_value_usd'] or 0:.2f} scan {age_h if age_h is None else round(age_h,1)}h "
          f"market {'open' if open_mkt else 'closed'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
