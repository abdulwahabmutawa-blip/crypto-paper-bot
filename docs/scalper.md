# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T04:44:03+00:00 · runs 845 · equity **$890.69** (-10.93%) · cash $0.00 · open 10/10 · round trips 305

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.36%/trade · realized $-106.60 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 233 | 47% | -0.34% | 44% | 47% | 9% |
| bottom | 72 | 43% | -0.42% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-14T18:08 | ICPUSDT | surge | TIME | 24.0 | -0.68% | $-0.65 |
| 2026-09-14T17:50 | OPUSDT | surge | TARGET | 0.8 | +2.75% | $+2.56 |
| 2026-09-14T17:15 | XLMUSDT | surge | TARGET | 5.8 | +2.75% | $+2.51 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T13:08 | CAKEUSDT | surge | 2.364 | 2.338 | -1.10% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 148.5 | -1.51% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 662.04 | -0.25% |
| 2026-09-14T18:08 | XLMUSDT | surge | 0.1966 | 0.1926 | -2.03% |
| 2026-09-15T03:20 | JSTUSDT | surge | 0.11522 | 0.11511 | -0.10% |
| 2026-09-15T03:37 | BANKUSDT | bottom | 0.0274 | 0.0275 | +0.36% |
| 2026-09-15T03:37 | GRAMUSDT | bottom | 1.341 | 1.345 | +0.30% |
| 2026-09-15T04:09 | DODOUSDT | surge | 0.01822 | 0.01847 | +1.37% |
| 2026-09-15T04:26 | FETUSDT | bottom | 0.1619 | 0.1621 | +0.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
