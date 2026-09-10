# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T02:07:40+00:00 · runs 399 · equity **$970.58** (-2.94%) · cash $290.41 · open 7/10 · round trips 142

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.16%/trade · realized $-22.78 · worst day $-27.16 · trades/day 23.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 88 | 52% | -0.10% | 48% | 43% | 9% |
| bottom | 54 | 46% | -0.25% | 44% | 44% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T02:05 | MINAUSDT | surge | STOP | 1.5 | -3.25% | $-3.25 |
| 2026-09-10T00:37 | SAHARAUSDT | surge | STOP | 2.0 | -3.25% | $-3.14 |
| 2026-09-10T00:20 | MINAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.72 |
| 2026-09-10T00:02 | MINAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.66 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 52.77 | -2.10% |
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1019.68 | -1.40% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 232.91 | -1.28% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 192.85 | -0.92% |
| 2026-09-09T16:47 | INTCBUSDT | surge | 106.11 | 104.38 | -1.63% |
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 132.65 | -0.05% |
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 92.21 | +0.64% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
