# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T18:30:30+00:00 · runs 2117 · equity **$890.59** (-10.94%) · cash $0.00 · open 10/10 · round trips 798

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-111.38 · worst day $-50.94 · trades/day 31.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 683 | 52% | -0.09% | 49% | 44% | 7% |
| bottom | 115 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-29T15:13 | BNCBUSDT | surge | STOP | 1.2 | -3.25% | $-3.13 |
| 2026-09-29T15:13 | COINBUSDT | surge | STOP | 2.2 | -3.25% | $-2.78 |
| 2026-09-29T15:13 | BABYUSDT | surge | TARGET | 2.5 | +2.75% | $+2.58 |
| 2026-09-29T15:13 | CRVUSDT | surge | TARGET | 8.2 | +2.75% | $+2.69 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 147.86 | +1.39% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 187.11 | -0.42% |
| 2026-09-29T15:31 | NIGHTUSDT | surge | 0.03196 | 0.03179 | -0.53% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01616 | -1.16% |
| 2026-09-29T16:59 | ICPUSDT | surge | 3.359 | 3.379 | +0.60% |
| 2026-09-29T16:59 | SKYUSDT | surge | 0.08484 | 0.0867 | +2.19% |
| 2026-09-29T17:35 | XLMUSDT | bottom | 0.2216 | 0.222 | +0.18% |
| 2026-09-29T17:53 | COTIUSDT | surge | 0.01344 | 0.01338 | -0.45% |
| 2026-09-29T18:10 | CRCLBUSDT | bottom | 83.55 | 83.8 | +0.30% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
