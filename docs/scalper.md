# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T05:40:49+00:00 · runs 2071 · equity **$907.09** (-9.29%) · cash $0.00 · open 10/10 · round trips 766

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-89.87 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 653 | 53% | -0.06% | 50% | 43% | 7% |
| bottom | 113 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29T05:39 | DODOUSDT | surge | STOP | 13.8 | -3.25% | $-2.90 |
| 2026-09-29T04:01 | ICPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.62 |
| 2026-09-29T04:01 | MINAUSDT | surge | STOP | 4.5 | -3.25% | $-2.99 |
| 2026-09-29T04:01 | ALGOUSDT | surge | TARGET | 8.2 | +2.75% | $+2.63 |
| 2026-09-29T03:44 | CRVUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-29T02:55 | PROMUSDT | surge | STOP | 13.5 | -3.25% | $-3.03 |
| 2026-09-29T02:39 | RUNEUSDT | surge | STOP | 6.8 | -3.25% | $-3.11 |
| 2026-09-28T23:32 | LINKUSDT | surge | TARGET | 3.5 | +2.75% | $+2.25 |
| 2026-09-28T23:15 | CRVUSDT | surge | TARGET | 1.5 | +2.75% | $+2.46 |
| 2026-09-28T21:35 | NMRUSDT | surge | STOP | 0.2 | -3.25% | $-3.01 |
| 2026-09-28T21:01 | LINEAUSDT | surge | STOP | 1.2 | -3.25% | $-3.11 |
| 2026-09-28T19:55 | WUSDT | bottom | STOP | 5.0 | -3.25% | $-2.74 |
| 2026-09-28T19:37 | ALGOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.54 |
| 2026-09-28T19:37 | 牛来USDT | surge | TARGET | 0.5 | +2.75% | $+2.48 |
| 2026-09-28T19:37 | NIGHTUSDT | surge | TARGET | 4.8 | +2.75% | $+2.63 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 228.31 | +0.18% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.13027 | +0.73% |
| 2026-09-28T19:37 | XLMUSDT | surge | 0.2289 | 0.2225 | -2.80% |
| 2026-09-28T23:32 | GRAMUSDT | bottom | 1.574 | 1.548 | -1.65% |
| 2026-09-29T02:55 | CRCLBUSDT | bottom | 85 | 85.14 | +0.16% |
| 2026-09-29T04:01 | CRVUSDT | surge | 0.3859 | 0.3878 | +0.49% |
| 2026-09-29T04:01 | ICPUSDT | surge | 3.234 | 3.251 | +0.53% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 145.65 | -0.12% |
| 2026-09-29T05:39 | CVXUSDT | surge | 2.268 | 2.247 | -0.93% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
