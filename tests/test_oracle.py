"""Oracle phase-0 tests — offline, no network, no writes outside a tmpdir.

These pin the guarantees the experiment's credibility rests on: it cannot
trade, it cannot look ahead, it cannot see outcomes while predicting, and it
cannot quietly rewrite its own history.
"""
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import oracle.config as config      # noqa: E402
import oracle.fetch as fetch        # noqa: E402
import oracle.ledger as ledger      # noqa: E402
import oracle.predict as predict    # noqa: E402
import oracle.resolve as resolve    # noqa: E402
import oracle.score as score        # noqa: E402
import oracle.universe as universe  # noqa: E402

# --- IT CANNOT TRADE ---------------------------------------------------------
# The whole premise is that this package is structurally incapable of
# placing an order. Grep every source file for the trading modules; a future
# refactor that wires them together fails the build here.
BANNED = ("binance_live", "lottery_live", "binance_broker", "ibkr_broker")
for py in (ROOT / "oracle").rglob("*.py"):
    src = py.read_text(encoding="utf-8")
    for mod in BANNED:
        assert f"import {mod}" not in src and f"from {mod}" not in src, \
            f"{py.name} imports {mod} — the oracle must never reach a broker"
# and no key material may be read
for py in (ROOT / "oracle").rglob("*.py"):
    src = py.read_text(encoding="utf-8")
    for secret in ("API_KEY", "API_SECRET", "LOTTERY_LIVE"):
        assert secret not in src, f"{py.name} references {secret}"

# the network surface is two market-data paths and nothing else
assert set(fetch.ALLOWED_PATHS) == {"/api/v3/exchangeInfo",
                                    "/api/v3/ticker/24hr", "/api/v3/klines"}
try:
    fetch._get("/api/v3/order")
    raise AssertionError("fetch must refuse non-market-data paths")
except ValueError as e:
    assert "refuses" in str(e)

# --- universe rule -----------------------------------------------------------
assert universe.eligible_symbol("PEPEUSDT", "TRADING")
assert not universe.eligible_symbol("PEPEUSDT", "BREAK"), "halted pair"
assert not universe.eligible_symbol("BTCUSDC", "TRADING"), "non-USDT quote"
assert not universe.eligible_symbol("USDCUSDT", "TRADING"), "stablecoin"
assert not universe.eligible_symbol("BTCUPUSDT", "TRADING"), "leveraged"


def rows(n, close=1.0, high=None, qv=1_000_000.0):
    """n synthetic daily klines."""
    high = close if high is None else high
    return [[i * 86400000, close, high, close, close, 1.0,
             i * 86400000 + 86399999, qv, 10, 1.0, 1.0, 0] for i in range(n)]


ok, why = universe.eligible_history(rows(200))
assert ok, why
ok, why = universe.eligible_history(rows(50))
assert not ok and "listed<" in why, "young listings cannot be judged"
ok, why = universe.eligible_history(rows(200, qv=1_000.0))
assert not ok and "below floor" in why, "illiquid coin is unexitable"
ok, why = universe.eligible_history(rows(200, qv=9e9))
assert not ok and "above ceiling" in why

# --- NO LOOKAHEAD in the climatology ----------------------------------------
# Only windows that had fully resolved before the reference candle may count.
# 100 flat days: no window can hit, and the count must exclude the final
# `horizon` days that had not yet resolved.
h, w = predict.explosion_rate(rows(100), horizon=30, mult=1.5, lookback=365)
# start days 0..69 each have a full 30-day window closing at or before the
# reference candle (index 99); day 70 onward would still be open.
assert h == 0 and w == 70, (h, w)
# a spike on the LAST day must not be counted by a window that had not closed
spiky = rows(100)
spiky[-1][2] = 99.0                 # huge high on the final candle
h2, w2 = predict.explosion_rate(spiky, horizon=30, mult=1.5, lookback=365)
assert w2 == w, "window count must not change"
assert h2 == 1, "only the single window ending on that day may count"

# --- the prediction contract has NO outcome fields --------------------------
FORBIDDEN = ("outcome", "resolved", "y_true", "hit", "max_high", "status")
sample = {
    "schema_version": config.SCHEMA_VERSION, "prediction_id": "x",
    "symbol": "AAAUSDT", "probability": 0.02,
    "reference": {"close_price": "1.0"},
    "event": {"threshold_mult": 1.5, "window_start_ms": 0,
              "window_end_ms": 86400000},
}
for f in FORBIDDEN:
    assert f not in sample, f"a prediction record must never carry '{f}'"

# --- the resolver sees five fields and no reasoning --------------------------
rec = dict(sample, reasoning="I feel good about this one",
           probability=0.9, mechanism_hypothesis="vibes")
q = resolve._question(rec)
assert set(q) == {"prediction_id", "symbol", "ref_close", "threshold_mult",
                  "window_start_ms", "window_end_ms"}
assert "reasoning" not in q and "probability" not in q, \
    "no channel may exist from narrative to resolution"

# --- resolution logic --------------------------------------------------------
_orig = fetch.klines
try:
    fetch.klines = lambda *a, **k: rows(30, close=1.0, high=1.60)
    r = resolve.resolve_one({"prediction_id": "p1", "symbol": "AAAUSDT",
                             "ref_close": 1.0, "threshold_mult": 1.5,
                             "window_start_ms": 0,
                             "window_end_ms": 30 * 86400000})
    assert r["status"] == "resolved" and r["outcome"] == 1, r

    fetch.klines = lambda *a, **k: rows(30, close=1.0, high=1.40)
    r = resolve.resolve_one({"prediction_id": "p2", "symbol": "AAAUSDT",
                             "ref_close": 1.0, "threshold_mult": 1.5,
                             "window_start_ms": 0,
                             "window_end_ms": 30 * 86400000})
    assert r["status"] == "resolved" and r["outcome"] == 0, r

    # delisted mid-window: annulled, never guessed
    fetch.klines = lambda *a, **k: rows(5, close=1.0, high=1.0)
    r = resolve.resolve_one({"prediction_id": "p3", "symbol": "AAAUSDT",
                             "ref_close": 1.0, "threshold_mult": 1.5,
                             "window_start_ms": 0,
                             "window_end_ms": 30 * 86400000})
    assert r["status"] == "annulled" and r["outcome"] is None, r
    assert "missing bars" in r["annul_reason"]
finally:
    fetch.klines = _orig

# --- scoring -----------------------------------------------------------------
# a perfectly correlated group has rho 1; independent groups near 0
rho, m = score.intraclass_rho([[1, 1, 1], [0, 0, 0], [1, 1, 1]])
assert rho > 0.9, rho
rho2, _ = score.intraclass_rho([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
assert rho2 < 0.2, rho2
assert score.required_n(0.0, 0.1) is None
assert score.required_n(1.0, 0.1) > 0

# the refusal to overclaim is code, not etiquette
tmp = Path(tempfile.mkdtemp())
orig = (config.PREDICTIONS, config.RESOLUTIONS)
try:
    config.PREDICTIONS = tmp / "p"
    config.RESOLUTIONS = tmp / "r"
    config.PREDICTIONS.mkdir()
    config.RESOLUTIONS.mkdir()
    pf = config.PREDICTIONS / "run.jsonl"
    rf = config.RESOLUTIONS / "run.jsonl"
    with pf.open("w", encoding="utf-8") as fh, rf.open("w", encoding="utf-8") as rh:
        for i in range(10):
            pid = f"id{i}"
            fh.write(json.dumps({
                "prediction_id": pid, "run_id": "r1", "symbol": f"S{i}",
                "probability": 0.02, "baseline_p_base_rate": 0.02}) + "\n")
            rh.write(json.dumps({
                "prediction_id": pid, "status": "resolved",
                "outcome": 1 if i == 0 else 0}) + "\n")
    s = score.compute()
    assert s["n_scored"] == 10
    assert s["verdict"] is None, "must refuse a verdict below n_eff"
    assert "NO CONCLUSION" in s["status"]
    md = score.report(s)
    assert "NO CONCLUSION" in md
    # banned metrics must appear in neither the scored data nor the report
    # body. The closing disclaimer NAMES them on purpose, so it is excluded.
    body = "\n".join(l for l in md.splitlines() if not l.startswith("_"))
    for banned in config.BANNED_METRICS:
        assert banned not in body.lower(), \
            f"'{banned}' must never be reported as a metric"
        assert not any(banned in k.lower() for k in s), \
            f"'{banned}' must never be computed into the scores"
finally:
    config.PREDICTIONS, config.RESOLUTIONS = orig

# --- the hash chain detects tampering ---------------------------------------
tmp2 = Path(tempfile.mkdtemp())
orig_chain, orig_root = config.CHAIN, config.ROOT
try:
    config.ROOT = tmp2
    config.CHAIN = tmp2 / "chain.jsonl"
    f1 = tmp2 / "a.jsonl"
    f1.write_text('{"x":1}\n', encoding="utf-8")
    e1 = ledger.append("predictions", f1, 1)
    f2 = tmp2 / "b.jsonl"
    f2.write_text('{"x":2}\n', encoding="utf-8")
    e2 = ledger.append("resolutions", f2, 1)
    assert e2["chain_prev"] == e1["chain_self"]
    ok, probs = ledger.verify()
    assert ok, probs

    # edit a historical record: verification must catch it
    f1.write_text('{"x":999}\n', encoding="utf-8")
    ok, probs = ledger.verify()
    assert not ok and any("CONTENT CHANGED" in p for p in probs), probs

    # edit the ledger line itself: also caught
    f1.write_text('{"x":1}\n', encoding="utf-8")
    lines = config.CHAIN.read_text(encoding="utf-8").splitlines()
    bad = json.loads(lines[0])
    bad["n_records"] = 42
    config.CHAIN.write_text(json.dumps(bad, sort_keys=True) + "\n"
                            + lines[1] + "\n", encoding="utf-8")
    ok, probs = ledger.verify()
    assert not ok and any("entry hash mismatch" in p for p in probs), probs
finally:
    config.CHAIN, config.ROOT = orig_chain, orig_root

print("test_oracle: ALL PASS")
