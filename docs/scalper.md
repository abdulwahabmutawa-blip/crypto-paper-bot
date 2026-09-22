# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T14:11:10+00:00 · runs 1493 · equity **$963.92** (-3.61%) · cash $0.00 · open 10/10 · round trips 540

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.06%/trade · realized $-38.75 · worst day $-50.94 · trades/day 30.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 450 | 54% | +0.02% | 51% | 42% | 8% |
| bottom | 90 | 42% | -0.50% | 40% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T13:15 | MARSCOINUSDT | surge | TARGET | 0.2 | +2.75% | $+2.78 |
| 2026-09-22T12:53 | UNIUSDT | bottom | TARGET | 0.5 | +2.75% | $+2.72 |
| 2026-09-22T12:53 | QNTUSDT | surge | TARGET | 0.5 | +2.75% | $+2.72 |
| 2026-09-22T12:53 | AVAUSDT | surge | TARGET | 1.0 | +2.75% | $+2.73 |
| 2026-09-22T12:53 | BCHUSDT | surge | TARGET | 22.2 | +2.75% | $+2.65 |
| 2026-09-22T12:01 | TUTUSDT | surge | TARGET | 2.5 | +2.75% | $+2.65 |
| 2026-09-22T12:01 | TSTUSDT | surge | TARGET | 2.5 | +2.75% | $+2.65 |
| 2026-09-22T11:44 | BROCCOLI714USDT | surge | TARGET | 0.0 | +2.75% | $+2.66 |
| 2026-09-22T11:27 | BANKUSDT | surge | STOP | 19.2 | -3.25% | $-3.25 |
| 2026-09-22T10:35 | XPLUSDT | bottom | STOP | 0.2 | -3.25% | $-3.16 |
| 2026-09-22T10:00 | KITEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.60 |
| 2026-09-22T09:26 | TSTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.57 |
| 2026-09-22T09:26 | FILUSDT | surge | STOP | 4.8 | -3.25% | $-3.25 |
| 2026-09-22T08:51 | LTCUSDT | surge | STOP | 18.2 | -3.25% | $-3.14 |
| 2026-09-22T08:34 | MUBUSDT | surge | STOP | 18.5 | -3.25% | $-3.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 377.11 | +0.68% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 619.53 | +1.65% |
| 2026-09-21T17:17 | QQQBUSDT | surge | 738.89 | 744.7 | +0.79% |
| 2026-09-22T06:32 | PROVEUSDT | bottom | 0.2277 | 0.2284 | +0.31% |
| 2026-09-22T10:35 | KITEUSDT | surge | 0.1323 | 0.1326 | +0.23% |
| 2026-09-22T12:53 | TUTUSDT | surge | 0.02425 | 0.02401 | -0.99% |
| 2026-09-22T12:53 | SPCXBUSDT | bottom | 152.07 | 152.87 | +0.53% |
| 2026-09-22T12:53 | ONDOUSDT | bottom | 0.4304 | 0.4323 | +0.44% |
| 2026-09-22T13:15 | TSTUSDT | surge | 0.01908 | 0.01895 | -0.68% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
