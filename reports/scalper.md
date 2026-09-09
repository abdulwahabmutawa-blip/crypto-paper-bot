# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T23:11:56+00:00 · runs 389 · equity **$977.03** (-2.30%) · cash $98.21 · open 9/10 · round trips 138

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.15%/trade · realized $-21.76 · worst day $-27.16 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 84 | 52% | -0.09% | 48% | 43% | 10% |
| bottom | 54 | 46% | -0.25% | 44% | 44% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-09T23:09 | LITEBUSDT | surge | STOP | 8.8 | -3.25% | $-3.30 |
| 2026-09-09T22:17 | XVGUSDT | surge | STOP | 2.2 | -3.25% | $-3.18 |
| 2026-09-09T22:17 | DODOUSDT | surge | STOP | 7.0 | -3.25% | $-3.29 |
| 2026-09-09T22:17 | HBARUSDT | bottom | STOP | 21.0 | -3.25% | $-3.27 |
| 2026-09-09T20:03 | NEARUSDT | surge | STOP | 6.2 | -3.25% | $-3.24 |
| 2026-09-09T19:46 | PYTHUSDT | surge | STOP | 3.8 | -3.25% | $-3.29 |
| 2026-09-09T16:47 | COTIUSDT | surge | TARGET | 0.0 | +2.75% | $+2.62 |
| 2026-09-09T16:30 | HOLOUSDT | surge | STOP | 6.0 | -3.25% | $-3.20 |
| 2026-09-09T15:54 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.71 |
| 2026-09-09T15:36 | XTZUSDT | surge | STOP | 0.2 | -3.25% | $-3.29 |
| 2026-09-09T15:36 | MINAUSDT | surge | STOP | 1.0 | -3.25% | $-3.29 |
| 2026-09-09T15:36 | INTCBUSDT | surge | TIME | 24.0 | +1.00% | $+0.99 |
| 2026-09-09T15:13 | XTZUSDT | surge | TARGET | 0.8 | +2.75% | $+2.79 |
| 2026-09-09T15:13 | IOUSDT | surge | STOP | 2.8 | -3.25% | $-3.50 |
| 2026-09-09T15:13 | SPCXBUSDT | surge | STOP | 21.8 | -3.25% | $-3.18 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 53.02 | -1.63% |
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1023.98 | -0.98% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 234.46 | -0.62% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 196.76 | +1.09% |
| 2026-09-09T16:47 | INTCBUSDT | surge | 106.11 | 105.4 | -0.67% |
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 132.74 | +0.02% |
| 2026-09-09T22:17 | MINAUSDT | surge | 0.0915 | 0.0906 | -0.98% |
| 2026-09-09T22:17 | SAHARAUSDT | surge | 0.01043 | 0.01062 | +1.82% |
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 92.32 | +0.76% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
