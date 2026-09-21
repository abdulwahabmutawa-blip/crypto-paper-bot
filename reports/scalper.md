# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-21T16:45:54+00:00 · runs 1413 · equity **$944.90** (-5.51%) · cash $0.00 · open 10/10 · round trips 516

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-55.59 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 429 | 53% | -0.03% | 50% | 42% | 8% |
| bottom | 87 | 43% | -0.47% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-21T09:02 | BOMEUSDT | surge | TARGET | 4.2 | +2.75% | $+2.42 |
| 2026-09-21T08:44 | 0GUSDT | surge | TARGET | 2.0 | +2.75% | $+2.67 |
| 2026-09-21T08:44 | ZROUSDT | surge | TARGET | 10.0 | +2.75% | $+2.60 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-21T05:27 | LPTUSDT | surge | 1.678 | 1.698 | +1.19% |
| 2026-09-21T09:19 | BTCUSDT | surge | 83925.5 | 85859.1 | +2.30% |
| 2026-09-21T13:53 | MUBUSDT | surge | 1060.18 | 1039.83 | -1.92% |
| 2026-09-21T14:28 | BCHUSDT | surge | 267.7 | 263.1 | -1.72% |
| 2026-09-21T14:28 | LTCUSDT | surge | 62.05 | 62.06 | +0.02% |
| 2026-09-21T15:39 | TSLABUSDT | surge | 374.57 | 374.13 | -0.12% |
| 2026-09-21T15:55 | BANKUSDT | surge | 0.0352 | 0.0354 | +0.57% |
| 2026-09-21T16:11 | AMDBUSDT | surge | 609.45 | 611.28 | +0.30% |
| 2026-09-21T16:44 | FLOKIUSDT | surge | 2.885e-05 | 2.881e-05 | -0.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
