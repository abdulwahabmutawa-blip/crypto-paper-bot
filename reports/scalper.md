# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-15T16:48:47+00:00 · runs 890 · equity **$883.51** (-11.65%) · cash $353.07 · open 6/10 · round trips 321

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.37%/trade · realized $-116.27 · worst day $-50.94 · trades/day 29.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 247 | 47% | -0.34% | 45% | 47% | 8% |
| bottom | 74 | 42% | -0.49% | 41% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-15T16:12 | SKHYBUSDT | surge | STOP | 2.2 | -3.25% | $-2.79 |
| 2026-09-15T15:03 | TUTUSDT | surge | TARGET | 1.2 | +2.75% | $+2.36 |
| 2026-09-15T15:03 | INJUSDT | bottom | STOP | 2.5 | -3.25% | $-2.94 |
| 2026-09-15T14:12 | SPCXBUSDT | surge | STOP | 21.8 | -3.25% | $-3.17 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-14T17:15 | METABUSDT | surge | 663.73 | 665.92 | +0.33% |
| 2026-09-15T03:20 | JSTUSDT | surge | 0.11522 | 0.11575 | +0.46% |
| 2026-09-15T03:37 | BANKUSDT | bottom | 0.0274 | 0.0275 | +0.36% |
| 2026-09-15T03:37 | GRAMUSDT | bottom | 1.341 | 1.33 | -0.82% |
| 2026-09-15T04:09 | DODOUSDT | surge | 0.01822 | 0.01811 | -0.60% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
