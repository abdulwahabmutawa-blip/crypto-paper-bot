# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T03:06:41+00:00 · runs 1892 · equity **$937.03** (-6.30%) · cash $0.00 · open 10/10 · round trips 678

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-62.72 · worst day $-50.94 · trades/day 29.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 579 | 54% | -0.01% | 50% | 42% | 7% |
| bottom | 99 | 43% | -0.49% | 39% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-26T20:51 | STXUSDT | surge | STOP | 11.0 | -3.25% | $-3.16 |
| 2026-09-26T20:51 | INJUSDT | bottom | STOP | 15.8 | -3.25% | $-3.18 |
| 2026-09-26T20:15 | ZENUSDT | surge | STOP | 3.5 | -3.25% | $-3.09 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.0772 | -0.61% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 71.19 | -0.59% |
| 2026-09-26T20:51 | SEIUSDT | bottom | 0.0712 | 0.07252 | +1.85% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.333 | -0.60% |
| 2026-09-26T22:02 | SUPERUSDT | surge | 0.2006 | 0.2011 | +0.25% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1639.6 | -0.82% |
| 2026-09-27T00:59 | XPLUSDT | bottom | 0.11061 | 0.11017 | -0.40% |
| 2026-09-27T02:48 | PYTHUSDT | surge | 0.08262 | 0.08257 | -0.06% |
| 2026-09-27T03:05 | WUSDT | surge | 0.01362 | 0.01373 | +0.81% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
