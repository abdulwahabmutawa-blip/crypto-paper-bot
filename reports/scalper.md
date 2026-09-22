# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T11:46:09+00:00 · runs 1484 · equity **$950.18** (-4.98%) · cash $0.00 · open 10/10 · round trips 533

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-57.67 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 444 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 89 | 42% | -0.54% | 39% | 46% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T11:44 | BROCCOLI714USDT | surge | TARGET | 0.0 | +2.75% | $+2.66 |
| 2026-09-22T11:27 | BANKUSDT | surge | STOP | 19.2 | -3.25% | $-3.25 |
| 2026-09-22T10:35 | XPLUSDT | bottom | STOP | 0.2 | -3.25% | $-3.16 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T14:28 | BCHUSDT | surge | 267.7 | 270.8 | +1.16% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 378.34 | +1.01% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 608.12 | -0.22% |
| 2026-09-21T17:17 | QQQBUSDT | surge | 738.89 | 741.84 | +0.40% |
| 2026-09-22T06:32 | PROVEUSDT | bottom | 0.2277 | 0.2292 | +0.66% |
| 2026-09-22T09:26 | TSTUSDT | surge | 0.0184 | 0.01869 | +1.58% |
| 2026-09-22T09:26 | TUTUSDT | surge | 0.02334 | 0.02384 | +2.14% |
| 2026-09-22T10:35 | KITEUSDT | surge | 0.1323 | 0.1324 | +0.08% |
| 2026-09-22T11:44 | AVAUSDT | surge | 0.2666 | 0.2703 | +1.39% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
