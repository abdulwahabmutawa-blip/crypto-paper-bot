# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T00:04:38+00:00 · runs 392 · equity **$980.43** (-1.96%) · cash $98.74 · open 9/10 · round trips 139

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.13%/trade · realized $-19.10 · worst day $-27.16 · trades/day 23.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 85 | 53% | -0.05% | 48% | 42% | 9% |
| bottom | 54 | 46% | -0.25% | 44% | 44% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T00:02 | MINAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.66 |
| 2026-09-09T23:09 | LITEBUSDT | surge | STOP | 8.8 | -3.25% | $-3.30 |
| 2026-09-09T22:17 | XVGUSDT | surge | STOP | 2.2 | -3.25% | $-3.18 |
| 2026-09-09T22:17 | DODOUSDT | surge | STOP | 7.0 | -3.25% | $-3.29 |
| 2026-09-09T22:17 | HBARUSDT | bottom | STOP | 21.0 | -3.25% | $-3.27 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 53.22 | -1.26% |
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1027.11 | -0.68% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 235.42 | -0.21% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 196.68 | +1.05% |
| 2026-09-09T16:47 | INTCBUSDT | surge | 106.11 | 105.78 | -0.31% |
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 133.82 | +0.84% |
| 2026-09-09T22:17 | SAHARAUSDT | surge | 0.01043 | 0.01038 | -0.48% |
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 92.78 | +1.27% |
| 2026-09-10T00:02 | MINAUSDT | surge | 0.0939 | 0.0933 | -0.64% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
