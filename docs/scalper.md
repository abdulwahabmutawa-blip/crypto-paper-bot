# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T21:19:07+00:00 · runs 469 · equity **$933.11** (-6.69%) · cash $278.14 · open 7/10 · round trips 166

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.41%/trade · realized $-67.77 · worst day $-46.01 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 108 | 46% | -0.46% | 43% | 50% | 7% |
| bottom | 58 | 45% | -0.34% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T21:17 | DOTUSDT | bottom | TARGET | 6.2 | +2.75% | $+2.56 |
| 2026-09-10T20:44 | ETHFIUSDT | surge | STOP | 2.0 | -3.25% | $-3.00 |
| 2026-09-10T19:51 | FFUSDT | surge | TARGET | 4.0 | +2.75% | $+2.56 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 90.16 | -1.59% |
| 2026-09-10T14:59 | METUSDT | surge | 0.217 | 0.2172 | +0.09% |
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 6 | +1.95% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 325.95 | +0.64% |
| 2026-09-10T19:51 | FFUSDT | surge | 0.16816 | 0.16879 | +0.37% |
| 2026-09-10T21:17 | WLFIUSDT | surge | 0.0565 | 0.0564 | -0.18% |
| 2026-09-10T21:17 | REZUSDT | bottom | 0.003125 | 0.003116 | -0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
