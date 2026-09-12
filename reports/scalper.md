# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-12T10:55:30+00:00 · runs 605 · equity **$910.36** (-8.96%) · cash $0.00 · open 10/10 · round trips 207

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.42%/trade · realized $-85.41 · worst day $-50.94 · trades/day 25.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 142 | 46% | -0.45% | 44% | 51% | 6% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-12T10:53 | CAKEUSDT | surge | TARGET | 18.0 | +2.75% | $+2.57 |
| 2026-09-12T02:18 | KAVAUSDT | surge | TARGET | 17.8 | +2.75% | $+2.39 |
| 2026-09-11T20:35 | HOLOUSDT | surge | STOP | 2.8 | -3.25% | $-3.02 |
| 2026-09-11T17:44 | DOGSUSDT | surge | TARGET | 1.2 | +2.75% | $+2.49 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-11T13:14 | POLUSDT | surge | 0.09563 | 0.09593 | +0.31% |
| 2026-09-11T13:47 | AAPLBUSDT | surge | 333.04 | 333.1 | +0.02% |
| 2026-09-11T13:47 | BTCUSDT | surge | 77877.3 | 77320 | -0.72% |
| 2026-09-11T15:48 | GOOGLBUSDT | surge | 341.35 | 339.7 | -0.48% |
| 2026-09-11T16:04 | SOXLBUSDT | surge | 123.42 | 121.95 | -1.19% |
| 2026-09-11T16:04 | PLUMEUSDT | surge | 0.01336 | 0.01331 | -0.37% |
| 2026-09-11T16:38 | KAITOUSDT | surge | 0.3105 | 0.3106 | +0.03% |
| 2026-09-11T20:35 | SPCXBUSDT | surge | 150.6 | 150.1 | -0.33% |
| 2026-09-12T02:18 | ACEUSDT | surge | 0.1653 | 0.1615 | -2.30% |
| 2026-09-12T10:53 | PROMUSDT | surge | 5.762 | 5.78 | +0.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
