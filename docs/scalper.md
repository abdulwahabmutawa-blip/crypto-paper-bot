# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-28T15:50:54+00:00 · runs 4607 · equity **$624.72** (-37.53%) · cash $0.00 · open 10/10 · round trips 1640

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-375.35 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1429 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 211 | 44% | -0.46% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-28T15:27 | BANKUSDT | bottom | STOP | 1.2 | -3.25% | $-1.91 |
| 2026-10-28T14:38 | FLOKIUSDT | surge | STOP | 2.8 | -3.25% | $-1.93 |
| 2026-10-28T14:22 | BMTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.56 |
| 2026-10-28T14:05 | AXTIBUSDT | surge | STOP | 0.0 | -3.25% | $-1.91 |
| 2026-10-28T13:49 | NBISBUSDT | surge | STOP | 1.0 | -3.25% | $-1.89 |
| 2026-10-28T13:49 | SKHYBUSDT | surge | TARGET | 9.5 | +2.75% | $+1.65 |
| 2026-10-28T13:49 | MRNABUSDT | surge | TARGET | 15.5 | +2.75% | $+1.66 |
| 2026-10-28T13:49 | LSKUSDT | surge | TIME | 24.0 | -1.73% | $-0.96 |
| 2026-10-28T12:43 | MARSCOINUSDT | surge | STOP | 8.5 | -3.25% | $-1.95 |
| 2026-10-28T12:27 | VANAUSDT | surge | STOP | 4.2 | -3.25% | $-2.06 |
| 2026-10-28T11:38 | SHELLUSDT | surge | STOP | 0.5 | -3.25% | $-1.99 |
| 2026-10-28T10:49 | DRAMBUSDT | surge | TARGET | 9.2 | +2.75% | $+1.64 |
| 2026-10-28T07:45 | VANAUSDT | surge | TARGET | 10.2 | +2.75% | $+1.70 |
| 2026-10-28T04:12 | MRVLBUSDT | surge | TARGET | 12.8 | +2.75% | $+1.67 |
| 2026-10-28T04:12 | TRXUSDT | bottom | TIME | 24.0 | +0.39% | $+0.22 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-27T16:24 | TQQQBUSDT | surge | 71.21 | 71.33 | +0.17% |
| 2026-10-28T01:41 | MUBUSDT | surge | 955.09 | 971.67 | +1.74% |
| 2026-10-28T01:58 | EWYBUSDT | surge | 162.51 | 164.39 | +1.16% |
| 2026-10-28T12:27 | BNBUSDT | surge | 756.74 | 749.2 | -1.00% |
| 2026-10-28T13:49 | SNDKBUSDT | surge | 1381.1 | 1381.78 | +0.05% |
| 2026-10-28T13:49 | SPCXBUSDT | bottom | 144.87 | 145.24 | +0.26% |
| 2026-10-28T14:22 | TUTUSDT | surge | 0.02021 | 0.01997 | -1.19% |
| 2026-10-28T14:38 | CHIPUSDT | bottom | 0.05076 | 0.05102 | +0.51% |
| 2026-10-28T15:27 | SHELLUSDT | surge | 0.0262 | 0.02575 | -1.72% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
