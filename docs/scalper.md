# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-17T10:55:05+00:00 · runs 6203 · equity **$497.25** (-50.27%) · cash $0.00 · open 10/10 · round trips 2042

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-500.59 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1762 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 280 | 42% | -0.51% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-17T10:22 | ZROUSDT | surge | STOP | 6.5 | -3.25% | $-1.54 |
| 2026-11-17T09:18 | GTCUSDT | surge | TARGET | 1.0 | +2.75% | $+1.18 |
| 2026-11-17T09:02 | DODOUSDT | surge | TARGET | 19.2 | +2.75% | $+1.23 |
| 2026-11-17T08:14 | ERAUSDT | surge | STOP | 9.2 | -3.25% | $-1.44 |
| 2026-11-17T04:33 | PHAUSDT | surge | STOP | 1.0 | -3.25% | $-1.54 |
| 2026-11-17T03:43 | ZAMAUSDT | surge | TARGET | 7.5 | +2.75% | $+1.27 |
| 2026-11-17T03:26 | PHAUSDT | surge | TARGET | 1.2 | +2.75% | $+1.27 |
| 2026-11-17T03:26 | MMTUSDT | surge | TARGET | 2.8 | +2.75% | $+1.27 |
| 2026-11-17T02:19 | MSTRBUSDT | surge | TIME | 24.0 | -0.29% | $-0.13 |
| 2026-11-17T02:02 | ICPUSDT | surge | STOP | 7.0 | -3.25% | $-1.50 |
| 2026-11-17T01:46 | ZROUSDT | surge | TARGET | 9.5 | +2.75% | $+1.24 |
| 2026-11-17T00:21 | GRAMUSDT | bottom | TARGET | 10.0 | +2.75% | $+1.24 |
| 2026-11-16T21:19 | SAGAUSDT | surge | TIME | 24.0 | +0.74% | $+0.33 |
| 2026-11-16T19:59 | ZAMAUSDT | surge | TARGET | 3.5 | +2.75% | $+1.24 |
| 2026-11-16T19:10 | PHAUSDT | surge | TARGET | 1.0 | +2.75% | $+1.31 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-16T16:12 | ATOMUSDT | surge | 1.329 | 1.316 | -0.98% |
| 2026-11-16T19:10 | XPLUSDT | surge | 0.04537 | 0.04477 | -1.32% |
| 2026-11-17T02:02 | PUMPUSDT | bottom | 0.002766 | 0.002725 | -1.48% |
| 2026-11-17T02:19 | QNTUSDT | bottom | 152.98 | 153.38 | +0.26% |
| 2026-11-17T03:26 | MMTUSDT | surge | 0.1152 | 0.1138 | -1.22% |
| 2026-11-17T04:33 | 币安人生USDT | surge | 0.489 | 0.4901 | +0.22% |
| 2026-11-17T09:02 | PROMUSDT | surge | 5.634 | 5.607 | -0.48% |
| 2026-11-17T09:18 | GTCUSDT | surge | 0.14546 | 0.14402 | -0.99% |
| 2026-11-17T10:22 | RUNEUSDT | surge | 0.537 | 0.544 | +1.30% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
