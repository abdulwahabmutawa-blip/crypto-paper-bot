# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T20:06:04+00:00 · runs 378 · equity **$987.07** (-1.29%) · cash $0.00 · open 10/10 · round trips 134

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.06%/trade · realized $-8.73 · worst day $-18.97 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 81 | 54% | +0.03% | 49% | 41% | 10% |
| bottom | 53 | 47% | -0.20% | 45% | 43% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-09T20:03 | NEARUSDT | surge | STOP | 6.2 | -3.25% | $-3.24 |
| 2026-09-09T19:46 | PYTHUSDT | surge | STOP | 3.8 | -3.25% | $-3.29 |
| 2026-09-09T16:47 | COTIUSDT | surge | TARGET | 0.0 | +2.75% | $+2.62 |
| 2026-09-09T16:30 | HOLOUSDT | surge | STOP | 6.0 | -3.25% | $-3.20 |
| 2026-09-09T15:54 | PHAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.71 |
| 2026-09-09T15:36 | XTZUSDT | surge | STOP | 0.2 | -3.25% | $-3.29 |
| 2026-09-09T15:36 | MINAUSDT | surge | STOP | 1.0 | -3.25% | $-3.29 |
| 2026-09-09T15:36 | INTCBUSDT | surge | TIME | 24.0 | +1.00% | $+0.99 |
| 2026-09-09T15:13 | XTZUSDT | surge | TARGET | 0.8 | +2.75% | $+2.79 |
| 2026-09-09T15:13 | IOUSDT | surge | STOP | 2.8 | -3.25% | $-3.50 |
| 2026-09-09T15:13 | SPCXBUSDT | surge | STOP | 21.8 | -3.25% | $-3.18 |
| 2026-09-09T14:20 | DASHUSDT | surge | STOP | 5.5 | -3.25% | $-3.40 |
| 2026-09-09T14:02 | CHIPUSDT | surge | STOP | 2.2 | -3.25% | $-3.41 |
| 2026-09-09T14:02 | QQQBUSDT | bottom | TIME | 24.0 | -0.04% | $-0.04 |
| 2026-09-09T13:44 | TSLABUSDT | surge | TARGET | 23.5 | +2.75% | $+2.67 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.07703 | -2.43% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 53.51 | -0.72% |
| 2026-09-09T14:02 | LITEBUSDT | surge | 1011.88 | 987.19 | -2.44% |
| 2026-09-09T15:13 | DODOUSDT | surge | 0.01839 | 0.01844 | +0.27% |
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1027.84 | -0.61% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 234.53 | -0.59% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 197.99 | +1.72% |
| 2026-09-09T16:47 | INTCBUSDT | surge | 106.11 | 106 | -0.10% |
| 2026-09-09T19:46 | XVGUSDT | surge | 0.003252 | 0.003283 | +0.95% |
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 132.45 | -0.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
