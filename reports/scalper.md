# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-24T14:30:17+00:00 · runs 1671 · equity **$933.38** (-6.66%) · cash $0.00 · open 10/10 · round trips 587

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.12%/trade · realized $-74.99 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 492 | 53% | -0.04% | 49% | 43% | 8% |
| bottom | 95 | 42% | -0.54% | 39% | 46% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-24T14:28 | MORPHOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.53 |
| 2026-09-24T14:28 | COMPUSDT | surge | TARGET | 0.5 | +2.75% | $+2.53 |
| 2026-09-24T09:44 | FFUSDT | surge | STOP | 1.2 | -3.25% | $-3.05 |
| 2026-09-24T09:44 | LTCUSDT | surge | STOP | 2.0 | -3.25% | $-3.05 |
| 2026-09-24T09:11 | ONDOUSDT | surge | STOP | 1.0 | -3.25% | $-3.05 |
| 2026-09-24T09:11 | MSTRBUSDT | bottom | STOP | 18.2 | -3.25% | $-3.06 |
| 2026-09-23T21:33 | RAYUSDT | surge | STOP | 1.5 | -3.25% | $-3.07 |
| 2026-09-23T16:19 | SKYUSDT | surge | STOP | 3.0 | -3.25% | $-3.21 |
| 2026-09-23T16:02 | MUBUSDT | surge | TIME | 24.0 | -0.14% | $-0.13 |
| 2026-09-23T15:46 | NEARUSDT | surge | STOP | 0.5 | -3.25% | $-3.07 |
| 2026-09-23T15:30 | RAYUSDT | surge | TARGET | 0.0 | +2.75% | $+2.60 |
| 2026-09-23T15:13 | SNDKBUSDT | surge | TIME | 24.0 | -1.24% | $-1.19 |
| 2026-09-23T14:24 | HBARUSDT | bottom | STOP | 0.0 | -3.25% | $-3.18 |
| 2026-09-23T14:24 | ZROUSDT | surge | STOP | 0.0 | -3.25% | $-3.18 |
| 2026-09-23T14:24 | COTIUSDT | surge | STOP | 0.2 | -3.25% | $-3.28 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-23T14:40 | BNBUSDT | bottom | 760.19 | 782.73 | +2.97% |
| 2026-09-23T14:40 | BTCUSDT | bottom | 84041.7 | 84860.8 | +0.97% |
| 2026-09-24T13:06 | MINAUSDT | surge | 0.1516 | 0.1524 | +0.53% |
| 2026-09-24T13:06 | MUBUSDT | bottom | 1048.13 | 1056.43 | +0.79% |
| 2026-09-24T13:39 | GIGGLEUSDT | surge | 41.48 | 41.88 | +0.96% |
| 2026-09-24T13:39 | CAKEUSDT | surge | 2.667 | 2.676 | +0.34% |
| 2026-09-24T13:39 | RENDERUSDT | surge | 1.834 | 1.861 | +1.47% |
| 2026-09-24T14:28 | TSTUSDT | surge | 0.02002 | 0.02013 | +0.55% |
| 2026-09-24T14:28 | INTCBUSDT | surge | 123.87 | 124.35 | +0.39% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
