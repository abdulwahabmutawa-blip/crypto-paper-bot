# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T12:36:21+00:00 · runs 436 · equity **$939.83** (-6.02%) · cash $189.95 · open 8/10 · round trips 151

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-44.10 · worst day $-27.16 · trades/day 25.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 96 | 49% | -0.30% | 45% | 47% | 8% |
| bottom | 55 | 45% | -0.29% | 44% | 44% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T12:16 | INTCBUSDT | surge | STOP | 19.2 | -3.25% | $-3.18 |
| 2026-09-10T12:16 | MRVLBUSDT | surge | STOP | 20.2 | -3.25% | $-3.20 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1001.09 | -3.19% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 189.64 | -2.57% |
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 129.92 | -2.10% |
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 90.43 | -1.30% |
| 2026-09-10T03:56 | ENAUSDT | bottom | 0.1503 | 0.1482 | -1.40% |
| 2026-09-10T10:49 | RUNEUSDT | surge | 0.498 | 0.489 | -1.81% |
| 2026-09-10T11:41 | FFUSDT | surge | 0.15745 | 0.15517 | -1.45% |
| 2026-09-10T11:58 | ETHFIUSDT | surge | 0.6458 | 0.6271 | -2.90% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
