"""Scalper paper bot — offline cycle against fake candles. No network."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import config  # noqa: E402


def candle(t, o, h, l, c, qv=1000.0, tb=600.0):
    return [t, o, h, l, c, 0, t + 899_000, qv, 10, 0, tb, 0]


def _flat(px=100.0, n=120, qv=1000.0):
    return [candle(i * 900_000, px, px * 1.001, px * 0.999, px, qv) for i in range(n)]


def _surge(n=120):
    # quiet, then 4h of 3x volume grinding +4% to the range top
    k = _flat(n=n - 16)
    px = 100.0
    for i in range(16):
        px *= 1.0025
        k.append(candle((n - 16 + i) * 900_000, px, px * 1.002, px * 0.998, px, 3000.0))
    return k


def _run(tmp_path, monkeypatch, kl, now_ms):
    import bot_scalper as sc
    import smallwins_lab as lab
    import binance_data
    monkeypatch.setattr(config, "DATA", tmp_path)
    monkeypatch.setattr(sc, "STATE", tmp_path / "scalper_state.json")
    monkeypatch.setattr(sc, "REPORT", tmp_path / "scalper.md")
    monkeypatch.setattr(sc, "_remote_state", lambda: None)
    monkeypatch.setattr(lab, "universe", lambda: [s for s in kl if s != "BTCUSDT"])
    monkeypatch.setattr(binance_data, "klines", lambda s, i="15m", n=120: kl.get(s, []))
    from datetime import datetime, timezone
    monkeypatch.setattr(sc, "_now", lambda: datetime.fromtimestamp(now_ms / 1000, tz=timezone.utc))
    monkeypatch.setattr(lab, "_now", sc._now)
    assert sc.main() == 0
    return json.loads(sc.STATE.read_text()), sc


def test_fills_seats_on_surge_and_marks_equity(tmp_path, monkeypatch):
    kl = {"BTCUSDT": _flat(50000.0), "AAAUSDT": _surge(), "BBBUSDT": _surge(), "QUIETUSDT": _flat()}
    st, sc = _run(tmp_path, monkeypatch, kl, 120 * 900_000 + 1000)
    assert {p["symbol"] for p in st["open"]} == {"AAAUSDT", "BBBUSDT"}
    assert all(p["shape"] == "surge" for p in st["open"])
    assert abs(st["cash"] + sum(p["stake"] for p in st["open"]) - 1000.0) < 1e-6
    assert abs(st["equity"] - 1000.0) < 1e-6


def test_target_hit_books_profit_and_reuses_cash(tmp_path, monkeypatch):
    kl = {"BTCUSDT": _flat(50000.0), "AAAUSDT": _surge()}
    st, sc = _run(tmp_path, monkeypatch, kl, 120 * 900_000 + 1000)
    p = st["open"][0]
    e = p["entry"]
    # next cycle: a later candle touches +3%
    kl["AAAUSDT"] = kl["AAAUSDT"] + [candle(120 * 900_000, e, e * 1.035, e * 0.999, e * 1.03, 3000.0)]
    kl["BTCUSDT"] = _flat(50000.0, n=121)
    st, sc = _run(tmp_path, monkeypatch, kl, 121 * 900_000 + 1000)
    assert st["trades"] and st["trades"][-1]["how"] == "TARGET"
    assert abs(st["trades"][-1]["ret"] - (0.03 - sc.COST)) < 1e-9
    assert st["equity"] > 1000.0


def test_stop_sets_cooldown(tmp_path, monkeypatch):
    kl = {"BTCUSDT": _flat(50000.0), "AAAUSDT": _surge()}
    st, sc = _run(tmp_path, monkeypatch, kl, 120 * 900_000 + 1000)
    e = st["open"][0]["entry"]
    kl["AAAUSDT"] = kl["AAAUSDT"] + [candle(120 * 900_000, e, e * 1.001, e * 0.96, e * 0.97, 3000.0)]
    kl["BTCUSDT"] = _flat(50000.0, n=121)
    st, sc = _run(tmp_path, monkeypatch, kl, 121 * 900_000 + 1000)
    assert st["trades"][-1]["how"] == "STOP" and "AAAUSDT" in st["cooldown"]
    assert st["open"] == []            # cooldown blocks the immediate re-entry


def test_merge_keeps_trades_and_rederives_cash():
    import bot_scalper as sc
    a = {"cash": 900.0, "open": [{"symbol": "X", "entry_ms": 1, "stake": 100.0}], "trades": [], "runs": 3}
    b = {"cash": 1010.0, "open": [], "runs": 4,
         "trades": [{"symbol": "X", "entry_ms": 1, "stake": 100.0, "pnl_usd": 10.0, "exit_ts": "t"}]}
    m = sc.merge_states(a, b)
    assert m["open"] == [] and len(m["trades"]) == 1 and abs(m["cash"] - 1010.0) < 1e-9 and m["runs"] == 4
