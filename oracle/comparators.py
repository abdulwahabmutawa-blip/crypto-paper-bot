"""Phase-1 comparator forecasters — four honest dummies, no LLM, no lookahead.

WHY THESE EXIST (owner-approved 2026-08-20): with only baserate_v1 on the
board, September's first resolutions can say "was the base rate calibrated"
but not "was it beatable by anything cheap". Any generation-2 forecaster
must clear the best of THESE before its edge means anything. They ride
along as fields on the baseline's prediction rows — same question, same
resolution, same paired scoring — so they add zero resolution work and
cannot disturb the baseline's record.

NO LOOKAHEAD, same guarantee as the climatology: every number below is
pooled from per-symbol (own_hits, own_windows) counts, and predict.py's
explosion_rate() only counts windows that had FULLY RESOLVED before the
reference candle. The bucket edges are cross-sectional (this run's slate),
which is knowable at prediction time by construction.

The four:
  liqtier_v1 — pooled hit rate by 30d-median-quote-volume tercile. The
               2y study's strongest single covariate: small books explode.
  ownrate_v1 — each coin's own rate, shrunk toward the pooled base rate
               (K=25 pseudo-windows) so a 3-window listing cannot scream.
  momo_v1    — pooled rate by trailing-30d-return tercile: does "already
               moving" predict touching 1.5x?
  age_v1     — pooled rate by listing age (<180d / <365d / >=365d).

Probabilities are clamped to [0.005, 0.75]: a comparator that says 0 or 1
is not a probability, it is a dare.
"""
from __future__ import annotations

COMPARATOR_SPEC = "comparators_v2"   # v2 (08-21): + momo_v2, liq_band_v1
P_FLOOR, P_CEIL = 0.005, 0.75
OWNRATE_K = 25          # shrinkage pseudo-windows toward the pooled rate
AGE_EDGES = (180, 365)  # days: young / adolescent / mature
# mid-band liquidity (forensics 08-21): the 9 interim hits clustered in the
# $0.75M-$4M median-30d-quote-volume band; top- and bottom-tier were at or
# below chance. Shipped as an INDICATOR lens (not the multiplicative
# own-rate x liquidity combo, which underperformed own-rate alone 2/9 vs
# 3/9 on the same interim data). September grades it like every other lens.
LIQ_BAND = (750_000.0, 4_000_000.0)


def _clamp(p: float) -> float:
    return round(min(P_CEIL, max(P_FLOOR, p)), 6)


def _terciles(vals: list[float]) -> tuple[float, float]:
    s = sorted(vals)
    return s[len(s) // 3], s[(2 * len(s)) // 3]


def _pooled(slate: list[dict], bucket_of) -> dict:
    """hits/windows pooled per bucket -> {bucket: rate}; empty bucket
    falls back to the caller's base rate (handled in probabilities())."""
    agg: dict[object, list[int]] = {}
    for s in slate:
        b = bucket_of(s)
        h, w = agg.setdefault(b, [0, 0])
        agg[b] = [h + s["own_hits"], w + s["own_windows"]]
    return {b: (h / w if w else None) for b, (h, w) in agg.items()}


def probabilities(slate: list[dict], base_rate: float
                  ) -> tuple[dict[str, dict[str, float]], dict]:
    """Per-symbol {forecaster_id: p} plus the meta block for the snapshot.

    Slate rows need: symbol, median_qv_30d, own_hits, own_windows,
    listed_days, ret_30d.
    """
    q1, q2 = _terciles([s["median_qv_30d"] for s in slate])
    m1, m2 = _terciles([s["ret_30d"] for s in slate])

    def liq_bucket(s):
        v = s["median_qv_30d"]
        return "low" if v <= q1 else ("mid" if v <= q2 else "high")

    def momo_bucket(s):
        v = s["ret_30d"]
        return "down" if v <= m1 else ("flat" if v <= m2 else "up")

    def age_bucket(s):
        d = s["listed_days"]
        return ("young" if d < AGE_EDGES[0]
                else "adolescent" if d < AGE_EDGES[1] else "mature")

    def band_bucket(s):
        return "mid" if LIQ_BAND[0] <= s["median_qv_30d"] <= LIQ_BAND[1] \
            else "outside"

    liq = _pooled(slate, liq_bucket)
    momo = _pooled(slate, momo_bucket)
    age = _pooled(slate, age_bucket)
    band = _pooled(slate, band_bucket)

    # momo_v2 (08-21): the momentum-FOLLOWING falsification twin of momo_v1.
    # momo_v1 pools historical rates per tercile and comes out reversion-
    # tilted (down-coins exploded more historically); the forensics' clean
    # pre-window momentum ran the other way (interim AUC 0.94, rally-week
    # caveat). v2 encodes the opposite belief — p rises monotonically with
    # momentum rank — so September can crown one and kill the other.
    ranked = sorted(s["ret_30d"] for s in slate)
    n_r = max(1, len(ranked) - 1)

    def mom_rank(s):
        import bisect
        return bisect.bisect_left(ranked, s["ret_30d"]) / n_r

    out: dict[str, dict[str, float]] = {}
    for s in slate:
        own = ((s["own_hits"] + OWNRATE_K * base_rate)
               / (s["own_windows"] + OWNRATE_K))
        out[s["symbol"]] = {
            "liqtier_v1": _clamp(liq[liq_bucket(s)] or base_rate),
            "ownrate_v1": _clamp(own),
            "momo_v1": _clamp(momo[momo_bucket(s)] or base_rate),
            "age_v1": _clamp(age[age_bucket(s)] or base_rate),
            "momo_v2": _clamp(base_rate * (0.5 + mom_rank(s))),
            "liq_band_v1": _clamp(band[band_bucket(s)] or base_rate),
        }

    meta = {
        "spec": COMPARATOR_SPEC,
        "ownrate_shrinkage_k": OWNRATE_K,
        "p_clamp": [P_FLOOR, P_CEIL],
        "liqtier_edges_qv": [round(q1, 2), round(q2, 2)],
        "liqtier_rates": {k: round(v, 6) for k, v in liq.items()
                          if v is not None},
        "momo_edges_ret30d": [round(m1, 6), round(m2, 6)],
        "momo_rates": {k: round(v, 6) for k, v in momo.items()
                       if v is not None},
        "age_edges_days": list(AGE_EDGES),
        "age_rates": {k: round(v, 6) for k, v in age.items()
                      if v is not None},
        "liq_band_usd": list(LIQ_BAND),
        "liq_band_rates": {k: round(v, 6) for k, v in band.items()
                           if v is not None},
        "momo_v2": "p = base_rate * (0.5 + rank_pct(ret_30d)), clamped",
    }
    return out, meta
