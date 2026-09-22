# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T04:39:36+00:00 · runs 1458 · equity **$944.78** (-5.52%) · cash $0.00 · open 10/10 · round trips 521

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-48.35 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 434 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 87 | 43% | -0.47% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T04:21 | DOGEUSDT | surge | TARGET | 7.0 | +2.75% | $+2.75 |
| 2026-09-22T04:21 | FLOKIUSDT | surge | TARGET | 11.5 | +2.75% | $+2.60 |
| 2026-09-21T21:10 | PENGUUSDT | surge | STOP | 1.2 | -3.25% | $-3.36 |
| 2026-09-21T19:43 | BTCUSDT | surge | TARGET | 10.0 | +2.75% | $+2.77 |
| 2026-09-21T17:17 | LPTUSDT | surge | TARGET | 11.8 | +2.75% | $+2.49 |
| 2026-09-21T16:44 | ARKMUSDT | surge | STOP | 2.8 | -3.25% | $-3.17 |
| 2026-09-21T16:11 | XPLUSDT | surge | STOP | 2.0 | -3.25% | $-3.17 |
| 2026-09-21T15:55 | BANKUSDT | surge | TARGET | 2.5 | +2.75% | $+2.67 |
| 2026-09-21T15:39 | SNDKBUSDT | surge | STOP | 6.2 | -3.25% | $-2.94 |
| 2026-09-21T14:28 | SOXLBUSDT | surge | TARGET | 5.8 | +2.75% | $+2.75 |
| 2026-09-21T14:28 | TRXUSDT | surge | TIME | 24.0 | -0.74% | $-0.67 |
| 2026-09-21T13:53 | MSTRBUSDT | surge | TARGET | 3.2 | +2.75% | $+2.77 |
| 2026-09-21T13:53 | SNXXBUSDT | surge | STOP | 5.0 | -3.25% | $-3.19 |
| 2026-09-21T13:53 | MUBUSDT | surge | TARGET | 10.8 | +2.75% | $+2.53 |
| 2026-09-21T13:02 | ATOMUSDT | surge | TARGET | 20.0 | +2.75% | $+2.60 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T13:53 | MUBUSDT | surge | 1060.18 | 1043.43 | -1.58% |
| 2026-09-21T14:28 | BCHUSDT | surge | 267.7 | 265.1 | -0.97% |
| 2026-09-21T14:28 | LTCUSDT | surge | 62.05 | 60.98 | -1.72% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 376.13 | +0.42% |
| 2026-09-21T15:55 | BANKUSDT | surge | 0.0352 | 0.0344 | -2.27% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 616.03 | +1.08% |
| 2026-09-21T17:17 | QQQBUSDT | surge | 738.89 | 742.78 | +0.53% |
| 2026-09-22T04:21 | SHIBUSDT | surge | 6.21e-06 | 6.13e-06 | -1.29% |
| 2026-09-22T04:21 | FILUSDT | surge | 1.005 | 0.9946 | -1.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
