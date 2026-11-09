# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-09T04:04:15+00:00 · runs 5564 · equity **$506.23** (-49.38%) · cash $0.00 · open 10/10 · round trips 1906

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-494.91 · worst day $-50.94 · trades/day 29.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1652 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 254 | 41% | -0.60% | 35% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-08T23:31 | QNTUSDT | bottom | TARGET | 1.2 | +2.75% | $+1.28 |
| 2026-11-08T22:06 | RSRUSDT | surge | STOP | 0.2 | -3.25% | $-1.41 |
| 2026-11-08T22:06 | SNDKBUSDT | surge | STOP | 2.2 | -3.25% | $-1.66 |
| 2026-11-08T22:06 | GRAMUSDT | bottom | STOP | 4.8 | -3.25% | $-1.51 |
| 2026-11-08T22:06 | PEPEUSDT | surge | STOP | 8.5 | -3.25% | $-1.48 |
| 2026-11-08T22:06 | HBARUSDT | bottom | STOP | 16.8 | -3.25% | $-1.56 |
| 2026-11-08T22:06 | DASHUSDT | surge | STOP | 17.5 | -3.25% | $-1.63 |
| 2026-11-08T22:06 | ARBUSDT | surge | STOP | 18.5 | -3.25% | $-1.56 |
| 2026-11-08T22:06 | MSTRBUSDT | bottom | STOP | 20.2 | -3.25% | $-1.57 |
| 2026-11-08T21:50 | DODOUSDT | surge | STOP | 4.0 | -3.25% | $-1.65 |
| 2026-11-08T21:35 | NEIROUSDT | surge | STOP | 0.5 | -3.25% | $-1.46 |
| 2026-11-08T20:48 | KORUBUSDT | surge | STOP | 2.0 | -3.25% | $-1.51 |
| 2026-11-08T19:30 | ETHFIUSDT | surge | TIME | 24.0 | -0.69% | $-0.35 |
| 2026-11-08T17:57 | BEAMXUSDT | surge | STOP | 5.2 | -3.25% | $-1.56 |
| 2026-11-08T17:41 | RSRUSDT | surge | STOP | 0.5 | -3.25% | $-1.70 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-08T22:06 | BNBUSDT | bottom | 680.36 | 687.7 | +1.08% |
| 2026-11-08T22:06 | HYPEUSDT | bottom | 74.24 | 74.46 | +0.30% |
| 2026-11-08T23:31 | RWUSDUSDT | bottom | 0.9998 | 1 | +0.02% |
| 2026-11-09T00:04 | DODOUSDT | surge | 0.02221 | 0.02241 | +0.90% |
| 2026-11-09T01:11 | ARBUSDT | surge | 0.1709 | 0.1727 | +1.05% |
| 2026-11-09T02:00 | SPCXBUSDT | surge | 137.01 | 137.88 | +0.63% |
| 2026-11-09T02:00 | RENDERUSDT | surge | 1.57 | 1.576 | +0.38% |
| 2026-11-09T02:00 | PEPEUSDT | surge | 5.14e-06 | 5.06e-06 | -1.56% |
| 2026-11-09T02:17 | DRAMBUSDT | surge | 39.83 | 39.69 | -0.35% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
