# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-25T18:40:58+00:00 · runs 6764 · equity **$482.92** (-51.71%) · cash $0.00 · open 10/10 · round trips 2214

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-520.23 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1901 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 313 | 42% | -0.51% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-25T18:38 | QQQBUSDT | bottom | TARGET | 2.0 | +2.75% | $+1.19 |
| 2026-11-25T18:38 | NVDABUSDT | bottom | TARGET | 2.0 | +2.75% | $+1.19 |
| 2026-11-25T18:21 | WLFIUSDT | surge | TARGET | 1.8 | +2.75% | $+1.19 |
| 2026-11-25T18:03 | 牛来USDT | surge | TARGET | 1.5 | +2.75% | $+1.19 |
| 2026-11-25T17:45 | ANTBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.19 |
| 2026-11-25T17:28 | XPLUSDT | surge | TARGET | 0.2 | +2.75% | $+1.19 |
| 2026-11-25T17:28 | SQQQBUSDT | surge | STOP | 0.8 | -3.25% | $-1.40 |
| 2026-11-25T15:06 | SOLUSDT | bottom | STOP | 6.5 | -3.25% | $-1.42 |
| 2026-11-25T14:48 | ICPUSDT | bottom | STOP | 10.8 | -3.25% | $-1.43 |
| 2026-11-25T13:37 | ALICEUSDT | surge | STOP | 2.5 | -3.25% | $-1.42 |
| 2026-11-25T13:37 | ERAUSDT | surge | STOP | 4.8 | -3.25% | $-1.43 |
| 2026-11-25T13:37 | AAVEUSDT | bottom | TIME | 24.0 | -1.82% | $-0.79 |
| 2026-11-25T07:47 | TAOUSDT | bottom | STOP | 9.5 | -3.25% | $-1.43 |
| 2026-11-25T07:29 | USUALUSDT | surge | STOP | 0.2 | -3.25% | $-1.44 |
| 2026-11-25T06:21 | USUALUSDT | surge | TARGET | 1.2 | +2.75% | $+1.21 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-25T16:17 | GOOGLBUSDT | bottom | 265.1 | 271.07 | +2.25% |
| 2026-11-25T16:35 | SENTUSDT | surge | 0.02055 | 0.02081 | +1.27% |
| 2026-11-25T17:28 | XPLUSDT | surge | 0.04703 | 0.04815 | +2.38% |
| 2026-11-25T17:28 | SUPERUSDT | surge | 0.1125 | 0.1147 | +1.96% |
| 2026-11-25T17:45 | STXUSDT | surge | 0.2623 | 0.2612 | -0.42% |
| 2026-11-25T18:03 | WLDUSDT | surge | 0.2375 | 0.2374 | -0.04% |
| 2026-11-25T18:21 | BCHUSDT | surge | 200.2 | 200.8 | +0.30% |
| 2026-11-25T18:38 | PUMPUSDT | surge | 0.002462 | 0.002463 | +0.04% |
| 2026-11-25T18:38 | XLMUSDT | surge | 0.1262 | 0.1257 | -0.40% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
