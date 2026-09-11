# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T00:05:42+00:00 · runs 479 · equity **$928.38** (-7.16%) · cash $90.35 · open 9/10 · round trips 168

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.44%/trade · realized $-72.70 · worst day $-50.94 · trades/day 28.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 109 | 46% | -0.48% | 42% | 50% | 7% |
| bottom | 59 | 44% | -0.36% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T23:47 | RAYUSDT | surge | STOP | 0.0 | -3.25% | $-3.03 |
| 2026-09-10T22:42 | CRCLBUSDT | bottom | TIME | 24.0 | -1.96% | $-1.90 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-10T14:59 | METUSDT | surge | 0.217 | 0.2151 | -0.88% |
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.953 | +1.16% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 325.76 | +0.58% |
| 2026-09-10T19:51 | FFUSDT | surge | 0.16816 | 0.16992 | +1.05% |
| 2026-09-10T21:17 | WLFIUSDT | surge | 0.0565 | 0.0562 | -0.53% |
| 2026-09-10T21:17 | REZUSDT | bottom | 0.003125 | 0.003114 | -0.35% |
| 2026-09-10T21:50 | EIGENUSDT | surge | 0.2177 | 0.2142 | -1.61% |
| 2026-09-10T22:42 | THEUSDT | bottom | 0.0663 | 0.0663 | +0.00% |
| 2026-09-10T23:31 | DEXEUSDT | surge | 1.906 | 1.939 | +1.73% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
