# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-14T17:34:59+00:00 · runs 805 · equity **$905.43** (-9.46%) · cash $0.00 · open 10/10 · round trips 291

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-98.70 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 220 | 48% | -0.32% | 45% | 47% | 8% |
| bottom | 71 | 44% | -0.42% | 42% | 45% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-14T17:15 | XLMUSDT | surge | TARGET | 5.8 | +2.75% | $+2.51 |
| 2026-09-14T16:57 | JTOUSDT | surge | TARGET | 10.2 | +2.75% | $+2.50 |
| 2026-09-14T16:03 | BBUSDT | surge | STOP | 1.2 | -3.25% | $-3.27 |
| 2026-09-14T14:30 | REDUSDT | surge | TARGET | 0.2 | +2.75% | $+2.70 |
| 2026-09-14T14:14 | MSTRBUSDT | surge | TARGET | 4.0 | +2.75% | $+2.62 |
| 2026-09-14T13:08 | ZROUSDT | surge | STOP | 5.2 | -3.25% | $-2.80 |
| 2026-09-14T12:52 | TRUMPUSDT | surge | TARGET | 9.2 | +2.75% | $+2.42 |
| 2026-09-14T11:14 | LAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.44 |
| 2026-09-14T10:41 | CAKEUSDT | surge | TARGET | 6.5 | +2.75% | $+2.37 |
| 2026-09-14T10:09 | BANKUSDT | surge | TARGET | 0.5 | +2.75% | $+2.55 |
| 2026-09-14T09:20 | BANKUSDT | surge | TARGET | 1.2 | +2.75% | $+2.49 |
| 2026-09-14T07:48 | BANKUSDT | surge | TARGET | 4.8 | +2.75% | $+2.42 |
| 2026-09-14T07:31 | BABYUSDT | surge | STOP | 2.5 | -3.25% | $-2.90 |
| 2026-09-14T06:21 | CRVUSDT | surge | TARGET | 17.5 | +2.75% | $+2.43 |
| 2026-09-14T04:54 | BABYUSDT | surge | TARGET | 2.5 | +2.75% | $+2.39 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-13T17:46 | ICPUSDT | surge | 2.784 | 2.753 | -1.11% |
| 2026-09-14T00:07 | TRXUSDT | bottom | 0.3384 | 0.3409 | +0.74% |
| 2026-09-14T02:18 | AEROUSDT | surge | 0.5712 | 0.5748 | +0.63% |
| 2026-09-14T04:02 | ONDOUSDT | surge | 0.353 | 0.3568 | +1.08% |
| 2026-09-14T12:52 | XPLUSDT | surge | 0.08266 | 0.08294 | +0.34% |
| 2026-09-14T13:08 | CAKEUSDT | surge | 2.364 | 2.363 | -0.04% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 151.72 | +0.63% |
| 2026-09-14T16:57 | OPUSDT | surge | 0.1009 | 0.1032 | +2.28% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 664.15 | +0.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
