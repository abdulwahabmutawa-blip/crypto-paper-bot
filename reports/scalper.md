# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-14T14:53:30+00:00 · runs 796 · equity **$896.80** (-10.32%) · cash $0.00 · open 10/10 · round trips 288

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-100.42 · worst day $-50.94 · trades/day 28.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 217 | 47% | -0.34% | 44% | 47% | 8% |
| bottom | 71 | 44% | -0.42% | 42% | 45% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-14T03:45 | ARUSDT | surge | STOP | 1.0 | -3.25% | $-2.94 |
| 2026-09-14T03:45 | LAUSDT | surge | STOP | 1.2 | -3.25% | $-2.86 |
| 2026-09-14T03:23 | CAKEUSDT | surge | TARGET | 7.5 | +2.75% | $+2.36 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-13T17:46 | ICPUSDT | surge | 2.784 | 2.733 | -1.83% |
| 2026-09-14T00:07 | TRXUSDT | bottom | 0.3384 | 0.3411 | +0.80% |
| 2026-09-14T02:18 | AEROUSDT | surge | 0.5712 | 0.5745 | +0.58% |
| 2026-09-14T04:02 | ONDOUSDT | surge | 0.353 | 0.3517 | -0.37% |
| 2026-09-14T06:21 | JTOUSDT | surge | 0.4401 | 0.4414 | +0.30% |
| 2026-09-14T11:14 | XLMUSDT | surge | 0.189 | 0.1898 | +0.42% |
| 2026-09-14T12:52 | XPLUSDT | surge | 0.08266 | 0.08112 | -1.86% |
| 2026-09-14T13:08 | CAKEUSDT | surge | 2.364 | 2.373 | +0.38% |
| 2026-09-14T14:30 | BBUSDT | surge | 0.0085 | 0.0084 | -1.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
