# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T13:16:23+00:00 · runs 527 · equity **$907.22** (-9.28%) · cash $0.00 · open 10/10 · round trips 189

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.53%/trade · realized $-97.32 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 126 | 44% | -0.57% | 41% | 52% | 6% |
| bottom | 63 | 43% | -0.45% | 41% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-11T13:14 | DOGSUSDT | surge | TARGET | 1.8 | +2.75% | $+2.43 |
| 2026-09-11T13:14 | ADAUSDT | bottom | TARGET | 2.0 | +2.75% | $+2.46 |
| 2026-09-11T13:14 | POLUSDT | surge | TARGET | 2.2 | +2.75% | $+2.46 |
| 2026-09-11T12:52 | THETAUSDT | surge | STOP | 0.8 | -3.25% | $-3.00 |
| 2026-09-11T12:52 | 0GUSDT | surge | STOP | 2.0 | -3.25% | $-2.94 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.886 | +0.02% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 326.23 | +0.73% |
| 2026-09-11T08:21 | KAVAUSDT | surge | 0.06512 | 0.06522 | +0.15% |
| 2026-09-11T10:54 | ORCLBUSDT | surge | 164.06 | 163.81 | -0.15% |
| 2026-09-11T11:11 | LINKUSDT | bottom | 11.369 | 11.656 | +2.52% |
| 2026-09-11T12:52 | SOXLBUSDT | surge | 119.88 | 121.47 | +1.33% |
| 2026-09-11T12:52 | BMNRBUSDT | surge | 24.62 | 24.7 | +0.32% |
| 2026-09-11T13:14 | DOGSUSDT | surge | 5.069e-05 | 5.013e-05 | -1.10% |
| 2026-09-11T13:14 | POLUSDT | surge | 0.09563 | 0.09693 | +1.36% |
| 2026-09-11T13:14 | MORPHOUSDT | surge | 2.375 | 2.373 | -0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
