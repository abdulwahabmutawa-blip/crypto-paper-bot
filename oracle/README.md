# The Oracle — a predict-only forecasting experiment (PRE-REGISTRATION)

**This package cannot trade. It holds no keys, imports no broker, and CI
fails the build if it ever imports a trading module.** It emits falsifiable
predictions about Binance USDT coins, resolves them mechanically, and scores
itself against baselines it must beat. Nothing here touches the lottery book.

This file is the pre-registration. It was written BEFORE any prediction was
made, and the parts marked FROZEN may not be changed without opening a new
generation (which resets the track record to zero — see Generations).

---

## The question, frozen

> For symbol S, given its daily close at T0, will
> `max(high)` over the next 30 days reach **1.50x** that close?

- Universe: `universe_rule_v1` (below), evaluated fresh each run.
- Horizon: 30 days. Threshold: +50%.
- Resolution source: Binance `/api/v3/klines`, interval `1d`, public.
- Every slate member gets a probability. **Forced coverage.**

## Why forced coverage

The single easiest way to fool yourself is to choose the denominator after
seeing the data. The slate is fixed by a frozen rule before probabilities
exist, so it cannot be. A forecaster may FLAG a conviction subset (`emit`),
and a selective score is published alongside — but never instead of — the
forced-coverage score, always with its coverage fraction stated.

## universe_rule_v1 (FROZEN)

- Binance SPOT, quote asset USDT, status TRADING
- listed >= 90 days (needs history to be judged)
- 30-day median quote volume in **[$200k, $50M]** — above the floor an exit
  is plausible; below the ceiling the coin can still move
- excludes stablecoins and leveraged tokens

## Base rate (the incumbent to beat)

Climatology, computed per run from a rolling 365-day window ending at
**T0 - 31 days** — i.e. only from questions that had already fully resolved
before the prediction was made. No lookahead, by construction.

## What Phase 0 is for

Phase 0 contains **no LLM**. The forecaster emits the base rate for every
coin. That sounds pointless and is not: it validates the contract end to
end, and it measures the three numbers that decide whether the whole
experiment is feasible.

1. the empirical **base rate** of a +50%/30d move on this universe
2. the **annulment rate** — how often the question is unanswerable
   (delisting, halts, data gaps). Target < 4%; above 8% the question
   template itself is broken and must be rewritten, not the forecaster.
3. the **cluster correlation rho** — outcomes are not independent (the
   2-year study found 64% of explosions cluster on market-wide wave days).
   rho sets the effective sample size, and therefore how long any later
   claim will take to earn.

Phase 0's deliverable is a calibrated, tamper-evident, empty scoreboard.
That is the honest starting point, not a disappointment.

## Scoring (FROZEN)

- **Primary**: paired per-item Brier difference
  `d_i = (p_baseline_i - y_i)^2 - (p_forecaster_i - y_i)^2`,
  reported as mean(d), sd(d), n, n_eff. Positive means the forecaster beat
  the baseline. Pairing on the identical slate at the identical timestamp is
  far more sample-efficient than comparing two separately averaged means.
- **n_eff** = n / (1 + (m-1) * rho), with rho MEASURED from the data
  (intraclass correlation of outcomes grouped by run), never assumed.
- **BANNED from every report**: AUC, precision, recall, raw hit rate. In the
  audited literature, models spanning ROC AUC 0.627-0.974 all lost money.
  A model is judged on paired probabilistic scores and net-of-cost outcomes.
- **No conclusion may be stated** until `n_eff >= 100`. Until then every
  report prints the countdown and refuses to characterise performance. This
  is enforced in code (`oracle/score.py`), not by discipline.

## Anti-fooling (mechanisms, not intentions)

- **No outcome fields exist in a prediction record.** Resolution lives in a
  separate file keyed by `prediction_id`. Retro-fitting is not discouraged;
  it is structurally impossible.
- **Append-only hash chain** (`oracle/data/ledger/chain.jsonl`): each entry
  commits to the sha256 of the file it describes and to the previous entry.
  CI rebuilds the chain on every push and fails on any break.
- **CI append-only check**: any modification or deletion of an existing file
  under `predictions/` or `resolutions/` fails the build.
- **Inputs are snapshotted by value** with a sha256 and never re-fetched.
- **The resolver never sees reasoning.** It reads only symbol, reference
  price, threshold, and window.

## Generations

A `generation_id` pins the forecaster, its prompt (when one exists), the
universe rule, and the scoring code. **Changing any frozen element opens a
new generation and the track record restarts at zero.** Generation churn —
not model quality — is the most likely way this experiment dies, so changes
are batched and rare. Phase 0 runs as `gen-000-baserate`.

## Kill criteria (pre-committed)

The experiment is declared dead, with the record left published, if:

1. at `n_eff >= 100`, the 90% upper bound on paired mean d versus the base
   rate lies below zero (worse than climatology);
2. at 18 months, mean d is non-positive after a multiple-trials haircut;
3. annulment rate stays above 8% for three months and no contract revision
   fixes it;
4. more than three generation resets occur in twelve months (no generation
   can ever accumulate evidence);
5. any unexplained chain break, force-push, or manual edit of a historical
   record — the experiment forfeits and restarts from a fresh chain.

Later phases add: a blinded reasoning-discrimination test (if a grader
cannot separate winning from losing reasoning above 55% over 200 matched
pairs, the premise of a reasoning-based forecaster is falsified), and a
shadow net-of-cost P&L at 31bps plus spread (an edge that exists only in
untradable microcaps is a true result with no use).

## Honest expected outcome

**A well-documented null is the overwhelmingly likely result**, and this
design should be judged on whether it can deliver that null credibly. No
forward-looking crypto explosion-prediction claim survived this project's
own source audit; human forecasters have beaten LLM bots every quarter for
two years. Probability that a durable, tradable edge survives every
guardrail here: low single digits.

The realistic payoff is different and still worth having: a falsification
instrument nobody can retro-fit, plus measured base rates, annulment rates
and cluster correlation for the whole fleet.

## Phases

- **Phase 0 (this)**: ledger, universe, resolver, base-rate forecaster, CI.
- **Phase 1**: comparators — random-K, the mechanical scout as a calibrated
  probability, a volatility-matched null, a wave-day null.
- **Phase 2**: the LLM arm as a challenger. Opens `gen-001`.
- **Phase 3** (only if gen-001 reaches n_eff >= 60 with no kill trigger):
  post-mortems, the failure taxonomy, and the lesson e-process. **Learning
  is built last**, because a lesson is only meaningful against a calibrated
  baseline.

Deferred indefinitely: multi-horizon grids, per-symbol specialisation, and
prompt tuning. Each multiplies the trial count or resets the generation.

## Usage

```bash
python -m oracle.run predict    # snapshot, build slate, write predictions
python -m oracle.run resolve    # resolve everything past its deadline
python -m oracle.run score      # scores + the countdown report
python -m oracle.run verify     # rebuild and check the hash chain
```
