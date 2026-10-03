# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-03T19:02:29+00:00 · runs 2461 · equity **$852.92** (-14.71%) · cash $0.00 · open 10/10 · round trips 936

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-142.63 · worst day $-50.94 · trades/day 32.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 810 | 52% | -0.12% | 49% | 44% | 7% |
| bottom | 126 | 46% | -0.38% | 40% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-03T18:08 | STXUSDT | surge | STOP | 1.0 | -3.25% | $-2.79 |
| 2026-10-03T18:08 | CRCLBUSDT | bottom | TIME | 24.0 | +1.33% | $+1.13 |
| 2026-10-03T17:51 | SUPERUSDT | surge | STOP | 1.5 | -3.25% | $-3.21 |
| 2026-10-03T17:34 | JTOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.36 |
| 2026-10-03T17:17 | BNBUSDT | bottom | TARGET | 22.2 | +2.75% | $+2.29 |
| 2026-10-03T16:59 | STXUSDT | surge | TARGET | 2.5 | +2.75% | $+2.30 |
| 2026-10-03T16:42 | ZROUSDT | surge | STOP | 0.0 | -3.25% | $-2.88 |
| 2026-10-03T16:25 | AVAUSDT | surge | STOP | 0.5 | -3.25% | $-2.97 |
| 2026-10-03T16:08 | SPCXBUSDT | surge | TIME | 24.0 | +0.92% | $+0.90 |
| 2026-10-03T15:50 | ARUSDT | surge | STOP | 3.0 | -3.25% | $-2.64 |
| 2026-10-03T15:33 | TSLABUSDT | surge | TIME | 24.0 | -0.32% | $-0.30 |
| 2026-10-03T14:59 | SUPERUSDT | surge | TARGET | 0.8 | +2.75% | $+2.30 |
| 2026-10-03T13:27 | SYNUSDT | surge | STOP | 5.2 | -3.25% | $-2.65 |
| 2026-10-03T13:27 | DODOUSDT | surge | TIME | 24.0 | -1.64% | $-1.47 |
| 2026-10-03T12:00 | RAYUSDT | surge | TARGET | 3.0 | +2.75% | $+2.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-03T01:28 | SNDKBUSDT | bottom | 1718.8 | 1715.58 | -0.19% |
| 2026-10-03T03:31 | INJUSDT | surge | 7.685 | 7.609 | -0.99% |
| 2026-10-03T14:59 | IOUSDT | surge | 0.1665 | 0.1649 | -0.96% |
| 2026-10-03T15:50 | MORPHOUSDT | surge | 2.724 | 2.725 | +0.04% |
| 2026-10-03T17:17 | BNBUSDT | surge | 789.96 | 789.53 | -0.05% |
| 2026-10-03T17:34 | TRBUSDT | surge | 20.91 | 20.87 | -0.19% |
| 2026-10-03T17:51 | ATOMUSDT | surge | 1.733 | 1.716 | -0.98% |
| 2026-10-03T18:08 | ZKUSDT | surge | 0.01311 | 0.01304 | -0.53% |
| 2026-10-03T18:08 | OPUSDT | surge | 0.1355 | 0.1338 | -1.25% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
