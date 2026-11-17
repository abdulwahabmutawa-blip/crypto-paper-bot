# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-17T02:04:28+00:00 · runs 6178 · equity **$501.55** (-49.84%) · cash $0.00 · open 10/10 · round trips 2033

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-502.15 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1753 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 280 | 42% | -0.51% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-17T02:02 | ICPUSDT | surge | STOP | 7.0 | -3.25% | $-1.50 |
| 2026-11-17T01:46 | ZROUSDT | surge | TARGET | 9.5 | +2.75% | $+1.24 |
| 2026-11-17T00:21 | GRAMUSDT | bottom | TARGET | 10.0 | +2.75% | $+1.24 |
| 2026-11-16T21:19 | SAGAUSDT | surge | TIME | 24.0 | +0.74% | $+0.33 |
| 2026-11-16T19:59 | ZAMAUSDT | surge | TARGET | 3.5 | +2.75% | $+1.24 |
| 2026-11-16T19:10 | PHAUSDT | surge | TARGET | 1.0 | +2.75% | $+1.31 |
| 2026-11-16T18:54 | SOXSBUSDT | surge | TARGET | 2.5 | +2.75% | $+1.24 |
| 2026-11-16T17:50 | SENTUSDT | surge | TARGET | 8.0 | +2.75% | $+1.27 |
| 2026-11-16T16:12 | PEPEUSDT | bottom | TARGET | 7.5 | +2.75% | $+1.23 |
| 2026-11-16T16:12 | TRXUSDT | bottom | TIME | 24.0 | -0.12% | $-0.05 |
| 2026-11-16T13:17 | PROMUSDT | surge | STOP | 11.8 | -3.25% | $-1.48 |
| 2026-11-16T12:28 | NBISBUSDT | bottom | STOP | 4.5 | -3.25% | $-1.52 |
| 2026-11-16T12:28 | SOXSBUSDT | surge | TARGET | 6.2 | +2.75% | $+1.21 |
| 2026-11-16T12:28 | BMNRBUSDT | surge | STOP | 9.5 | -3.25% | $-1.50 |
| 2026-11-16T09:14 | SENTUSDT | surge | TARGET | 12.5 | +2.75% | $+1.24 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-16T02:01 | MSTRBUSDT | surge | 102.8 | 103.24 | +0.43% |
| 2026-11-16T13:33 | DODOUSDT | surge | 0.03287 | 0.03367 | +2.43% |
| 2026-11-16T16:12 | ATOMUSDT | surge | 1.329 | 1.331 | +0.15% |
| 2026-11-16T19:10 | XPLUSDT | surge | 0.04537 | 0.04562 | +0.55% |
| 2026-11-16T19:59 | ZAMAUSDT | surge | 0.05652 | 0.05731 | +1.40% |
| 2026-11-16T21:19 | ERAUSDT | surge | 0.0749 | 0.076 | +1.47% |
| 2026-11-17T00:21 | MMTUSDT | surge | 0.1119 | 0.1142 | +2.06% |
| 2026-11-17T01:46 | PHAUSDT | surge | 0.0333 | 0.0331 | -0.60% |
| 2026-11-17T02:02 | PUMPUSDT | bottom | 0.002766 | 0.002773 | +0.25% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
