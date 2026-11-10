# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-10T18:13:37+00:00 · runs 5675 · equity **$501.34** (-49.87%) · cash $230.38 · open 5/10 · round trips 1938

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-498.39 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1678 | 48% | -0.33% | 46% | 48% | 7% |
| bottom | 260 | 42% | -0.56% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-10T11:39 | RENDERUSDT | surge | TIME | 24.0 | -0.63% | $-0.29 |
| 2026-11-10T09:22 | DODOUSDT | surge | TIME | 24.0 | -0.08% | $-0.04 |
| 2026-11-10T08:14 | AVAXUSDT | surge | STOP | 6.2 | -3.25% | $-1.51 |
| 2026-11-10T01:51 | TUTUSDT | surge | STOP | 11.0 | -3.25% | $-1.56 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-10T00:27 | RWUSDUSDT | bottom | 0.9998 | 0.9994 | -0.04% |
| 2026-11-10T08:14 | OPGUSDT | surge | 0.1287 | 0.1283 | -0.31% |
| 2026-11-10T16:24 | AVGOBUSDT | surge | 329.06 | 327.09 | -0.60% |
| 2026-11-10T16:24 | GRAMUSDT | surge | 1.107 | 1.111 | +0.36% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
