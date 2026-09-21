# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-21T14:12:54+00:00 · runs 1403 · equity **$947.71** (-5.23%) · cash $0.00 · open 10/10 · round trips 510

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-51.06 · worst day $-50.94 · trades/day 30.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 423 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 87 | 43% | -0.47% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-21T13:53 | MSTRBUSDT | surge | TARGET | 3.2 | +2.75% | $+2.77 |
| 2026-09-21T13:53 | SNXXBUSDT | surge | STOP | 5.0 | -3.25% | $-3.19 |
| 2026-09-21T13:53 | MUBUSDT | surge | TARGET | 10.8 | +2.75% | $+2.53 |
| 2026-09-21T13:02 | ATOMUSDT | surge | TARGET | 20.0 | +2.75% | $+2.60 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-20T14:10 | TRXUSDT | surge | 0.3466 | 0.3448 | -0.52% |
| 2026-09-21T05:27 | LPTUSDT | surge | 1.678 | 1.697 | +1.13% |
| 2026-09-21T08:24 | SOXLBUSDT | surge | 130.89 | 134.35 | +2.64% |
| 2026-09-21T09:02 | SNDKBUSDT | surge | 1822.27 | 1774.34 | -2.63% |
| 2026-09-21T09:19 | BTCUSDT | surge | 83925.5 | 85352.1 | +1.70% |
| 2026-09-21T13:02 | BANKUSDT | surge | 0.0349 | 0.0347 | -0.57% |
| 2026-09-21T13:53 | ARKMUSDT | surge | 0.1288 | 0.1279 | -0.70% |
| 2026-09-21T13:53 | MUBUSDT | surge | 1060.18 | 1033.17 | -2.55% |
| 2026-09-21T13:53 | XPLUSDT | surge | 0.10129 | 0.10126 | -0.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
