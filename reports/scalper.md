# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T13:34:48+00:00 · runs 878 · equity **$886.19** (-11.38%) · cash $0.00 · open 10/10 · round trips 317

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.35%/trade · realized $-109.73 · worst day $-50.94 · trades/day 28.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 244 | 48% | -0.32% | 45% | 47% | 8% |
| bottom | 73 | 42% | -0.46% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-15T13:33 | TUTUSDT | surge | TARGET | 2.8 | +2.75% | $+2.36 |
| 2026-09-15T13:16 | MINAUSDT | surge | STOP | 0.5 | -3.25% | $-2.80 |
| 2026-09-15T12:43 | SAGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.31 |
| 2026-09-15T12:27 | VTHOUSDT | surge | TARGET | 0.0 | +2.75% | $+2.42 |
| 2026-09-15T12:10 | MINAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.36 |
| 2026-09-15T11:54 | FETUSDT | bottom | STOP | 7.2 | -3.25% | $-2.82 |
| 2026-09-15T09:59 | COTIUSDT | surge | STOP | 0.5 | -3.25% | $-2.83 |
| 2026-09-15T09:09 | COTIUSDT | surge | TARGET | 1.5 | +2.75% | $+2.22 |
| 2026-09-15T08:36 | SAGAUSDT | surge | STOP | 0.0 | -3.25% | $-3.07 |
| 2026-09-15T08:03 | VANAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-15T07:59 | XLMUSDT | surge | STOP | 13.8 | -3.25% | $-3.09 |
| 2026-09-15T07:26 | CAKEUSDT | surge | STOP | 18.0 | -3.25% | $-2.71 |
| 2026-09-15T04:26 | REDUSDT | surge | TARGET | 0.5 | +2.75% | $+2.32 |
| 2026-09-15T04:09 | MSTRBUSDT | surge | STOP | 10.0 | -3.25% | $-3.11 |
| 2026-09-15T03:37 | LAUSDT | surge | STOP | 0.0 | -3.25% | $-2.91 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T16:03 | SPCXBUSDT | surge | 150.77 | 146.38 | -2.91% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 663.42 | -0.05% |
| 2026-09-15T03:20 | JSTUSDT | surge | 0.11522 | 0.11567 | +0.39% |
| 2026-09-15T03:37 | BANKUSDT | bottom | 0.0274 | 0.0275 | +0.36% |
| 2026-09-15T03:37 | GRAMUSDT | bottom | 1.341 | 1.34 | -0.07% |
| 2026-09-15T04:09 | DODOUSDT | surge | 0.01822 | 0.01786 | -1.98% |
| 2026-09-15T12:27 | INJUSDT | bottom | 5.912 | 5.9 | -0.20% |
| 2026-09-15T13:33 | SKHYBUSDT | surge | 179.14 | 180.86 | +0.96% |
| 2026-09-15T13:33 | TUTUSDT | surge | 0.01988 | 0.01974 | -0.70% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
