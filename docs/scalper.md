# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T08:50:10+00:00 · runs 423 · equity **$964.10** (-3.59%) · cash $95.74 · open 9/10 · round trips 144

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.19%/trade · realized $-27.97 · worst day $-27.16 · trades/day 24.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 89 | 52% | -0.13% | 47% | 44% | 9% |
| bottom | 55 | 45% | -0.29% | 44% | 44% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T03:56 | LTCUSDT | bottom | TIME | 24.0 | -2.09% | $-2.04 |
| 2026-09-10T03:21 | SAHARAUSDT | surge | STOP | 0.0 | -3.25% | $-3.15 |
| 2026-09-10T02:05 | MINAUSDT | surge | STOP | 1.5 | -3.25% | $-3.25 |
| 2026-09-10T00:37 | SAHARAUSDT | surge | STOP | 2.0 | -3.25% | $-3.14 |
| 2026-09-10T00:20 | MINAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.72 |
| 2026-09-10T00:02 | MINAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.66 |
| 2026-09-09T23:09 | LITEBUSDT | surge | STOP | 8.8 | -3.25% | $-3.30 |
| 2026-09-09T22:17 | XVGUSDT | surge | STOP | 2.2 | -3.25% | $-3.18 |
| 2026-09-09T22:17 | DODOUSDT | surge | STOP | 7.0 | -3.25% | $-3.29 |
| 2026-09-09T22:17 | HBARUSDT | bottom | STOP | 21.0 | -3.25% | $-3.27 |
| 2026-09-09T20:03 | NEARUSDT | surge | STOP | 6.2 | -3.25% | $-3.24 |
| 2026-09-09T19:46 | PYTHUSDT | surge | STOP | 3.8 | -3.25% | $-3.29 |
| 2026-09-09T16:47 | COTIUSDT | surge | TARGET | 0.0 | +2.75% | $+2.62 |
| 2026-09-09T16:30 | HOLOUSDT | surge | STOP | 6.0 | -3.25% | $-3.20 |
| 2026-09-09T15:54 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.71 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1019.99 | -1.37% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 232.06 | -1.64% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 192.43 | -1.14% |
| 2026-09-09T16:47 | INTCBUSDT | surge | 106.11 | 104.66 | -1.37% |
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 131.61 | -0.83% |
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 91.65 | +0.03% |
| 2026-09-10T03:56 | ENAUSDT | bottom | 0.1503 | 0.1494 | -0.60% |
| 2026-09-10T07:14 | VETUSDT | surge | 0.00802 | 0.007984 | -0.45% |
| 2026-09-10T08:30 | CKBUSDT | surge | 0.001209 | 0.0012 | -0.74% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
