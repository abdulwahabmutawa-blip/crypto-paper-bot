# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-28T01:27:11+00:00 · runs 4552 · equity **$630.10** (-36.99%) · cash $0.00 · open 10/10 · round trips 1623

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-374.15 · worst day $-50.94 · trades/day 30.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1414 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 209 | 44% | -0.45% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-27T13:26 | SENTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.72 |
| 2026-10-27T12:15 | HAEDALUSDT | surge | TARGET | 0.5 | +2.75% | $+1.67 |
| 2026-10-27T11:22 | ZROUSDT | bottom | TARGET | 7.0 | +2.75% | $+1.61 |
| 2026-10-27T11:22 | BEBUSDT | surge | TARGET | 18.2 | +2.75% | $+1.64 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-27T03:48 | TRXUSDT | bottom | 0.3292 | 0.3315 | +0.70% |
| 2026-10-27T13:44 | LSKUSDT | surge | 0.1694 | 0.1679 | -0.89% |
| 2026-10-27T14:01 | SNDKBUSDT | surge | 1299.08 | 1336.61 | +2.89% |
| 2026-10-27T15:13 | MRVLBUSDT | surge | 241.37 | 245.56 | +1.74% |
| 2026-10-27T15:48 | EWYBUSDT | surge | 157.89 | 161.96 | +2.58% |
| 2026-10-27T16:24 | TQQQBUSDT | surge | 71.21 | 71.57 | +0.51% |
| 2026-10-27T21:15 | VANAUSDT | surge | 0.857 | 0.85 | -0.82% |
| 2026-10-27T22:06 | MRNABUSDT | surge | 206.72 | 205.99 | -0.35% |
| 2026-10-28T01:25 | DRAMBUSDT | surge | 51.71 | 52.07 | +0.70% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
