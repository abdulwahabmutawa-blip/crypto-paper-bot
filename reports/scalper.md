# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T12:20:44+00:00 · runs 523 · equity **$896.39** (-10.36%) · cash $0.00 · open 10/10 · round trips 184

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 43% (break-even 54%) · mean -0.55%/trade · realized $-98.74 · worst day $-50.94 · trades/day 26.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 122 | 44% | -0.58% | 41% | 52% | 7% |
| bottom | 62 | 42% | -0.50% | 40% | 47% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-11T11:28 | AEROUSDT | surge | STOP | 1.8 | -3.25% | $-3.10 |
| 2026-09-11T11:11 | ORCAUSDT | surge | STOP | 4.2 | -3.25% | $-2.92 |
| 2026-09-11T11:11 | FFUSDT | surge | STOP | 15.0 | -3.25% | $-3.02 |
| 2026-09-11T10:54 | THETAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.47 |
| 2026-09-11T10:54 | EGLDUSDT | bottom | STOP | 8.2 | -3.25% | $-2.92 |
| 2026-09-11T10:54 | EIGENUSDT | surge | STOP | 12.8 | -3.25% | $-3.01 |
| 2026-09-11T10:37 | THEUSDT | bottom | STOP | 11.8 | -3.25% | $-3.03 |
| 2026-09-11T10:03 | WLFIUSDT | surge | STOP | 12.5 | -3.25% | $-3.01 |
| 2026-09-11T09:29 | THETAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.55 |
| 2026-09-11T08:21 | RUNEUSDT | surge | STOP | 1.5 | -3.25% | $-2.92 |
| 2026-09-11T07:47 | THETAUSDT | surge | TARGET | 7.2 | +2.75% | $+2.48 |
| 2026-09-11T06:30 | XTZUSDT | surge | STOP | 1.8 | -3.25% | $-3.01 |
| 2026-09-11T05:54 | DEXEUSDT | surge | STOP | 6.0 | -3.25% | $-3.03 |
| 2026-09-11T04:44 | ORCAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.48 |
| 2026-09-11T02:58 | METUSDT | surge | STOP | 11.8 | -3.25% | $-3.02 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.781 | -1.77% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 326.21 | +0.72% |
| 2026-09-11T08:21 | KAVAUSDT | surge | 0.06512 | 0.06544 | +0.49% |
| 2026-09-11T10:37 | 0GUSDT | surge | 0.195 | 0.194 | -0.51% |
| 2026-09-11T10:54 | POLUSDT | surge | 0.09415 | 0.09306 | -1.16% |
| 2026-09-11T10:54 | ORCLBUSDT | surge | 164.06 | 161.86 | -1.34% |
| 2026-09-11T10:54 | ADAUSDT | bottom | 0.2028 | 0.2022 | -0.30% |
| 2026-09-11T11:11 | DOGSUSDT | surge | 4.927e-05 | 4.967e-05 | +0.81% |
| 2026-09-11T11:11 | LINKUSDT | bottom | 11.369 | 11.376 | +0.06% |
| 2026-09-11T11:45 | THETAUSDT | surge | 0.1953 | 0.1908 | -2.30% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
