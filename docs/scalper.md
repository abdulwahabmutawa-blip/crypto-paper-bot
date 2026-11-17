# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-17T19:07:09+00:00 · runs 6220 · equity **$488.93** (-51.11%) · cash $0.00 · open 10/10 · round trips 2053

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-507.59 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1772 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 281 | 43% | -0.50% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-17T09:02 | DODOUSDT | surge | TARGET | 19.2 | +2.75% | $+1.23 |
| 2026-11-17T08:14 | ERAUSDT | surge | STOP | 9.2 | -3.25% | $-1.44 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-16T19:10 | XPLUSDT | surge | 0.04537 | 0.04471 | -1.45% |
| 2026-11-17T02:19 | QNTUSDT | bottom | 152.98 | 151.47 | -0.99% |
| 2026-11-17T17:44 | SPCXBUSDT | surge | 141.25 | 140.99 | -0.18% |
| 2026-11-17T17:44 | ZROUSDT | bottom | 1.417 | 1.384 | -2.33% |
| 2026-11-17T17:44 | HBARUSDT | bottom | 0.05642 | 0.05607 | -0.62% |
| 2026-11-17T18:01 | FFUSDT | surge | 0.10386 | 0.10507 | +1.17% |
| 2026-11-17T18:33 | SKYUSDT | surge | 0.05397 | 0.05392 | -0.09% |
| 2026-11-17T18:33 | CHIPUSDT | surge | 0.02844 | 0.02807 | -1.30% |
| 2026-11-17T18:33 | POLUSDT | surge | 0.0827 | 0.08118 | -1.84% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
