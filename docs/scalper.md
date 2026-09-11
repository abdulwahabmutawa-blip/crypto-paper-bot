# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T10:39:07+00:00 · runs 517 · equity **$906.17** (-9.38%) · cash $0.00 · open 10/10 · round trips 178

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.50%/trade · realized $-86.24 · worst day $-50.94 · trades/day 25.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 117 | 45% | -0.52% | 42% | 51% | 7% |
| bottom | 61 | 43% | -0.46% | 41% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-11T10:37 | THEUSDT | bottom | STOP | 11.8 | -3.25% | $-3.03 |
| 2026-09-11T10:03 | WLFIUSDT | surge | STOP | 12.5 | -3.25% | $-3.01 |
| 2026-09-11T09:29 | THETAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.55 |
| 2026-09-11T08:21 | RUNEUSDT | surge | STOP | 1.5 | -3.25% | $-2.92 |
| 2026-09-11T07:47 | THETAUSDT | surge | TARGET | 7.2 | +2.75% | $+2.48 |
| 2026-09-11T06:30 | XTZUSDT | surge | STOP | 1.8 | -3.25% | $-3.01 |
| 2026-09-11T05:54 | DEXEUSDT | surge | STOP | 6.0 | -3.25% | $-3.03 |
| 2026-09-11T04:44 | ORCAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.48 |
| 2026-09-11T02:58 | METUSDT | surge | STOP | 11.8 | -3.25% | $-3.02 |
| 2026-09-11T02:23 | REZUSDT | bottom | STOP | 4.8 | -3.25% | $-3.01 |
| 2026-09-10T23:47 | RAYUSDT | surge | STOP | 0.0 | -3.25% | $-3.03 |
| 2026-09-10T22:42 | CRCLBUSDT | bottom | TIME | 24.0 | -1.96% | $-1.90 |
| 2026-09-10T21:17 | DOTUSDT | bottom | TARGET | 6.2 | +2.75% | $+2.56 |
| 2026-09-10T20:44 | ETHFIUSDT | surge | STOP | 2.0 | -3.25% | $-3.00 |
| 2026-09-10T19:51 | FFUSDT | surge | TARGET | 4.0 | +2.75% | $+2.56 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.891 | +0.10% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 325.8 | +0.59% |
| 2026-09-10T19:51 | FFUSDT | surge | 0.16816 | 0.1651 | -1.82% |
| 2026-09-10T21:50 | EIGENUSDT | surge | 0.2177 | 0.2108 | -3.17% |
| 2026-09-11T02:23 | EGLDUSDT | bottom | 4.794 | 4.669 | -2.61% |
| 2026-09-11T06:30 | ORCAUSDT | surge | 1.453 | 1.414 | -2.68% |
| 2026-09-11T08:21 | KAVAUSDT | surge | 0.06512 | 0.06548 | +0.55% |
| 2026-09-11T09:29 | AEROUSDT | surge | 0.5603 | 0.5522 | -1.45% |
| 2026-09-11T10:03 | THETAUSDT | surge | 0.1884 | 0.1921 | +1.96% |
| 2026-09-11T10:37 | 0GUSDT | surge | 0.195 | 0.1956 | +0.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
