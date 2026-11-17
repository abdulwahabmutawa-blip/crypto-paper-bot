# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-17T02:38:10+00:00 · runs 6180 · equity **$498.54** (-50.15%) · cash $0.00 · open 10/10 · round trips 2034

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-502.28 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1754 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 280 | 42% | -0.51% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-17T02:19 | MSTRBUSDT | surge | TIME | 24.0 | -0.29% | $-0.13 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-16T13:33 | DODOUSDT | surge | 0.03287 | 0.03357 | +2.13% |
| 2026-11-16T16:12 | ATOMUSDT | surge | 1.329 | 1.329 | +0.00% |
| 2026-11-16T19:10 | XPLUSDT | surge | 0.04537 | 0.04488 | -1.08% |
| 2026-11-16T19:59 | ZAMAUSDT | surge | 0.05652 | 0.05714 | +1.10% |
| 2026-11-16T21:19 | ERAUSDT | surge | 0.0749 | 0.0751 | +0.27% |
| 2026-11-17T00:21 | MMTUSDT | surge | 0.1119 | 0.1126 | +0.63% |
| 2026-11-17T01:46 | PHAUSDT | surge | 0.0333 | 0.0331 | -0.60% |
| 2026-11-17T02:02 | PUMPUSDT | bottom | 0.002766 | 0.002759 | -0.25% |
| 2026-11-17T02:19 | QNTUSDT | bottom | 152.98 | 152.54 | -0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
