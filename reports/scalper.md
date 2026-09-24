# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-24T17:24:17+00:00 · runs 1682 · equity **$936.41** (-6.36%) · cash $0.00 · open 10/10 · round trips 594

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-70.61 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 497 | 53% | -0.03% | 49% | 43% | 8% |
| bottom | 97 | 43% | -0.50% | 39% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-24T16:27 | PLUMEUSDT | surge | TARGET | 1.5 | +2.75% | $+2.63 |
| 2026-09-24T15:51 | CAKEUSDT | surge | TARGET | 2.0 | +2.75% | $+2.53 |
| 2026-09-24T15:34 | ETCUSDT | surge | TARGET | 0.0 | +2.75% | $+2.52 |
| 2026-09-24T15:18 | TSTUSDT | surge | STOP | 0.8 | -3.25% | $-3.08 |
| 2026-09-24T15:01 | MINAUSDT | surge | STOP | 1.8 | -3.25% | $-3.00 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-24T13:06 | MUBUSDT | bottom | 1048.13 | 1073.98 | +2.47% |
| 2026-09-24T13:39 | GIGGLEUSDT | surge | 41.48 | 41.42 | -0.14% |
| 2026-09-24T13:39 | RENDERUSDT | surge | 1.834 | 1.879 | +2.45% |
| 2026-09-24T14:28 | INTCBUSDT | surge | 123.87 | 125.8 | +1.56% |
| 2026-09-24T14:45 | COMPUSDT | surge | 24.08 | 24.14 | +0.25% |
| 2026-09-24T15:01 | MORPHOUSDT | surge | 2.825 | 2.814 | -0.39% |
| 2026-09-24T15:34 | ENSUSDT | surge | 7.13 | 7.09 | -0.56% |
| 2026-09-24T15:51 | CAKEUSDT | surge | 2.758 | 2.748 | -0.36% |
| 2026-09-24T16:27 | ALGOUSDT | surge | 0.1113 | 0.1137 | +2.16% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
