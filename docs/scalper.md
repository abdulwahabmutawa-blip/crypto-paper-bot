# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T08:34:52+00:00 · runs 1912 · equity **$942.64** (-5.74%) · cash $0.00 · open 10/10 · round trips 686

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.07%/trade · realized $-56.71 · worst day $-50.94 · trades/day 29.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 586 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 100 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-27T08:15 | PYTHUSDT | surge | TARGET | 2.2 | +2.75% | $+2.57 |
| 2026-09-27T07:57 | SUPERUSDT | surge | TARGET | 9.5 | +2.75% | $+2.70 |
| 2026-09-27T05:52 | SEIUSDT | bottom | TARGET | 8.8 | +2.75% | $+2.50 |
| 2026-09-27T05:36 | CFGUSDT | surge | STOP | 1.0 | -3.25% | $-3.09 |
| 2026-09-27T05:36 | PYTHUSDT | surge | TARGET | 2.5 | +2.75% | $+2.67 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 71.73 | +0.17% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3343 | -0.21% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1664.3 | +0.68% |
| 2026-09-27T00:59 | XPLUSDT | bottom | 0.11061 | 0.11225 | +1.48% |
| 2026-09-27T04:45 | REUSDT | surge | 0.5005 | 0.4942 | -1.26% |
| 2026-09-27T05:36 | STXUSDT | surge | 0.3568 | 0.3496 | -2.02% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12531 | +0.52% |
| 2026-09-27T07:57 | BCHUSDT | surge | 343.4 | 344.5 | +0.32% |
| 2026-09-27T08:15 | ZROUSDT | surge | 1.659 | 1.651 | -0.48% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
