"""SURGE lane (owner decision 2026-09-05): the signal module offline, and the
real-money cycle driven through it with the fake exchange from
test_lottery_cycle."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_lottery_cycle import cycle, _completes, _sells  # noqa: E402,F401

import surge_signal as sg  # noqa: E402


def _k(closes, qv, hi=None, lo=None):
    rows = []
    for i, c in enumerate(closes):
        h = (hi[i] if hi else c * 1.01)
        l = (lo[i] if lo else c * 0.99)
        rows.append([i * 3600000, c, h, l, c, 1.0, i * 3600000 + 3599999, qv[i]])
    return rows


def _flat(n=170, c=1.0, qv=100.0):
    return _k([c] * n, [qv] * n)


def _surging():
    # 6 quiet days at $100/h volume, then 24h at 3x volume grinding +8% to the high
    closes = [1.0] * 146 + [1.0 + 0.08 * (i + 1) / 24 for i in range(24)]
    qv = [100.0] * 146 + [300.0] * 24
    return _k(closes, qv)


def test_features_reads_v24_pos24_r24():
    f = sg.features(_surging())
    assert f["v24"] == pytest.approx(3.0, abs=0.1)
    assert f["pos24"] > 0.85 and 0.07 < f["r24"] < 0.09


def test_candidates_filters_and_ranks(tmp_path, monkeypatch):
    monkeypatch.setattr(sg, "SIGNALS", tmp_path / "s.json")
    monkeypatch.setattr(sg, "LOG", tmp_path / "l.jsonl")
    tick = [{"symbol": s, "quoteVolume": "5000000", "priceChangePercent": "8"}
            for s in ("GOODUSDT", "CROWDUSDT", "OIUSDT", "QUIETUSDT")]
    tick.append({"symbol": "BTCUSDT", "quoteVolume": "9e9", "priceChangePercent": "0"})
    kl = {"GOODUSDT": _surging(), "CROWDUSDT": _surging(), "OIUSDT": _surging(),
          "QUIETUSDT": _flat(), "BTCUSDT": _flat()}
    out = sg.candidates(tickers=tick, klines=lambda s, i, n: kl[s],
                        funding={"GOODUSDT": 0.0001, "CROWDUSDT": 0.001, "OIUSDT": 0.0},
                        oi_chg=lambda s: 0.5 if s == "OIUSDT" else 0.05)
    assert [c["symbol"] for c in out] == ["GOODUSDT"]
    assert out[0]["actionable"] is True and out[0]["signal"] == "surge"
    doc = json.loads((tmp_path / "s.json").read_text())
    whys = {x["symbol"]: x["why"] for x in doc["skipped"]}
    assert "funding" in whys["CROWDUSDT"] and "OI" in whys["OIUSDT"]


def test_candidates_stand_down_when_btc_falls(tmp_path, monkeypatch):
    monkeypatch.setattr(sg, "SIGNALS", tmp_path / "s.json")
    monkeypatch.setattr(sg, "LOG", tmp_path / "l.jsonl")
    tick = [{"symbol": "GOODUSDT", "quoteVolume": "5000000", "priceChangePercent": "8"}]
    btc = _k([1.0] * 146 + [1.0 - 0.03 * (i + 1) / 24 for i in range(24)], [1.0] * 170)
    out = sg.candidates(tickers=tick, klines=lambda s, i, n: btc if s == "BTCUSDT" else _surging(),
                        funding={}, oi_chg=lambda s: 0.0)
    assert out == []


# --- the cycle ---------------------------------------------------------------
def _surge(cycle, syms=("ABCUSDT",)):
    cycle["monkeypatch"].setenv("LOTTERY_SURGE", "1")
    cycle["monkeypatch"].setenv("LOTTERY_LEGACY_SCOUT", "0")
    cycle["monkeypatch"].setattr(cycle["ll"].surge_signal, "candidates",
                                 lambda now=None, **k: [{"symbol": s, "signal": "surge",
                                                         "score": 0.9, "actionable": True,
                                                         "why": "test"} for s in syms])


def test_cash_plus_surge_candidate_buys_with_surge_exits(cycle):
    cycle["cash"]()
    _surge(cycle)
    _completes(cycle)
    st = cycle["state"]()
    assert [o[0] for o in cycle["orders"]] == ["BUY"], cycle["orders"]
    assert st["held_symbol"] == "ABCUSDT" and st["entry_source"] == "scout:surge"
    ep = cycle["bl"].exit_params("scout:surge")
    assert ep["stop_pct"] == -0.03 and ep["target_pct"] == 0.05 and ep["max_hold_h"] == 48


def test_legacy_scout_candidate_ignored_by_default(cycle):
    cycle["cash"]()
    cycle["scout"]()                       # an actionable ignition candidate
    _surge(cycle, syms=())
    _completes(cycle)
    assert cycle["orders"] == []


def test_dead_tape_no_longer_blocks_surge(cycle):
    cycle["cash"]()
    rows = [json.dumps({"ts": cycle["now"].isoformat(timespec="seconds"),
                        "symbol": f"T{i}USDT", "signal": "ignition", "ruleset": 3,
                        "ret_4h": -0.02}) for i in range(20)]
    (cycle["data"] / "scout_log.jsonl").write_text("\n".join(rows) + "\n")
    _surge(cycle)
    _completes(cycle)
    assert [o[0] for o in cycle["orders"]] == ["BUY"]


def test_surge_seat_takes_target(cycle):
    cycle["seat"](symbol="ABCUSDT", entry=1.0, units=46.0, source="scout:surge")
    cycle["price"] = 1.052
    _surge(cycle, syms=())
    _completes(cycle)
    st = cycle["state"]()
    assert st["held_symbol"] is None
    assert st["realized"][-1]["reason"].startswith("TARGET")


def test_surge_seat_stop_at_minus_3(cycle):
    cycle["seat"](symbol="ABCUSDT", entry=1.0, units=46.0, source="scout:surge")
    cycle["price"] = 0.968
    _surge(cycle, syms=())
    _completes(cycle)
    assert cycle["state"]()["realized"][-1]["reason"].startswith("STOP-LOSS")


def test_surge_seat_holds_between(cycle):
    cycle["seat"](symbol="ABCUSDT", entry=1.0, units=46.0, source="scout:surge")
    cycle["price"] = 1.02
    _surge(cycle, syms=())
    _completes(cycle)
    assert cycle["state"]()["held_symbol"] == "ABCUSDT" and not _sells(cycle)


def test_surge_scan_failure_is_a_no_entry_not_a_crash(cycle):
    cycle["cash"]()
    _surge(cycle, syms=())
    def boom(now=None, **k):
        raise RuntimeError("network")
    cycle["monkeypatch"].setattr(cycle["ll"].surge_signal, "candidates", boom)
    _completes(cycle)
    assert cycle["orders"] == []
