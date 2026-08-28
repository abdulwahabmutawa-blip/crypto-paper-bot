# Phase 1b — comparator features registered 2026-08-28 (PRE-REGISTRATION ADDENDUM)

Registered TODAY, before any of their evaluation windows open. Source: the
2026-08-28 cohort study of the first 12 days of gen-000 questions (320
symbols, 65 interim YES). That month is IN-SAMPLE for these features and is
**excluded from their judgment**: every comparator below is scored only on
questions whose window_start is **on or after 2026-08-29**.

The existing Phase-1 four (liqtier_v1, ownrate_v1, momo_v1, age_v1 —
registered 08-20) already cover liquidity, serial-exploder, momentum and
age. The study adds one falsifiable prediction about them, on record now:

> **ownrate_v1 will underperform the pooled base rate** (the study found
> the serial-exploder relationship INVERTED in the 08-17..28 cohort:
> highest-history quartile locked 16% vs 28% for modest-history coins).

## New comparators to implement (specs frozen now, code to follow)

1. **wave_state_v1** — pooled hit rate conditioned on the breadth/wave
   state at T0 (wave active vs not, from the scout's breadth file, no
   lookahead: the file's state as of the prediction run). Basis: 35/65
   interim YES locked inside one 48h macro wave; the 2y study's 64%
   clustering.
2. **scoutflag_v1** — pooled rate conditioned on "scout flagged this
   symbol within the 7 days BEFORE T0" (from data/scout_log.jsonl,
   timestamps strictly < T0). Basis: 37/65 winners were flagged days
   before their crossing (82% flagged overall vs 20% of losers).
3. **quietrev_v1** — pooled rate by joint bucket of trailing-30d realized
   vol (tercile) x trailing-30d drawdown band (mild -3..-15% vs deep
   <-15% vs none). Basis: winners were quieter (3.0% vs 3.5%) and mildly
   drawn down (-6.3% vs -2.2%), non-monotonic in depth — the revival
   shape.
4. **delistveto_v1** — any active exchange delisting notice at T0 forces
   p = 0.005 (the clamp floor), otherwise emit pooled base rate. Basis:
   STORJ/SCRT structural dumps; a coin being evicted has no 30-day story.

Rules inherited from Phase 1: ride-along fields on the baseline rows, same
resolution, paired scoring, probabilities clamped [0.005, 0.75], no
lookahead — every input must be knowable at the prediction run's start.
