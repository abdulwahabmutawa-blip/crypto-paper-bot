# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T10:19:46+00:00 · runs 1479 · equity **$946.98** (-5.30%) · cash $0.00 · open 10/10 · round trips 530

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-53.92 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 442 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 88 | 42% | -0.50% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T10:00 | KITEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.60 |
| 2026-09-22T09:26 | TSTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.57 |
| 2026-09-22T09:26 | FILUSDT | surge | STOP | 4.8 | -3.25% | $-3.25 |
| 2026-09-22T08:51 | LTCUSDT | surge | STOP | 18.2 | -3.25% | $-3.14 |
| 2026-09-22T08:34 | MUBUSDT | surge | STOP | 18.5 | -3.25% | $-3.17 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T14:28 | BCHUSDT | surge | 267.7 | 268.8 | +0.41% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 378.11 | +0.95% |
| 2026-09-21T15:55 | BANKUSDT | surge | 0.0352 | 0.0342 | -2.84% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 612.44 | +0.49% |
| 2026-09-21T17:17 | QQQBUSDT | surge | 738.89 | 742.5 | +0.49% |
| 2026-09-22T06:32 | PROVEUSDT | bottom | 0.2277 | 0.2321 | +1.93% |
| 2026-09-22T09:26 | TSTUSDT | surge | 0.0184 | 0.01843 | +0.16% |
| 2026-09-22T09:26 | TUTUSDT | surge | 0.02334 | 0.02343 | +0.39% |
| 2026-09-22T10:00 | XPLUSDT | bottom | 0.09511 | 0.09429 | -0.86% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
