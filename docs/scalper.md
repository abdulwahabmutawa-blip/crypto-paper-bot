# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T15:04:36+00:00 · runs 1496 · equity **$953.13** (-4.69%) · cash $0.00 · open 10/10 · round trips 543

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-48.65 · worst day $-50.94 · trades/day 30.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 453 | 54% | +0.00% | 50% | 42% | 8% |
| bottom | 90 | 42% | -0.50% | 40% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T15:02 | MARSCOINUSDT | surge | STOP | 0.0 | -3.25% | $-3.22 |
| 2026-09-22T14:44 | TSTUSDT | surge | STOP | 1.0 | -3.25% | $-3.38 |
| 2026-09-22T14:44 | TUTUSDT | surge | STOP | 1.5 | -3.25% | $-3.29 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 376.26 | +0.45% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 616.36 | +1.13% |
| 2026-09-21T17:17 | QQQBUSDT | surge | 738.89 | 744.78 | +0.80% |
| 2026-09-22T06:32 | PROVEUSDT | bottom | 0.2277 | 0.2242 | -1.54% |
| 2026-09-22T10:35 | KITEUSDT | surge | 0.1323 | 0.1352 | +2.19% |
| 2026-09-22T12:53 | SPCXBUSDT | bottom | 152.07 | 153.78 | +1.12% |
| 2026-09-22T12:53 | ONDOUSDT | bottom | 0.4304 | 0.4303 | -0.02% |
| 2026-09-22T14:44 | SKHYBUSDT | surge | 194.89 | 192.88 | -1.03% |
| 2026-09-22T15:02 | SNDKBUSDT | surge | 1858.77 | 1838.16 | -1.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
