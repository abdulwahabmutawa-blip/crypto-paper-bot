# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-12T03:30:14+00:00 · runs 579 · equity **$914.09** (-8.59%) · cash $0.00 · open 10/10 · round trips 206

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.43%/trade · realized $-87.99 · worst day $-50.94 · trades/day 25.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 141 | 46% | -0.47% | 43% | 51% | 6% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-11T13:47 | LINKUSDT | bottom | TARGET | 2.5 | +2.75% | $+2.43 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-11T13:14 | POLUSDT | surge | 0.09563 | 0.09642 | +0.83% |
| 2026-09-11T13:47 | AAPLBUSDT | surge | 333.04 | 332.75 | -0.09% |
| 2026-09-11T13:47 | BTCUSDT | surge | 77877.3 | 77280 | -0.77% |
| 2026-09-11T15:48 | GOOGLBUSDT | surge | 341.35 | 338.61 | -0.80% |
| 2026-09-11T16:04 | SOXLBUSDT | surge | 123.42 | 123.11 | -0.25% |
| 2026-09-11T16:04 | PLUMEUSDT | surge | 0.01336 | 0.01347 | +0.82% |
| 2026-09-11T16:38 | KAITOUSDT | surge | 0.3105 | 0.3134 | +0.93% |
| 2026-09-11T16:38 | CAKEUSDT | surge | 2.196 | 2.232 | +1.64% |
| 2026-09-11T20:35 | SPCXBUSDT | surge | 150.6 | 150.16 | -0.29% |
| 2026-09-12T02:18 | ACEUSDT | surge | 0.1653 | 0.1656 | +0.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
