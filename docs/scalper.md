# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T03:46:19+00:00 · runs 2064 · equity **$910.13** (-8.99%) · cash $0.00 · open 10/10 · round trips 762

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-89.24 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 649 | 53% | -0.05% | 50% | 43% | 7% |
| bottom | 113 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-28T19:37 | MSTRBUSDT | bottom | TARGET | 13.8 | +2.75% | $+2.60 |
| 2026-09-28T17:20 | LINKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.48 |
| 2026-09-28T16:47 | LINKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.37 |
| 2026-09-28T16:31 | ADAUSDT | bottom | TARGET | 1.2 | +2.75% | $+2.45 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 228.7 | +0.35% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.12874 | -0.46% |
| 2026-09-28T15:42 | DODOUSDT | surge | 0.01887 | 0.01846 | -2.17% |
| 2026-09-28T19:37 | ALGOUSDT | surge | 0.1337 | 0.1375 | +2.84% |
| 2026-09-28T19:37 | XLMUSDT | surge | 0.2289 | 0.2256 | -1.44% |
| 2026-09-28T23:15 | MINAUSDT | surge | 0.1483 | 0.1468 | -1.01% |
| 2026-09-28T23:32 | GRAMUSDT | bottom | 1.574 | 1.556 | -1.14% |
| 2026-09-29T02:55 | CRCLBUSDT | bottom | 85 | 85.21 | +0.25% |
| 2026-09-29T03:44 | ICPUSDT | surge | 3.139 | 3.196 | +1.82% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
