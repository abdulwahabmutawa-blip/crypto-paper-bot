# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-17T12:14:21+00:00 · runs 6208 · equity **$501.57** (-49.84%) · cash $0.00 · open 10/10 · round trips 2044

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-498.02 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1764 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 280 | 42% | -0.51% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-17T00:21 | GRAMUSDT | bottom | TARGET | 10.0 | +2.75% | $+1.24 |
| 2026-11-16T21:19 | SAGAUSDT | surge | TIME | 24.0 | +0.74% | $+0.33 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-16T16:12 | ATOMUSDT | surge | 1.329 | 1.33 | +0.08% |
| 2026-11-16T19:10 | XPLUSDT | surge | 0.04537 | 0.04497 | -0.88% |
| 2026-11-17T02:02 | PUMPUSDT | bottom | 0.002766 | 0.00278 | +0.51% |
| 2026-11-17T02:19 | QNTUSDT | bottom | 152.98 | 155.41 | +1.59% |
| 2026-11-17T04:33 | 币安人生USDT | surge | 0.489 | 0.4929 | +0.80% |
| 2026-11-17T09:02 | PROMUSDT | surge | 5.634 | 5.519 | -2.04% |
| 2026-11-17T09:18 | GTCUSDT | surge | 0.14546 | 0.143 | -1.69% |
| 2026-11-17T11:57 | BCHUSDT | surge | 211.5 | 210.5 | -0.47% |
| 2026-11-17T11:57 | MRVLBUSDT | surge | 151.4 | 153.24 | +1.22% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
