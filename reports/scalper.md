# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T02:15:56+00:00 · runs 836 · equity **$897.07** (-10.29%) · cash $0.00 · open 10/10 · round trips 297

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-95.23 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 225 | 48% | -0.30% | 45% | 47% | 8% |
| bottom | 72 | 43% | -0.42% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-14T10:41 | CAKEUSDT | surge | TARGET | 6.5 | +2.75% | $+2.37 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T02:18 | AEROUSDT | surge | 0.5712 | 0.5639 | -1.28% |
| 2026-09-14T13:08 | CAKEUSDT | surge | 2.364 | 2.333 | -1.31% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 148.87 | -1.26% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 663.24 | -0.07% |
| 2026-09-14T17:50 | MSTRBUSDT | surge | 136.73 | 134.14 | -1.89% |
| 2026-09-14T18:08 | XLMUSDT | surge | 0.1966 | 0.1959 | -0.36% |
| 2026-09-14T19:55 | OPUSDT | surge | 0.1035 | 0.1024 | -1.06% |
| 2026-09-15T00:24 | SAGAUSDT | surge | 0.01876 | 0.01862 | -0.75% |
| 2026-09-15T02:09 | UNIUSDT | surge | 6.678 | 6.647 | -0.46% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
