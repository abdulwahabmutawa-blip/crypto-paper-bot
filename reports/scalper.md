# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-11T01:05:51+00:00 · runs 5699 · equity **$506.24** (-49.38%) · cash $141.96 · open 7/10 · round trips 1942

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-494.66 · worst day $-50.94 · trades/day 28.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1681 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 261 | 42% | -0.56% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-11T01:04 | AVGOBUSDT | surge | TARGET | 8.5 | +2.75% | $+1.29 |
| 2026-11-11T00:31 | RWUSDUSDT | bottom | TIME | 24.0 | -0.25% | $-0.12 |
| 2026-11-10T23:09 | ICPUSDT | surge | TARGET | 2.5 | +2.75% | $+1.27 |
| 2026-11-10T20:50 | GRAMUSDT | surge | TARGET | 4.2 | +2.75% | $+1.29 |
| 2026-11-10T17:53 | QQQBUSDT | surge | TIME | 24.0 | -1.67% | $-0.80 |
| 2026-11-10T17:18 | MEGAUSDT | surge | STOP | 0.8 | -3.25% | $-1.52 |
| 2026-11-10T17:00 | AMDBUSDT | surge | STOP | 0.5 | -3.25% | $-1.52 |
| 2026-11-10T17:00 | SOPHUSDT | surge | STOP | 0.5 | -3.25% | $-1.52 |
| 2026-11-10T17:00 | TSLABUSDT | surge | TIME | 24.0 | -0.63% | $-0.30 |
| 2026-11-10T15:48 | XLMUSDT | bottom | STOP | 2.5 | -3.25% | $-1.53 |
| 2026-11-10T15:48 | ZROUSDT | bottom | TARGET | 14.8 | +2.75% | $+1.28 |
| 2026-11-10T13:05 | ZILUSDT | bottom | TARGET | 3.5 | +2.75% | $+1.28 |
| 2026-11-10T13:05 | JSTUSDT | surge | TIME | 24.0 | -1.57% | $-0.75 |
| 2026-11-10T12:13 | BEBUSDT | surge | STOP | 13.8 | -3.25% | $-1.53 |
| 2026-11-10T11:56 | SOPHUSDT | surge | TARGET | 0.0 | +2.75% | $+1.28 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-10T08:14 | OPGUSDT | surge | 0.1287 | 0.1279 | -0.62% |
| 2026-11-10T18:29 | GOOGLBUSDT | bottom | 285.98 | 289.1 | +1.09% |
| 2026-11-10T18:29 | BCHUSDT | bottom | 227 | 230.4 | +1.50% |
| 2026-11-10T19:57 | OPENUSDT | surge | 0.0915 | 0.0911 | -0.44% |
| 2026-11-10T23:42 | ICPUSDT | surge | 2.526 | 2.564 | +1.50% |
| 2026-11-11T00:31 | ERAUSDT | surge | 0.0812 | 0.0803 | -1.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
