# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T02:49:22+00:00 · runs 838 · equity **$894.72** (-10.53%) · cash $0.00 · open 10/10 · round trips 298

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-96.66 · worst day $-50.94 · trades/day 27.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 226 | 48% | -0.30% | 45% | 46% | 9% |
| bottom | 72 | 43% | -0.42% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-15T02:31 | AEROUSDT | surge | TIME | 24.0 | -1.63% | $-1.44 |
| 2026-09-15T02:09 | FLOKIUSDT | surge | STOP | 5.2 | -3.25% | $-2.88 |
| 2026-09-15T00:24 | TRXUSDT | bottom | TIME | 24.0 | -0.49% | $-0.42 |
| 2026-09-14T20:31 | ONDOUSDT | surge | TARGET | 16.2 | +2.75% | $+2.37 |
| 2026-09-14T19:55 | XPLUSDT | surge | TARGET | 6.8 | +2.75% | $+2.49 |
| 2026-09-14T18:08 | ICPUSDT | surge | TIME | 24.0 | -0.68% | $-0.65 |
| 2026-09-14T17:50 | OPUSDT | surge | TARGET | 0.8 | +2.75% | $+2.56 |
| 2026-09-14T17:15 | XLMUSDT | surge | TARGET | 5.8 | +2.75% | $+2.51 |
| 2026-09-14T16:57 | JTOUSDT | surge | TARGET | 10.2 | +2.75% | $+2.50 |
| 2026-09-14T16:03 | BBUSDT | surge | STOP | 1.2 | -3.25% | $-3.27 |
| 2026-09-14T14:30 | REDUSDT | surge | TARGET | 0.2 | +2.75% | $+2.70 |
| 2026-09-14T14:14 | MSTRBUSDT | surge | TARGET | 4.0 | +2.75% | $+2.62 |
| 2026-09-14T13:08 | ZROUSDT | surge | STOP | 5.2 | -3.25% | $-2.80 |
| 2026-09-14T12:52 | TRUMPUSDT | surge | TARGET | 9.2 | +2.75% | $+2.42 |
| 2026-09-14T11:14 | LAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.44 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T13:08 | CAKEUSDT | surge | 2.364 | 2.325 | -1.65% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 148.89 | -1.25% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 662.92 | -0.12% |
| 2026-09-14T17:50 | MSTRBUSDT | surge | 136.73 | 133.67 | -2.24% |
| 2026-09-14T18:08 | XLMUSDT | surge | 0.1966 | 0.1959 | -0.36% |
| 2026-09-14T19:55 | OPUSDT | surge | 0.1035 | 0.101 | -2.42% |
| 2026-09-15T00:24 | SAGAUSDT | surge | 0.01876 | 0.01886 | +0.53% |
| 2026-09-15T02:09 | UNIUSDT | surge | 6.678 | 6.595 | -1.24% |
| 2026-09-15T02:31 | TREEUSDT | surge | 0.0453 | 0.045 | -0.66% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
