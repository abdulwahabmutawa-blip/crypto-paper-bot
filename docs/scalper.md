# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T16:39:50+00:00 · runs 539 · equity **$911.02** (-8.90%) · cash $0.00 · open 10/10 · round trips 203

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.45%/trade · realized $-89.85 · worst day $-50.94 · trades/day 29.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 138 | 46% | -0.50% | 43% | 51% | 6% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-11T16:38 | HOLOUSDT | surge | TARGET | 2.0 | +2.75% | $+2.59 |
| 2026-09-11T16:38 | CRCLBUSDT | surge | STOP | 2.2 | -3.25% | $-3.04 |
| 2026-09-11T16:04 | MORPHOUSDT | surge | STOP | 1.8 | -3.25% | $-3.04 |
| 2026-09-11T16:04 | ADAUSDT | surge | STOP | 1.8 | -3.25% | $-3.04 |
| 2026-09-11T16:04 | AVAXUSDT | surge | STOP | 1.8 | -3.25% | $-3.04 |
| 2026-09-11T15:48 | SOXLBUSDT | surge | TARGET | 2.5 | +2.75% | $+2.43 |
| 2026-09-11T14:21 | DOGSUSDT | surge | TARGET | 1.0 | +2.75% | $+2.52 |
| 2026-09-11T14:04 | AEROUSDT | surge | TARGET | 0.0 | +2.75% | $+2.50 |
| 2026-09-11T14:04 | MORPHOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.52 |
| 2026-09-11T14:04 | BMNRBUSDT | surge | TARGET | 1.0 | +2.75% | $+2.43 |
| 2026-09-11T14:04 | INJUSDT | bottom | TARGET | 23.0 | +2.75% | $+2.56 |
| 2026-09-11T13:47 | LINKUSDT | bottom | TARGET | 2.5 | +2.75% | $+2.43 |
| 2026-09-11T13:47 | ORCLBUSDT | surge | STOP | 2.8 | -3.25% | $-2.91 |
| 2026-09-11T13:47 | AAPLBUSDT | surge | TARGET | 22.0 | +2.75% | $+2.56 |
| 2026-09-11T13:14 | DOGSUSDT | surge | TARGET | 1.8 | +2.75% | $+2.43 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-11T08:21 | KAVAUSDT | surge | 0.06512 | 0.06577 | +1.00% |
| 2026-09-11T13:14 | POLUSDT | surge | 0.09563 | 0.09689 | +1.32% |
| 2026-09-11T13:47 | AAPLBUSDT | surge | 333.04 | 334 | +0.29% |
| 2026-09-11T13:47 | BTCUSDT | surge | 77877.3 | 77654 | -0.29% |
| 2026-09-11T15:48 | GOOGLBUSDT | surge | 341.35 | 340.34 | -0.30% |
| 2026-09-11T16:04 | SOXLBUSDT | surge | 123.42 | 122.2 | -0.99% |
| 2026-09-11T16:04 | DOGSUSDT | surge | 5.183e-05 | 5.195e-05 | +0.23% |
| 2026-09-11T16:04 | PLUMEUSDT | surge | 0.01336 | 0.0134 | +0.30% |
| 2026-09-11T16:38 | KAITOUSDT | surge | 0.3105 | 0.3093 | -0.39% |
| 2026-09-11T16:38 | CAKEUSDT | surge | 2.196 | 2.192 | -0.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
