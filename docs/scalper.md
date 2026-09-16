# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-16T19:20:31+00:00 · runs 988 · equity **$865.20** (-13.48%) · cash $0.00 · open 10/10 · round trips 346

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.37%/trade · realized $-122.90 · worst day $-50.94 · trades/day 28.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 267 | 48% | -0.30% | 45% | 47% | 8% |
| bottom | 79 | 41% | -0.58% | 39% | 47% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-16T19:18 | SKHYBUSDT | surge | STOP | 13.5 | -3.25% | $-2.85 |
| 2026-09-16T18:45 | ZENUSDT | surge | STOP | 0.2 | -3.25% | $-3.07 |
| 2026-09-16T18:28 | NEARUSDT | surge | TARGET | 4.2 | +2.75% | $+2.56 |
| 2026-09-16T18:28 | ZENUSDT | surge | TARGET | 7.2 | +2.75% | $+2.50 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T09:55 | FFUSDT | bottom | 0.13714 | 0.13316 | -2.90% |
| 2026-09-16T10:12 | INTCBUSDT | surge | 102.11 | 99.76 | -2.30% |
| 2026-09-16T14:34 | TSLABUSDT | surge | 363.68 | 355.98 | -2.12% |
| 2026-09-16T15:10 | SPCXBUSDT | surge | 152.08 | 149.28 | -1.84% |
| 2026-09-16T15:45 | NVDABUSDT | surge | 216.32 | 212.9 | -1.58% |
| 2026-09-16T18:11 | LITEBUSDT | surge | 922.39 | 894.63 | -3.01% |
| 2026-09-16T18:28 | NEARUSDT | surge | 2.516 | 2.524 | +0.32% |
| 2026-09-16T18:45 | ASTERUSDT | surge | 0.688 | 0.685 | -0.44% |
| 2026-09-16T19:18 | RAYUSDT | surge | 1.3938 | 1.3966 | +0.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
