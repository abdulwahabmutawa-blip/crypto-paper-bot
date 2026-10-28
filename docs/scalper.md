# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-28T06:41:18+00:00 · runs 4572 · equity **$633.26** (-36.67%) · cash $0.00 · open 10/10 · round trips 1627

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-368.97 · worst day $-50.94 · trades/day 30.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1417 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 210 | 44% | -0.44% | 37% | 43% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-28T04:12 | MRVLBUSDT | surge | TARGET | 12.8 | +2.75% | $+1.67 |
| 2026-10-28T04:12 | TRXUSDT | bottom | TIME | 24.0 | +0.39% | $+0.22 |
| 2026-10-28T01:58 | EWYBUSDT | surge | TARGET | 9.8 | +2.75% | $+1.72 |
| 2026-10-28T01:41 | SNDKBUSDT | surge | TARGET | 11.2 | +2.75% | $+1.57 |
| 2026-10-28T01:25 | SKHYBUSDT | surge | TARGET | 23.5 | +2.75% | $+1.60 |
| 2026-10-27T22:06 | RWUSDUSDT | bottom | TIME | 24.0 | -0.24% | $-0.15 |
| 2026-10-27T21:15 | SENTUSDT | surge | STOP | 6.2 | -3.25% | $-2.07 |
| 2026-10-27T16:24 | TQQQBUSDT | surge | TARGET | 15.8 | +2.75% | $+1.73 |
| 2026-10-27T15:48 | AMDBUSDT | surge | TARGET | 4.2 | +2.75% | $+1.67 |
| 2026-10-27T15:13 | TSLABUSDT | surge | TIME | 24.0 | +1.65% | $+0.99 |
| 2026-10-27T14:55 | REZUSDT | surge | STOP | 0.2 | -3.25% | $-2.14 |
| 2026-10-27T14:19 | REZUSDT | surge | TARGET | 0.8 | +2.75% | $+1.76 |
| 2026-10-27T14:01 | SOXLBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.53 |
| 2026-10-27T13:44 | AIUSDT | surge | TIME | 24.0 | +0.26% | $+0.16 |
| 2026-10-27T13:44 | CELOUSDT | surge | TIME | 24.0 | -0.31% | $-0.16 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-27T13:44 | LSKUSDT | surge | 0.1694 | 0.1662 | -1.89% |
| 2026-10-27T16:24 | TQQQBUSDT | surge | 71.21 | 72.1 | +1.25% |
| 2026-10-27T21:15 | VANAUSDT | surge | 0.857 | 0.862 | +0.58% |
| 2026-10-27T22:06 | MRNABUSDT | surge | 206.72 | 206.55 | -0.08% |
| 2026-10-28T01:25 | DRAMBUSDT | surge | 51.71 | 52.79 | +2.09% |
| 2026-10-28T01:41 | MUBUSDT | surge | 955.09 | 970.62 | +1.63% |
| 2026-10-28T01:58 | EWYBUSDT | surge | 162.51 | 163.1 | +0.36% |
| 2026-10-28T04:12 | SKHYBUSDT | surge | 155.52 | 156.81 | +0.83% |
| 2026-10-28T04:12 | MARSCOINUSDT | surge | 0.0701 | 0.0692 | -1.28% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
