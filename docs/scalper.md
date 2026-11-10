# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-10T09:24:12+00:00 · runs 5652 · equity **$507.78** (-49.22%) · cash $0.00 · open 10/10 · round trips 1926

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-492.45 · worst day $-50.94 · trades/day 28.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1669 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 257 | 42% | -0.58% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-10T09:22 | DODOUSDT | surge | TIME | 24.0 | -0.08% | $-0.04 |
| 2026-11-10T08:14 | AVAXUSDT | surge | STOP | 6.2 | -3.25% | $-1.51 |
| 2026-11-10T01:51 | TUTUSDT | surge | STOP | 11.0 | -3.25% | $-1.56 |
| 2026-11-10T00:27 | BIOUSDT | surge | STOP | 8.5 | -3.25% | $-1.56 |
| 2026-11-10T00:27 | RWUSDUSDT | bottom | TIME | 24.0 | -0.23% | $-0.11 |
| 2026-11-09T22:26 | BNBUSDT | bottom | TIME | 24.0 | +1.16% | $+0.54 |
| 2026-11-09T17:34 | ENJUSDT | surge | STOP | 3.2 | -3.25% | $-1.60 |
| 2026-11-09T16:42 | HYPEUSDT | bottom | TARGET | 17.0 | +2.75% | $+1.28 |
| 2026-11-09T14:44 | AMDBUSDT | surge | TARGET | 3.0 | +2.75% | $+1.29 |
| 2026-11-09T14:44 | SPCXBUSDT | surge | TARGET | 12.5 | +2.75% | $+1.28 |
| 2026-11-09T14:10 | BIOUSDT | surge | TARGET | 1.0 | +2.75% | $+1.32 |
| 2026-11-09T12:45 | CHIPUSDT | surge | TARGET | 1.2 | +2.75% | $+1.29 |
| 2026-11-09T12:45 | ARBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.29 |
| 2026-11-09T10:29 | PORTALUSDT | surge | TARGET | 1.2 | +2.75% | $+1.28 |
| 2026-11-09T09:14 | DODOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.26 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-09T11:20 | RENDERUSDT | surge | 1.589 | 1.584 | -0.31% |
| 2026-11-09T12:45 | JSTUSDT | surge | 0.14623 | 0.1444 | -1.25% |
| 2026-11-09T16:42 | TSLABUSDT | surge | 377.77 | 376.36 | -0.37% |
| 2026-11-09T17:34 | QQQBUSDT | surge | 678.06 | 678 | -0.01% |
| 2026-11-09T22:26 | BEBUSDT | surge | 196.71 | 194.39 | -1.18% |
| 2026-11-10T00:27 | ZROUSDT | bottom | 1.484 | 1.512 | +1.89% |
| 2026-11-10T00:27 | RWUSDUSDT | bottom | 0.9998 | 0.9999 | +0.01% |
| 2026-11-10T08:14 | OPGUSDT | surge | 0.1287 | 0.1306 | +1.48% |
| 2026-11-10T09:22 | ZILUSDT | bottom | 0.001603 | 0.001609 | +0.37% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
