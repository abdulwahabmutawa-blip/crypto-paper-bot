# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T20:18:38+00:00 · runs 2124 · equity **$888.90** (-11.11%) · cash $92.48 · open 9/10 · round trips 802

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-112.38 · worst day $-50.94 · trades/day 32.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 687 | 52% | -0.09% | 49% | 44% | 7% |
| bottom | 115 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29T20:16 | ICPUSDT | surge | TARGET | 3.2 | +2.75% | $+2.48 |
| 2026-09-29T19:59 | SKYUSDT | surge | STOP | 1.0 | -3.25% | $-3.01 |
| 2026-09-29T19:59 | COTIUSDT | surge | STOP | 1.8 | -3.25% | $-2.95 |
| 2026-09-29T18:51 | SKYUSDT | surge | TARGET | 1.8 | +2.75% | $+2.48 |
| 2026-09-29T18:10 | ALICEUSDT | surge | STOP | 0.2 | -3.25% | $-2.79 |
| 2026-09-29T17:53 | AAVEUSDT | surge | STOP | 5.2 | -3.25% | $-3.05 |
| 2026-09-29T17:35 | ETHFIUSDT | surge | STOP | 1.2 | -3.25% | $-2.93 |
| 2026-09-29T17:35 | JASMYUSDT | surge | STOP | 1.8 | -3.25% | $-2.84 |
| 2026-09-29T16:59 | ZROUSDT | surge | STOP | 0.5 | -3.25% | $-2.93 |
| 2026-09-29T16:59 | ATOMUSDT | surge | STOP | 6.5 | -3.25% | $-3.12 |
| 2026-09-29T16:24 | REUSDT | surge | STOP | 1.0 | -3.25% | $-3.03 |
| 2026-09-29T16:06 | SPKUSDT | surge | STOP | 0.8 | -3.25% | $-3.03 |
| 2026-09-29T15:31 | ALICEUSDT | surge | STOP | 0.2 | -3.25% | $-3.03 |
| 2026-09-29T15:31 | BONKUSDT | surge | STOP | 0.5 | -3.25% | $-2.71 |
| 2026-09-29T15:31 | COMPUSDT | surge | STOP | 3.0 | -3.25% | $-3.05 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 149.37 | +2.43% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 186.73 | -0.62% |
| 2026-09-29T15:31 | NIGHTUSDT | surge | 0.03196 | 0.03211 | +0.47% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01603 | -1.96% |
| 2026-09-29T17:35 | XLMUSDT | bottom | 0.2216 | 0.2226 | +0.45% |
| 2026-09-29T18:10 | CRCLBUSDT | bottom | 83.55 | 83.6 | +0.06% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 7.1 | +0.85% |
| 2026-09-29T19:59 | PUMPUSDT | surge | 0.00588 | 0.005857 | -0.39% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
