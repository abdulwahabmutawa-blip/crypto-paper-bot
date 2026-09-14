# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-14T21:32:01+00:00 · runs 819 · equity **$903.34** (-9.67%) · cash $0.00 · open 10/10 · round trips 295

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.32%/trade · realized $-91.92 · worst day $-50.94 · trades/day 29.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 224 | 48% | -0.29% | 45% | 46% | 8% |
| bottom | 71 | 44% | -0.42% | 42% | 45% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-14T10:09 | BANKUSDT | surge | TARGET | 0.5 | +2.75% | $+2.55 |
| 2026-09-14T09:20 | BANKUSDT | surge | TARGET | 1.2 | +2.75% | $+2.49 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T00:07 | TRXUSDT | bottom | 0.3384 | 0.3393 | +0.27% |
| 2026-09-14T02:18 | AEROUSDT | surge | 0.5712 | 0.573 | +0.32% |
| 2026-09-14T13:08 | CAKEUSDT | surge | 2.364 | 2.355 | -0.38% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 148.36 | -1.60% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 664.43 | +0.11% |
| 2026-09-14T17:50 | MSTRBUSDT | surge | 136.73 | 136.6 | -0.10% |
| 2026-09-14T18:08 | XLMUSDT | surge | 0.1966 | 0.1937 | -1.48% |
| 2026-09-14T19:55 | OPUSDT | surge | 0.1035 | 0.1031 | -0.39% |
| 2026-09-14T20:31 | FLOKIUSDT | surge | 2.526e-05 | 2.48e-05 | -1.82% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
