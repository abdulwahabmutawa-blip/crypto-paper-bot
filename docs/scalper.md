# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T08:21:41+00:00 · runs 859 · equity **$883.28** (-11.67%) · cash $0.00 · open 10/10 · round trips 308

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.37%/trade · realized $-109.87 · worst day $-50.94 · trades/day 28.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 236 | 47% | -0.35% | 44% | 47% | 8% |
| bottom | 72 | 43% | -0.42% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-15T08:03 | VANAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-15T07:59 | XLMUSDT | surge | STOP | 13.8 | -3.25% | $-3.09 |
| 2026-09-15T07:26 | CAKEUSDT | surge | STOP | 18.0 | -3.25% | $-2.71 |
| 2026-09-15T04:26 | REDUSDT | surge | TARGET | 0.5 | +2.75% | $+2.32 |
| 2026-09-15T04:09 | MSTRBUSDT | surge | STOP | 10.0 | -3.25% | $-3.11 |
| 2026-09-15T03:37 | LAUSDT | surge | STOP | 0.0 | -3.25% | $-2.91 |
| 2026-09-15T03:37 | UNIUSDT | surge | STOP | 1.2 | -3.25% | $-2.79 |
| 2026-09-15T03:37 | SAGAUSDT | surge | STOP | 3.0 | -3.25% | $-2.81 |
| 2026-09-15T03:20 | TREEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
| 2026-09-15T03:20 | OPUSDT | surge | STOP | 7.2 | -3.25% | $-3.02 |
| 2026-09-15T02:31 | AEROUSDT | surge | TIME | 24.0 | -1.63% | $-1.44 |
| 2026-09-15T02:09 | FLOKIUSDT | surge | STOP | 5.2 | -3.25% | $-2.88 |
| 2026-09-15T00:24 | TRXUSDT | bottom | TIME | 24.0 | -0.49% | $-0.42 |
| 2026-09-14T20:31 | ONDOUSDT | surge | TARGET | 16.2 | +2.75% | $+2.37 |
| 2026-09-14T19:55 | XPLUSDT | surge | TARGET | 6.8 | +2.75% | $+2.49 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 148.25 | -1.67% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 658.76 | -0.75% |
| 2026-09-15T03:20 | JSTUSDT | surge | 0.11522 | 0.11525 | +0.03% |
| 2026-09-15T03:37 | BANKUSDT | bottom | 0.0274 | 0.0272 | -0.73% |
| 2026-09-15T03:37 | GRAMUSDT | bottom | 1.341 | 1.341 | +0.00% |
| 2026-09-15T04:09 | DODOUSDT | surge | 0.01822 | 0.01787 | -1.92% |
| 2026-09-15T04:26 | FETUSDT | bottom | 0.1619 | 0.1583 | -2.22% |
| 2026-09-15T07:26 | COTIUSDT | surge | 0.01704 | 0.01732 | +1.64% |
| 2026-09-15T08:20 | SAGAUSDT | surge | 0.01906 | 0.01875 | -1.63% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
