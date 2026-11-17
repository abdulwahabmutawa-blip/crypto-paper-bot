# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-17T13:49:26+00:00 · runs 6214 · equity **$501.35** (-49.86%) · cash $0.00 · open 10/10 · round trips 2046

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-498.22 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1765 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 281 | 43% | -0.50% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-17T13:16 | PUMPUSDT | bottom | TARGET | 11.0 | +2.75% | $+1.23 |
| 2026-11-17T12:29 | GTCUSDT | surge | STOP | 3.0 | -3.25% | $-1.43 |
| 2026-11-17T11:57 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+1.26 |
| 2026-11-17T11:57 | MMTUSDT | surge | TARGET | 8.2 | +2.75% | $+1.31 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-16T16:12 | ATOMUSDT | surge | 1.329 | 1.327 | -0.15% |
| 2026-11-16T19:10 | XPLUSDT | surge | 0.04537 | 0.04476 | -1.34% |
| 2026-11-17T02:19 | QNTUSDT | bottom | 152.98 | 155.23 | +1.47% |
| 2026-11-17T04:33 | 币安人生USDT | surge | 0.489 | 0.4916 | +0.53% |
| 2026-11-17T09:02 | PROMUSDT | surge | 5.634 | 5.606 | -0.50% |
| 2026-11-17T11:57 | BCHUSDT | surge | 211.5 | 212.7 | +0.57% |
| 2026-11-17T11:57 | MRVLBUSDT | surge | 151.4 | 150.9 | -0.33% |
| 2026-11-17T12:29 | NBISBUSDT | surge | 110.19 | 109.41 | -0.71% |
| 2026-11-17T13:16 | INJUSDT | surge | 7.527 | 7.495 | -0.43% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
