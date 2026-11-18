# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-18T00:35:00+00:00 · runs 6239 · equity **$493.63** (-50.64%) · cash $0.00 · open 10/10 · round trips 2059

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-504.71 · worst day $-50.94 · trades/day 27.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1774 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 285 | 43% | -0.47% | 37% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-17T23:59 | QNTUSDT | bottom | TARGET | 21.0 | +2.75% | $+1.24 |
| 2026-11-17T23:26 | MSTRBUSDT | bottom | TARGET | 3.2 | +2.75% | $+1.26 |
| 2026-11-17T23:26 | CHIPUSDT | surge | TARGET | 4.5 | +2.75% | $+1.23 |
| 2026-11-17T23:26 | HBARUSDT | bottom | TARGET | 5.5 | +2.75% | $+1.23 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-17T17:44 | SPCXBUSDT | surge | 141.25 | 143.23 | +1.40% |
| 2026-11-17T18:01 | FFUSDT | surge | 0.10386 | 0.10346 | -0.39% |
| 2026-11-17T18:33 | SKYUSDT | surge | 0.05397 | 0.05315 | -1.52% |
| 2026-11-17T18:33 | POLUSDT | surge | 0.0827 | 0.0825 | -0.24% |
| 2026-11-17T20:59 | WUSDT | surge | 0.00878 | 0.0089 | +1.37% |
| 2026-11-17T23:26 | PENGUUSDT | surge | 0.004934 | 0.004865 | -1.40% |
| 2026-11-17T23:26 | TQQQBUSDT | surge | 54.67 | 53.98 | -1.26% |
| 2026-11-17T23:26 | NVDABUSDT | surge | 163.75 | 161.99 | -1.07% |
| 2026-11-17T23:59 | AVGOBUSDT | surge | 351.62 | 349.91 | -0.49% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
