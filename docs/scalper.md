# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-17T22:54:53+00:00 · runs 6234 · equity **$493.53** (-50.65%) · cash $0.00 · open 10/10 · round trips 2055

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-509.66 · worst day $-50.94 · trades/day 27.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1773 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 282 | 43% | -0.51% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-17T19:54 | ZROUSDT | bottom | STOP | 2.0 | -3.25% | $-1.45 |
| 2026-11-17T19:21 | XPLUSDT | surge | TIME | 24.0 | -1.26% | $-0.62 |
| 2026-11-17T17:44 | INJUSDT | surge | STOP | 2.2 | -3.25% | $-1.49 |
| 2026-11-17T17:44 | NBISBUSDT | surge | STOP | 3.2 | -3.25% | $-1.39 |
| 2026-11-17T17:44 | MRVLBUSDT | surge | STOP | 3.0 | -3.25% | $-1.56 |
| 2026-11-17T17:44 | BCHUSDT | surge | STOP | 4.0 | -3.25% | $-1.56 |
| 2026-11-17T17:44 | PROMUSDT | surge | STOP | 7.0 | -3.25% | $-1.49 |
| 2026-11-17T17:44 | 币安人生USDT | surge | STOP | 11.0 | -3.25% | $-1.49 |
| 2026-11-17T17:44 | ATOMUSDT | surge | TIME | 24.0 | -0.85% | $-0.38 |
| 2026-11-17T13:16 | PUMPUSDT | bottom | TARGET | 11.0 | +2.75% | $+1.23 |
| 2026-11-17T12:29 | GTCUSDT | surge | STOP | 3.0 | -3.25% | $-1.43 |
| 2026-11-17T11:57 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+1.26 |
| 2026-11-17T11:57 | MMTUSDT | surge | TARGET | 8.2 | +2.75% | $+1.31 |
| 2026-11-17T10:22 | ZROUSDT | surge | STOP | 6.5 | -3.25% | $-1.54 |
| 2026-11-17T09:18 | GTCUSDT | surge | TARGET | 1.0 | +2.75% | $+1.18 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-17T02:19 | QNTUSDT | bottom | 152.98 | 155.35 | +1.55% |
| 2026-11-17T17:44 | SPCXBUSDT | surge | 141.25 | 142.78 | +1.08% |
| 2026-11-17T17:44 | HBARUSDT | bottom | 0.05642 | 0.05762 | +2.13% |
| 2026-11-17T18:01 | FFUSDT | surge | 0.10386 | 0.10388 | +0.02% |
| 2026-11-17T18:33 | SKYUSDT | surge | 0.05397 | 0.05334 | -1.17% |
| 2026-11-17T18:33 | CHIPUSDT | surge | 0.02844 | 0.02867 | +0.81% |
| 2026-11-17T18:33 | POLUSDT | surge | 0.0827 | 0.08198 | -0.87% |
| 2026-11-17T19:54 | MSTRBUSDT | bottom | 97.11 | 99.51 | +2.47% |
| 2026-11-17T20:59 | WUSDT | surge | 0.00878 | 0.00887 | +1.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
