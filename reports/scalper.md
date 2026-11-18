# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-18T03:57:24+00:00 · runs 6251 · equity **$487.04** (-51.30%) · cash $0.00 · open 10/10 · round trips 2063

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-510.66 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1778 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 285 | 43% | -0.47% | 37% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-18T03:38 | SKYUSDT | surge | STOP | 8.8 | -3.25% | $-1.45 |
| 2026-11-18T02:14 | NVDABUSDT | surge | STOP | 2.5 | -3.25% | $-1.50 |
| 2026-11-18T01:57 | TQQQBUSDT | surge | STOP | 2.2 | -3.25% | $-1.50 |
| 2026-11-18T01:57 | PENGUUSDT | surge | STOP | 2.2 | -3.25% | $-1.50 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-17T17:44 | SPCXBUSDT | surge | 141.25 | 142.08 | +0.59% |
| 2026-11-17T18:01 | FFUSDT | surge | 0.10386 | 0.102 | -1.79% |
| 2026-11-17T18:33 | POLUSDT | surge | 0.0827 | 0.0819 | -0.97% |
| 2026-11-17T20:59 | WUSDT | surge | 0.00878 | 0.00873 | -0.57% |
| 2026-11-17T23:59 | AVGOBUSDT | surge | 351.62 | 345.29 | -1.80% |
| 2026-11-18T01:57 | RENDERUSDT | surge | 1.45 | 1.454 | +0.28% |
| 2026-11-18T01:57 | PHAUSDT | bottom | 0.032 | 0.0319 | -0.31% |
| 2026-11-18T02:31 | TAOUSDT | surge | 196.8 | 196.4 | -0.20% |
| 2026-11-18T03:38 | ZKPUSDT | surge | 0.0328 | 0.0327 | -0.30% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
