# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-28T12:28:54+00:00 · runs 4594 · equity **$628.40** (-37.16%) · cash $0.00 · open 10/10 · round trips 1631

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-369.68 · worst day $-50.94 · trades/day 30.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1421 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 210 | 44% | -0.44% | 37% | 43% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-28T12:27 | VANAUSDT | surge | STOP | 4.2 | -3.25% | $-2.06 |
| 2026-10-28T11:38 | SHELLUSDT | surge | STOP | 0.5 | -3.25% | $-1.99 |
| 2026-10-28T10:49 | DRAMBUSDT | surge | TARGET | 9.2 | +2.75% | $+1.64 |
| 2026-10-28T07:45 | VANAUSDT | surge | TARGET | 10.2 | +2.75% | $+1.70 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-27T13:44 | LSKUSDT | surge | 0.1694 | 0.1676 | -1.06% |
| 2026-10-27T16:24 | TQQQBUSDT | surge | 71.21 | 71.95 | +1.04% |
| 2026-10-27T22:06 | MRNABUSDT | surge | 206.72 | 204.36 | -1.14% |
| 2026-10-28T01:41 | MUBUSDT | surge | 955.09 | 961.95 | +0.72% |
| 2026-10-28T01:58 | EWYBUSDT | surge | 162.51 | 162.97 | +0.28% |
| 2026-10-28T04:12 | SKHYBUSDT | surge | 155.52 | 156.18 | +0.42% |
| 2026-10-28T04:12 | MARSCOINUSDT | surge | 0.0701 | 0.0681 | -2.85% |
| 2026-10-28T11:38 | FLOKIUSDT | surge | 2.399e-05 | 2.38e-05 | -0.79% |
| 2026-10-28T12:27 | BNBUSDT | surge | 756.74 | 756.9 | +0.02% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
