"""Social-heat layer — deterministic, offline, no network.
The pure helpers are pinned here; fetchers are best-effort by design."""
import json
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import social_heat as sh    # noqa: E402
import binance_scout as sc  # noqa: E402

UNI = {"PEPE", "BTC", "WLD", "ONE", "TRUMP", "GAS"}

# --- symbol extraction: conservative on purpose ------------------------------
# cashtags always count, even for ambiguous names — $ONE is a deliberate ref
assert sh.extract_symbols(["$PEPE to the moon", "$ONE pumping"], UNI) == \
    ["PEPE", "ONE"]
# bare ambiguous words must NOT count: a Trump headline is not a TRUMP-coin
# signal, "one bill" is not Harmony
assert sh.extract_symbols(["Trump signs ONE bill on GAS prices"], UNI) == []
# bare unambiguous uppercase coin names count
assert sh.extract_symbols(["BREAKING: WLD surges after announcement"], UNI) \
    == ["WLD"]
# unknown symbols never count
assert sh.extract_symbols(["$DOGE and $SHIB rallying"], UNI) == []
# duplicates collapse
assert sh.extract_symbols(["$PEPE!", "PEPE again", "$PEPE"], UNI) == ["PEPE"]

# --- stocktwits: .X suffix is crypto, everything else is equities ------------
assert sh.stocktwits_bases(["BTC.X", "AAPL", "PEPE.X", "TSLA"], UNI) == \
    ["BTC", "PEPE"]

# --- aggregation: DISTINCT surfaces, duplicates within a source collapse -----
heat = sh.aggregate({"a": ["PEPE", "BTC"], "b": ["PEPE"],
                     "c": ["PEPE", "PEPE"], "d": []})
assert heat[0] == {"symbol": "PEPE", "surfaces": 3,
                   "sources": ["a", "b", "c"]}, heat[0]
assert heat[1]["symbol"] == "BTC" and heat[1]["surfaces"] == 1

# --- watcher surface: only euphoric, only fresh ------------------------------
tmp = Path(tempfile.mkdtemp())
orig_sent = sh.SENTINEL
sh.SENTINEL = tmp / "sentinel_state.json"
try:
    now = datetime(2026, 8, 16, 12, 0, tzinfo=timezone.utc)
    sh.SENTINEL.write_text(json.dumps({"scans": [{
        "ts": "2026-08-16T10:00:00+00:00",
        "crypto_hype": [{"symbol": "PEPE", "mood": "euphoric"},
                        {"symbol": "BTC", "mood": "mixed"},
                        {"symbol": "NOPE", "mood": "euphoric"}]}]}))
    assert sh.watcher_surface(now, UNI) == ["PEPE"], \
        "euphoric-only, universe-only"
    stale = datetime(2026, 8, 17, 12, 0, tzinfo=timezone.utc)
    assert sh.watcher_surface(stale, UNI) == [], "a stale scan is no surface"
finally:
    sh.SENTINEL = orig_sent

# --- scout integration: heat candidates flow through the same machinery ------
orig_heat = sc.HEAT_FILE
sc.HEAT_FILE = tmp / "social_heat.json"
try:
    now = datetime(2026, 8, 16, 12, 0, tzinfo=timezone.utc)
    sc.HEAT_FILE.write_text(json.dumps({
        "ts": "2026-08-16T11:50:00+00:00",
        "heat": [
            {"symbol": "PEPE", "surfaces": 4,
             "sources": ["coingecko", "movers", "reddit", "stocktwits"],
             "funding": 0.0012},
            {"symbol": "BTC", "surfaces": 2, "sources": ["movers", "reddit"]},
            {"symbol": "GONE", "surfaces": 5, "sources": ["a", "b", "c", "d", "e"]},
        ]}))
    tickers = {"PEPEUSDT": {"symbol": "PEPEUSDT", "lastPrice": "0.00002",
                            "priceChangePercent": "9.5"},
               "BTCUSDT": {"symbol": "BTCUSDT", "lastPrice": "100000",
                           "priceChangePercent": "0.4"}}
    cands = sc.heat_candidates(tickers, {"signals": {}}, now)
    assert len(cands) == 1, f"only 3+ surfaces AND tradeable: {cands}"
    c = cands[0]
    assert c["symbol"] == "PEPEUSDT" and c["signal"] == "heat"
    assert c["price"] == 0.00002 and "4 independent surfaces" in c["why"]
    # stale heat file -> no candidates (yesterday's crowd)
    later = datetime(2026, 8, 16, 14, 0, tzinfo=timezone.utc)
    assert sc.heat_candidates(tickers, {"signals": {}}, later) == []
finally:
    sc.HEAT_FILE = orig_heat

# --- the gate applies to heat like everything else ---------------------------
assert "heat" in sc.SIGNAL_TYPES
ok, why = sc.signal_actionable({"signals": {}}, "heat")
assert not ok and "probation" in why, \
    "heat starts on probation and must earn real money like every signal"

print("test_social_heat: ALL PASS")
