# Lottery book — pre-committed finish lines (OWNER-ACCEPTED 2026-08-20)

Set at the 2026-08-20 scorecard review and accepted verbatim by the owner,
so that no red candle at 2am ever gets to renegotiate them.

## Stop line (enforced in code)
If the book's managed value closes **below $25**, the book takes **no new
entries** (binance_live.book_floor_reason; exits still run so no seat is
ever trapped) and the experiment owes a **full post-mortem** before any
restart or top-up: what the record says about every signal, what was
structural vs market, and whether the thesis deserves more capital.

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
