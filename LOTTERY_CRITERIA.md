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
