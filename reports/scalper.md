# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-21T12:12:59+00:00 · runs 1396 · equity **$950.41** (-4.96%) · cash $0.00 · open 10/10 · round trips 506

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-55.78 · worst day $-50.94 · trades/day 29.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 419 | 53% | -0.03% | 50% | 42% | 8% |
| bottom | 87 | 43% | -0.47% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-21T10:28 | SEIUSDT | surge | TARGET | 1.8 | +2.75% | $+2.70 |
| 2026-09-21T09:19 | CHIPUSDT | surge | TARGET | 0.5 | +2.75% | $+2.70 |
| 2026-09-21T09:02 | BOMEUSDT | surge | TARGET | 4.2 | +2.75% | $+2.42 |
| 2026-09-21T08:44 | 0GUSDT | surge | TARGET | 2.0 | +2.75% | $+2.67 |
| 2026-09-21T08:44 | ZROUSDT | surge | TARGET | 10.0 | +2.75% | $+2.60 |
| 2026-09-21T08:44 | RUNEUSDT | surge | TARGET | 14.2 | +2.75% | $+2.60 |
| 2026-09-21T08:24 | SOXLBUSDT | surge | TARGET | 7.5 | +2.75% | $+2.68 |
| 2026-09-21T06:31 | APTUSDT | surge | TARGET | 13.5 | +2.75% | $+2.60 |
| 2026-09-21T05:27 | SNXXBUSDT | surge | STOP | 4.0 | -3.25% | $-3.04 |
| 2026-09-21T04:38 | BERAUSDT | surge | STOP | 0.0 | -3.25% | $-2.96 |
| 2026-09-21T04:22 | MIRAUSDT | surge | TARGET | 2.0 | +2.75% | $+2.43 |
| 2026-09-21T02:55 | XRPUSDT | bottom | TIME | 24.0 | +0.85% | $+0.78 |
| 2026-09-21T02:03 | RENDERUSDT | surge | STOP | 2.2 | -3.25% | $-2.97 |
| 2026-09-21T01:11 | BNCBUSDT | surge | TARGET | 10.8 | +2.75% | $+2.50 |
| 2026-09-21T00:36 | SEIUSDT | surge | TARGET | 2.5 | +2.75% | $+2.60 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-20T14:10 | TRXUSDT | surge | 0.3466 | 0.3441 | -0.72% |
| 2026-09-20T16:49 | ATOMUSDT | surge | 1.765 | 1.793 | +1.59% |
| 2026-09-21T02:55 | MUBUSDT | surge | 1027.56 | 1037.07 | +0.93% |
| 2026-09-21T05:27 | LPTUSDT | surge | 1.678 | 1.702 | +1.43% |
| 2026-09-21T08:24 | SOXLBUSDT | surge | 130.89 | 133.17 | +1.74% |
| 2026-09-21T08:44 | SNXXBUSDT | surge | 18.4 | 18.49 | +0.49% |
| 2026-09-21T09:02 | SNDKBUSDT | surge | 1822.27 | 1817.7 | -0.25% |
| 2026-09-21T09:19 | BTCUSDT | surge | 83925.5 | 85053.1 | +1.34% |
| 2026-09-21T10:28 | MSTRBUSDT | surge | 164.16 | 163.91 | -0.15% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
