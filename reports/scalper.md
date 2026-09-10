# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T20:46:24+00:00 · runs 467 · equity **$932.27** (-6.77%) · cash $367.94 · open 6/10 · round trips 165

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.43%/trade · realized $-70.33 · worst day $-48.57 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 108 | 46% | -0.46% | 43% | 50% | 7% |
| bottom | 57 | 44% | -0.39% | 42% | 46% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-10T12:16 | INTCBUSDT | surge | STOP | 19.2 | -3.25% | $-3.18 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 90.21 | -1.54% |
| 2026-09-10T14:59 | METUSDT | surge | 0.217 | 0.2164 | -0.28% |
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.988 | +1.75% |
| 2026-09-10T14:59 | DOTUSDT | bottom | 1.083 | 1.106 | +2.12% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 326.19 | +0.71% |
| 2026-09-10T19:51 | FFUSDT | surge | 0.16816 | 0.16829 | +0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
