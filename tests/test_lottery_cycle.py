"""End-to-end CYCLE tests for the real-money book — lottery_live.main() run
against a fully mocked exchange, in a temp data dir, with no network.

Why this file exists (incident 2026-09-01): two production outages of the
real book were the same class of bug — code that compiled but could not
RUN through a real cycle:
  * 08-23..08-26: an indent slip made the entry path unreachable.
  * 08-31..09-01: the golden-ticket commit read `halt_why` in the turbo-hop
    rule before the variable was assigned. Every cycle holding a seat under
    TURBO_MODE died with UnboundLocalError after the exit rules and before
    the state write; the dashboard froze on the BERAUSDT buy and the
    resting-stop sync never ran.
Unit tests of the helpers passed both times. Only a test that drives
main() through its real control flow catches this class, so that is what
these do. Every scenario asserts the cycle COMPLETES and the state file is
rewritten — the two facts the owner's phone dashboard depends on.

The second half covers the exchange-resting stop against the same harness
(review 2026-09-02): a resting stop LOCKS the units, so the sell path must
cancel it before sizing, must never sell the owner's own coins of the same
asset, and must recover a stop-limit stranded above the market.

Offline: no keys used for anything but arming, no network, no data/ writes
outside a temp dir.
"""
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import config  # noqa: E402


@pytest.fixture
def cycle(tmp_path, monkeypatch):
    """A harness: temp data dir, armed env, mocked exchange, recorded orders.

    The fake exchange models free vs LOCKED base units: a resting stop locks
    them (free 0), a cancel frees them, a market sell needs them free.
    """
    monkeypatch.setenv("BINANCE_LIVE_API_KEY", "k")
    monkeypatch.setenv("BINANCE_LIVE_API_SECRET", "s")
    monkeypatch.setenv("LOTTERY_LIVE", "1")
    monkeypatch.delenv("LOTTERY_EXCHANGE_STOPS", raising=False)
    data = tmp_path / "data"
    data.mkdir()
    monkeypatch.setattr(config, "DATA", data)

    import binance_live as bl
    import lottery_live as ll
    monkeypatch.setattr(bl, "LEDGER", data / "lottery_ledger.jsonl")
    monkeypatch.setattr(bl, "KILL_SWITCH", data / "KILL_SWITCH")
    monkeypatch.setattr(ll, "STATE", data / "lottery_state.json")
    monkeypatch.setattr(ll, "SENTINEL", data / "sentinel_state.json")

    h = {"price": 1.0, "usdt": 46.0, "base": {}, "locked": {}, "orders": [],
         "calls": [], "ticker": None, "open_orders": {},  # id -> order dict
         "order_types": ["LIMIT", "MARKET", "STOP_LOSS", "STOP_LOSS_LIMIT"]}

    def _price(sym):
        return h["price"]

    def _balances():
        d = {"USDT": h["usdt"]}
        for k, v in h["base"].items():
            if v > 0:
                d[k] = v
        return d

    def _balances_valuation(held=None):
        d = _balances()
        if held:
            b = held[:-4]
            d[b] = h["base"].get(b, 0.0) + h["locked"].get(b, 0.0)
        return d

    def _market(action, symbol, quote_qty=None, qty=None):
        h["orders"].append((action, symbol, quote_qty, qty))
        b = symbol[:-4]
        if action == "BUY":
            units = round(quote_qty / h["price"], 6)
            h["base"][b] = h["base"].get(b, 0.0) + units
            h["usdt"] = 0.0
            fill = {"price": h["price"], "qty": units, "order_id": "1",
                    "commission": 0.0, "commission_asset": "BNB"}
        else:
            assert qty <= h["base"].get(b, 0.0) + 1e-9, \
                f"sold {qty} but only {h['base'].get(b, 0.0)} free"
            h["base"][b] = h["base"].get(b, 0.0) - qty
            h["usdt"] = round(qty * h["price"], 4)
            fill = {"price": h["price"], "qty": qty, "order_id": "2",
                    "commission": 0.0, "commission_asset": "BNB"}
        bl.log({"event": "fill", "action": action, "symbol": symbol,
                "price": fill["price"], "qty": fill["qty"]})
        return fill

    def _call(method, path, params=None, **kw):
        h["calls"].append((method, path, dict(params or {})))
        params = params or {}
        if path == "/v3/exchangeInfo":
            return {"symbols": [{"orderTypes": h["order_types"], "filters": [
                {"filterType": "LOT_SIZE", "stepSize": "0.001"},
                {"filterType": "PRICE_FILTER", "tickSize": "0.0001"}]}]}
        if path == "/v3/ticker/24hr":
            return h["ticker"]
        if path == "/v3/openOrders":
            return [o for o in h["open_orders"].values()
                    if o["status"] in ("NEW", "PARTIALLY_FILLED")]
        if path == "/v3/order" and method == "GET":
            return h["open_orders"].get(str(params.get("orderId")))
        if path == "/v3/order" and method == "DELETE":
            o = h["open_orders"].get(str(params.get("orderId")))
            if not o or o["status"] != "NEW":
                return None            # nothing to cancel (already filled)
            o["status"] = "CANCELED"
            b = params["symbol"][:-4]
            h["base"][b] = h["base"].get(b, 0.0) + h["locked"].pop(b, 0.0)
            return o
        if path == "/v3/order" and method == "POST":
            # a protective stop: lock the units, remember the order
            oid = str(100 + len(h["open_orders"]))
            b = params["symbol"][:-4]
            q = float(params["quantity"])
            h["locked"][b] = h["locked"].get(b, 0.0) + q
            h["base"][b] = h["base"].get(b, 0.0) - q
            h["open_orders"][oid] = {"orderId": oid, "symbol": params["symbol"],
                                     "side": "SELL", "type": params["type"],
                                     "status": "NEW", "isWorking": False,
                                     "price": params.get("price", "0"),
                                     "stopPrice": params["stopPrice"],
                                     "origQty": params["quantity"]}
            return {"orderId": oid}
        return None

    monkeypatch.setattr(bl, "price", _price)
    monkeypatch.setattr(bl, "balances", _balances)
    monkeypatch.setattr(bl, "balances_valuation", _balances_valuation)
    monkeypatch.setattr(bl, "market", _market)
    monkeypatch.setattr(bl, "_call", _call)
    monkeypatch.setattr(bl, "late_entry_check", lambda *a, **k: None)
    monkeypatch.setattr(bl, "depth_5pct", lambda s: (1_000_000.0, 1_000_000.0))
    monkeypatch.setattr(bl, "guard", lambda *a, **k: None)

    now = datetime.now(timezone.utc)
    (data / "sentinel_state.json").write_text(json.dumps({"scans": [
        {"ts": now.isoformat(timespec="seconds"), "risk_level": "caution",
         "crypto_hype": []}]}))

    def seat(symbol="BERAUSDT", entry=0.1837, units=254.654,
             source="scout:breakout", hours_held=3.0, score=0.75):
        h["base"][symbol[:-4]] = units
        h["usdt"] = 0.5
        h["price"] = entry
        st = {"created": "2026-09-01", "held_symbol": symbol,
              "entry_price": entry, "units": units, "entry_scan_ts": "x",
              "entry_source": source, "stopped": {}, "entries": {},
              "realized": [], "hwm": entry, "entry_score": score,
              "book_hwm_usd": 58.0,
              "entry_time": (now - timedelta(hours=hours_held)
                             ).isoformat(timespec="seconds")}
        ll.STATE.write_text(json.dumps(st))
        bl.LEDGER.write_text(json.dumps({
            "ts": st["entry_time"], "event": "fill", "action": "BUY",
            "symbol": symbol, "price": entry, "qty": units}) + "\n")
        return st

    def rest_stop(stop_price, order_type="STOP_LOSS_LIMIT", limit=None,
                  working=False):
        """A protective stop already resting at the exchange AND recorded in
        state, locking the seat's units (what _sync_stop leaves behind)."""
        st = json.loads(ll.STATE.read_text())
        b = st["held_symbol"][:-4]
        q = h["base"].pop(b, 0.0)
        h["locked"][b] = q
        oid = "77"
        h["open_orders"][oid] = {"orderId": oid, "symbol": st["held_symbol"],
                                 "side": "SELL", "type": order_type,
                                 "status": "NEW", "isWorking": working,
                                 "price": str(limit or 0),
                                 "stopPrice": str(stop_price), "origQty": str(q)}
        st["stop_order"] = {"order_id": oid, "stop": stop_price,
                            "limit": limit, "qty": q}
        ll.STATE.write_text(json.dumps(st))
        return oid

    def cash():
        h["base"] = {}
        h["locked"] = {}
        h["usdt"] = 46.0
        ll.STATE.write_text(json.dumps({
            "created": "2026-09-01", "held_symbol": None, "entry_price": None,
            "units": 0.0, "entry_scan_ts": None, "entry_source": None,
            "stopped": {}, "entries": {}, "realized": [],
            "book_hwm_usd": 46.0}))
        bl.LEDGER.write_text("")

    def scout(symbol="ABCUSDT", signal="breakout", actionable=True, score=0.8,
              extra=None):
        cands = [{"symbol": symbol, "signal": signal, "score": score,
                  "actionable": actionable, "why": "test"}]
        if extra:
            cands += extra
        (data / "scout_signals.json").write_text(json.dumps({
            "ts": now.isoformat(timespec="seconds"), "ruleset": 3,
            "candidates": cands,
            "breadth": {"count": 10, "baseline": 11.0, "wave": False}}))

    def state():
        return json.loads(ll.STATE.read_text())

    def ledger_events():
        return [json.loads(l)["event"] for l in bl.LEDGER.read_text().splitlines()
                if l.strip()]

    h.update(dict(data=data, ll=ll, bl=bl, seat=seat, cash=cash, scout=scout,
                  state=state, now=now, rest_stop=rest_stop,
                  ledger_events=ledger_events, monkeypatch=monkeypatch))
    return h


def _completes(c):
    """The one property every scenario needs: main() returns normally AND
    rewrites the state file (last_updated_utc is only set at the end)."""
    before = c["state"]().get("last_updated_utc")
    c["ll"].main()
    after = c["state"]().get("last_updated_utc")
    assert after and after != before, "cycle did not reach the state write"


def _sells(c):
    return [o for o in c["orders"] if o[0] == "SELL"]


# --- the 09-01 incident, exactly ----------------------------------------
def test_turbo_held_seat_cycle_completes(cycle):
    (cycle["data"] / "TURBO_MODE").write_text("on")
    cycle["seat"]()                       # flat price: nothing should sell
    _completes(cycle)
    assert cycle["state"]()["held_symbol"] == "BERAUSDT"
    assert not _sells(cycle)


def test_turbo_held_seat_stop_loss_fires_and_cycle_completes(cycle):
    (cycle["data"] / "TURBO_MODE").write_text("on")
    cycle["seat"]()
    cycle["price"] = 0.1837 * 0.93        # -7% < the -6% burst-seat stop
    _completes(cycle)
    st = cycle["state"]()
    assert st["held_symbol"] is None
    assert st["realized"] and st["realized"][-1]["reason"].startswith("STOP-LOSS")
    assert [o[0] for o in cycle["orders"]] == ["SELL"]


def test_gate_mode_held_seat_cycle_completes(cycle):
    cycle["seat"]()
    _completes(cycle)
    assert cycle["state"]()["held_symbol"] == "BERAUSDT"


# --- the 08-26 incident class: the entry path must be REACHABLE ----------
def test_cash_plus_actionable_scout_candidate_buys(cycle):
    cycle["cash"]()
    cycle["scout"]()
    _completes(cycle)
    st = cycle["state"]()
    assert [o[0] for o in cycle["orders"]] == ["BUY"], cycle["orders"]
    assert st["held_symbol"] == "ABCUSDT"
    assert st["entry_source"] == "scout:breakout"
    assert st["units"] > 0 and st["hwm"] == cycle["price"]


def test_benched_candidate_is_never_bought_even_in_turbo(cycle):
    (cycle["data"] / "TURBO_MODE").write_text("on")
    cycle["cash"]()
    cycle["scout"](actionable=False)      # owner decision 08-31: hard bar
    _completes(cycle)
    assert cycle["orders"] == []
    assert cycle["state"]()["held_symbol"] is None


def test_candidate_without_actionable_key_is_not_bought(cycle):
    cycle["cash"]()
    cycle["scout"]()
    d = json.loads((cycle["data"] / "scout_signals.json").read_text())
    del d["candidates"][0]["actionable"]  # a hand-edited / older file
    (cycle["data"] / "scout_signals.json").write_text(json.dumps(d))
    _completes(cycle)
    assert cycle["orders"] == []


# --- a losing exit this cycle must be counted by THIS cycle's breaker -----
def test_second_loss_today_halts_entry_in_the_same_cycle(cycle):
    st = cycle["seat"]()
    today = str(cycle["now"].date())
    # one material loss already booked today
    st["realized"] = [{"symbol": "XYZUSDT", "date": today, "pnl_usd": -1.2,
                       "pnl_pct": -2.5, "spent_usd": 46.0, "got_usd": 44.8}]
    cycle["ll"].STATE.write_text(json.dumps(st))
    cycle["scout"]()                      # a fresh actionable candidate waits
    cycle["price"] = 0.1837 * 0.93        # the seat stops out: loss #2
    _completes(cycle)
    orders = [o[0] for o in cycle["orders"]]
    assert orders == ["SELL"], orders      # sold, and NOT re-bought
    s = cycle["state"]()
    assert s["held_symbol"] is None
    assert "entries_halted" in cycle["ledger_events"]()


# --- turbo hop may only rotate into a candidate the entry lane would take --
def test_turbo_hop_ignores_benched_candidate(cycle):
    (cycle["data"] / "TURBO_MODE").write_text("on")
    cycle["seat"](score=0.60, hours_held=2.0)
    cycle["scout"](symbol="ZKCUSDT", signal="ignition", actionable=False,
                   score=0.95)           # benched, but scores far higher
    _completes(cycle)
    assert not _sells(cycle), "hopped into a benched candidate"
    assert cycle["state"]()["held_symbol"] == "BERAUSDT"


def test_turbo_hop_takes_actionable_candidate(cycle):
    (cycle["data"] / "TURBO_MODE").write_text("on")
    cycle["seat"](score=0.60, hours_held=2.0)
    cycle["scout"](symbol="ZKCUSDT", signal="breakout", actionable=True,
                   score=0.95)
    _completes(cycle)
    assert len(_sells(cycle)) == 1
    assert cycle["state"]()["realized"][-1]["reason"].startswith("TURBO HOP")


# --- exchange-resting stop: the units are LOCKED while it rests ------------
def test_resting_stop_is_cancelled_before_a_poll_exit_sells(cycle):
    cycle["monkeypatch"].setenv("LOTTERY_EXCHANGE_STOPS", "1")
    cycle["seat"]()
    oid = cycle["rest_stop"](0.1727)      # -6% floor resting, units locked
    assert cycle["base"].get("BERA", 0.0) == 0.0      # free is ZERO
    cycle["price"] = 0.1837 * 0.93        # gapped through the trigger level
    _completes(cycle)
    sells = _sells(cycle)
    assert len(sells) == 1 and abs(sells[0][3] - 254.654) < 0.01, sells
    assert cycle["open_orders"][oid]["status"] == "CANCELED"
    calls = [(m, p) for m, p, _ in cycle["calls"]]
    assert calls.index(("DELETE", "/v3/order")) < len(calls)  # cancel happened
    st = cycle["state"]()
    assert st["held_symbol"] is None and "stop_order" not in st


def test_resting_stop_never_sells_the_owners_own_coins(cycle):
    cycle["monkeypatch"].setenv("LOTTERY_EXCHANGE_STOPS", "1")
    cycle["seat"]()
    cycle["rest_stop"](0.1727)
    cycle["base"]["BERA"] = 100.0         # the OWNER's own free BERA
    cycle["price"] = 0.1837 * 0.93
    _completes(cycle)
    sells = _sells(cycle)
    assert len(sells) == 1
    assert abs(sells[0][3] - 254.654) < 0.01, "sold a different quantity"
    # the owner's 100 are untouched: what is left free is exactly theirs
    assert abs(cycle["base"]["BERA"] - 100.0) < 0.01


def test_ratchet_exit_still_works_with_a_resting_stop(cycle):
    cycle["monkeypatch"].setenv("LOTTERY_EXCHANGE_STOPS", "1")
    st = cycle["seat"]()
    st["hwm"] = 0.1837 * 1.15             # ride peaked +15%: ratchet armed
    cycle["ll"].STATE.write_text(json.dumps(st))
    cycle["rest_stop"](0.1727)
    cycle["price"] = 0.1837 * 1.06        # fell to +6%: below the +7.5% floor
    _completes(cycle)
    sells = _sells(cycle)
    assert len(sells) == 1, "poll RATCHET was a no-op behind the resting stop"
    assert cycle["state"]()["realized"][-1]["reason"].startswith("RATCHET")


def test_stranded_stop_limit_is_cancelled_and_market_sold(cycle):
    cycle["monkeypatch"].setenv("LOTTERY_EXCHANGE_STOPS", "1")
    cycle["seat"]()
    # stop triggered at 0.1727, limit 0.1701 is now ABOVE the market: the
    # exchange reports a working limit order (NEW, isWorking) and the seat
    # is unprotected with its units locked
    oid = cycle["rest_stop"](0.1727, limit=0.1701, working=True)
    cycle["price"] = 0.160                # -12.9%, well under the limit
    _completes(cycle)
    assert cycle["open_orders"][oid]["status"] == "CANCELED"
    assert len(_sells(cycle)) == 1
    assert "stop_stranded" in cycle["ledger_events"]()
    assert cycle["state"]()["held_symbol"] is None


def test_fresh_seat_gets_a_market_stop_resting_at_minus_six_percent(cycle):
    cycle["monkeypatch"].setenv("LOTTERY_EXCHANGE_STOPS", "1")
    cycle["seat"]()                       # flat, nothing to sell
    _completes(cycle)
    st = cycle["state"]()
    so = st.get("stop_order")
    assert so and so["type"] == "STOP_LOSS", so   # pair supports market stops
    assert abs(so["stop"] / 0.1837 - 0.94) < 0.001
    assert cycle["locked"]["BERA"] > 0            # units locked at the exchange


def test_state_write_is_atomic_leaves_no_tmp(cycle):
    cycle["seat"]()
    _completes(cycle)
    assert not (cycle["data"] / "lottery_state.json.tmp").exists()
    json.loads(cycle["ll"].STATE.read_text())     # parseable
