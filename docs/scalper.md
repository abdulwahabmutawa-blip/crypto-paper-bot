# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T12:00:52+00:00 · runs 434 · equity **$948.49** (-5.15%) · cash $0.00 · open 10/10 · round trips 149

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.25%/trade · realized $-37.71 · worst day $-27.16 · trades/day 24.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 94 | 50% | -0.23% | 46% | 46% | 9% |
| bottom | 55 | 45% | -0.29% | 44% | 44% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T10:49 | VETUSDT | surge | STOP | 3.5 | -3.25% | $-3.11 |
| 2026-09-10T10:15 | REUSDT | surge | STOP | 0.0 | -3.25% | $-3.05 |
| 2026-09-10T09:57 | RAYUSDT | surge | STOP | 0.2 | -3.25% | $-3.06 |
| 2026-09-10T09:40 | DODOUSDT | surge | TARGET | 0.0 | +2.75% | $+2.59 |
| 2026-09-10T09:22 | CKBUSDT | surge | STOP | 0.5 | -3.25% | $-3.11 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1008.72 | -2.46% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 228.87 | -2.99% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 191.24 | -1.75% |
| 2026-09-09T16:47 | INTCBUSDT | surge | 106.11 | 103.39 | -2.56% |
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 131.32 | -1.05% |
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 91.46 | -0.17% |
| 2026-09-10T03:56 | ENAUSDT | bottom | 0.1503 | 0.1493 | -0.67% |
| 2026-09-10T10:49 | RUNEUSDT | surge | 0.498 | 0.496 | -0.40% |
| 2026-09-10T11:41 | FFUSDT | surge | 0.15745 | 0.15527 | -1.38% |
| 2026-09-10T11:58 | ETHFIUSDT | surge | 0.6458 | 0.6411 | -0.73% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
