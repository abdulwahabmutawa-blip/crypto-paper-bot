# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-28T16:25:15+00:00 · runs 4609 · equity **$619.78** (-38.02%) · cash $0.00 · open 10/10 · round trips 1642

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-379.06 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1430 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 212 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-28T16:23 | SHELLUSDT | surge | STOP | 0.8 | -3.25% | $-1.84 |
| 2026-10-28T16:23 | CHIPUSDT | bottom | STOP | 1.5 | -3.25% | $-1.87 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-27T16:24 | TQQQBUSDT | surge | 71.21 | 71.3 | +0.13% |
| 2026-10-28T01:41 | MUBUSDT | surge | 955.09 | 973.06 | +1.88% |
| 2026-10-28T01:58 | EWYBUSDT | surge | 162.51 | 164.96 | +1.51% |
| 2026-10-28T12:27 | BNBUSDT | surge | 756.74 | 749.57 | -0.95% |
| 2026-10-28T13:49 | SNDKBUSDT | surge | 1381.1 | 1379.5 | -0.12% |
| 2026-10-28T13:49 | SPCXBUSDT | bottom | 144.87 | 144.69 | -0.12% |
| 2026-10-28T14:22 | TUTUSDT | surge | 0.02021 | 0.01984 | -1.83% |
| 2026-10-28T16:23 | BLURUSDT | surge | 0.00877 | 0.00849 | -3.19% |
| 2026-10-28T16:23 | LTCUSDT | surge | 58.66 | 58.91 | +0.43% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
