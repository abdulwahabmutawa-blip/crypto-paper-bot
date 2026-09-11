# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T08:23:26+00:00 · runs 509 · equity **$912.25** (-8.78%) · cash $0.00 · open 10/10 · round trips 175

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.48%/trade · realized $-82.74 · worst day $-50.94 · trades/day 25.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 115 | 45% | -0.52% | 42% | 51% | 7% |
| bottom | 60 | 43% | -0.41% | 42% | 45% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-10T19:34 | SPCXBUSDT | surge | STOP | 3.2 | -3.25% | $-3.07 |
| 2026-09-10T18:13 | KAVAUSDT | surge | STOP | 2.0 | -3.25% | $-3.07 |
| 2026-09-10T16:52 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.56 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.973 | +1.50% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 326.21 | +0.72% |
| 2026-09-10T19:51 | FFUSDT | surge | 0.16816 | 0.16651 | -0.98% |
| 2026-09-10T21:17 | WLFIUSDT | surge | 0.0565 | 0.0556 | -1.59% |
| 2026-09-10T21:50 | EIGENUSDT | surge | 0.2177 | 0.2137 | -1.84% |
| 2026-09-10T22:42 | THEUSDT | bottom | 0.0663 | 0.0656 | -1.06% |
| 2026-09-11T02:23 | EGLDUSDT | bottom | 4.794 | 4.74 | -1.13% |
| 2026-09-11T06:30 | ORCAUSDT | surge | 1.453 | 1.435 | -1.24% |
| 2026-09-11T07:47 | THETAUSDT | surge | 0.1867 | 0.1864 | -0.16% |
| 2026-09-11T08:21 | KAVAUSDT | surge | 0.06512 | 0.06533 | +0.32% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
