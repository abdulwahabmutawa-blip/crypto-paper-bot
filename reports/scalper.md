# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T02:45:13+00:00 · runs 1451 · equity **$945.68** (-5.43%) · cash $0.00 · open 10/10 · round trips 519

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-53.70 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 432 | 53% | -0.02% | 50% | 42% | 8% |
| bottom | 87 | 43% | -0.47% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-21T10:28 | SEIUSDT | surge | TARGET | 1.8 | +2.75% | $+2.70 |
| 2026-09-21T09:19 | CHIPUSDT | surge | TARGET | 0.5 | +2.75% | $+2.70 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T13:53 | MUBUSDT | surge | 1060.18 | 1050.86 | -0.88% |
| 2026-09-21T14:28 | BCHUSDT | surge | 267.7 | 266.4 | -0.49% |
| 2026-09-21T14:28 | LTCUSDT | surge | 62.05 | 61 | -1.69% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 376.99 | +0.65% |
| 2026-09-21T15:55 | BANKUSDT | surge | 0.0352 | 0.0352 | +0.00% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 620.87 | +1.87% |
| 2026-09-21T16:44 | FLOKIUSDT | surge | 2.885e-05 | 2.883e-05 | -0.07% |
| 2026-09-21T17:17 | QQQBUSDT | surge | 738.89 | 743.81 | +0.67% |
| 2026-09-21T21:10 | DOGEUSDT | surge | 0.10018 | 0.09963 | -0.55% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
