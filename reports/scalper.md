# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-24T14:46:47+00:00 · runs 1672 · equity **$927.51** (-7.25%) · cash $0.00 · open 10/10 · round trips 589

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-72.22 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 492 | 53% | -0.04% | 49% | 43% | 8% |
| bottom | 97 | 43% | -0.50% | 39% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-24T14:45 | BTCUSDT | bottom | TIME | 24.0 | +0.19% | $+0.18 |
| 2026-09-24T14:45 | BNBUSDT | bottom | TARGET | 23.8 | +2.75% | $+2.59 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-24T13:06 | MINAUSDT | surge | 0.1516 | 0.1498 | -1.19% |
| 2026-09-24T13:06 | MUBUSDT | bottom | 1048.13 | 1056.44 | +0.79% |
| 2026-09-24T13:39 | GIGGLEUSDT | surge | 41.48 | 41.41 | -0.17% |
| 2026-09-24T13:39 | CAKEUSDT | surge | 2.667 | 2.694 | +1.01% |
| 2026-09-24T13:39 | RENDERUSDT | surge | 1.834 | 1.841 | +0.38% |
| 2026-09-24T14:28 | TSTUSDT | surge | 0.02002 | 0.01983 | -0.95% |
| 2026-09-24T14:28 | INTCBUSDT | surge | 123.87 | 123.88 | +0.01% |
| 2026-09-24T14:45 | COMPUSDT | surge | 24.08 | 24.07 | -0.04% |
| 2026-09-24T14:45 | PLUMEUSDT | surge | 0.01782 | 0.0178 | -0.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
