# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-18T19:04:46+00:00 · runs 6289 · equity **$483.06** (-51.69%) · cash $-0.00 · open 10/10 · round trips 2077

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-517.54 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1791 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 286 | 43% | -0.48% | 37% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-18T16:38 | ZBTUSDT | surge | STOP | 1.2 | -3.25% | $-1.40 |
| 2026-11-18T16:38 | BMTUSDT | surge | STOP | 9.0 | -3.25% | $-1.39 |
| 2026-11-18T16:38 | TAOUSDT | surge | STOP | 13.2 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | RENDERUSDT | surge | STOP | 14.0 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | WUSDT | surge | TARGET | 16.2 | +2.75% | $+1.26 |
| 2026-11-18T16:38 | POLUSDT | surge | STOP | 21.8 | -3.25% | $-1.45 |
| 2026-11-18T16:38 | SPCXBUSDT | surge | TARGET | 21.8 | +2.75% | $+1.23 |
| 2026-11-18T12:51 | ALLOUSDT | surge | STOP | 3.2 | -3.25% | $-1.44 |
| 2026-11-18T09:23 | ENSOUSDT | surge | TARGET | 2.0 | +2.75% | $+1.19 |
| 2026-11-18T07:30 | USUALUSDT | surge | TARGET | 0.0 | +2.75% | $+1.19 |
| 2026-11-18T07:14 | PHAUSDT | bottom | STOP | 4.8 | -3.25% | $-1.45 |
| 2026-11-18T07:14 | FFUSDT | surge | STOP | 11.5 | -3.25% | $-1.45 |
| 2026-11-18T05:36 | USUALUSDT | surge | TARGET | 1.0 | +2.75% | $+1.15 |
| 2026-11-18T04:29 | ZKPUSDT | surge | STOP | 0.5 | -3.25% | $-1.40 |
| 2026-11-18T03:38 | SKYUSDT | surge | STOP | 8.8 | -3.25% | $-1.45 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-17T23:59 | AVGOBUSDT | surge | 351.62 | 355.38 | +1.07% |
| 2026-11-18T07:30 | EWYBUSDT | surge | 138.73 | 136.72 | -1.45% |
| 2026-11-18T17:11 | TLMUSDT | bottom | 0.000919 | 0.000923 | +0.44% |
| 2026-11-18T17:11 | NVDABUSDT | bottom | 151.75 | 151.83 | +0.05% |
| 2026-11-18T17:11 | ICPUSDT | bottom | 2.193 | 2.225 | +1.46% |
| 2026-11-18T17:27 | CHIPUSDT | surge | 0.02944 | 0.02945 | +0.03% |
| 2026-11-18T17:27 | PROMUSDT | surge | 5.559 | 5.573 | +0.25% |
| 2026-11-18T17:43 | WCTUSDT | surge | 0.02981 | 0.02968 | -0.44% |
| 2026-11-18T17:43 | AMDBUSDT | surge | 521.9 | 521.43 | -0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
