# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-14T10:43:11+00:00 · runs 780 · equity **$892.29** (-10.77%) · cash $0.00 · open 10/10 · round trips 283

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.39%/trade · realized $-107.80 · worst day $-50.94 · trades/day 28.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 212 | 47% | -0.38% | 43% | 48% | 8% |
| bottom | 71 | 44% | -0.42% | 42% | 45% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-14T02:50 | SAGAUSDT | bottom | TARGET | 4.5 | +2.75% | $+2.35 |
| 2026-09-14T02:34 | PEPEUSDT | bottom | TARGET | 4.0 | +2.75% | $+2.42 |
| 2026-09-14T02:18 | LAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.39 |
| 2026-09-14T00:07 | PUMPUSDT | bottom | STOP | 1.8 | -3.25% | $-2.78 |
| 2026-09-13T22:29 | ALGOUSDT | surge | STOP | 0.8 | -3.25% | $-2.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-13T17:46 | ICPUSDT | surge | 2.784 | 2.764 | -0.72% |
| 2026-09-14T00:07 | TRXUSDT | bottom | 0.3384 | 0.3406 | +0.65% |
| 2026-09-14T02:18 | AEROUSDT | surge | 0.5712 | 0.5748 | +0.63% |
| 2026-09-14T03:23 | TRUMPUSDT | surge | 2.003 | 1.999 | -0.20% |
| 2026-09-14T04:02 | ONDOUSDT | surge | 0.353 | 0.3562 | +0.91% |
| 2026-09-14T06:21 | JTOUSDT | surge | 0.4401 | 0.4387 | -0.32% |
| 2026-09-14T07:31 | ZROUSDT | surge | 1.043 | 1.037 | -0.58% |
| 2026-09-14T10:09 | MSTRBUSDT | surge | 132.09 | 131.7 | -0.30% |
| 2026-09-14T10:41 | LAUSDT | surge | 0.0696 | 0.0697 | +0.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
