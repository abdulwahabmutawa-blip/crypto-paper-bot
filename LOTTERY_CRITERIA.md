# Lottery book — pre-committed finish lines (OWNER-ACCEPTED 2026-08-20)

Set at the 2026-08-20 scorecard review and accepted verbatim by the owner,
so that no red candle at 2am ever gets to renegotiate them.

## Stop line (enforced in code)
**Percentage form since 2026-08-21 (owner decision: "amount of money
should not matter — we are focusing on creating a successful strategy").**
If the book's managed value falls **below 62.5% of its own peak value**
(a −37.5% drawdown — exactly what the original $25-of-$40 line encoded),
the book takes **no new entries** (binance_live.book_floor_reason; exits
still run so no seat is ever trapped) and the experiment owes a **full
post-mortem** before any restart or top-up: what the record says about
every signal, what was structural vs market, and whether the thesis
deserves more capital. Deposits raise the peak automatically, so the
protection is identical at any capital scale and no rule in this system
references a dollar amount.

## Success marker
The thesis is "catch an explosion early and hold it": the marker is the
**first revival-sourced trade ratcheted past +30%**. Fee-scratch wins do
not count; that is the event this book exists for.

## Checkpoint
**2026-09-30**, regardless of P&L: full review of every signal's record,
the Oracle's first resolved cohort (windows close 2026-09-16), and a
keep/stop/resize decision by the owner.

## Wave-day entry rule (accepted same review)
A breadth wave-day grants **one extra daily entry** (base 3 + 1), once per
UTC day, read from the scout's breadth file while fresh. Rationale: 64% of
explosions cluster within a day of a mass-trough (2-year study, n=1,908),
and the 08-20 wave found the daily budget already spent on scratch trades
hours before breadth fired. Pre-registered at the review — deliberately
not invented mid-wave.

## Wave-aware LATE cap (owner-directed, 2026-08-27)

The late-entry run-up cap is now regime-conditioned: **15% off the 24h low
normally, 25% while a breadth wave is active** (same freshness condition as
the wave-day +1 entry). Basis: replay of all 48 guard refusals since 08-19
under the live exit stack (arm +10%, stop -6%) — refused-LATE entries made
+1.72% mean, 22/39 wins, with every large winner a wave-day mover; the same
replay's dead-tape half shows no edge, so the wider cap stays wave-gated.

**Pre-registered review at the 2026-09-30 checkpoint:** judge all real
entries admitted in the 15–25% band (they are identifiable from the ledger's
entry run-up) on their own record. If their net P&L is negative, the wave
cap reverts to a flat 15%. Criterion set before outcomes, per house rule.

## TURBO MODE (owner-directed, 2026-08-28)

Owner decision, made with the 08-27 evidence in hand and against its
recommendation — recorded, not litigated: the book runs aggressive.
`data/TURBO_MODE` (phone-deletable) flips it: gate advisory, best-score
hunting, 8 entries/day, 1h cooldown, 25% LATE cap, hop-if-25%-better with
three frictions (30min min hold, no hopping out of dips >-3%, cooldown
stamps). Unchanged: $25 floor, -6%/-10% stops, ratchet, depth/announcement/
unlock vetoes, severe+stale grounding, watcher bench.

**Pre-registered evaluation, set before outcomes:** after **20 turbo round
trips** or at the **09-30 checkpoint**, whichever first: turbo keeps running
only if its own realized net (sum of pnl_usd on trades entered while turbo)
is **positive after fees**. Negative → delete the flag file and the gate
resumes. Every realized trade now records its entry_score so the picks are
attributable. The per-trade learning loop: scout scorecard (labels),
exit_auditor (post-exit paths), repeat-loser retirement, cooldown stamps.

## Forensics response (owner decisions, 2026-08-31)

Basis: the 35-trade forensic study (17 agents + 3-skeptic panel, artifact
"Lottery Bot Forensics"). Owner chose: keep turbo's speed, revoke its
benched-signal privilege; ship the exit deletions only (the 8% trail stays
un-shipped as in-sample until forward-tested).

1. **actionable=TRUE is a hard entry requirement in every mode.** Benched-
   taken-by-turbo: 6 trades, -$4.95, both biggest losses. Turbo keeps
   8/day, 1h cooldown, 25% LATE cap, hop.
2. **Hype-faded no longer market-sells.** It tightens the leash to 6% off
   peak and lets price confirm (-$10.41 forward P&L as a market sell; sold
   PUMP -1.9% before +47%). grok-STALE grounding untouched — iron rule.
3. **CLIMAX needs >=4 closed post-entry candles AND MFE >= +5%** (UNI: fired
   on one candle of "move history", sold within 1% of the local low).
4. **FUEL GONE ineligible before hour 4** (winners' median first +15% takes
   88h; an hour-two volume lull is not a dead thesis).

Turbo's pre-registered 20-RT evaluation continues unchanged — trades 1-11
(net -$4.96) stand in its record; the bench revocation applies from RT 12.
Open items from the study, deliberately NOT shipped today: 8% trail
(forward-test as candidate), multi-day promotion (shadow-test only),
watcher-lane bench (moot while watcher stays benched), VWAP fill cap,
refusal-streak veto, book cap decision (owner must choose), and
LOTTERY_EXCHANGE_STOPS=1 (owner flips on the VPS — SHIP FIRST rec).

## Golden ticket through the breaker (owner amendment, 2026-08-31)

Owner: "it's ok to stop for a while, but a high-percentage, low-risk
opportunity should not be missed." Encoded with PROVEN keys only — score
and Grok sentiment are explicitly not keys (forensics: corr(score,pnl)
+0.09; hype lane owned every disaster):

- The loss-count breaker becomes overridable for **one entry per UTC day**,
  taken only by an **actionable** candidate that is EITHER on an **active
  breadth wave** OR a **revival** signal, passing every normal guard, and
  never a symbol that already lost money today.
- The **-10% day-loss line and the API-burst freeze stay absolute** (the
  day-loss check now runs first so it can never be masked).
- No turbo-hops while halted (a sell during a halt cannot be re-bought).
- Every use is ledger-tagged `breaker_override`. **Pre-registered
  evaluation: at 09-30 or after 6 override trades, whichever first — the
  ticket survives only if its own net P&L is positive.**
