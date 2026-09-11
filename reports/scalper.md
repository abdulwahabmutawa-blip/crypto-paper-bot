# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T15:49:56+00:00 · runs 536 · equity **$918.07** (-8.19%) · cash $0.00 · open 10/10 · round trips 198

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.41%/trade · realized $-80.28 · worst day $-50.94 · trades/day 28.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 133 | 47% | -0.44% | 44% | 50% | 6% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-11T13:14 | ADAUSDT | bottom | TARGET | 2.0 | +2.75% | $+2.46 |
| 2026-09-11T13:14 | POLUSDT | surge | TARGET | 2.2 | +2.75% | $+2.46 |
| 2026-09-11T12:52 | THETAUSDT | surge | STOP | 0.8 | -3.25% | $-3.00 |
| 2026-09-11T12:52 | 0GUSDT | surge | STOP | 2.0 | -3.25% | $-2.94 |
| 2026-09-11T11:28 | AEROUSDT | surge | STOP | 1.8 | -3.25% | $-3.10 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-11T08:21 | KAVAUSDT | surge | 0.06512 | 0.06576 | +0.98% |
| 2026-09-11T13:14 | POLUSDT | surge | 0.09563 | 0.09595 | +0.33% |
| 2026-09-11T13:47 | AAPLBUSDT | surge | 333.04 | 334.34 | +0.39% |
| 2026-09-11T13:47 | BTCUSDT | surge | 77877.3 | 78567.7 | +0.89% |
| 2026-09-11T14:04 | CRCLBUSDT | surge | 94.88 | 93.3 | -1.67% |
| 2026-09-11T14:04 | AVAXUSDT | surge | 7.773 | 7.679 | -1.21% |
| 2026-09-11T14:04 | ADAUSDT | surge | 0.2143 | 0.2126 | -0.79% |
| 2026-09-11T14:04 | MORPHOUSDT | surge | 2.46 | 2.391 | -2.80% |
| 2026-09-11T14:21 | HOLOUSDT | surge | 0.0626 | 0.064 | +2.24% |
| 2026-09-11T15:48 | GOOGLBUSDT | surge | 341.35 | 341.23 | -0.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
