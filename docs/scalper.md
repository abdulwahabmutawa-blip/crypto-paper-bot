# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-11T13:49:35+00:00 · runs 529 · equity **$912.62** (-8.74%) · cash $0.00 · open 10/10 · round trips 192

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.51%/trade · realized $-95.24 · worst day $-50.94 · trades/day 27.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 128 | 45% | -0.57% | 41% | 52% | 6% |
| bottom | 64 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-11T13:47 | LINKUSDT | bottom | TARGET | 2.5 | +2.75% | $+2.43 |
| 2026-09-11T13:47 | ORCLBUSDT | surge | STOP | 2.8 | -3.25% | $-2.91 |
| 2026-09-11T13:47 | AAPLBUSDT | surge | TARGET | 22.0 | +2.75% | $+2.56 |
| 2026-09-11T13:14 | DOGSUSDT | surge | TARGET | 1.8 | +2.75% | $+2.43 |
| 2026-09-11T13:14 | ADAUSDT | bottom | TARGET | 2.0 | +2.75% | $+2.46 |
| 2026-09-11T13:14 | POLUSDT | surge | TARGET | 2.2 | +2.75% | $+2.46 |
| 2026-09-11T12:52 | THETAUSDT | surge | STOP | 0.8 | -3.25% | $-3.00 |
| 2026-09-11T12:52 | 0GUSDT | surge | STOP | 2.0 | -3.25% | $-2.94 |
| 2026-09-11T11:28 | AEROUSDT | surge | STOP | 1.8 | -3.25% | $-3.10 |
| 2026-09-11T11:11 | ORCAUSDT | surge | STOP | 4.2 | -3.25% | $-2.92 |
| 2026-09-11T11:11 | FFUSDT | surge | STOP | 15.0 | -3.25% | $-3.02 |
| 2026-09-11T10:54 | THETAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.47 |
| 2026-09-11T10:54 | EGLDUSDT | bottom | STOP | 8.2 | -3.25% | $-2.92 |
| 2026-09-11T10:54 | EIGENUSDT | surge | STOP | 12.8 | -3.25% | $-3.01 |
| 2026-09-11T10:37 | THEUSDT | bottom | STOP | 11.8 | -3.25% | $-3.03 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.94 | +0.93% |
| 2026-09-11T08:21 | KAVAUSDT | surge | 0.06512 | 0.0659 | +1.20% |
| 2026-09-11T12:52 | SOXLBUSDT | surge | 119.88 | 121.89 | +1.68% |
| 2026-09-11T12:52 | BMNRBUSDT | surge | 24.62 | 25.27 | +2.64% |
| 2026-09-11T13:14 | DOGSUSDT | surge | 5.069e-05 | 5.096e-05 | +0.53% |
| 2026-09-11T13:14 | POLUSDT | surge | 0.09563 | 0.09707 | +1.51% |
| 2026-09-11T13:14 | MORPHOUSDT | surge | 2.375 | 2.384 | +0.38% |
| 2026-09-11T13:47 | AEROUSDT | surge | 0.5823 | 0.5832 | +0.15% |
| 2026-09-11T13:47 | AAPLBUSDT | surge | 333.04 | 331.26 | -0.53% |
| 2026-09-11T13:47 | BTCUSDT | surge | 77877.3 | 78100 | +0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
