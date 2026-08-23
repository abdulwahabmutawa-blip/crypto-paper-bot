"""The Scout — reads every Binance USDT pair, finds opportunity, learns.

Bot #14, and it CANNOT TRADE: it holds no keys, imports no broker, and
touches only public GET endpoints. It writes a ranked opinion to
data/scout_signals.json; the lottery book reads that file and decides. A
scout that cannot place an order also cannot lose money by being wrong,
which is what lets it be aggressive.

Why it exists: the Watcher (Grok) is qualitative and arrives every 2h at
best. A pump is often over inside that window. Price and volume are free,
instant, and cover all ~670 pairs, so the Scout runs every cycle (~10 min)
and is the fast half of perception; the Watcher stays the slow, contextual
half that knows *why* something is moving.

EXACTLY WHAT THE SCOUT IS FOR
----------------------------
Answering one question every 10 minutes: "of all ~670 tradeable USDT pairs,
which ones are moving abnormally RIGHT NOW, and in which of three ways?"
It ranks them, says why in plain language, and stops. It does not size,
time, or place anything.

Abnormal means measured against the coin's OWN recent behaviour, never
against other coins: a 5% hour is nothing for a memecoin and an earthquake
for BTC, so every feature is a ratio to that symbol's own trailing history.

THREE SIGNALS, in the order a move actually unfolds:

  IGNITION  — volume detonating (>=3x the prior 4h) while price has barely
              moved (<4% in the hour). Somebody is accumulating and the
              chart has not caught up. This is the EARLIEST and most
              valuable catch: entry before the crowd. It is also the most
              likely to be a false alarm — volume spikes often lead
              nowhere, which is exactly why the learning loop below tracks
              its hit rate separately.

  BREAKOUT  — volume surging AND price already accelerating into the top of
              its 24h range. The move is confirmed and underway. Later
              entry, higher conviction, less upside left.

  REVERSION — dumped hard from its 24h high on capitulation volume, now
              printing consecutive green candles. Riding the correction of
              an overshoot, not catching a knife: a coin down more than 45%
              on the day is refused outright, because at that depth the
              cause is usually an exploit, an unlock, or a delisting, and
              none of those bounce on a schedule.

  HEAT      — (2026-08-16, owner request) social_heat.py's cross-source
              agreement: the same coin trending on 3+ INDEPENDENT surfaces
              at once (CoinGecko, Reddit, StockTwits, Binance movers, the
              Watcher's X read, CryptoPanic). One surface is noise and any
              one is gameable; simultaneous agreement is the crowd actually
              arriving. Price/volume features are not required here — the
              claim is social, and the gate decides if the claim pays.

  REVIVAL   — (2026-08-16, from the explosion study: every Binance coin
              that ran +50% in the prior month, n=109) the measured profile
              of a move's DAY ONE, not its peak: an old coin (>6mo listed —
              69/109 exploders were >1y) that FELL last week (58/73 were
              down, median -12%), trading QUIETLY (median $0.3M/day;
              77/88 sat below this scout's own $2M floor, which is why
              revival scans its own lighter tier), whose volume is
              ARRIVING TODAY (3x+ its own week) while the price has just
              turned but not yet run (<20% off its 30d low; the study's
              peak-buyers ate a median -29%, its trough-buyers kept +29%).
              On WAVE DAYS — 35 of 109 troughs were the SAME day (07-29),
              breadth is the tide — revival scores get louder.

WHAT IT DELIBERATELY DOES NOT DO: predict. It has no view on where anything
is going. It reports what is measurably unusual this minute and lets the
book's own stops decide how long to stay.

LEARNING (the honest kind, not a black box): every candidate the Scout
flags is logged WITH ITS FEATURES and its price. On later cycles the Scout
looks up what actually happened 1h/4h/24h afterwards and records the
forward return. Rolling per-signal stats (CURRENT ruleset only) accumulate
in data/scout_scorecard.json and feed two mechanisms:

  * WEIGHTS — each signal's score is multiplied by its own measured edge;
    a signal that keeps being wrong gets quieter, one that works louder.
  * THE GATE — every candidate carries an `actionable` flag the real-money
    book obeys. A signal type must EARN it: enough resolved samples under
    the current rules, beating fees on average, hit rate above the floor.
    Until then its candidates are logged and displayed but not traded.
    Learning speed is unaffected — outcomes resolve from the log, not
    from fills, so a benched signal keeps building its record for free.

The scorecard starts empty and every signal starts at weight 1.0. Until
roughly 30 resolved samples exist per signal the weights barely move: small
samples are noise, and this project has been burned by treating them as
evidence before.

RULESET v2 (2026-08-16) came out of the first log autopsy (48 resolved
picks): 9 were pegged/tracker assets that cannot move (pure fee bleed, and
two of them nearly became real all-in buys); the two chased breakouts were
the book's worst scout losses (−18.8%, −5.6% at 4h); one falling coin was
re-flagged five times in 70 minutes; reversion went 0-for-7 at 4h. Each
mistake is now a named rule below. Bumping RULESET retires the old rows
from the card: results earned under different rules are history, not
evidence — in either direction.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone

import binance_data
import config


def _atomic_write(path, text: str) -> None:
    """Write-then-rename so a reader never sees a truncated file and a
    mid-write death never destroys the old one (audit 08-15: the signals
    file is read by a real-money bot every cycle, and the log rewrite held
    the entire learning history in a truncate-then-write window)."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)

SIGNALS = config.DATA / "scout_signals.json"
LOG = config.DATA / "scout_log.jsonl"
SCORECARD = config.DATA / "scout_scorecard.json"
SNAPSHOT = config.DATA / "scout_snapshot.json"
HEAT_FILE = config.DATA / "social_heat.json"
BREADTH_FILE = config.DATA / "breadth.json"

SIGNAL_TYPES = ("ignition", "breakout", "reversion", "heat", "revival")

# Thresholds below are tagged [EVIDENCE] where a published study supports the
# number, and [JUDGEMENT] where it is a defensible guess. Research pass
# 2026-08-15 replaced several numbers that were folklore — notably a 2x volume
# trigger, which NO paper uses standalone.

# ---- universe filters -------------------------------------------------------
MIN_24H_QUOTE_VOL = 2_000_000.0   # [EVIDENCE-anchored] below this an $11 exit
                                  # is not reliably clean
MAX_SPREAD_BPS = 20.0             # [EVIDENCE-anchored] round-trip taker fee is
                                  # already 20bps; a 20bps spread doubles the
                                  # cost floor. This single filter decides
                                  # whether profit is arithmetically possible.
MIN_24H_TRADES = 5_000            # [JUDGEMENT] abandonment proxy — 53% of
                                  # tokens issued 2021-25 are no longer
                                  # actively traded
SHORTLIST = 90                    # rate limits are NOT the binding constraint:
                                  # 90 kline calls = 180 weight, ~3% of the
                                  # 6000/min cap
TOP_N = 8
MIN_RANGE_24H = 0.02              # [EVIDENCE — log autopsy 08-16] 9 of the
                                  # first 48 picks (XAUT, QQQB, U…) were
                                  # pegged or tracker assets: every one
                                  # resolved within ±0.06%, pure fee bleed.
                                  # They pass every volume filter — a peg's
                                  # rebalancing flow looks exactly like an
                                  # ignition — but a coin whose entire 24h
                                  # range is under 2% cannot pay the 0.2%
                                  # round trip inside the book's ≤8h hold.
                                  # The floor catches them without needing
                                  # to know their names.

# ---- ignition (earliest: volume detonating before price moves) --------------
IGN_MIN_VOL_SURGE = 5.0     # [EVIDENCE] arXiv 2503.08692 published +400%
                            # (=5x) volume in a rule scoring precision 0.84 /
                            # recall 0.62. La Morgia measured ~9x pre-pump.
IGN_MAX_1H = 0.04           # [JUDGEMENT] price has NOT gone yet — the point
IGN_MIN_1H = -0.02
IGN_MIN_TRADE_SURGE = 4.0   # [EVIDENCE-led] trade ARRIVAL outranks notional:
                            # La Morgia RF Gini has StdTrades 0.202 vs
                            # AvgVolumes 0.097, so trade count is primary and
                            # notional is confirmation
IGN_MIN_TAKER_BUY = 0.60    # [EVIDENCE-led] taker-buy share is the closest
                            # public-spot proxy to "rush orders", the single
                            # highest-importance feature family in that model
IGN_MIN_BURST_USD = 50_000  # [JUDGEMENT] absolute floor beside the ratio —
                            # 53.5% of pump targets traded <$10k beforehand,
                            # so a bare 5x ratio is arithmetically free there

# ---- breakout (confirmed: volume AND price moving) --------------------------
BRK_MIN_VOL_SURGE = 5.0     # [EVIDENCE] same published rule as ignition
BRK_MIN_TRADE_SURGE = 4.0   # [EVIDENCE-led]
BRK_MIN_TAKER_BUY = 0.60    # [EVIDENCE-led]
BRK_MIN_BURST_USD = 50_000  # [JUDGEMENT]
BRK_MIN_1H = 0.02           # [JUDGEMENT]
BRK_MIN_RANGE_POS = 0.80    # [JUDGEMENT]
BRK_MAX_1H = 0.08           # [EVIDENCE — log autopsy 08-16] the two chased
                            # entries (+18.5%/h → −18.8% by 4h; +8.8%/h →
                            # −5.6%) were the book's worst scout losses; the
                            # only breakout that worked entered at +4.2%/h.
                            # A candle this vertical is a blow-off top, not
                            # a breakout — the COW lesson, mechanized.
BRK_MAX_24H = 0.25          # [EVIDENCE-anchored] REDUSDT was already +27% on
                            # the day at entry; COW was +49% (the pick that
                            # created the Scout). The published pump anatomy
                            # says gains complete in minutes — a day that
                            # has already paid out is not "about to".

# ---- reversion (cross-sectional, per the published method) ------------------
REV_XS_PERCENTILE = 0.10    # [EVIDENCE] the papers sort the universe and take
                            # the bottom decile — a cross-sectional rank IS the
                            # published method; an absolute threshold is not
REV_MAX_24H = -0.12         # [JUDGEMENT] floor so a quiet day's bottom decile
                            # (only -2% deep) is not traded
REV_FLOOR_24H = -0.35       # [EVIDENCE-anchored] below this the cause is
                            # usually delisting (-25..-40%, no reversion) or an
                            # exploit (-80..-90%, permanent) — neither bounces
REV_MIN_BOUNCE_15M = 0.004
REV_MIN_GREEN = 2

# ---- market-wide veto -------------------------------------------------------
BTC_VETO_1H = -0.03         # [EVIDENCE-led] the reversal literature is
                            # cross-sectional, not directional: when BTC is
                            # dumping, a coin's fall is market beta, not an
                            # idiosyncratic overshoot to fade

# ---- learning ---------------------------------------------------------------
HORIZONS_H = (1, 4, 24)
MIN_SAMPLES_TO_TRUST = 30
WEIGHT_FLOOR, WEIGHT_CEIL = 0.5, 1.5
ROUND_TRIP = 0.002          # 10bps per side at Binance spot
RULESET = 3                 # bump when signal RULES change: rows from other
                            # rulesets stop feeding the card, so new rules
                            # are judged only on their own record — old
                            # failures can't damn them, old wins can't
                            # launder them. v3 (2026-08-16 evening, owner
                            # approved): 2y-study calibration — revival
                            # quiet-ceiling $1.5M->$4M, serial-exploder
                            # prior. Bumped while every v2 record was hours
                            # old, deliberately: resetting an empty ledger
                            # is free, resetting a week-old one is not.
ROLL_WINDOW = 30            # rolling resolved samples per signal/horizon:
                            # the card tracks what a signal IS, not what it
                            # once was, so a benched signal can earn its way
                            # back and a lucky streak decays
RESIGNAL_COOLDOWN_H = 3.0   # [EVIDENCE — log autopsy 08-16] BICO was flagged
                            # 5x in 70 min while falling, BCH 4x, U 5x. One
                            # event, five rows: pseudo-replication pollutes
                            # the very scorecard the weights and gate obey.
# THE GATE — what a signal type must show (current ruleset, rolling window)
# before the real-money book may act on its candidates:
MIN_ACT_SAMPLES = 12        # [JUDGEMENT] fewer is a coin-flip streak
MIN_ACT_HIT = 0.40
FEE_K = 4.0                 # REVAMP 08-23: mean must beat 4x the round trip
MIN_PAYOFF = 1.0            # avg win / avg loss unless hit >= 65%
# Each signal is judged on ITS OWN clock: benching a days-scale grind
# signal on 4h outcomes would test a marathoner over a sprint distance.
ACT_HORIZON_H = {"revival": 24}     # everything else defaults to 4

# ---- heat (cross-source social agreement, from social_heat.py) --------------
HEAT_MIN_SURFACES = 3       # [JUDGEMENT] 1 surface is noise, 2 is a maybe,
                            # 3 independent surfaces at once is the pattern
                            # worth logging — the gate decides if it pays
HEAT_FRESH_MIN = 45.0       # stale heat is yesterday's crowd

# ---- revival (explosion study 2026-08-16, n=109 +50% runs in 31 days) -------
# Every number below is read off that dataset, not guessed.
REV2_MIN_AGE_D = 181            # [EVIDENCE] 69/109 exploders were >1y listed;
                                # new listings behave differently (bStocks)
                                # and are a different trade
REV2_QV_FLOOR = 250_000         # [JUDGEMENT] a $40 all-in exit is <0.05% of
                                # $250k/day — exitable; the $2M main floor
                                # was calibrated for clean exits at size the
                                # book does not have, and it blinded the
                                # scout to 77/88 of the month's exploders
REV2_MAX_PRE_QV = 4_000_000     # [EVIDENCE] quiet before the run — 2y study
                                # (n=1,908): median pre-run $1.76M/day, 75%
                                # under $5M. The recent month's $0.3M was
                                # the extreme, not the norm; $4M covers the
                                # fat middle without admitting loud names.
REV2_MIN_WEEK_FALL = -0.08      # [EVIDENCE] 58/73 fell the week before the
                                # trough, median -11.8%
REV2_MIN_VOL_ARRIVAL = 3.0      # [EVIDENCE] day-1 volume arrival; peak days
                                # ran 25.8x, but day one is the catchable
                                # moment — 3x a quiet week is already loud
REV2_MAX_RUNUP_30D = 0.20       # [EVIDENCE] the money was made low: trough
                                # buyers kept +29% median, peak buyers ate
                                # -29%. Past +20% off the low is not day one.
REV2_TURN_MIN = 0.02            # turning today...
REV2_TURN_MAX = 0.15            # ...but not already gone
REV2_KLINE_BUDGET = 12          # bounded probes per cycle
SERIAL_FILE = config.DATA / "explosion_history.json"
SERIAL_MIN_N = 2                # [EVIDENCE — 2y study] 87% of exploders
                                # exploded 2+ times (RSR 13x, ZEC 11x; TUT's
                                # +1,990% was its NINTH). History is the
                                # strongest single prior the study found.
SERIAL_BOOST_PER = 0.04         # +4% score per prior event...
SERIAL_BOOST_CAP = 1.40         # ...capped at +40% (10 events)

# ---- breadth (the wave-day tide) --------------------------------------------
BREADTH_MIN_CHG = 0.10          # a coin counts as "moving" at +10% on the day
BREADTH_MIN_QV = 300_000        # with enough volume to be a real print
BREADTH_WAVE_RATIO = 2.0        # [EVIDENCE-anchored] 07-29 put 35 of 109
                                # troughs on ONE day — wave days exist and
                                # they are when revival profiles fire en
                                # masse. 2x the trailing week's median count
                                # of movers = the tide is in.
BREADTH_MIN_HISTORY = 12        # no wave calls until the baseline is real


def _pct(a: float, b: float) -> float:
    return (a / b - 1.0) if b else 0.0


def universe_ok(t: dict) -> bool:
    """Liquidity, cost-floor and can-it-even-move filters for one 24h ticker
    row. Everything here is decided from the ticker we already hold — zero
    extra API weight."""
    sym = t.get("symbol", "")
    if not binance_data.is_tradeable_pair(sym):
        return False
    if float(t.get("quoteVolume", 0) or 0) < MIN_24H_QUOTE_VOL:
        return False
    if float(t.get("count", 0) or 0) < MIN_24H_TRADES:
        return False
    try:
        high, low = float(t["highPrice"]), float(t["lowPrice"])
        # pegged/tracker assets (gold, index trackers, dead pegs) sail
        # through every volume filter and can never pay for the trade
        if low <= 0 or (high - low) / low < MIN_RANGE_24H:
            return False
        # SPREAD FILTER — the single filter that decides whether this
        # strategy is arithmetically capable of profit at all. Round-trip
        # taker fee is already 20bps; a 20bps spread doubles the cost floor
        # before any slippage. Free: bid/ask ride along in the same call.
        bid, ask = float(t["bidPrice"]), float(t["askPrice"])
        mid = (bid + ask) / 2.0
        if mid <= 0 or (ask - bid) / mid * 10_000 > MAX_SPREAD_BPS:
            return False
    except Exception:
        return False
    return True


def market_wide_surge(tickers: list[dict], now: datetime) -> dict[str, float]:
    """Volume-surge ratio for EVERY pair, at zero extra API cost.

    The shortlist cannot be ranked by price move alone: an IGNITION has by
    definition not moved yet, so a price-ranked shortlist would never see
    the one signal that catches a pump early. This closes that hole by
    diffing consecutive scans of the 24h ticker we already fetch.

    quoteVolume is a rolling 24h sum, so the delta between two scans is
    (traded since last scan) minus (what rolled off the back). Over a 10
    minute gap the roll-off is ~0.7% of the window and the approximation is
    fine for ranking. Compared against the coin's own average slice of the
    same length, so it is self-normalising across wildly different sizes.
    """
    prev = {}
    if SNAPSHOT.exists():
        try:
            prev = json.loads(SNAPSHOT.read_text())
        except Exception:
            prev = {}
    prev_rows = prev.get("rows") or {}
    prev_ts = prev.get("ts")
    gap_min = None
    if prev_ts:
        try:
            gap_min = (now - datetime.fromisoformat(prev_ts)).total_seconds() / 60.0
        except Exception:
            gap_min = None

    out = {}
    rows = {}
    for t in tickers:
        sym = t["symbol"]
        qv = float(t.get("quoteVolume", 0) or 0)
        cnt = float(t.get("count", 0) or 0)
        rows[sym] = [qv, cnt]
        p = prev_rows.get(sym)
        # need a sane gap: too short is noise, too long (a restart) is stale
        if p and gap_min and 3.0 <= gap_min <= 45.0 and qv > 0:
            traded = max(0.0, qv - float(p[0]))
            expected = qv * (gap_min / (24 * 60))     # this coin's own pace
            if expected > 0:
                out[sym] = traded / expected
    _atomic_write(SNAPSHOT, json.dumps(
        {"ts": now.isoformat(timespec="seconds"), "rows": rows}))
    return out


def features(sym: str, t: dict) -> dict | None:
    """Per-symbol features from 5m candles + the 24h ticker row."""
    rows = binance_data.klines(sym, "5m", 60)      # 5 hours of history
    s = binance_data.candle_series(rows)
    if len(s["close"]) < 40:
        return None
    close = s["close"]
    last = close[-1]            # live price: the forming bar's close IS spot

    # Binance returns the CURRENT, still-forming bar last. Measuring volume
    # on it compares a partial candle against complete ones and understates
    # every ratio, so all burst maths uses index -2, the last CLOSED bar.
    b = -2
    prior_q = s["quote"][-50:b]
    prior_t = s["trades"][-50:b]
    if len(prior_q) < 20:
        return None

    def _median(xs):
        xs = sorted(xs)
        n = len(xs)
        return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2.0

    # MEDIAN, not mean: a single historical spike in the baseline would
    # otherwise mask a genuine burst (and one quiet stretch would fake one).
    med_q = _median(prior_q)
    med_t = _median(prior_t)
    burst_quote = s["quote"][b]
    burst_taker = s["taker_buy"][b]
    taker_buy_frac = (burst_taker / burst_quote) if burst_quote > 0 else 0.0
    hour_quote, prior_quote = burst_quote, med_q
    hour_trades, prior_trades = s["trades"][b], med_t
    high24, low24 = float(t["highPrice"]), float(t["lowPrice"])
    rng = (high24 - low24) or 1e-12
    green = 0
    for c_now, c_prev in zip(reversed(close), reversed(close[:-1])):
        if c_now > c_prev:
            green += 1
        else:
            break
    return {
        "price": last,
        "chg_24h": float(t["priceChangePercent"]) / 100.0,
        "vol_surge": (hour_quote / prior_quote) if prior_quote > 0 else 0.0,
        "trade_surge": (hour_trades / prior_trades) if prior_trades > 0 else 0.0,
        "chg_15m": _pct(last, close[-4]),
        "chg_1h": _pct(last, close[-13]),
        "drawdown_24h": _pct(last, high24),
        "range_pos": (last - low24) / rng,
        "green_streak": green,
        "quote_vol_24h": float(t["quoteVolume"]),
        "taker_buy_frac": taker_buy_frac,
        "burst_usd": burst_quote,
    }


def score_ignition(f: dict) -> tuple[float, str] | None:
    """Volume detonating before the price has moved — the earliest catch.

    The trade-count requirement is the honest filter here: one whale
    printing a single huge order also spikes notional volume, but a genuine
    ignition is MANY participants arriving at once. Notional alone would
    happily flag an OTC block trade as a crowd."""
    if f["trade_surge"] < IGN_MIN_TRADE_SURGE:      # PRIMARY (trade arrival)
        return None
    if f["vol_surge"] < IGN_MIN_VOL_SURGE:          # confirmation
        return None
    if f["burst_usd"] < IGN_MIN_BURST_USD:
        return None
    if f["taker_buy_frac"] < IGN_MIN_TAKER_BUY:     # buyers lifting offers
        return None
    if not (IGN_MIN_1H <= f["chg_1h"] <= IGN_MAX_1H):
        return None
    # already at the top of the range means the move has happened — that is
    # a breakout, and it gets scored as one instead
    if f["range_pos"] > 0.90:
        return None
    score = (min(f["trade_surge"], 10.0) / 10.0) * 0.40 \
        + (min(f["vol_surge"], 10.0) / 10.0) * 0.25 \
        + min(f["taker_buy_frac"], 1.0) * 0.25 \
        + (1.0 - abs(f["chg_1h"]) / max(IGN_MAX_1H, 1e-9)) * 0.10
    why = (f"trades {f['trade_surge']:.1f}x and volume {f['vol_surge']:.1f}x "
           f"the prior 4h, {f['taker_buy_frac']:.0%} taker-buy, "
           f"${f['burst_usd']:,.0f} burst — while price has only moved "
           f"{f['chg_1h']:+.1%}")
    return score, why


def score_breakout(f: dict) -> tuple[float, str] | None:
    if f["trade_surge"] < BRK_MIN_TRADE_SURGE:
        return None
    if f["vol_surge"] < BRK_MIN_VOL_SURGE:
        return None
    if f["burst_usd"] < BRK_MIN_BURST_USD:
        return None
    if f["taker_buy_frac"] < BRK_MIN_TAKER_BUY:
        return None
    if f["chg_1h"] < BRK_MIN_1H:
        return None
    if f["range_pos"] < BRK_MIN_RANGE_POS:
        return None
    # anti-chase caps (log autopsy 08-16): a vertical hour is a blow-off and
    # a day that already paid is late — both funded someone else's exit
    if f["chg_1h"] > BRK_MAX_1H:
        return None
    if f["chg_24h"] > BRK_MAX_24H:
        return None
    score = (min(f["trade_surge"], 8.0) / 8.0) * 0.30 \
        + (min(f["vol_surge"], 8.0) / 8.0) * 0.25 \
        + min(f["chg_1h"] / BRK_MAX_1H, 1.0) * 0.25 \
        + min(f["taker_buy_frac"], 1.0) * 0.20
    why = (f"trades {f['trade_surge']:.1f}x, volume {f['vol_surge']:.1f}x, "
           f"{f['taker_buy_frac']:.0%} taker-buy, {f['chg_1h']:+.1%} in an "
           f"hour, at {f['range_pos']:.0%} of its 24h range")
    return score, why


def score_reversion(f: dict) -> tuple[float, str] | None:
    """Cross-sectional short-term reversal — the one signal here with real
    academic support (Zaremba et al., >3,600 coins; and a 200-coin
    replication). Two constraints come straight from that literature and are
    not negotiable knobs:

      * it is a BOTTOM-DECILE sort against the universe this scan, not an
        absolute percentage — `xs_rank` is supplied by the caller;
      * the effect is an ILLIQUIDITY premium and REVERSES SIGN in the largest
        coins, so a mega-cap that dumped is not a fade candidate.
    """
    if not f.get("xs_bottom_decile"):
        return None
    # free-fall is not a dip: delisting (-25..-40%, no reversion) and exploits
    # (-80..-90%, permanent) both live below this line
    if f["chg_24h"] < REV_FLOOR_24H:
        return None
    if f["chg_24h"] > REV_MAX_24H:
        return None
    if f["chg_15m"] < REV_MIN_BOUNCE_15M:
        return None
    if f["green_streak"] < REV_MIN_GREEN:
        return None
    # the reversal premium lives in the illiquid tail; the biggest names show
    # daily MOMENTUM instead, so fading them trades against the evidence
    if f.get("liq_rank_pct", 0.0) > 0.90:
        return None
    score = min(abs(f["chg_24h"]) / 0.35, 1.0) * 0.40 \
        + min(f["chg_15m"] / 0.03, 1.0) * 0.30 \
        + (1.0 - f.get("liq_rank_pct", 0.5)) * 0.30
    why = (f"down {f['chg_24h']:.0%} on the day (bottom decile of the "
           f"market), now {f['chg_15m']:+.1%} over 15m with "
           f"{f['green_streak']} green candles")
    return score, why


# ---- learning ---------------------------------------------------------------

def load_scorecard() -> dict:
    if SCORECARD.exists():
        try:
            return json.loads(SCORECARD.read_text())
        except Exception:
            pass
    return {"signals": {}, "updated": None}


def signal_weight(card: dict, signal: str) -> float:
    """Multiplier from this signal's OWN measured 4h hit rate. Stays at 1.0
    until enough resolved samples exist — a handful of wins is not evidence,
    which this project has learned the expensive way."""
    s = (card.get("signals") or {}).get(signal) or {}
    n = s.get("n_4h", 0)
    if n < MIN_SAMPLES_TO_TRUST:
        return 1.0
    hit = s.get("hit_rate_4h", 0.5)
    return max(WEIGHT_FLOOR, min(WEIGHT_CEIL, 0.5 + hit))


def signal_actionable(card: dict, signal: str) -> tuple[bool, str]:
    """The gate the real-money book obeys. Earned, never assumed: a signal
    type with no record under the CURRENT rules is on probation — its
    candidates are logged and shown but not traded. It arms itself by
    beating fees over a real sample and benches itself again if the rolling
    record decays. Weights fine-tune the ranking; this decides whether real
    money listens at all."""
    s = (card.get("signals") or {}).get(signal) or {}
    h = ACT_HORIZON_H.get(signal, 4)
    n = s.get(f"n_{h}h", 0)
    if n < MIN_ACT_SAMPLES:
        return False, (f"probation — {n}/{MIN_ACT_SAMPLES} resolved {h}h "
                       f"samples under ruleset {RULESET}")
    hit = s.get(f"hit_rate_{h}h", 0.0)
    mean = s.get(f"mean_ret_{h}h", 0.0)
    # FEE_K x fees, not 1x: a mean that only matches the round trip is
    # trading for nothing while still risking the stop. REVAMP 08-23:
    # 3x -> 4x (Binance bots review: turnover governed by fees is the #1
    # shared mechanic of verified winners; 3+1 all-in round trips/day is
    # 15-24%/month of book in fees if every slot fires).
    if hit < MIN_ACT_HIT or mean < FEE_K * ROUND_TRIP:
        return False, (f"benched — hit {hit:.0%}, mean {mean:+.2%} over "
                       f"last {n} at {h}h: not beating {FEE_K:g}x the "
                       f"round trip")
    # REVAMP 08-23: both halves of the rolling record must pay (a regime
    # that flattered the first half is not a signal), and the payoff shape
    # must be right — verified durable traders run 20-46% win rates with
    # 2-5x payoff; the 98%-win / 5-10x-loss profile is the one that dies.
    if s.get(f"both_halves_{h}h") is False:
        return False, (f"benched — only one half of the last {n} paid at "
                       f"{h}h: regime luck, not a signal")
    payoff = s.get(f"payoff_{h}h")
    if payoff is not None and payoff < MIN_PAYOFF and hit < 0.65:
        return False, (f"benched — payoff {payoff:.2f} (avg win / avg loss) "
                       f"with hit {hit:.0%}: losers outweigh winners")
    return True, ""


def wave_call(count: int, history: list[int]) -> tuple[bool, float | None]:
    """Is today a wave day? Pure: count of movers now vs the trailing
    baseline. No call without a real baseline — the first days of history
    must not all look like waves."""
    if len(history) < BREADTH_MIN_HISTORY:
        return False, None
    hs = sorted(history)
    base = hs[len(hs) // 2] or 1
    return count >= BREADTH_WAVE_RATIO * base, float(base)


def breadth_state(raw_tickers: list[dict], now: datetime) -> dict:
    """Count the market's movers (+10% on real volume), keep 7 days of
    history, and call wave days. The study's single loudest fact: 35 of 109
    explosion troughs landed on ONE calendar day."""
    count = 0
    for t in raw_tickers:
        try:
            if (float(t.get("priceChangePercent", 0) or 0) / 100.0
                    >= BREADTH_MIN_CHG
                    and float(t.get("quoteVolume", 0) or 0) >= BREADTH_MIN_QV):
                count += 1
        except Exception:
            continue
    hist = []
    if BREADTH_FILE.exists():
        try:
            hist = json.loads(BREADTH_FILE.read_text()).get("history") or []
        except Exception:
            hist = []
    cutoff = (now - timedelta(days=7)).isoformat(timespec="seconds")
    hist = [h for h in hist if h.get("ts", "") >= cutoff]
    wave, base = wave_call(count, [h["n"] for h in hist])
    hist.append({"ts": now.isoformat(timespec="seconds"), "n": count})
    _atomic_write(BREADTH_FILE, json.dumps(
        {"history": hist[-1200:], "count": count,
         "baseline": base, "wave": wave}))
    return {"count": count, "baseline": base, "wave": wave}


def prorated_day_volume(partial_qv: float, elapsed_frac: float,
                        min_frac: float = 2.0 / 24.0) -> float | None:
    """Project the current partial UTC day's volume to a full-day rate.

    BUG FIX 2026-08-20: revival compared today's PARTIAL volume against
    full prior days and demanded 3x — so at 08:00 UTC a coin needed a 9x
    pace to register, and in 3 days revival logged ZERO candidates while
    the other signals logged 389. The one strategy the 2-year study
    supports was structurally muted for most of every day. None before
    min_frac elapsed: a 30-minute-old day projects pure noise.
    """
    if elapsed_frac < min_frac:
        return None
    return partial_qv / elapsed_frac


def revival_verdict(f: dict) -> tuple[float, str] | None:
    """Pure verdict on a precomputed revival profile (see the constants —
    every threshold is read off the explosion study, n=109)."""
    if not f.get("age_ok"):
        return None
    if not (REV2_TURN_MIN <= f["chg_24h"] <= REV2_TURN_MAX):
        return None
    if f["week_chg"] > REV2_MIN_WEEK_FALL:
        return None                      # was not beaten down — wrong species
    if f["med_pre_qv"] > REV2_MAX_PRE_QV or f["med_pre_qv"] <= 0:
        return None                      # was not quiet
    arrival = f["today_qv"] / f["med_pre_qv"]
    if arrival < REV2_MIN_VOL_ARRIVAL:
        return None                      # the crowd has not actually arrived
    if f["runup_30d"] > REV2_MAX_RUNUP_30D:
        return None                      # not day one any more
    score = min(abs(f["week_chg"]) / 0.30, 1.0) * 0.35 \
        + min(arrival / 10.0, 1.0) * 0.35 \
        + (1.0 - f["runup_30d"] / REV2_MAX_RUNUP_30D) * 0.30
    why = (f"revival day-one: fell {f['week_chg']:+.0%} last week on "
           f"${f['med_pre_qv'] / 1e6:.2f}M/day quiet, volume arriving "
           f"{arrival:.1f}x today, only {f['runup_30d']:+.0%} off its 30d "
           f"low")
    # the serial-exploder prior: coins that have done this before do it
    # again — the strongest single regularity in the 2y study
    n_prior = int(f.get("serial_n") or 0)
    if n_prior >= SERIAL_MIN_N:
        score *= min(1.0 + n_prior * SERIAL_BOOST_PER, SERIAL_BOOST_CAP)
        why += f" · serial exploder: {n_prior} runs in 2y"
    if f.get("wave"):
        score = min(score * 1.25, 1.0)
        why += " — ON A WAVE DAY (breadth {:.0f} vs {:.0f} base)".format(
            f.get("wave_count", 0), f.get("wave_base") or 0)
    return score, why


def serial_counts() -> dict[str, int]:
    """Per-symbol explosion counts from the 2y study snapshot (committed as
    data/explosion_history.json; regenerate from trading-research). Missing
    file = empty prior, never an error."""
    try:
        d = json.loads(SERIAL_FILE.read_text())
        return {s: v.get("n", 0) for s, v in (d.get("symbols") or {}).items()}
    except Exception:
        return {}


def revival_candidates(raw_tickers: list[dict], card: dict, breadth: dict,
                       now: datetime) -> list[dict]:
    """Day-one grind candidates from the quiet tier the main floor cannot
    see. Bounded: ticker-level prefilter first, at most REV2_KLINE_BUDGET
    daily-kline probes per cycle."""
    serial = serial_counts()
    short = []
    for t in raw_tickers:
        try:
            chg = float(t.get("priceChangePercent", 0) or 0) / 100.0
            qv = float(t.get("quoteVolume", 0) or 0)
            if not (REV2_TURN_MIN <= chg <= REV2_TURN_MAX):
                continue
            if qv < REV2_QV_FLOOR:
                continue
            bid, ask = float(t["bidPrice"]), float(t["askPrice"])
            mid = (bid + ask) / 2.0
            if mid <= 0 or (ask - bid) / mid * 10_000 > MAX_SPREAD_BPS:
                continue
            short.append((chg, t))
        except Exception:
            continue
    short.sort(key=lambda x: -x[0])

    out = []
    probes = 0
    for chg, t in short:
        if probes >= REV2_KLINE_BUDGET:
            break
        sym = t["symbol"]
        probes += 1
        rows = binance_data.klines(sym, "1d", REV2_MIN_AGE_D)
        if len(rows) < REV2_MIN_AGE_D:      # younger than the dino floor
            continue
        try:
            closes = [float(r[4]) for r in rows]
            lows = [float(r[3]) for r in rows]
            qvs = [float(r[7]) for r in rows]
            last = float(t.get("lastPrice", 0) or 0)
            pre_qv = sorted(qvs[-8:-1])
            f = {
                "age_ok": True, "chg_24h": chg,
                "week_chg": closes[-2] / closes[-9] - 1.0,
                "med_pre_qv": pre_qv[len(pre_qv) // 2],
                # projected full-day rate, not the raw partial (bug fix
                # 08-20 — see prorated_day_volume)
                "today_qv": prorated_day_volume(
                    qvs[-1],
                    (now.hour * 3600 + now.minute * 60 + now.second)
                    / 86400.0),
                "runup_30d": last / min(lows[-31:]) - 1.0,
                "wave": breadth.get("wave"),
                "wave_count": breadth.get("count"),
                "wave_base": breadth.get("baseline"),
                "serial_n": serial.get(sym, 0),
            }
        except Exception:
            continue
        if f["today_qv"] is None:
            continue          # under 2h into the UTC day: no honest rate yet
        hit = revival_verdict(f)
        if not hit:
            continue
        raw_score, why = hit
        w = signal_weight(card, "revival")
        out.append({
            "symbol": sym, "signal": "revival",
            "score": round(raw_score * w, 4),
            "raw_score": round(raw_score, 4), "weight": round(w, 3),
            "price": last, "why": why,
            "chg_24h": round(f["chg_24h"], 4),
            "vol_surge": round(f["today_qv"] / f["med_pre_qv"], 1),
            "chg_1h": None, "market_surge": None,
        })
    return out


def heat_candidates(tickers_by_sym: dict[str, dict], card: dict,
                    now: datetime) -> list[dict]:
    """Candidates from cross-source social agreement (social_heat.py).

    No price/volume gate of its own beyond the universe filters the ticker
    already passed — the claim being tested is purely social, and mixing in
    momentum conditions here would make the scorecard unreadable (whose edge
    was it?). The gate machinery decides whether the social claim pays."""
    if not HEAT_FILE.exists():
        return []
    try:
        d = json.loads(HEAT_FILE.read_text())
        age_min = (now - datetime.fromisoformat(d["ts"])
                   ).total_seconds() / 60.0
    except Exception:
        return []
    if age_min > HEAT_FRESH_MIN:
        return []
    out = []
    for h in d.get("heat") or []:
        if h.get("surfaces", 0) < HEAT_MIN_SURFACES:
            continue
        sym = h["symbol"] + "USDT"
        t = tickers_by_sym.get(sym)
        if not t:            # not spot-tradeable / failed universe filters
            continue
        raw = min(h["surfaces"], 5) / 5.0
        w = signal_weight(card, "heat")
        why = (f"lit up on {h['surfaces']} independent surfaces at once "
               f"({'+'.join(h.get('sources', []))})")
        if h.get("funding") is not None:
            why += f" · funding {h['funding']:+.3%}"
        if h.get("long_short") is not None:
            why += f" · L/S {h['long_short']}"
        out.append({
            "symbol": sym, "signal": "heat",
            "score": round(raw * w, 4), "raw_score": round(raw, 4),
            "weight": round(w, 3), "price": float(t.get("lastPrice", 0) or 0),
            "why": why,
            "chg_24h": round(float(t.get("priceChangePercent", 0) or 0) / 100.0, 4),
            "vol_surge": None, "chg_1h": None,
            "market_surge": h["surfaces"],
        })
    return out


def recently_flagged(rows: list[dict], symbol: str, signal: str,
                     now: datetime) -> bool:
    """True if this (symbol, signal) was already flagged inside the
    cooldown. One event must be one log row: BICO re-flagged five times in
    70 minutes was five chances for the book to catch the same knife, and
    five correlated 'samples' skewing the scorecard."""
    for r in reversed(rows):
        if r.get("symbol") == symbol and r.get("signal") == signal:
            try:
                age_h = (now - datetime.fromisoformat(r["ts"])
                         ).total_seconds() / 3600.0
            except Exception:
                return False
            return age_h < RESIGNAL_COOLDOWN_H
    return False


def log_candidates(cands: list[dict], now: datetime) -> None:
    """Full features per row (autopsy 08-16: the first analysis had to dig
    features back out of git history — the log should carry its own
    evidence)."""
    with LOG.open("a", encoding="utf-8") as fh:
        for c in cands:
            fh.write(json.dumps({
                "ts": now.isoformat(timespec="seconds"),
                "symbol": c["symbol"], "signal": c["signal"],
                "score": round(c["score"], 4), "price": c["price"],
                "ruleset": RULESET, "actionable": c.get("actionable"),
                "chg_24h": c.get("chg_24h"), "chg_1h": c.get("chg_1h"),
                "vol_surge": c.get("vol_surge"),
                "market_surge": c.get("market_surge"),
            }) + "\n")


def resolve_outcomes(now: datetime) -> tuple[dict, list[dict]]:
    """Look up what actually happened to earlier candidates and rebuild the
    scorecard. This is the whole learning loop: flagged -> waited -> priced.
    A candidate counts as a HIT if it was up at all at that horizon, net of
    a round trip at Binance's 10bps-per-side spot tier.

    Integrity rules (audit 08-15):
      * a horizon resolved LATER than 1.5x its window gets a None sentinel,
        never a fake return — after downtime, stamping ret_1h with a
        48-hour price move would poison every hit rate the weights obey;
      * a symbol whose price cannot be fetched 3 cycles running while OTHER
        symbols price fine (proves connectivity) is marked dead — usually a
        delisting — so it stops re-entering pending forever;
      * the log rewrite happens only when something actually changed, and
        atomically.
    """
    if not LOG.exists():
        return load_scorecard(), []
    rows = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        try:
            rows.append(json.loads(line))
        except Exception:
            continue
    rows = rows[-4000:]
    changed = False
    pending = {}
    for r in rows:
        if r.get("dead"):
            continue
        try:
            ts = datetime.fromisoformat(r["ts"])
        except Exception:
            continue
        age_h = (now - ts).total_seconds() / 3600.0
        for h in HORIZONS_H:
            if f"ret_{h}h" in r:
                continue
            if age_h > h * 1.5:
                r[f"ret_{h}h"] = None      # too late to be a real {h}h return
                changed = True
            elif age_h >= h:
                pending.setdefault(r["symbol"], []).append((r, h))
    if pending:
        px = binance_data.prices(list(pending)[:100])
        for sym, items in pending.items():
            p_now = px.get(sym)
            if p_now:
                for r, h in items:
                    if r.get("price"):
                        r[f"ret_{h}h"] = round(p_now / r["price"] - 1.0, 5)
                        changed = True
            elif px:
                # others priced fine -> this symbol itself is the problem
                for r, _h in items:
                    r["px_miss"] = r.get("px_miss", 0) + 1
                    if r["px_miss"] >= 3:
                        r["dead"] = True
                    changed = True
    if changed:
        _atomic_write(LOG, "\n".join(json.dumps(r) for r in rows) + "\n")

    # The card obeys two honesty rules: only rows earned under the CURRENT
    # ruleset count (old rules' results are history, not evidence), and only
    # the rolling window counts (what the signal is, not what it once was).
    card = {"signals": {}, "ruleset": RULESET,
            "updated": now.isoformat(timespec="seconds")}
    live = [r for r in rows if r.get("ruleset") == RULESET]
    for sig in SIGNAL_TYPES:
        entry = {}
        for h in HORIZONS_H:
            # `is not None`: sentinels are excluded, a legitimate 0.0 counts
            rets = [r[f"ret_{h}h"] for r in live
                    if r.get("signal") == sig
                    and r.get(f"ret_{h}h") is not None][-ROLL_WINDOW:]
            if rets:
                entry[f"n_{h}h"] = len(rets)
                entry[f"hit_rate_{h}h"] = round(
                    sum(1 for x in rets if x > ROUND_TRIP) / len(rets), 3)
                entry[f"mean_ret_{h}h"] = round(sum(rets) / len(rets), 5)
                entry[f"median_ret_{h}h"] = round(
                    sorted(rets)[len(rets) // 2], 5)
                # REVAMP 08-23 (Bailey/Quantopian: IS Sharpe predicts OOS
                # Sharpe at R^2 < 0.025; both-halves profitability and
                # payoff shape predict better than any mean): record
                # whether BOTH halves of the rolling record pay, and the
                # avg-win/avg-loss payoff ratio. The gate reads both.
                half = len(rets) // 2
                if half >= 3:
                    a, b = rets[:half], rets[half:]
                    entry[f"both_halves_{h}h"] = bool(
                        sum(a) / len(a) > 0 and sum(b) / len(b) > 0)
                wins = [x for x in rets if x > 0]
                losses = [x for x in rets if x < 0]
                if wins:
                    entry[f"avg_win_{h}h"] = round(sum(wins) / len(wins), 5)
                if losses:
                    entry[f"avg_loss_{h}h"] = round(
                        sum(losses) / len(losses), 5)
                if wins and losses:
                    entry[f"payoff_{h}h"] = round(
                        (sum(wins) / len(wins))
                        / abs(sum(losses) / len(losses)), 3)
        if entry:
            card["signals"][sig] = entry
    _atomic_write(SCORECARD, json.dumps(card, indent=2))
    return card, rows


# ---- main -------------------------------------------------------------------

def scan(now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    card, history = resolve_outcomes(now)

    raw = binance_data.all_tickers_24h()
    raw_tradeable = [t for t in raw
                     if binance_data.is_tradeable_pair(t.get("symbol", ""))]
    # breadth runs BEFORE the veto so its history never gaps — wave days and
    # BTC-dump days are different phenomena and both need honest baselines
    breadth = breadth_state(raw_tradeable, now)
    if breadth.get("wave"):
        print(f"[scout] WAVE DAY — {breadth['count']} movers vs "
              f"~{breadth['baseline']:.0f} baseline; the tide is in")

    # MARKET-WIDE VETO: the reversal literature is cross-sectional, not
    # directional. When BTC itself is falling, a coin being down is market
    # beta rather than an idiosyncratic overshoot worth fading — and a
    # breakout into a falling market is a trap.
    btc = next((t for t in raw if t.get("symbol") == "BTCUSDT"), None)
    btc_1h = None
    if btc:
        k = binance_data.candle_series(binance_data.klines("BTCUSDT", "5m", 13))
        if len(k["close"]) >= 13:
            btc_1h = _pct(k["close"][-1], k["close"][0])
    if btc_1h is not None and btc_1h <= BTC_VETO_1H:
        print(f"[scout] MARKET VETO — BTC {btc_1h:+.1%} in the last hour; "
              f"no idiosyncratic signal is trustworthy in a market-wide dump")
        out = {"ts": now.isoformat(timespec="seconds"), "candidates": [],
               "veto": f"BTC {btc_1h:+.1%}/1h"}
        _atomic_write(SIGNALS, json.dumps(out, indent=2))
        return out

    tickers = [t for t in raw if universe_ok(t)]
    if not tickers:
        print("[scout] no market data this cycle")
        return {"ts": now.isoformat(timespec="seconds"), "candidates": []}

    # cross-sectional context for the reversion sort (the published method)
    changes = sorted(float(t["priceChangePercent"]) for t in tickers)
    decile_cut = changes[max(0, int(len(changes) * REV_XS_PERCENTILE) - 1)]
    vols = sorted(float(t["quoteVolume"]) for t in tickers)

    # Prefilter for the expensive kline calls, from three angles because the
    # three signals live in different places: the day's winners (breakout),
    # the day's losers (reversion), and — critically — whatever is trading
    # abnormally hard right now regardless of price (ignition).
    surge = market_wide_surge(tickers, now)
    by_move = sorted(tickers, key=lambda t: float(t["priceChangePercent"]),
                     reverse=True)
    per = max(6, SHORTLIST // 3)
    picks = {t["symbol"]: t for t in by_move[:per]}
    picks.update({t["symbol"]: t for t in by_move[-per:]})
    if surge:
        hot = sorted(surge.items(), key=lambda kv: -kv[1])[:per]
        by_sym = {t["symbol"]: t for t in tickers}
        picks.update({s: by_sym[s] for s, _ in hot if s in by_sym})
    shortlist = list(picks.values())

    cands = []
    for t in shortlist:
        sym = t["symbol"]
        f = features(sym, t)
        if not f:
            continue
        f["market_surge"] = round(surge.get(sym, 0.0), 2)
        f["xs_bottom_decile"] = float(t["priceChangePercent"]) <= decile_cut
        qv = float(t["quoteVolume"])
        f["liq_rank_pct"] = sum(1 for v in vols if v <= qv) / len(vols)
        for name, fn in (("ignition", score_ignition),
                         ("breakout", score_breakout),
                         ("reversion", score_reversion)):
            hit = fn(f)
            if not hit:
                continue
            raw, why = hit
            w = signal_weight(card, name)
            cands.append({
                "symbol": sym, "signal": name,
                "score": round(raw * w, 4), "raw_score": round(raw, 4),
                "weight": round(w, 3), "price": f["price"], "why": why,
                "chg_24h": round(f["chg_24h"], 4),
                "vol_surge": round(f["vol_surge"], 2),
                "chg_1h": round(f["chg_1h"], 4),
                "market_surge": f["market_surge"],
            })

    # the heat layer: social agreement candidates join the same ranking,
    # cooldown, gate, and logging as every price-driven signal
    cands.extend(heat_candidates({t["symbol"]: t for t in tickers},
                                 card, now))
    # the revival layer: day-one grind profiles from the quiet tier below
    # the main volume floor (where 77/88 of the month's exploders lived)
    cands.extend(revival_candidates(raw_tradeable, card, breadth, now))

    cands.sort(key=lambda c: -c["score"])
    cands = cands[:TOP_N]

    # one event, one row: a coin still inside its re-signal cooldown was
    # already flagged, logged, and offered — repeating it every 10 minutes
    # just multiplies the same mistake
    fresh = []
    for c in cands:
        if recently_flagged(history, c["symbol"], c["signal"], now):
            print(f"[scout] {c['symbol']} {c['signal']} inside the "
                  f"{RESIGNAL_COOLDOWN_H:.0f}h re-signal cooldown — skip")
        else:
            fresh.append(c)
    cands = fresh

    # KNIFE-FILTER UPGRADE (research-flagged as the biggest single win):
    # a reversion is only a dip if the forced selling is spent. On the top
    # reversion candidates only (bounded API cost — 2 futures calls each),
    # confirm the liquidation cascade has cleared open interest and that
    # funding shows shorts capitulating. If OI is intact on a big drop, the
    # cause is fundamental (exploit/news) — drop the candidate entirely.
    funding = binance_data.funding_extremes()
    checked = 0
    kept = []
    for c in cands:
        if c["signal"] == "reversion" and checked < 3:
            checked += 1
            oi_drop = binance_data.open_interest_drop(c["symbol"])
            fr = funding.get(c["symbol"])
            c["oi_drop"] = round(oi_drop, 3) if oi_drop is not None else None
            c["funding"] = round(fr, 5) if fr is not None else None
            # OI known AND barely moved on a hard fall = knife, not dip
            if oi_drop is not None and oi_drop < 0.10:
                c["dropped"] = "OI intact — forced selling not spent, likely fundamental"
                continue
            # shorts capitulating (very negative funding) is a real tailwind
            if oi_drop is not None and oi_drop >= 0.25:
                c["score"] = round(c["score"] * 1.15, 4)
                c["why"] += f" · OI −{oi_drop:.0%} (cascade clearing)"
            if fr is not None and fr <= -0.005:
                c["why"] += f" · funding {fr:.2%} (shorts paying)"
        kept.append(c)
    kept.sort(key=lambda c: -c["score"])
    cands = kept

    # THE GATE: stamp every candidate with whether its signal type has
    # EARNED the right to real money under the current ruleset
    gate = {}
    for sig in SIGNAL_TYPES:
        ok, why_not = signal_actionable(card, sig)
        gate[sig] = "actionable" if ok else why_not
    for c in cands:
        c["actionable"] = gate[c["signal"]] == "actionable"
        if not c["actionable"]:
            c["status"] = gate[c["signal"]]
    log_candidates(cands, now)

    out = {
        "ts": now.isoformat(timespec="seconds"),
        "scanned": len(tickers),
        "ruleset": RULESET,
        "candidates": cands,
        "gate": gate,
        "breadth": breadth,
        "scorecard": card.get("signals", {}),
        "note": "READ-ONLY scout. Ranked opinion only — the book decides.",
    }
    _atomic_write(SIGNALS, json.dumps(out, indent=2))
    return out


def main():
    out = scan()
    print(f"[scout] scanned {out.get('scanned', 0)} liquid pairs — "
          f"{len(out['candidates'])} candidates")
    for c in out["candidates"]:
        tag = "" if c.get("actionable") else "  [NOT TRADEABLE]"
        print(f"  {c['signal']:<9} {c['symbol']:<14} score {c['score']:.3f} "
              f"(w{c['weight']}){tag} — {c['why']}")
    for sig, status in (out.get("gate") or {}).items():
        print(f"  [gate] {sig}: {status}")
    for sig, s in (out.get("scorecard") or {}).items():
        if s.get("n_4h"):
            print(f"  [learned] {sig}: {s['n_4h']} resolved 4h samples, "
                  f"hit rate {s.get('hit_rate_4h')}, "
                  f"mean {s.get('mean_ret_4h')}")


if __name__ == "__main__":
    main()
