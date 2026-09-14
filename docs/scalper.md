# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-14T20:15:51+00:00 · runs 814 · equity **$909.57** (-9.04%) · cash $0.00 · open 10/10 · round trips 294

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-94.30 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 223 | 48% | -0.30% | 45% | 47% | 9% |
| bottom | 71 | 44% | -0.42% | 42% | 45% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-14T07:48 | BANKUSDT | surge | TARGET | 4.8 | +2.75% | $+2.42 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T00:07 | TRXUSDT | bottom | 0.3384 | 0.3406 | +0.65% |
| 2026-09-14T02:18 | AEROUSDT | surge | 0.5712 | 0.5805 | +1.63% |
| 2026-09-14T04:02 | ONDOUSDT | surge | 0.353 | 0.362 | +2.55% |
| 2026-09-14T13:08 | CAKEUSDT | surge | 2.364 | 2.385 | +0.89% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 148.06 | -1.80% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 665.18 | +0.22% |
| 2026-09-14T17:50 | MSTRBUSDT | surge | 136.73 | 136.97 | +0.18% |
| 2026-09-14T18:08 | XLMUSDT | surge | 0.1966 | 0.1952 | -0.71% |
| 2026-09-14T19:55 | OPUSDT | surge | 0.1035 | 0.1046 | +1.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
