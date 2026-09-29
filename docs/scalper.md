# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T09:41:09+00:00 · runs 2086 · equity **$923.74** (-7.63%) · cash $0.00 · open 10/10 · round trips 773

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-77.54 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 660 | 53% | -0.04% | 50% | 43% | 7% |
| bottom | 113 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29T09:39 | CVXUSDT | surge | TARGET | 3.8 | +2.75% | $+2.37 |
| 2026-09-29T08:30 | CELOUSDT | surge | TARGET | 2.0 | +2.75% | $+2.65 |
| 2026-09-29T07:56 | AAVEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.65 |
| 2026-09-29T06:44 | CRVUSDT | surge | TARGET | 2.2 | +2.75% | $+2.61 |
| 2026-09-29T06:28 | PHAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.55 |
| 2026-09-29T06:28 | ICPUSDT | surge | TARGET | 2.0 | +2.75% | $+2.61 |
| 2026-09-29T05:55 | XLMUSDT | surge | STOP | 10.0 | -3.25% | $-3.11 |
| 2026-09-29T05:39 | DODOUSDT | surge | STOP | 13.8 | -3.25% | $-2.90 |
| 2026-09-29T04:01 | ICPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.62 |
| 2026-09-29T04:01 | MINAUSDT | surge | STOP | 4.5 | -3.25% | $-2.99 |
| 2026-09-29T04:01 | ALGOUSDT | surge | TARGET | 8.2 | +2.75% | $+2.63 |
| 2026-09-29T03:44 | CRVUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-29T02:55 | PROMUSDT | surge | STOP | 13.5 | -3.25% | $-3.03 |
| 2026-09-29T02:39 | RUNEUSDT | surge | STOP | 6.8 | -3.25% | $-3.11 |
| 2026-09-28T23:32 | LINKUSDT | surge | TARGET | 3.5 | +2.75% | $+2.25 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 230.47 | +1.13% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.13041 | +0.84% |
| 2026-09-28T23:32 | GRAMUSDT | bottom | 1.574 | 1.582 | +0.51% |
| 2026-09-29T02:55 | CRCLBUSDT | bottom | 85 | 86.58 | +1.86% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 146.69 | +0.59% |
| 2026-09-29T06:44 | CRVUSDT | surge | 0.3959 | 0.4002 | +1.09% |
| 2026-09-29T07:56 | ICPUSDT | surge | 3.386 | 3.312 | -2.19% |
| 2026-09-29T08:30 | CELOUSDT | surge | 0.10681 | 0.10504 | -1.66% |
| 2026-09-29T09:39 | 币安人生USDT | surge | 0.5147 | 0.5122 | -0.49% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
