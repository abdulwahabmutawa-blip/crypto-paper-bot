# Fleet Kill Criteria — pre-registered 2026-07-18

These rules are committed BEFORE seeing the results they will judge. That is
the point: decided in advance = science; decided after = excuse-making.
The git timestamp of this file is the proof of pre-registration.

**Amendment rule:** criteria may only be changed at a scheduled review, BEFORE
looking at that period's results, and any change must be committed with a
written rationale. Changing a threshold after seeing a bot's numbers voids
the discipline this file exists to protect.

Each bot's benchmark is the `bench` series already recorded in its own state
file (data/*_state.json) — the comparison it has shown on its dashboard since
day one. "pp" = percentage points. "Trading days" = days with a history entry.

## R1 — Hard stop (checked every day, applies immediately)

Equity closes below **$750** (−25% from the $1,000 start)
→ bot is RETIRED: flagged for forced-cash/removal at the earliest opportunity.
No exceptions, no "it will come back."

## R2 — Chronic underperformance (checked at scheduled reviews only)

Over a window of **at least 60 trading days**:
cumulative return trails its benchmark by **≥ 10 pp** AND absolute return is
**negative** → bot is KILLED.
(Trailing the bench while making money = benchmark was hot, bot survives.
Losing money while also losing to the bench = no reason to exist.)

## R3 — Probation (checked at scheduled reviews)

Trails its benchmark by ≥ 5 pp over the trailing 60 trading days (but not
meeting R2) → PROBATION: flagged in every supervisor brief; next review is
its R2 test. No strategy changes allowed during probation — it dies or
survives as designed.

## R4 — Dead-money flag (informational, never auto-kill)

**> 30 consecutive trading days 100% in cash** while its benchmark gained
> 5% → logic review is due (is the entry condition unreachable?). Not a kill:
correct defensiveness is a feature; a broken entry rule is a bug. Review
distinguishes them.

## R5 — Promotion (the positive case, checked at reviews)

**AMENDED 2026-07-23** — before any v2 results were examined, on external
evidence (see specs/evidence-review-2026-07.md §5). Original rule was a
per-bot bootstrap p < 0.10. That is wrong when 8-10 correlated bots compete
and the best is promoted: with 10 bots, a per-bot 10% bar promotes ~1 bot by
luck alone. Multiple testing must be corrected across the FLEET, not per bot.

Promotion to doubled paper capital ($2,000) requires ALL of:
1. **≥ 90 trading days** live, and
2. positive cumulative excess return vs its benchmark, and
3. bootstrap p-value on daily excess returns that survives a **Holm-Bonferroni
   correction across every bot tested that review** (i.e. ranked p-values
   compared against 0.10/(n), 0.10/(n-1), ... for n bots), and
4. a **Deflated Sharpe Ratio > 0** (Bailey & López de Prado) computed with
   the trial count set to the number of strategies the fleet has ever run —
   including dead ones, since they were part of the search.

Rationale for keeping a 0.10 family-wise base rather than 0.05: this is paper
capital reallocation, not a publication claim; the cost of a false promotion
is bounded and reversible via R1-R3.

Corollary (recorded so it cannot be forgotten): the fleet's BEST performer at
any review is the single least trustworthy number in the project — it is the
maximum of many draws. Judge it by these rules, never by its rank.

## Review schedule

- **2026-07-31 (v2):** first checkpoint. Sample will be ~10 trading days —
  far too small for any statistical verdict. Therefore: **no kills at v2
  except R1 hard-stop breaches.** v2 is for process upgrades (vol sizing,
  stops), scorecard baseline, and the insider-bot data decision.
- **~2026-10-10 (first kill window):** ~60 trading days live. R2/R3 verdicts
  become eligible.
- **~2026-11-20:** ~90 trading days. R5 promotions become eligible.

## Roster covered

crypto (regime switcher), stock (TQQQ MA200), meanrev, commodity, allweather,
congress, hunter, hype trader. The Watcher (sentinel) holds no capital and is
judged separately via the supervisor's judgment scoreboard (60+ scored calls,
positive cumulative alpha, per the standing agreement).
