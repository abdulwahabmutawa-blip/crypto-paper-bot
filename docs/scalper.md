# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-10T13:24:01+00:00 · runs 5666 · equity **$507.55** (-49.25%) · cash $141.11 · open 7/10 · round trips 1931

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-492.47 · worst day $-50.94 · trades/day 28.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1673 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 258 | 42% | -0.57% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-10T13:05 | ZILUSDT | bottom | TARGET | 3.5 | +2.75% | $+1.28 |
| 2026-11-10T13:05 | JSTUSDT | surge | TIME | 24.0 | -1.57% | $-0.75 |
| 2026-11-10T12:13 | BEBUSDT | surge | STOP | 13.8 | -3.25% | $-1.53 |
| 2026-11-10T11:56 | SOPHUSDT | surge | TARGET | 0.0 | +2.75% | $+1.28 |
| 2026-11-10T11:39 | RENDERUSDT | surge | TIME | 24.0 | -0.63% | $-0.29 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-09T16:42 | TSLABUSDT | surge | 377.77 | 374.05 | -0.98% |
| 2026-11-09T17:34 | QQQBUSDT | surge | 678.06 | 677.05 | -0.15% |
| 2026-11-10T00:27 | ZROUSDT | bottom | 1.484 | 1.506 | +1.48% |
| 2026-11-10T00:27 | RWUSDUSDT | bottom | 0.9998 | 0.9999 | +0.01% |
| 2026-11-10T08:14 | OPGUSDT | surge | 0.1287 | 0.1284 | -0.23% |
| 2026-11-10T13:05 | XLMUSDT | bottom | 0.1454 | 0.1453 | -0.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
