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

### v2 review record (2026-07-31)

- **stock bot RETIRED by OWNER OVERRIDE — explicitly outside these rules.**
  Final mark $892.30 (2026-07-30), weakest book (-10.8% vs bench -1.3%). R1
  was NOT breached; R2/R3 need 60 trading days. The owner directed the kill
  after seeing the standings, which the amendment rule does not permit as a
  criteria change — so it is recorded as what it is: a discretionary owner
  decision, not a rules-based kill. These criteria remain unamended and in
  force for the rest of the fleet. (For the record: at ~10 trading days the
  weakest book is mostly noise — same corollary as R5's, in the other
  direction.)
- **The Scholar ADDED (bot #10, synthesis of tested lessons)** — spec at
  reports/scholar_spec.md (registered launch day; see its
  provenance-integrity note for what the git timestamp does and does not
  prove, and its backtest record for the v1 retraction). Enters the roster
  under R1-R5 from day one; its clock starts 2026-07-31, so its first R2/R3
  window is ~2026-10-24, R5 ~2026-12-05.
- Process upgrades shipped with it: the parked trailing-stop/cooldown
  overlay and vol-target sizing now exist in selection_engine as opt-in SPEC
  config. Applied to the Scholar ONLY — meanrev/commodity keep running
  unmodified so their live experiments stay uncontaminated.
- **THE ANALYST ADDED same day (bot #11, LLM trading agent)** — the v2
  record above initially deferred the build; the owner reversed that
  deferral hours later, before any Scholar results existed. Spec was
  pre-registered 2026-07-22 (trading/specs/analyst-agent-spec.md). One
  amendment, recorded BEFORE its first decision: model launched as
  claude-opus-5 (spec said claude-sonnet-5 "to start"; model is a config
  constant logged in every decision). No backtest is possible for this bot
  by design — the live run is the test. Under R1-R5 from day one; its API
  costs are charged inside its own account. Clock starts on its first
  decision (needs the owner's ANTHROPIC_API_KEY repo secret; the agent
  skips gracefully until then).
- **~2026-10-10 (first kill window):** ~60 trading days live. R2/R3 verdicts
  become eligible.
- **~2026-11-20:** ~90 trading days. R5 promotions become eligible.

### Owner override 2026-09-04

Outside the scheduled-review rule, same as the 07-31 stock-bot kill, and
recorded as such: the owner retired **congress** ($1,003 after 37 days,
-0.9% at last full mark vs bench +2.6%; the pre-registered finding that
copying Congress does not beat the index already stood), **hunter**
($1,014 after 40 days, behind its +3.6% bench, max DD -7.3%), **analyst**
(LLM agent, 1 trade in 26 days, holding SPY; the corpus's own review rates
LLMs as verified-bad traders and its API cost is not covered by one index
trade), and confirmed **hypecrypto**'s R1 retirement ($739). Their state
files and dashboards remain as frozen archives; they leave the Actions
roster. Kept: crypto, meanrev, commodity, allweather (control), scholar,
sentiment (under audit for a suspected stale-fill inflation, see STATUS).

### Owner override 2026-09-05

Second override, recorded as such: the owner retired the four least
successful remaining bots by value at the 09-05 digest: **scholar**
($1,019.62), **allweather** ($1,023.80, the control), **commodity**
($1,031.42) and **crypto** ($1,089.97, behind BTC over the same window).
Frozen archives as before. Kept: meanrev ($1,298.52) and sentiment
($2,453.00, still under fill audit). Added **scalper** (src/bot_scalper.py):
the small-wins protocol from the lab run hyper-aggressively, 10 seats,
+3%/-3%/24h, surge + range-bottom shapes on 15m candles, never idle.
Pre-registered: judged on >= 100 round trips against a 54% break-even hit
rate; under R1-R5 like every other paper bot.

## Roster covered

crypto (regime switcher), meanrev, commodity, allweather, congress, hunter,
hype trader, scholar (from 2026-07-31), analyst (from its first decision).
Retired: stock/TQQQ MA200 (owner override 2026-07-31, see v2 record). The
Watcher (sentinel) holds no capital and is judged separately via the
supervisor's judgment scoreboard (60+ scored calls, positive cumulative
alpha, per the standing agreement).
