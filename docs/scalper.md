# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T19:12:47+00:00 · runs 375 · equity **$993.76** (-0.62%) · cash $0.00 · open 10/10 · round trips 132

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.01%/trade · realized $-2.20 · worst day $-18.97 · trades/day 26.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 79 | 56% | +0.11% | 51% | 39% | 10% |
| bottom | 53 | 47% | -0.20% | 45% | 43% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-09T12:16 | NEARUSDT | surge | TARGET | 0.5 | +2.75% | $+2.89 |
| 2026-09-09T11:38 | MINAUSDT | surge | STOP | 0.0 | -3.25% | $-3.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.07811 | -1.06% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 54.01 | +0.20% |
| 2026-09-09T13:44 | NEARUSDT | surge | 2.59 | 2.568 | -0.85% |
| 2026-09-09T14:02 | LITEBUSDT | surge | 1011.88 | 1002.11 | -0.97% |
| 2026-09-09T15:13 | DODOUSDT | surge | 0.01839 | 0.01833 | -0.33% |
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1023.16 | -1.06% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 234.97 | -0.40% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 198.16 | +1.81% |
| 2026-09-09T15:54 | PYTHUSDT | surge | 0.05603 | 0.05537 | -1.18% |
| 2026-09-09T16:47 | INTCBUSDT | surge | 106.11 | 105.96 | -0.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
