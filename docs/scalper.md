# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-18T08:20:04+00:00 · runs 6262 · equity **$486.88** (-51.31%) · cash $0.00 · open 10/10 · round trips 2068

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-512.63 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1782 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 286 | 43% | -0.48% | 37% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-18T07:30 | USUALUSDT | surge | TARGET | 0.0 | +2.75% | $+1.19 |
| 2026-11-18T07:14 | PHAUSDT | bottom | STOP | 4.8 | -3.25% | $-1.45 |
| 2026-11-18T07:14 | FFUSDT | surge | STOP | 11.5 | -3.25% | $-1.45 |
| 2026-11-18T05:36 | USUALUSDT | surge | TARGET | 1.0 | +2.75% | $+1.15 |
| 2026-11-18T04:29 | ZKPUSDT | surge | STOP | 0.5 | -3.25% | $-1.40 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-17T17:44 | SPCXBUSDT | surge | 141.25 | 142.79 | +1.09% |
| 2026-11-17T18:33 | POLUSDT | surge | 0.0827 | 0.08156 | -1.38% |
| 2026-11-17T20:59 | WUSDT | surge | 0.00878 | 0.00887 | +1.03% |
| 2026-11-17T23:59 | AVGOBUSDT | surge | 351.62 | 346.53 | -1.45% |
| 2026-11-18T01:57 | RENDERUSDT | surge | 1.45 | 1.432 | -1.24% |
| 2026-11-18T02:31 | TAOUSDT | surge | 196.8 | 195.7 | -0.56% |
| 2026-11-18T05:36 | BMTUSDT | surge | 0.02019 | 0.02039 | +0.99% |
| 2026-11-18T07:14 | ENSOUSDT | surge | 0.408 | 0.41 | +0.49% |
| 2026-11-18T07:30 | EWYBUSDT | surge | 138.73 | 138.77 | +0.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
