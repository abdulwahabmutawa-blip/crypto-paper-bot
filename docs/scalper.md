# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-17T02:49:28+00:00 · runs 1015 · equity **$887.28** (-11.27%) · cash $0.00 · open 10/10 · round trips 354

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-113.76 · worst day $-50.94 · trades/day 27.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 273 | 49% | -0.26% | 46% | 46% | 8% |
| bottom | 81 | 41% | -0.57% | 40% | 47% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-17T01:19 | RAYUSDT | surge | TARGET | 5.8 | +2.75% | $+2.34 |
| 2026-09-17T00:44 | DASHUSDT | surge | TARGET | 3.8 | +2.75% | $+2.41 |
| 2026-09-17T00:26 | NEARUSDT | surge | TARGET | 3.2 | +2.75% | $+2.67 |
| 2026-09-17T00:26 | ASTERUSDT | surge | TARGET | 5.2 | +2.75% | $+2.51 |
| 2026-09-16T20:59 | NEARUSDT | surge | TARGET | 2.5 | +2.75% | $+2.60 |
| 2026-09-16T20:42 | INJUSDT | bottom | TARGET | 0.8 | +2.75% | $+2.34 |
| 2026-09-16T19:35 | LITEBUSDT | surge | STOP | 1.2 | -3.25% | $-2.83 |
| 2026-09-16T19:35 | FFUSDT | bottom | STOP | 9.5 | -3.25% | $-2.89 |
| 2026-09-16T19:18 | SKHYBUSDT | surge | STOP | 13.5 | -3.25% | $-2.85 |
| 2026-09-16T18:45 | ZENUSDT | surge | STOP | 0.2 | -3.25% | $-3.07 |
| 2026-09-16T18:28 | NEARUSDT | surge | TARGET | 4.2 | +2.75% | $+2.56 |
| 2026-09-16T18:28 | ZENUSDT | surge | TARGET | 7.2 | +2.75% | $+2.50 |
| 2026-09-16T18:11 | DASHUSDT | surge | STOP | 1.0 | -3.25% | $-2.93 |
| 2026-09-16T16:56 | BOMEUSDT | surge | STOP | 2.8 | -3.25% | $-3.02 |
| 2026-09-16T15:45 | LAUSDT | surge | STOP | 2.2 | -3.25% | $-2.76 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T10:12 | INTCBUSDT | surge | 102.11 | 102.45 | +0.33% |
| 2026-09-16T14:34 | TSLABUSDT | surge | 363.68 | 360.9 | -0.76% |
| 2026-09-16T15:10 | SPCXBUSDT | surge | 152.08 | 152.36 | +0.18% |
| 2026-09-16T15:45 | NVDABUSDT | surge | 216.32 | 215.84 | -0.22% |
| 2026-09-16T19:35 | GRAMUSDT | bottom | 1.289 | 1.316 | +2.09% |
| 2026-09-17T00:26 | WLDUSDT | surge | 0.3733 | 0.3733 | +0.00% |
| 2026-09-17T00:26 | TRUMPUSDT | surge | 1.932 | 1.944 | +0.62% |
| 2026-09-17T00:44 | AEROUSDT | surge | 0.5507 | 0.551 | +0.05% |
| 2026-09-17T01:19 | KORUBUSDT | surge | 19.19 | 18.98 | -1.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
