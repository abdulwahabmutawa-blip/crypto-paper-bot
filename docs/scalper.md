# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-16T18:13:33+00:00 · runs 984 · equity **$881.32** (-11.87%) · cash $0.00 · open 10/10 · round trips 342

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.37%/trade · realized $-122.03 · worst day $-50.94 · trades/day 28.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 263 | 48% | -0.31% | 45% | 47% | 8% |
| bottom | 79 | 41% | -0.58% | 39% | 47% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-16T18:11 | DASHUSDT | surge | STOP | 1.0 | -3.25% | $-2.93 |
| 2026-09-16T16:56 | BOMEUSDT | surge | STOP | 2.8 | -3.25% | $-3.02 |
| 2026-09-16T15:45 | LAUSDT | surge | STOP | 2.2 | -3.25% | $-2.76 |
| 2026-09-16T15:10 | HBARUSDT | bottom | STOP | 9.2 | -3.25% | $-2.85 |
| 2026-09-16T14:34 | HEIUSDT | surge | TARGET | 0.0 | +2.75% | $+2.46 |
| 2026-09-16T14:17 | SOXLBUSDT | surge | TARGET | 7.0 | +2.75% | $+2.39 |
| 2026-09-16T13:59 | DASHUSDT | surge | TARGET | 2.0 | +2.75% | $+2.48 |
| 2026-09-16T13:59 | NEARUSDT | surge | TARGET | 3.0 | +2.75% | $+2.50 |
| 2026-09-16T13:24 | AAVEUSDT | bottom | STOP | 7.0 | -3.25% | $-2.85 |
| 2026-09-16T11:52 | ZECUSDT | surge | TARGET | 4.2 | +2.75% | $+2.42 |
| 2026-09-16T10:29 | HEIUSDT | surge | TARGET | 0.2 | +2.75% | $+2.45 |
| 2026-09-16T10:29 | MARSCOINUSDT | surge | TARGET | 1.2 | +2.75% | $+2.42 |
| 2026-09-16T10:12 | PUNDIXUSDT | surge | STOP | 0.8 | -3.25% | $-2.85 |
| 2026-09-16T09:55 | ACEUSDT | bottom | TARGET | 4.0 | +2.75% | $+2.41 |
| 2026-09-16T07:24 | ZECUSDT | surge | TARGET | 1.5 | +2.75% | $+2.41 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T05:40 | SKHYBUSDT | surge | 178.8 | 176.95 | -1.03% |
| 2026-09-16T09:55 | FFUSDT | bottom | 0.13714 | 0.13492 | -1.62% |
| 2026-09-16T10:12 | INTCBUSDT | surge | 102.11 | 102.21 | +0.10% |
| 2026-09-16T10:45 | ZENUSDT | surge | 6.48 | 6.714 | +3.61% |
| 2026-09-16T13:59 | NEARUSDT | surge | 2.47 | 2.544 | +3.00% |
| 2026-09-16T14:34 | TSLABUSDT | surge | 363.68 | 360.84 | -0.78% |
| 2026-09-16T15:10 | SPCXBUSDT | surge | 152.08 | 151.08 | -0.66% |
| 2026-09-16T15:45 | NVDABUSDT | surge | 216.32 | 215.85 | -0.22% |
| 2026-09-16T18:11 | LITEBUSDT | surge | 922.39 | 932.99 | +1.15% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
