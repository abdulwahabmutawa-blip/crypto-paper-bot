# The Scholar (العالِم) — bot #10 spec

**Registered 2026-07-31 (launch day), the same day the stock bot was retired.**
Canonical copy: this file, in the public repo, so it carries a git timestamp
per the project's own proof standard (kill_criteria.md). A working copy lives
in the local trading folder.

**Provenance-integrity note (honesty first):** this file was first committed
AFTER the launch-day backtests had already run — the local folder it was
drafted in is gitignored, so "spec written before the backtest" is
self-asserted, not provable by timestamp. What the git timestamp DOES prove:
the spec, its parameters, and the restated backtest numbers below were all
fixed before the bot's first live trading day ended, and no parameter was
changed after the corrected backtest was seen.

Born at the v2 review as the fleet's synthesis bot: one strategy built only
from ingredients that survived our own research. Replaces the retired stock
bot's slot (owner decision, recorded in kill_criteria.md and the journal).

## Rule

Hold the single instrument with the best vol-adjusted momentum among those in
confirmed uptrends; size the position to a volatility target; protect it with
a trailing stop; stand in cash when nothing qualifies.

- **Universe (12, cross-asset, NO leveraged ETFs):**
  SPY, QQQ, IWM, EFA, EEM, TLT, GLD, SLV, USO, DBC, BTC-USD, ETH-USD
- **Signals on each asset's NATIVE trading calendar** (crypto 365d/yr,
  equities 252d/yr — both for windows and for vol annualization)
- **Eligible:** price > its own 200-day MA AND 90-day momentum > 0
- **Score:** mom90 ÷ annualized 90-day volatility
- **Switch rule:** challenger must score > 1.25× the current holding
  (no hysteresis test if holding is ineligible or CASH)
- **Position size:** fraction = min(1, 20% ÷ instrument's annualized vol),
  set at entry; remainder stays in cash
- **Risk overlay:** 10% trailing stop from high-water mark (stop exits to
  CASH) + **5-calendar-day** re-entry cooldown on the stopped ticker only;
  Watcher SEVERE → forced cash (engine default)
- **Benchmark:** SPY buy & hold, $1,000 same day
- **Costs in backtest:** 0.1% per side

## Provenance — where each piece was earned

| Ingredient | Source | Inherited or new? |
|---|---|---|
| mom90 + MA200, standard params, no grid tuning | commodity bot (best live book); stats-lab lesson 3 (tuned params = luckiest coin flipper) | inherited |
| MA gate framed as protection, not alpha | stats-lab lesson 2 (p=0.29 return edge; maxDD −77%→−32%) | inherited |
| Vol-adjusted score (reward per unit risk) | Hunter (score = mom/vol) | concept inherited; **90d windows are a NEW choice** (Hunter used 20d, itself grid-picked) |
| Positive-momentum requirement | crypto phase ("never hold a falling asset") | inherited |
| 1.25× switch hysteresis | Hunter design; lesson 4 (costs scale with churn) | inherited |
| Vol-targeted sizing instead of all-in | Turtle concept (v2 backlog #2, untested); Hunter's −78% backtest maxDD is the all-in counterexample | concept from backlog; **the 20% number is a NEW choice** |
| 10% trailing stop + 5d cooldown | risk overlay built & verified 07-19, parked for v2 | inherited (cooldown counted in **calendar days**, as the overlay implemented it) |
| No leveraged ETFs in universe | stats-lab lesson 5 (TQQQ = beta 2.96, alpha −4.7%/yr, R²=.998) | inherited |
| Cross-asset breadth incl. bonds/commodities | all-weather (lowest DD) + Dual Momentum phase | inherited |
| 0.1%/side cost haircut in backtest | evidence review (backlog #6) | inherited |
| Expectation = half the backtest | McLean & Pontiff decay haircut (evidence review) | inherited |

## Backtest record — v1 INVALIDATED, v2 is canonical

- **v1 (retracted same day):** reported +26.2%/yr 2017+, maxDD −23.7%. The
  pre-launch adversarial review proved the lab's union equity+crypto calendar
  left every equity's MA200 permanently NaN — the "12-asset" test had
  silently run a **BTC/ETH-only rotation**. Those numbers describe a
  different strategy and are void.
- **v2 (corrected lab, native calendars, per-asset annualization, stop→CASH,
  calendar-day cooldown, 0.1%/side):**
  - 2017+: **+10.9%/yr, maxDD −29.0%** vs SPY +15.0%, −33.7% → **lagged SPY**
  - 2020+: **+16.9%/yr** vs SPY +15.0% → slight beat
  - 2024+: **+23.3%/yr, maxDD −27.6%** vs SPY +20.5%, −18.8% → slight beat,
    **worse drawdown**
- Honest reading: SPY-like, mixed by window, drawdown NOT clearly better.
  After the McLean-Pontiff haircut the expected edge is ~zero. The live run
  is the real test, same as every other bot.

## Pre-registered expectations & failure modes

- Failure mode 1: hysteresis too loose for a 12-asset board → churn → cost
  drag (watch trade legs vs commodity bot's; the lab counter counts LEGS,
  a round trip = 2).
- Failure mode 2: vol sizing + trailing stop + MA gate = triple defense →
  dead-money drift (R4 flag) in fast rebounds.
- Judged by kill_criteria.md R1–R5 like every other bot: first R2/R3 window
  ~2026-10-24, R5 ~2026-12-05. No parameter changes outside scheduled reviews.

## Known live↔lab divergences (documented, accepted)

- Lab fills at the signal day's close; live defers equity fills to regular
  hours (market-hours gate) — lab is optimistic by up to one bar.
- Cooldown is 5 CALENDAR days in both (an equity stopped Friday is only
  blocked ~2-3 trading days); single-slot memory (only the most recent
  stop-out cools down) in both.
- Engine freezes a cycle (no trade, no mark) on stale bars, dead price
  columns, or undelivered equity bars — the lab has no equivalent because
  its data is complete by construction.
