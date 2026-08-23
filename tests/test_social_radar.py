"""Social radar v2 guards — the owner's hard rule, the counting (which
Grok must never do), and the pre-registered hypotheses. Offline."""
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import social_radar as sr  # noqa: E402

# --- snowflake: our only trustworthy time channel --------------------------
# 1288834974657 is the X epoch; id 0 decodes to it exactly
assert sr.snowflake_ms("0") == 1288834974657
assert sr.snowflake_ms(str(1 << 22)) == 1288834974658
assert sr.snowflake_ms("not-an-id") is None

# --- discovery parse: tolerant of prose, normalizes, keeps evidence -------
raw = '''sure:
{"coins": [
 {"symbol": "$pepe-usdt", "catalyst_type": "LISTING",
  "catalyst_text": "Upbit notice posted", "catalyst_date_utc": "2026-09-01",
  "catalyst_already_occurred": false,
  "evidence_urls": ["https://x.com/a/status/1"], "handles_seen": ["@A"]},
 {"symbol": "!!", "catalyst_type": "none"}
]}'''
d = sr.parse_discovery(raw)
assert len(d) == 1 and d[0]["symbol"] == "PEPE", d
assert d[0]["catalyst_type"] == "listing" and d[0]["handles_seen"] == ["@a"]
assert sr.parse_discovery("no json") == []

# --- admit: Binance numbers decide, never Grok -----------------------------
listed = {"PEPE", "UPUP", "THIN", "MOVR"}
tk = {"PEPE": {"priceChangePercent": "1.2", "quoteVolume": "5000000",
               "lastPrice": "0.00001"},
      "UPUP": {"priceChangePercent": "18.0", "quoteVolume": "9000000"},
      "THIN": {"priceChangePercent": "0.5", "quoteVolume": "50000"},
      "MOVR": {"priceChangePercent": "4.0", "quoteVolume": "9000000"}}
movers = {"MOVR"}
assert sr.admit("PEPE", tk, movers, listed)[0]
ok, why = sr.admit("UPUP", tk, movers, listed)
assert not ok and "already up" in why
ok, why = sr.admit("MOVR", tk, movers, listed)
assert not ok and "top-50" in why, "a top mover is already up, whatever Grok says"
ok, why = sr.admit("THIN", tk, movers, listed)
assert not ok and "thin" in why
# the listing precondition: 13.7% of v1 calls named untradable coins
ok, why = sr.admit("HYPE", tk, movers, listed)
assert not ok and "no Binance" in why

# --- THE COUNTER: features come from rows, never from Grok's prose --------
def row(w, t, pid=None, handle=None, text=None, status="posts",
        is_reply=False, has_link=False):
    return {"window": w, "tier": t, "status": status, "post_id": pid,
            "post_url": None, "handle": handle, "text": text,
            "is_reply": is_reply, "has_link": has_link}

base = 1 << 22
rows = [
    row("W0", "T0", str(base * 1), "@a", "mainnet is live soon"),
    row("W0", "T0", str(base * 2), "@b", "mainnet is live soon"),   # dupe text
    row("W0", "T0", str(base * 3), "@c", "wallet moved 4m tokens"),
    row("W0", "T0", str(base * 3), "@c", "wallet moved 4m tokens"),  # dupe id
    row("W1", "T1", str(base * 9), "@a", "reply", is_reply=True, has_link=True),
    row("W0", "T2", None, None, None, status="empty"),
    row("W0", "T3", None, None, None, status="empty"),
]
f = sr.count_features(rows, prior_handles={"@a"})
assert f["n_posts"] == 4, f["n_posts"]           # id-dedupe worked
assert f["distinct_handles"] == 3
assert f["new_handles_ratio"] == round(2 / 3, 3)  # @b,@c new; @a known
assert f["duplicate_text_ratio"] > 0
assert f["loud_t2_hit"] is False and f["loud_t3_hit"] is False, \
    "empty engagement tiers must read as NOT loud"
assert f["min_inter_post_gap_sec"] is not None
assert len(f["evidence_post_ids"]) == 4, "one id per deduped post"
# saturation is reported, never guessed past the 10-post cap
f2 = sr.count_features([row("W0", "T3", "1", "@x", "t", status="saturated")],
                       set())
assert f2["tier_state"]["T3"] == "saturated" and f2["loud_t3_hit"] is True

# --- pre-registered hypotheses -------------------------------------------
live = []
for i in range(10):
    quiet = i % 2 == 0
    live.append({"symbol": f"C{i}",
                 "prior_24h_ret": 0.01 if quiet else 0.20,
                 "excess_24h": 0.05 if quiet else -0.04,
                 "excess_72h": 0.02, "distinct_handles": 9 if quiet else 2,
                 "loud_t3_hit": not quiet, "first_seen_ever": quiet,
                 "catalyst_type": "listing",
                 "catalyst_already_occurred": not quiet,
                 "new_handles_ratio": 0.9 if quiet else 0.1,
                 "link_share": 0.2, "btc_vol_24h": 0.03,
                 "catalyst_text": "upbit notice" if quiet
                 else "binance volume spike"})
h = sr.hypotheses(live)
assert h["H1_quiet_entry_beats_hot"]["edge_pp"] == 9.0, h["H1_quiet_entry_beats_hot"]
assert h["H2_breadth_beats_loudness"]["edge_pp"] == 9.0
assert h["H8_novelty_pays"]["edge_pp"] == 9.0
assert h["H6_exchange_surface_words_exhaust"]["edge_pp"] == -9.0, \
    "scanner-surface wording should read as the WORSE side"
# a hypothesis with no data must not crash or invent an edge
empty = sr.hypotheses([])
assert empty["H1_quiet_entry_beats_hot"].get("edge_pp") is None

# --- scorecard: only BTC-excess-scored rows are learned from --------------
card = sr.scorecard(live + [{"symbol": "X", "catalyst_type": "meme"}])
assert card["n_scored_excess_24h"] == 10
assert card["objective"] == "BTC-excess 24h"
assert "H1_quiet_entry_beats_hot" in card["hypotheses"]

print("test_social_radar: ALL PASS")
