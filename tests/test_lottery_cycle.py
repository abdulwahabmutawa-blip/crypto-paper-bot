"""End-to-end CYCLE tests for the real-money book — lottery_live.main() run
against a fully mocked exchange, in a temp data dir, with no network.

Why this file exists (incident 2026-09-01): two production outages of the
real book were the same class of bug — code that compiled but could not
RUN through a real cycle:
  * 08-23..08-26: an indent slip made the whole entry path unreachable.
  * 08-31..09-01: the golden-ticket commit read `halt_why` in the turbo-hop
    rule before the variable was assigned. Every cycle holding a seat under
    TURBO_MODE died with UnboundLocalError after the exit rules and before
    the state write; the dashboard froze on the BERAUSDT buy and the
    resting-stop sync never ran.
Unit tests of the helpers passed both times. Only a test that drives
main() through its real control flow catches this class, so that is what
these do. Every scenario asserts the cycle COMPLETES and the state file is
rewritten — the two facts the owner's phone dashboard depends on.

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
    """A harness: temp data dir, armed env, mocked exchange, recorded orders."""
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

    h = {"price": 1.0, "usdt": 46.0, "base": {}, "orders": [], "ticker": None}

    def _price(sym):
        return h["price"]

    def _balances():
        d = {"USDT": h["usdt"]}
        d.update(h["base"])
        return d

    def _market(action, symbol, quote_qty=None, qty=None):
        h["orders"].append((action, symbol, quote_qty, qty))
        if action == "BUY":
            units = round(quote_qty / h["price"], 6)
            h["base"][symbol[:-4]] = units
            h["usdt"] = 0.0
            fill = {"price": h["price"], "qty": units, "order_id": "1",
                    "commission": 0.0, "commission_asset": "BNB"}
        else:
            h["base"].pop(symbol[:-4], None)
            h["usdt"] = round(qty * h["price"], 4)
            fill = {"price": h["price"], "qty": qty, "order_id": "2",
                    "commission": 0.0, "commission_asset": "BNB"}
        bl.log({"event": "fill", "action": action, "symbol": symbol,
                "price": fill["price"], "qty": fill["qty"]})
        return fill

    def _call(method, path, params=None, **kw):
        # exchangeInfo for the sell's LOT_SIZE lookup; everything else
        # (klines, 24hr tickers, depth) returns "no data" and the rules
        # must fail toward HOLD, never toward a crash.
        if path == "/v3/exchangeInfo":
            return {"symbols": [{"filters": [
                {"filterType": "LOT_SIZE", "stepSize": "0.001"},
                {"filterType": "PRICE_FILTER", "tickSize": "0.0001"}]}]}
        if path == "/v3/ticker/24hr":
            return h["ticker"]
        return None

    monkeypatch.setattr(bl, "price", _price)
    monkeypatch.setattr(bl, "balances", _balances)
    monkeypatch.setattr(bl, "balances_valuation", lambda held=None: _balances())
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

    def cash():
        h["base"] = {}
        h["usdt"] = 46.0
        ll.STATE.write_text(json.dumps({
            "created": "2026-09-01", "held_symbol": None, "entry_price": None,
            "units": 0.0, "entry_scan_ts": None, "entry_source": None,
            "stopped": {}, "entries": {}, "realized": [],
            "book_hwm_usd": 46.0}))
        bl.LEDGER.write_text("")

    def scout(symbol="ABCUSDT", signal="breakout", actionable=True, score=0.8):
        (data / "scout_signals.json").write_text(json.dumps({
            "ts": now.isoformat(timespec="seconds"), "ruleset": 3,
            "candidates": [{"symbol": symbol, "signal": signal, "score": score,
                            "actionable": actionable, "why": "test"}],
            "breadth": {"count": 10, "baseline": 11.0, "wave": False}}))

    def state():
        return json.loads(ll.STATE.read_text())

    h.update(dict(data=data, ll=ll, bl=bl, seat=seat, cash=cash, scout=scout,
                  state=state, now=now))
    return h


def _completes(c):
    """The one property every scenario needs: main() returns normally AND
    rewrites the state file (last_updated_utc is only set at the end)."""
    before = c["state"]().get("last_updated_utc")
    c["ll"].main()
    after = c["state"]().get("last_updated_utc")
    assert after and after != before, "cycle did not reach the state write"


# --- the 09-01 incident, exactly ----------------------------------------
def test_turbo_held_seat_cycle_completes(cycle):
    (cycle["data"] / "TURBO_MODE").write_text("on")
    cycle["seat"]()                       # flat price: nothing should sell
    _completes(cycle)
    assert cycle["state"]()["held_symbol"] == "BERAUSDT"
    assert not any(o[0] == "SELL" for o in cycle["orders"])


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
    assert "CIRCUIT BREAKER" in (s.get("halt_flagged") or "").upper() or \
        any(json.loads(l).get("event") == "entries_halted"
            for l in cycle["bl"].LEDGER.read_text().splitlines() if l.strip())
