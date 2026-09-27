# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T07:01:31+00:00 · runs 1906 · equity **$935.59** (-6.44%) · cash $0.00 · open 10/10 · round trips 684

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-61.97 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 584 | 53% | -0.02% | 50% | 42% | 8% |
| bottom | 100 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-27T00:06 | GRAMUSDT | surge | TARGET | 3.5 | +2.75% | $+2.62 |
| 2026-09-26T23:13 | KMNOUSDT | surge | TARGET | 6.0 | +2.75% | $+2.53 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 70.81 | -1.12% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3332 | -0.54% |
| 2026-09-26T22:02 | SUPERUSDT | surge | 0.2006 | 0.2034 | +1.40% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1655.11 | +0.12% |
| 2026-09-27T00:59 | XPLUSDT | bottom | 0.11061 | 0.11094 | +0.30% |
| 2026-09-27T04:45 | REUSDT | surge | 0.5005 | 0.4949 | -1.12% |
| 2026-09-27T05:36 | STXUSDT | surge | 0.3568 | 0.3521 | -1.32% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12516 | +0.40% |
| 2026-09-27T05:52 | PYTHUSDT | surge | 0.08544 | 0.08471 | -0.85% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
