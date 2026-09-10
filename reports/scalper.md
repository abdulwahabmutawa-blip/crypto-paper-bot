# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T19:36:16+00:00 · runs 462 · equity **$937.13** (-6.29%) · cash $275.89 · open 7/10 · round trips 163

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.44%/trade · realized $-69.89 · worst day $-48.13 · trades/day 27.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 106 | 46% | -0.46% | 42% | 50% | 8% |
| bottom | 57 | 44% | -0.39% | 42% | 46% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T19:34 | SPCXBUSDT | surge | STOP | 3.2 | -3.25% | $-3.07 |
| 2026-09-10T18:13 | KAVAUSDT | surge | STOP | 2.0 | -3.25% | $-3.07 |
| 2026-09-10T16:52 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.56 |
| 2026-09-10T16:20 | VETUSDT | surge | STOP | 0.5 | -3.25% | $-3.02 |
| 2026-09-10T15:48 | SAGAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.56 |
| 2026-09-10T13:09 | FFUSDT | surge | STOP | 1.2 | -3.25% | $-3.01 |
| 2026-09-10T13:09 | RUNEUSDT | surge | STOP | 2.0 | -3.25% | $-3.01 |
| 2026-09-10T13:09 | ENAUSDT | bottom | STOP | 9.0 | -3.25% | $-3.11 |
| 2026-09-10T13:09 | MSTRBUSDT | bottom | STOP | 16.8 | -3.25% | $-3.13 |
| 2026-09-10T12:51 | ETHFIUSDT | surge | STOP | 0.8 | -3.25% | $-3.01 |
| 2026-09-10T12:51 | SKHYBUSDT | surge | STOP | 21.0 | -3.25% | $-3.20 |
| 2026-09-10T12:51 | MUBUSDT | surge | STOP | 21.5 | -3.25% | $-3.29 |
| 2026-09-10T12:16 | INTCBUSDT | surge | STOP | 19.2 | -3.25% | $-3.18 |
| 2026-09-10T12:16 | MRVLBUSDT | surge | STOP | 20.2 | -3.25% | $-3.20 |
| 2026-09-10T10:49 | VETUSDT | surge | STOP | 3.5 | -3.25% | $-3.11 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 91 | -0.68% |
| 2026-09-10T14:59 | METUSDT | surge | 0.217 | 0.2179 | +0.41% |
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.986 | +1.72% |
| 2026-09-10T14:59 | DOTUSDT | bottom | 1.083 | 1.102 | +1.75% |
| 2026-09-10T15:31 | FFUSDT | surge | 0.1649 | 0.16855 | +2.21% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 325.61 | +0.53% |
| 2026-09-10T18:30 | ETHFIUSDT | surge | 0.6981 | 0.7094 | +1.62% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
