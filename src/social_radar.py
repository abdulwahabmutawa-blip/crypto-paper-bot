"""Social radar v2 — LEARN which X chatter precedes Binance rises.

Owner directive (08-23): "I want the X scan to almost be able to predict
what coins are about to rise — look for chatter, then see on Binance which
sources / words associate with rises, and learn. I don't want to scan
something that already is up, no matter what."

REBUILT 08-24 to the X-CHATTER-PRECURSORS spec (25-agent study,
trading-research/x_chatter_precursors_2026-08-23.md). Two findings forced
the rewrite:

  1. GROK CANNOT COUNT. x_keyword_search returns at most 10 posts per
     call, no pagination, no aggregation primitive. Any number Grok states
     in prose is invented over <=10 posts. v1 asked it for "velocity" and
     "~120 distinct accounts" — those were fabrications.
     THE RULE: **Grok is a URL harvester; this module is the counter.**
     Post ids are snowflakes, so exact timestamps are recoverable locally:
     epoch_ms = (id >> 22) + 1288834974657.
  2. OUR OWN WATCHER IS A LAGGING INDICATOR (measured, Grade A): of 307
     euphoric calls, 77.7% were already up >10% in the prior 24h (base
     rate 23.3%), and they returned +0.97% at 24h against +4.88% for a
     random hour in the same universe — i.e. ~3.9pp WORSE than doing
     nothing, and -8.36% BTC-excess at 72h. The >5%/top-50 filter rejects
     ~88% of them, which is exactly the cut worth keeping; the surviving
     ~12% has never been measured separately. That is hypothesis H1.

THE LOOP
  STAGE 1 DISCOVERY  — one Grok call: name candidate coins with a dated
      catalyst and evidence URLs. Symbols and links only; no counts, no
      adjectives, no scores.
  ADMIT (Binance, not Grok) — spot pair must exist (13.7% of v1 calls
      named untradable coins; the most-flagged symbol of all, HYPE, has
      no pair), day change <= +5%, not a top-50 24h mover, volume floor.
      Runs BEFORE stage 2 so no evidence call is spent on a dead name.
  STAGE 2 EVIDENCE  — per admitted symbol: hour-windowed, engagement-
      tiered post harvest. Verbatim rows only.
  COUNT (this module) — breadth (distinct handles, new handles vs 7d
      history), loudness (which engagement tiers returned anything),
      authenticity (duplicate text, reply share, burst gaps), from the
      rows themselves. Breadth and loudness are NEVER collapsed into one
      "hype score": the evidence says they point opposite ways.
  LABEL  — +4h/+12h/+24h/+72h raw AND BTC-excess, plus MFE/MAE inside
      24h (a +20% row that first drew -40% is not a tradable signal).
  LEARN  — feature scorecard + the eight PRE-REGISTERED hypotheses
      (H1..H8). Pre-registered so the split cannot be chosen after
      seeing the answer.
  GATE   — nothing here trades. Ever, until a pattern clears the same
      bar as every other signal (n>=12, >=4x fees, both halves, payoff)
      AND the owner says so.

Power note, stated up front: the filter admits ~3.5 candidates/day, so
two weeks is ~50 rows and roughly half that in independent episodes.
That supports coarse binary splits of >=5pp only — H1/H4/H5/H8 get a
directional read; H2/H3/H6/H7 need 4-8 weeks. No capital is gated on
anything under 30 independent episodes.

Honest framing: the peer-reviewed record says X chatter mostly MIRRORS
price, the instrument itself broke (X API 2023, ~80% bot activity,
$TICKER suppression since Dec 2025), and influencer mentions are
NEGATIVE from day +1. This module exists to test the owner's thesis on
our own data and let the scorecard — not anyone's belief — decide.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone

import config

BASE = "https://api.x.ai/v1"
MODEL = "grok-4.5"
LOG = config.DATA / "social_radar_log.jsonl"
CARD = config.DATA / "social_radar_card.json"
STATE = config.DATA / "social_radar_state.json"
REPORT = config.DATA.parent / "reports" / "social_radar.md"
DATA_HOSTS = ("https://data-api.binance.vision", "https://api.binance.com")

SCAN_INTERVAL_H = 2.0
MONTHLY_CAP = 300           # discovery calls; evidence calls counted too
MAX_DISCOVERY = 12          # symbols Grok may name per scan
MAX_EVIDENCE = 5            # admitted symbols we spend evidence calls on
EVIDENCE_WINDOWS = 3        # 3 x 4h = last 12h
WINDOW_H = 4
TIERS = (("T0", ""), ("T1", "min_faves:10"),
         ("T2", "min_faves:100"), ("T3", "min_faves:1000"))
SNOWFLAKE_EPOCH = 1288834974657

# the owner's hard rule, enforced with Binance numbers
MAX_DAY_CHANGE = 0.05
TOP_MOVER_RANK_EXCLUDE = 50
MIN_QV_24H = 500_000.0

HORIZONS_H = (4, 12, 24, 72)
HIT_PCT = 0.03
ROLL_WINDOW = 120
NEW_HANDLE_LOOKBACK_D = 7


# ---------------------------------------------------------------- helpers
def _public(path: str, params: dict | None = None):
    qs = urllib.parse.urlencode(params or {})
    for host in DATA_HOSTS:
        try:
            return json.load(urllib.request.urlopen(
                f"{host}/api/v3{path}" + (f"?{qs}" if qs else ""),
                timeout=20))
        except Exception:
            continue
    return None


def snowflake_ms(post_id: str) -> int | None:
    """Exact post time from an X status id — the only trustworthy time
    channel (the study: never trust Grok's prose, trust the ids)."""
    try:
        return (int(str(post_id).strip()) >> 22) + SNOWFLAKE_EPOCH
    except Exception:
        return None


def spot_symbols() -> set[str]:
    """Base assets with a live USDT spot pair. The listing precondition:
    v1 spent 13.7% of its calls on coins that cannot be traded at all."""
    info = _public("/exchangeInfo") or {}
    return {s["baseAsset"] for s in info.get("symbols", [])
            if s.get("quoteAsset") == "USDT"
            and s.get("status") == "TRADING"}


def tickers() -> dict[str, dict]:
    d = _public("/ticker/24hr") or []
    return {t["symbol"][:-4]: t for t in d
            if str(t.get("symbol", "")).endswith("USDT")}


def top_movers(tk: dict[str, dict], n: int) -> set[str]:
    rows = []
    for base, t in tk.items():
        try:
            rows.append((float(t.get("priceChangePercent", 0) or 0), base))
        except Exception:
            pass
    rows.sort(reverse=True)
    return {b for _c, b in rows[:n]}


# ------------------------------------------------------------ stage 1
DISCOVERY_PROMPT = """You are a retrieval tool, not an analyst.

Search X for cryptocurrency coins that are getting NEW attention in the
last 12 hours while their price has NOT moved yet. I check prices myself
on Binance and discard anything already up — naming a coin that already
ran wastes a slot.

What qualifies as a lead:
  * posts from DIFFERENT accounts (not one account repeated, not a reply
    ring) discussing a SPECIFIC, DATED catalyst: exchange listing or
    exchange notice, mainnet/upgrade date, token generation or airdrop,
    unlock, product launch, partnership document, governance vote;
  * builder/dev/researcher accounts shipping or explaining something,
    on-chain sleuth observations with a transaction or wallet reference.
What does NOT qualify, and must never be listed:
  * coins already pumping, trending lists, "top gainer" posts;
  * paid promotion, giveaway/airdrop farming, "100x"/"next SOL" calls,
    call groups, engagement-farming replies;
  * large influencer/KOL enthusiasm with no dated catalyst.

CRITICAL OUTPUT RULES — you have no aggregation tool and can see at most
a handful of posts per search, so:
  * NEVER state a count, percentage, score, velocity or "mentions" number
  * NEVER use adjectives like "surging", "exploding", "massive"
  * Report only what you can copy verbatim from a post you actually
    retrieved: the coin symbol, the catalyst, its date, and post URLs.

Return ONLY this JSON, no prose:
{
 "coins": [
  {"symbol": "COIN",
   "catalyst_type": "listing"|"unlock"|"tge_airdrop"|"mainnet_upgrade"|"partnership"|"buyback_burn"|"governance"|"etf"|"celebrity"|"exploit"|"narrative"|"none",
   "catalyst_text": "under 15 words, copied or closely paraphrased",
   "catalyst_date_utc": "YYYY-MM-DD or null",
   "catalyst_already_occurred": true|false,
   "evidence_urls": ["https://x.com/handle/status/123..."],
   "handles_seen": ["@handle1", "@handle2"]}
 ]
}
At most %d coins. An empty list is a perfectly good answer — never fill
the quota.""" % MAX_DISCOVERY


def EVIDENCE_PROMPT(symbol: str, windows: list[tuple[str, str]]) -> str:
    win = "\n".join(f"  W{i}: since:{a}_UTC until:{b}_UTC"
                    for i, (a, b) in enumerate(windows))
    tiers = "\n".join(f"  {name}: {op or '(no operator)'}"
                      for name, op in TIERS)
    return f"""You are a retrieval tool, not an analyst. Return rows only.

For the symbol {symbol}, run x_keyword_search separately for EACH
(window x tier) pair below. Mode: "Latest". Do not merge windows, do not
infer, do not fill gaps, do not count anything.

QUERY TEMPLATE:
  (${symbol} OR "{symbol}") since:<START>_UTC until:<END>_UTC <TIER_OP> -filter:retweets

WINDOWS:
{win}

TIERS (run all four per window):
{tiers}

For every post retrieved emit exactly one row, fields copied VERBATIM.
If a window+tier returns nothing emit one row with status "empty" and
null post fields. If it returns the full 10 emit status "saturated" on
each row — never guess what was beyond the cap.

Return ONLY:
{{"rows": [{{"window": "W0", "tier": "T0", "status": "posts"|"empty"|"saturated",
 "post_id": "string or null", "post_url": "string or null",
 "handle": "@handle or null", "text": "verbatim post text or null",
 "is_reply": true|false, "has_link": true|false}}]}}"""


def _grok(prompt: str, timeout: int = 300) -> str:
    key = os.environ.get("XAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("XAI_API_KEY missing")
    req = urllib.request.Request(
        BASE + "/responses",
        data=json.dumps({"model": MODEL,
                         "input": [{"role": "user", "content": prompt}],
                         "tools": [{"type": "x_search"}]}).encode(),
        headers={"Authorization": f"Bearer {key}",
                 "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = json.load(r)
    if isinstance(data.get("output_text"), str) and data["output_text"]:
        return data["output_text"]
    parts = []
    for item in data.get("output", []):
        for c in item.get("content", []) or []:
            if isinstance(c, dict) and c.get("text"):
                parts.append(c["text"])
    return "\n".join(parts)


def _json_block(raw: str) -> dict:
    m = re.search(r"\{.*\}", raw or "", re.S)
    if not m:
        return {}
    try:
        return json.loads(m.group(0))
    except Exception:
        return {}


def parse_discovery(raw: str) -> list[dict]:
    out = []
    for c in (_json_block(raw).get("coins") or []):
        if not isinstance(c, dict):
            continue
        sym = re.sub(r"[-/]?(USDT|USDC|USD)$", "",
                     str(c.get("symbol", "")).upper().lstrip("$").strip())
        if not sym or not sym.isalnum():
            continue
        out.append({
            "symbol": sym,
            "catalyst_type": str(c.get("catalyst_type") or "none").lower(),
            "catalyst_text": str(c.get("catalyst_text") or "")[:120],
            "catalyst_date_utc": c.get("catalyst_date_utc") or None,
            "catalyst_already_occurred": bool(
                c.get("catalyst_already_occurred", False)),
            "evidence_urls": [str(u) for u in
                              (c.get("evidence_urls") or [])][:10],
            "handles_seen": [str(h).lower() for h in
                             (c.get("handles_seen") or [])][:10],
        })
    return out


def parse_evidence(raw: str) -> list[dict]:
    out = []
    for r in (_json_block(raw).get("rows") or []):
        if not isinstance(r, dict):
            continue
        out.append({
            "window": str(r.get("window") or ""),
            "tier": str(r.get("tier") or ""),
            "status": str(r.get("status") or "posts"),
            "post_id": (str(r.get("post_id")) if r.get("post_id")
                        else None),
            "post_url": r.get("post_url"),
            "handle": (str(r.get("handle")).lower().strip()
                       if r.get("handle") else None),
            "text": (str(r.get("text"))[:400] if r.get("text") else None),
            "is_reply": bool(r.get("is_reply", False)),
            "has_link": bool(r.get("has_link", False)),
        })
    return out


# ------------------------------------------------------------ counting
def count_features(rows: list[dict], prior_handles: set[str]) -> dict:
    """THE COUNTER. Everything here is computed from retrieved rows, never
    taken from Grok's prose. Breadth and loudness stay separate."""
    posts = [r for r in rows if r.get("post_id") and r.get("handle")]
    seen_ids, uniq = set(), []
    for r in posts:                       # dedupe on status id
        if r["post_id"] in seen_ids:
            continue
        seen_ids.add(r["post_id"])
        uniq.append(r)
    handles = {r["handle"] for r in uniq}
    times = sorted(t for t in (snowflake_ms(r["post_id"]) for r in uniq)
                   if t)
    gaps = [(b - a) / 1000.0 for a, b in zip(times, times[1:])]
    texts = [(r.get("text") or "").strip().lower()[:120] for r in uniq]
    dupes = len(texts) - len(set(t for t in texts if t))
    tier_rows: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        tier_rows[r.get("tier") or "?"].append(r)

    def tier_state(t: str) -> str:
        rs = tier_rows.get(t) or []
        if not rs or all(r.get("status") == "empty" for r in rs):
            return "empty"
        if any(r.get("status") == "saturated" for r in rs):
            return "saturated"
        return str(len([r for r in rs if r.get("post_id")]))

    new_handles = handles - prior_handles
    return {
        # breadth (hypothesised POSITIVE)
        "n_posts": len(uniq),
        "distinct_handles": len(handles),
        "handles": sorted(handles)[:20],
        "new_handles_ratio": round(len(new_handles) / len(handles), 3)
        if handles else None,
        "tier_state": {t: tier_state(t) for t, _op in TIERS},
        # loudness (hypothesised NEGATIVE) — tiers are the only honest
        # reach proxy: per-post metrics need a per-URL query we do not buy
        "loud_t2_hit": tier_state("T2") not in ("empty",),
        "loud_t3_hit": tier_state("T3") not in ("empty",),
        # authenticity
        "reply_share": round(sum(1 for r in uniq if r.get("is_reply"))
                             / len(uniq), 3) if uniq else None,
        "duplicate_text_ratio": round(dupes / len(uniq), 3) if uniq else None,
        "min_inter_post_gap_sec": round(min(gaps), 1) if gaps else None,
        "link_share": round(sum(1 for r in uniq if r.get("has_link"))
                            / len(uniq), 3) if uniq else None,
        "evidence_post_ids": [r["post_id"] for r in uniq][:20],
    }


def admit(symbol: str, tk: dict[str, dict], movers: set[str],
          listed: set[str]) -> tuple[bool, str]:
    """The owner's hard rule, decided by Binance numbers — never by Grok."""
    if symbol not in listed:
        return False, "no Binance USDT spot pair"
    t = tk.get(symbol)
    if not t:
        return False, "no ticker"
    try:
        chg = float(t.get("priceChangePercent", 0) or 0) / 100.0
        qv = float(t.get("quoteVolume", 0) or 0)
    except Exception:
        return False, "ticker unreadable"
    if chg > MAX_DAY_CHANGE:
        return False, f"already up {chg:+.1%} on the day"
    if symbol in movers:
        return False, "top-50 24h mover = already up"
    if qv < MIN_QV_24H:
        return False, f"24h volume ${qv:,.0f} too thin"
    return True, "admitted"


# ------------------------------------------------------------- labelling
def _closes(symbol: str, start_ms: int, hours: int) -> list[list]:
    return _public("/klines", {"symbol": f"{symbol}USDT", "interval": "1h",
                               "startTime": int(start_ms),
                               "limit": min(500, hours + 5)}) or []


def resolve(rows: list[dict], now: datetime) -> bool:
    """Raw and BTC-EXCESS returns at every horizon, plus MFE/MAE inside
    24h. Raw and excess disagreed by ~9pp at 72h in our own data, so both
    are recorded and the scorecard reads excess."""
    now_ms = now.timestamp() * 1000
    due = [r for r in rows
           if r.get("price") and r.get("ts_ms")
           and any(r.get(f"ret_{h}h") is None
                   and now_ms - r["ts_ms"] >= h * 3.6e6 for h in HORIZONS_H)]
    if not due:
        return False
    changed = False
    btc_cache: dict[int, list] = {}
    for r in due:
        k = _closes(r["symbol"], r["ts_ms"], max(HORIZONS_H))
        if not k:
            continue
        start = r["ts_ms"]
        bkey = int(start // 3.6e6)
        if bkey not in btc_cache:
            btc_cache[bkey] = _public(
                "/klines", {"symbol": "BTCUSDT", "interval": "1h",
                            "startTime": int(start),
                            "limit": max(HORIZONS_H) + 5}) or []
        bk = btc_cache[bkey]
        for h in HORIZONS_H:
            if r.get(f"ret_{h}h") is not None:
                continue
            if now_ms - start < h * 3.6e6:
                continue
            seg = [row for row in k if float(row[6]) <= start + h * 3.6e6]
            if not seg:
                continue
            ret = float(seg[-1][4]) / r["price"] - 1.0
            r[f"ret_{h}h"] = round(ret, 5)
            bseg = [row for row in bk
                    if float(row[6]) <= start + h * 3.6e6]
            if bseg and float(bseg[0][1]) > 0:
                bret = float(bseg[-1][4]) / float(bseg[0][1]) - 1.0
                r[f"excess_{h}h"] = round(ret - bret, 5)
            changed = True
        seg24 = [row for row in k if float(row[6]) <= start + 24 * 3.6e6]
        if seg24 and r.get("mfe_24h") is None \
                and now_ms - start >= 24 * 3.6e6:
            hi = max(float(x[2]) for x in seg24)
            lo = min(float(x[3]) for x in seg24)
            r["mfe_24h"] = round(hi / r["price"] - 1.0, 5)
            r["mae_24h"] = round(lo / r["price"] - 1.0, 5)
            best = max(seg24, key=lambda x: float(x[2]))
            r["time_to_mfe_min"] = int((float(best[0]) - start) / 60000)
            changed = True
    return changed


# -------------------------------------------------------------- learning
def _stats(vals: list[float]) -> dict:
    n = len(vals)
    s = sorted(vals)
    return {"n": n,
            "hit": round(sum(1 for x in vals if x >= HIT_PCT) / n, 3),
            "mean": round(sum(vals) / n, 5),
            "median": round(s[n // 2], 5)}


def hypotheses(live: list[dict]) -> dict:
    """The eight PRE-REGISTERED splits (spec §5.6). Registered before the
    data exists so the split cannot be chosen after seeing the answer.
    Scored on 24h BTC-excess unless the hypothesis names another horizon."""
    def ex(r, h=24):
        return r.get(f"excess_{h}h")

    def split(name, pred, horizon=24, note=""):
        a = [ex(r, horizon) for r in live
             if pred(r) is True and ex(r, horizon) is not None]
        b = [ex(r, horizon) for r in live
             if pred(r) is False and ex(r, horizon) is not None]
        out = {"note": note, "horizon_h": horizon,
               "group_true": _stats(a) if a else None,
               "group_false": _stats(b) if b else None}
        if a and b:
            out["edge_pp"] = round((sum(a) / len(a) - sum(b) / len(b))
                                   * 100, 2)
        return {name: out}

    def band(r):
        p = r.get("prior_24h_ret")
        if p is None:
            return None
        return True if -0.02 <= p <= 0.05 else (False if p > 0.10 else None)

    def breadth_vs_loud(r):
        d, loud = r.get("distinct_handles"), r.get("loud_t3_hit")
        if d is None:
            return None
        if d >= 8 and not loud:
            return True
        if d < 8 and loud:
            return False
        return None

    h = {}
    h.update(split("H1_quiet_entry_beats_hot", band,
                   note="prior24h in [-2%,+5%] vs >+10%"))
    h.update(split("H2_breadth_beats_loudness", breadth_vs_loud,
                   note=">=8 distinct handles & no T3 vs narrow+loud"))
    h.update(split("H3_official_chatter_worthless",
                   lambda r: (r.get("link_share") or 0) > 0.6
                   if r.get("link_share") is not None else None,
                   note="link-heavy (announcement relay) vs organic"))
    h.update(split("H4_occurred_catalyst_fades",
                   lambda r: bool(r.get("catalyst_already_occurred"))
                   if r.get("catalyst_type") not in (None, "none") else None,
                   horizon=72, note="occurred vs pending, 72h"))
    h.update(split("H5_volatility_gate",
                   lambda r: (r.get("btc_vol_24h") or 0) >= 0.02
                   if r.get("btc_vol_24h") is not None else None,
                   note="BTC 24h realized vol high vs low"))
    h.update(split("H6_exchange_surface_words_exhaust",
                   lambda r: any(w in (r.get("catalyst_text") or "").lower()
                                 for w in ("binance", "volume", "trending",
                                           "mover", "coingecko"))
                   if r.get("catalyst_text") else None,
                   note="scanner/exchange-surface wording vs organic"))
    h.update(split("H7_extreme_velocity_contrarian",
                   lambda r: (r.get("new_handles_ratio") or 0) >= 0.8
                   if r.get("new_handles_ratio") is not None else None,
                   horizon=72, note="all-new handles vs familiar, 72h"))
    h.update(split("H8_novelty_pays",
                   lambda r: bool(r.get("first_seen_ever")),
                   note="first ever appearance vs repeat"))
    return h


def scorecard(rows: list[dict]) -> dict:
    live = [r for r in rows if r.get("excess_24h") is not None][-ROLL_WINDOW:]
    feats: dict[str, dict[str, list[float]]] = {
        "catalyst": defaultdict(list), "tier_T3": defaultdict(list),
        "handle": defaultdict(list), "all": defaultdict(list)}
    for r in live:
        e = r["excess_24h"]
        feats["all"]["all"].append(e)
        feats["catalyst"][r.get("catalyst_type") or "none"].append(e)
        feats["tier_T3"][str(bool(r.get("loud_t3_hit")))].append(e)
        for hnd in (r.get("handles") or [])[:10]:
            feats["handle"][hnd].append(e)
    card = {
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "spec": "x_chatter_precursors_2026-08-23",
        "n_rows_total": len(rows), "n_scored_excess_24h": len(live),
        "objective": "BTC-excess 24h", "hit_threshold": HIT_PCT,
        "features": {k: {kk: _stats(v) for kk, v in d.items()
                         if len(v) >= 3} for k, d in feats.items()},
        "hypotheses": hypotheses(live),
    }
    ranked = [(st["mean"], kind, f, st)
              for kind in ("catalyst", "handle")
              for f, st in card["features"].get(kind, {}).items()
              if st["n"] >= 5]
    ranked.sort(reverse=True)
    card["leaders"] = [{"kind": k, "feature": f, **st}
                       for _m, k, f, st in ranked[:12]]
    card["laggards"] = [{"kind": k, "feature": f, **st}
                        for _m, k, f, st in ranked[-8:]][::-1]
    return card


def render(card: dict, latest: list[dict], rejected: list[tuple]) -> None:
    L = ["# Social radar — which X chatter precedes rises (learning)", "",
         f"updated {card['updated']} · rows {card['n_rows_total']} · "
         f"scored@24h-excess {card['n_scored_excess_24h']} · objective "
         f"**{card['objective']}**", "",
         "_Grok harvests posts; this module counts. Observation only — "
         "nothing trades until a pattern clears the gate (n>=12, 4x fees, "
         "both halves, payoff) **and** the owner approves. Power: ~3.5 "
         "candidates/day, so only large (>=5pp) effects are readable in "
         "two weeks._", ""]
    a = card["features"].get("all", {}).get("all")
    if a:
        L += [f"**All admitted rows**: n {a['n']} · hit {a['hit']:.0%} · "
              f"mean {a['mean']:+.2%} · median {a['median']:+.2%}", ""]
    L += ["## Pre-registered hypotheses", "",
          "| # | split | n(true/false) | edge (pp) |", "|---|---|---|---|"]
    for name, h in (card.get("hypotheses") or {}).items():
        gt, gf = h.get("group_true"), h.get("group_false")
        L.append(f"| {name} | {h.get('note','')} | "
                 f"{gt['n'] if gt else 0}/{gf['n'] if gf else 0} | "
                 f"{h.get('edge_pp', '—')} |")
    L.append("")
    if card.get("leaders"):
        L += ["## Leading features (24h BTC-excess, n>=5)", "",
              "| kind | feature | n | hit | mean | median |",
              "|---|---|---|---|---|---|"]
        for x in card["leaders"]:
            L.append(f"| {x['kind']} | {x['feature']} | {x['n']} | "
                     f"{x['hit']:.0%} | {x['mean']:+.2%} | "
                     f"{x['median']:+.2%} |")
        L.append("")
    if latest:
        L += ["## Latest admitted candidates", "",
              "| coin | prior 24h | handles | new% | T3 loud | catalyst | when |",
              "|---|---|---|---|---|---|---|"]
        for r in latest:
            L.append(f"| {r['symbol']} | {(r.get('prior_24h_ret') or 0):+.1%} "
                     f"| {r.get('distinct_handles')} | "
                     f"{(r.get('new_handles_ratio') or 0):.0%} | "
                     f"{'yes' if r.get('loud_t3_hit') else 'no'} | "
                     f"{r.get('catalyst_type')} | "
                     f"{r.get('catalyst_date_utc') or '—'} |")
        L.append("")
    if rejected:
        L += ["## Rejected this scan (the filter doing its job)", "",
              ", ".join(f"{s} ({w})" for s, w in rejected[:12]), ""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(L), encoding="utf-8", newline="\n")


# ------------------------------------------------------------------ run
def _load_rows() -> list[dict]:
    if not LOG.exists():
        return []
    out = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                out.append(json.loads(line))
            except Exception:
                pass
    return out


def _write_rows(rows: list[dict]) -> None:
    LOG.write_text("\n".join(json.dumps(r, ensure_ascii=False)
                             for r in rows) + ("\n" if rows else ""),
                   encoding="utf-8", newline="\n")


def _btc_vol_24h() -> float | None:
    k = _public("/klines", {"symbol": "BTCUSDT", "interval": "1h",
                            "limit": 25}) or []
    try:
        rets = [float(b[4]) / float(a[4]) - 1 for a, b in zip(k, k[1:])]
        if len(rets) < 12:
            return None
        m = sum(rets) / len(rets)
        var = sum((x - m) ** 2 for x in rets) / len(rets)
        return round(var ** 0.5 * (24 ** 0.5), 5)
    except Exception:
        return None


def run() -> None:
    now = datetime.now(timezone.utc)
    st = {}
    if STATE.exists():
        try:
            st = json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            st = {}
    rows = _load_rows()

    if resolve(rows, now):          # LABEL first: cheap, no Grok
        _write_rows(rows)

    last = st.get("last_scan_utc")
    due = True
    if last:
        try:
            due = (now - datetime.fromisoformat(last)).total_seconds() \
                >= SCAN_INTERVAL_H * 3600
        except Exception:
            due = True
    month = now.strftime("%Y-%m")
    used = int((st.get("month_calls") or {}).get(month, 0))
    latest: list[dict] = []
    rejected: list[tuple] = []

    if due and used < MONTHLY_CAP and os.environ.get("XAI_API_KEY", "").strip():
        calls = 0
        try:
            raw = _grok(DISCOVERY_PROMPT)
            calls += 1
            found = parse_discovery(raw)
            listed, tk = spot_symbols(), tickers()
            movers = top_movers(tk, TOP_MOVER_RANK_EXCLUDE)
            admitted = []
            for c in found:
                ok, why = admit(c["symbol"], tk, movers, listed)
                (admitted if ok else rejected).append(
                    c if ok else (c["symbol"], why))
            print(f"[radar] discovery named {len(found)}; admitted "
                  f"{len(admitted)}, rejected {len(rejected)}")

            seen_before: dict[str, set] = defaultdict(set)
            cutoff = (now - timedelta(days=NEW_HANDLE_LOOKBACK_D)).timestamp() * 1000
            hist_syms = set()
            for r in rows:
                hist_syms.add(r.get("symbol"))
                if (r.get("ts_ms") or 0) >= cutoff:
                    for hnd in r.get("handles") or []:
                        seen_before[r["symbol"]].add(hnd)

            windows = []
            for i in range(EVIDENCE_WINDOWS):
                b = now - timedelta(hours=WINDOW_H * i)
                a = b - timedelta(hours=WINDOW_H)
                windows.append((a.strftime("%Y-%m-%d_%H:%M:%S"),
                                b.strftime("%Y-%m-%d_%H:%M:%S")))
            btc_vol = _btc_vol_24h()

            for c in admitted[:MAX_EVIDENCE]:
                sym = c["symbol"]
                feats = {}
                try:
                    ev_raw = _grok(EVIDENCE_PROMPT(sym, windows), timeout=300)
                    calls += 1
                    feats = count_features(parse_evidence(ev_raw),
                                           seen_before.get(sym, set()))
                except Exception as e:
                    print(f"[radar] evidence {sym} failed: {e}")
                t = tk[sym]
                k24 = _public("/klines", {"symbol": f"{sym}USDT",
                                          "interval": "1h", "limit": 73}) or []
                def back(n):
                    try:
                        return round(float(k24[-1][4]) / float(k24[-n][4]) - 1, 5)
                    except Exception:
                        return None
                row = {**c, **feats,
                       "ts": now.isoformat(timespec="seconds"),
                       "ts_ms": int(now.timestamp() * 1000),
                       "price": float(t.get("lastPrice") or 0),
                       "prior_4h_ret": back(5), "prior_24h_ret": back(25),
                       "prior_72h_ret": back(73),
                       "qv_24h": float(t.get("quoteVolume", 0) or 0),
                       "btc_vol_24h": btc_vol,
                       "first_seen_ever": sym not in hist_syms,
                       "grok_call_count": calls,
                       "spec": "radar_v2"}
                rows.append(row)
                latest.append(row)
            _write_rows(rows)
            st["last_scan_utc"] = now.isoformat(timespec="seconds")
            st.setdefault("month_calls", {})[month] = used + calls
        except Exception as e:
            print(f"[radar] scan failed: {e}")
    else:
        print("[radar] scan not due / capped / no key — labels only")

    card = scorecard(rows)
    CARD.write_text(json.dumps(card, indent=1, ensure_ascii=False),
                    encoding="utf-8", newline="\n")
    render(card, latest, rejected)
    STATE.write_text(json.dumps(st, indent=1), encoding="utf-8",
                     newline="\n")
    print(f"[radar] rows {len(rows)} · scored {card['n_scored_excess_24h']}")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:      # observation only: never take a cycle down
        print(f"[radar] non-fatal: {e}")
        sys.exit(0)
