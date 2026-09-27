# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T05:04:05+00:00 · runs 1899 · equity **$934.32** (-6.57%) · cash $0.00 · open 10/10 · round trips 681

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-64.05 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 582 | 53% | -0.02% | 50% | 42% | 8% |
| bottom | 99 | 43% | -0.49% | 39% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-27T04:45 | KITEUSDT | surge | STOP | 1.0 | -3.25% | $-3.03 |
| 2026-09-27T04:28 | SKYUSDT | surge | TIME | 24.0 | -0.83% | $-0.80 |
| 2026-09-27T03:38 | WUSDT | surge | TARGET | 0.2 | +2.75% | $+2.49 |
| 2026-09-27T03:05 | GRAMUSDT | surge | STOP | 2.2 | -3.25% | $-3.05 |
| 2026-09-27T02:48 | KITEUSDT | surge | TARGET | 3.5 | +2.75% | $+2.60 |
| 2026-09-27T00:59 | ESPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-27T00:41 | ESPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.58 |
| 2026-09-27T00:41 | TUSDT | surge | STOP | 0.0 | -3.25% | $-3.05 |
| 2026-09-27T00:24 | RUNEUSDT | surge | TARGET | 2.5 | +2.75% | $+2.42 |
| 2026-09-27T00:24 | ESPUSDT | surge | TARGET | 7.5 | +2.75% | $+2.61 |
| 2026-09-27T00:06 | GRAMUSDT | surge | TARGET | 3.5 | +2.75% | $+2.62 |
| 2026-09-26T23:13 | KMNOUSDT | surge | TARGET | 6.0 | +2.75% | $+2.53 |
| 2026-09-26T22:02 | KITEUSDT | surge | TARGET | 1.5 | +2.75% | $+2.62 |
| 2026-09-26T21:44 | LSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.96 |
| 2026-09-26T20:51 | WLDUSDT | surge | STOP | 1.8 | -3.25% | $-2.83 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 71.46 | -0.21% |
| 2026-09-26T20:51 | SEIUSDT | bottom | 0.0712 | 0.07181 | +0.86% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3331 | -0.57% |
| 2026-09-26T22:02 | SUPERUSDT | surge | 0.2006 | 0.1997 | -0.45% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1638.45 | -0.89% |
| 2026-09-27T00:59 | XPLUSDT | bottom | 0.11061 | 0.11005 | -0.51% |
| 2026-09-27T02:48 | PYTHUSDT | surge | 0.08262 | 0.08289 | +0.33% |
| 2026-09-27T04:28 | CFGUSDT | surge | 0.1739 | 0.1723 | -0.92% |
| 2026-09-27T04:45 | REUSDT | surge | 0.5005 | 0.5042 | +0.74% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
