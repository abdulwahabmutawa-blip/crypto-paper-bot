"""Hype trader on IBKR — offline cycle tests against a fake broker.
No network, no Gateway, no keys."""
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import config  # noqa: E402


@pytest.fixture
def h(tmp_path, monkeypatch):
    monkeypatch.setenv("HYPE_IBKR_ARMED", "1")
    monkeypatch.delenv("IBKR_PORT", raising=False)
    monkeypatch.delenv("HYPE_IBKR_REAL", raising=False)
    data = tmp_path / "data"
    data.mkdir()
    monkeypatch.setattr(config, "DATA", data)
    import ibkr_live as bl
    import hype_ibkr as hb
    import market_hours
    monkeypatch.setattr(bl, "LEDGER", data / "hype_ibkr_ledger.jsonl")
    monkeypatch.setattr(bl, "KILL_SWITCH", data / "KILL_SWITCH")
    monkeypatch.setattr(hb, "STATE", data / "hype_ibkr_state.json")
    monkeypatch.setattr(hb, "SENTINEL", data / "sentinel_state.json")
    monkeypatch.setattr(market_hours, "us_equities_open", lambda now=None: True)
    fx = {"px": {"NVDA": 100.0, "DELL": 50.0}, "pos": {}, "settled": 300.0, "orders": []}

    def buy(t, usd):
        fx["orders"].append(("BUY", t, usd))
        q = usd / fx["px"][t]
        fx["pos"][t] = fx["pos"].get(t, 0) + q
        fx["settled"] -= usd
        bl.log({"event": "fill", "action": "BUY", "ticker": t, "qty": q, "price": fx["px"][t]})
        return {"qty": q, "price": fx["px"][t], "commission": 1.0, "order_id": "1"}

    def sell(t, qty):
        fx["orders"].append(("SELL", t, qty))
        fx["pos"][t] = fx["pos"].get(t, 0) - qty
        bl.log({"event": "fill", "action": "SELL", "ticker": t, "qty": qty, "price": fx["px"][t]})
        return {"qty": qty, "price": fx["px"][t], "commission": 1.0, "order_id": "2"}

    monkeypatch.setattr(bl, "quote", lambda t: fx["px"].get(t))
    monkeypatch.setattr(bl, "market_buy", buy)
    monkeypatch.setattr(bl, "market_sell", sell)
    monkeypatch.setattr(bl, "positions", lambda: {k: v for k, v in fx["pos"].items() if v > 1e-9})
    monkeypatch.setattr(bl, "account", lambda: {"settled_cash": fx["settled"], "net_liq": 300.0})

    def scan(symbols, age_h=1.0, risk="caution"):
        ts = (datetime.now(timezone.utc) - timedelta(hours=age_h)).isoformat(timespec="seconds")
        (data / "sentinel_state.json").write_text(json.dumps({"scans": [
            {"ts": ts, "risk_level": risk,
             "hype": [{"symbol": s, "mood": "euphoric"} for s in symbols]}]}))
        return ts

    def state():
        return json.loads(hb.STATE.read_text())

    fx.update(dict(hb=hb, bl=bl, scan=scan, state=state, data=data))
    return fx


def test_buys_top_euphoric_us_stock_skips_crypto(h):
    h["scan"](["BTC", "NVDA", "DELL"])
    h["hb"].main()
    assert h["orders"] == [("BUY", "NVDA", 300.0)]
    s = h["state"]()
    assert s["holding"] == "NVDA" and s["paper"] is True


def test_fade_waits_for_min_hold_then_rotates(h):
    ts = h["scan"](["NVDA"])
    h["hb"].main()
    # newer scan without NVDA, 1h later: must HOLD (min hold 48h)
    h["scan"](["DELL"], age_h=0.5)
    h["hb"].main()
    assert h["state"]()["holding"] == "NVDA"
    # age the entry past 48h -> rotate: sell NVDA, and (budget allows) buy DELL
    s = h["state"](); s["entry_time"] = (datetime.now(timezone.utc) - timedelta(hours=50)).isoformat(timespec="seconds")
    h["hb"].STATE.write_text(json.dumps(s))
    h["settled"] = 300.0
    h["hb"].main()
    acts = [o[0] + ":" + o[1] for o in h["orders"]]
    assert acts == ["BUY:NVDA", "SELL:NVDA", "BUY:DELL"], acts


def test_stop_loss_ignores_min_hold(h):
    h["scan"](["NVDA"])
    h["hb"].main()
    h["px"]["NVDA"] = 89.0            # -11%
    h["hb"].main()
    assert [o[0] for o in h["orders"]] == ["BUY", "SELL"]
    assert h["state"]()["realized"][-1]["reason"].startswith("STOP-LOSS")


def test_entry_budget_two_per_week(h):
    s = h["hb"]._load()
    now = datetime.now(timezone.utc)
    s["entries"] = [(now - timedelta(days=1)).isoformat(timespec="seconds"),
                    (now - timedelta(days=3)).isoformat(timespec="seconds")]
    h["hb"].STATE.write_text(json.dumps(s))
    h["scan"](["NVDA"])
    h["hb"].main()
    assert h["orders"] == []


def test_stale_scan_blocks_entry(h):
    h["scan"](["NVDA"], age_h=30)
    h["hb"].main()
    assert h["orders"] == []


def test_live_port_refused_without_real_flag(h, monkeypatch):
    monkeypatch.setenv("IBKR_PORT", "4001")
    assert h["bl"].connect() is None
    assert any(json.loads(l)["event"] == "refused"
               for l in h["bl"].LEDGER.read_text().splitlines() if l.strip())


def test_external_close_clears_seat(h):
    h["scan"](["NVDA"])
    h["hb"].main()
    h["pos"]["NVDA"] = 0.0            # owner sold it in the IBKR app
    h["hb"].main()
    assert h["state"]()["holding"] is None
    assert [o[0] for o in h["orders"]] == ["BUY"]
