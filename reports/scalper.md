# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-28T23:17:07+00:00 · runs 4634 · equity **$619.57** (-38.04%) · cash $0.00 · open 10/10 · round trips 1652

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-378.57 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1440 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 212 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-28T22:59 | AXTIBUSDT | surge | STOP | 0.5 | -3.25% | $-1.91 |
| 2026-10-28T22:10 | AXTIBUSDT | surge | TARGET | 0.2 | +2.75% | $+1.57 |
| 2026-10-28T21:37 | SKHYBUSDT | surge | STOP | 4.8 | -3.25% | $-1.92 |
| 2026-10-28T20:59 | BLURUSDT | surge | TARGET | 2.0 | +2.75% | $+1.55 |
| 2026-10-28T20:24 | TIAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.66 |
| 2026-10-28T19:50 | MUBUSDT | surge | TARGET | 18.0 | +2.75% | $+1.62 |
| 2026-10-28T18:58 | SNXXBUSDT | surge | TARGET | 2.0 | +2.75% | $+1.62 |
| 2026-10-28T18:41 | TUTUSDT | surge | STOP | 4.0 | -3.25% | $-1.89 |
| 2026-10-28T16:40 | BLURUSDT | surge | STOP | 0.0 | -3.25% | $-1.79 |
| 2026-10-28T16:40 | TQQQBUSDT | surge | TIME | 24.0 | -0.03% | $-0.02 |
| 2026-10-28T16:23 | SHELLUSDT | surge | STOP | 0.8 | -3.25% | $-1.84 |
| 2026-10-28T16:23 | CHIPUSDT | bottom | STOP | 1.5 | -3.25% | $-1.87 |
| 2026-10-28T15:27 | BANKUSDT | bottom | STOP | 1.2 | -3.25% | $-1.91 |
| 2026-10-28T14:38 | FLOKIUSDT | surge | STOP | 2.8 | -3.25% | $-1.93 |
| 2026-10-28T14:22 | BMTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.56 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-28T01:58 | EWYBUSDT | surge | 162.51 | 163.17 | +0.41% |
| 2026-10-28T12:27 | BNBUSDT | surge | 756.74 | 758.2 | +0.19% |
| 2026-10-28T13:49 | SNDKBUSDT | surge | 1381.1 | 1370.59 | -0.76% |
| 2026-10-28T13:49 | SPCXBUSDT | bottom | 144.87 | 144.1 | -0.53% |
| 2026-10-28T16:23 | LTCUSDT | surge | 58.66 | 59.17 | +0.87% |
| 2026-10-28T18:58 | DRAMBUSDT | surge | 53.98 | 52.71 | -2.35% |
| 2026-10-28T20:24 | TIAUSDT | surge | 0.5563 | 0.5523 | -0.72% |
| 2026-10-28T20:59 | RAYUSDT | surge | 1.8232 | 1.8112 | -0.66% |
| 2026-10-28T22:59 | PUMPUSDT | surge | 0.004525 | 0.004548 | +0.51% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
