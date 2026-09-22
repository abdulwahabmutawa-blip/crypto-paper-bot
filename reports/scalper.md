# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T07:43:47+00:00 · runs 1470 · equity **$944.57** (-5.54%) · cash $0.00 · open 10/10 · round trips 525

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-49.53 · worst day $-50.94 · trades/day 29.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 437 | 54% | -0.00% | 50% | 42% | 8% |
| bottom | 88 | 42% | -0.50% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T06:32 | ONEUSDT | bottom | STOP | 0.0 | -3.25% | $-3.32 |
| 2026-09-22T06:16 | BROCCOLI714USDT | surge | TARGET | 0.0 | +2.75% | $+2.73 |
| 2026-09-22T05:59 | BONKUSDT | surge | TARGET | 0.8 | +2.75% | $+2.66 |
| 2026-09-22T05:10 | SHIBUSDT | surge | STOP | 0.5 | -3.25% | $-3.25 |
| 2026-09-22T04:21 | DOGEUSDT | surge | TARGET | 7.0 | +2.75% | $+2.75 |
| 2026-09-22T04:21 | FLOKIUSDT | surge | TARGET | 11.5 | +2.75% | $+2.60 |
| 2026-09-21T21:10 | PENGUUSDT | surge | STOP | 1.2 | -3.25% | $-3.36 |
| 2026-09-21T19:43 | BTCUSDT | surge | TARGET | 10.0 | +2.75% | $+2.77 |
| 2026-09-21T17:17 | LPTUSDT | surge | TARGET | 11.8 | +2.75% | $+2.49 |
| 2026-09-21T16:44 | ARKMUSDT | surge | STOP | 2.8 | -3.25% | $-3.17 |
| 2026-09-21T16:11 | XPLUSDT | surge | STOP | 2.0 | -3.25% | $-3.17 |
| 2026-09-21T15:55 | BANKUSDT | surge | TARGET | 2.5 | +2.75% | $+2.67 |
| 2026-09-21T15:39 | SNDKBUSDT | surge | STOP | 6.2 | -3.25% | $-2.94 |
| 2026-09-21T14:28 | SOXLBUSDT | surge | TARGET | 5.8 | +2.75% | $+2.75 |
| 2026-09-21T14:28 | TRXUSDT | surge | TIME | 24.0 | -0.74% | $-0.67 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T13:53 | MUBUSDT | surge | 1060.18 | 1037.74 | -2.12% |
| 2026-09-21T14:28 | BCHUSDT | surge | 267.7 | 264.9 | -1.05% |
| 2026-09-21T14:28 | LTCUSDT | surge | 62.05 | 60.71 | -2.16% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 377.28 | +0.72% |
| 2026-09-21T15:55 | BANKUSDT | surge | 0.0352 | 0.0346 | -1.70% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 612.35 | +0.48% |
| 2026-09-21T17:17 | QQQBUSDT | surge | 738.89 | 741.27 | +0.32% |
| 2026-09-22T04:21 | FILUSDT | surge | 1.005 | 0.9925 | -1.24% |
| 2026-09-22T06:32 | PROVEUSDT | bottom | 0.2277 | 0.2296 | +0.83% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
