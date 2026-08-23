"""Social radar guards — the owner's hard rule ("never observe a coin that
is already up") and the feature learning, offline. Run directly."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import social_radar as sr  # noqa: E402

# --- parse: tolerant of prose, normalizes symbols, keeps features ----------
raw = '''Here you go:
{"coins": [
 {"symbol": "$pepe-usdt", "velocity": 4, "distinct_accounts": "~120",
  "breadth": "many", "top_accounts": ["@A", "@B"], "top_terms": ["Mainnet", "listing"],
  "catalyst_type": "listing", "catalyst_date": "2026-09-01", "organic": true,
  "promo_risk": "low", "why": "dev posts + listing rumor"},
 {"symbol": "BAD!", "velocity": "x"}
]}'''
coins = sr.parse_coins(raw)
assert len(coins) == 1 and coins[0]["symbol"] == "PEPE", coins
assert coins[0]["top_terms"] == ["mainnet", "listing"]
assert coins[0]["top_accounts"] == ["@a", "@b"]
assert sr.parse_coins("no json here") == []

# --- admit: Binance numbers decide, never Grok ------------------------------
tk = {"PEPE": {"priceChangePercent": "1.2", "quoteVolume": "5000000",
               "lastPrice": "0.00001"},
      "UPUP": {"priceChangePercent": "18.0", "quoteVolume": "9000000",
               "lastPrice": "1"},
      "THIN": {"priceChangePercent": "0.5", "quoteVolume": "50000",
               "lastPrice": "1"},
      "MOVR": {"priceChangePercent": "4.0", "quoteVolume": "9000000",
               "lastPrice": "1"}}
top = {"MOVR"}
ok, why = sr.admit({"symbol": "PEPE", "organic": True, "promo_risk": "low"}, tk, top)
assert ok, why
ok, why = sr.admit({"symbol": "UPUP", "organic": True, "promo_risk": "low"}, tk, top)
assert not ok and "already up" in why, "up +18% on the day must be dropped"
ok, why = sr.admit({"symbol": "MOVR", "organic": True, "promo_risk": "low"}, tk, top)
assert not ok and "top-50" in why, "a top mover is already up, whatever Grok says"
ok, why = sr.admit({"symbol": "THIN", "organic": True, "promo_risk": "low"}, tk, top)
assert not ok and "thin" in why
ok, why = sr.admit({"symbol": "PEPE", "organic": False, "promo_risk": "low"}, tk, top)
assert not ok and "promotion" in why, "promoted chatter is never observed"
ok, why = sr.admit({"symbol": "NOPE", "organic": True, "promo_risk": "low"}, tk, top)
assert not ok and "no Binance" in why

# --- scorecard: features learn from resolved rows ---------------------------
rows = []
for i in range(12):
    rows.append({"symbol": f"C{i}", "top_terms": ["mainnet"] if i % 2 == 0
                 else ["giveaway"], "top_accounts": ["@good"] if i % 2 == 0
                 else ["@shill"], "catalyst_type": "listing" if i % 2 == 0
                 else "meme", "breadth": "many", "velocity": 3,
                 "ret_24h": 0.06 if i % 2 == 0 else -0.04})
card = sr.scorecard(rows)
assert card["n_resolved_24h"] == 12
assert card["features"]["term"]["mainnet"]["hit"] == 1.0
assert card["features"]["term"]["giveaway"]["hit"] == 0.0
assert card["leaders"][0]["feature"] in ("mainnet", "@good", "listing"), card["leaders"][0]
assert card["laggards"][0]["feature"] in ("giveaway", "@shill", "meme")
# unresolved rows are not learned from
assert sr.scorecard([{"symbol": "X", "top_terms": ["x"]}])["n_resolved_24h"] == 0

print("test_social_radar: ALL PASS")
