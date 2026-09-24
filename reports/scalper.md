# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-24T22:07:11+00:00 · runs 1698 · equity **$932.70** (-6.73%) · cash $0.00 · open 10/10 · round trips 597

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-62.93 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 499 | 54% | -0.02% | 50% | 42% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-24T20:19 | INTCBUSDT | surge | TARGET | 5.8 | +2.75% | $+2.60 |
| 2026-09-24T20:01 | MUBUSDT | bottom | TARGET | 6.8 | +2.75% | $+2.53 |
| 2026-09-24T18:33 | RENDERUSDT | surge | TARGET | 4.8 | +2.75% | $+2.53 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-24T13:39 | GIGGLEUSDT | surge | 41.48 | 41 | -1.16% |
| 2026-09-24T14:45 | COMPUSDT | surge | 24.08 | 23.97 | -0.46% |
| 2026-09-24T15:01 | MORPHOUSDT | surge | 2.825 | 2.812 | -0.46% |
| 2026-09-24T15:34 | ENSUSDT | surge | 7.13 | 7.02 | -1.54% |
| 2026-09-24T15:51 | CAKEUSDT | surge | 2.758 | 2.741 | -0.62% |
| 2026-09-24T16:27 | ALGOUSDT | surge | 0.1113 | 0.1124 | +0.99% |
| 2026-09-24T18:33 | TRBUSDT | surge | 20.75 | 20.32 | -2.07% |
| 2026-09-24T20:01 | AMDBUSDT | surge | 629.27 | 630.12 | +0.14% |
| 2026-09-24T20:19 | LINKUSDT | surge | 13.172 | 13.232 | +0.46% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
