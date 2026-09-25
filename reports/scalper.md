# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-25T02:18:58+00:00 · runs 1714 · equity **$930.60** (-6.94%) · cash $0.00 · open 10/10 · round trips 603

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-70.13 · worst day $-50.94 · trades/day 28.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 505 | 53% | -0.04% | 50% | 43% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-25T02:01 | GIGGLEUSDT | surge | STOP | 12.2 | -3.25% | $-3.00 |
| 2026-09-25T01:44 | MANTRAUSDT | surge | STOP | 0.2 | -3.25% | $-3.28 |
| 2026-09-25T01:44 | CHIPUSDT | surge | STOP | 2.2 | -3.25% | $-3.06 |
| 2026-09-25T01:28 | ALGOUSDT | surge | TARGET | 8.8 | +2.75% | $+2.70 |
| 2026-09-24T23:16 | XPLUSDT | surge | TARGET | 0.5 | +2.75% | $+2.52 |
| 2026-09-24T22:43 | TRBUSDT | surge | STOP | 3.8 | -3.25% | $-3.08 |
| 2026-09-24T20:19 | INTCBUSDT | surge | TARGET | 5.8 | +2.75% | $+2.60 |
| 2026-09-24T20:01 | MUBUSDT | bottom | TARGET | 6.8 | +2.75% | $+2.53 |
| 2026-09-24T18:33 | RENDERUSDT | surge | TARGET | 4.8 | +2.75% | $+2.53 |
| 2026-09-24T16:27 | PLUMEUSDT | surge | TARGET | 1.5 | +2.75% | $+2.63 |
| 2026-09-24T15:51 | CAKEUSDT | surge | TARGET | 2.0 | +2.75% | $+2.53 |
| 2026-09-24T15:34 | ETCUSDT | surge | TARGET | 0.0 | +2.75% | $+2.52 |
| 2026-09-24T15:18 | TSTUSDT | surge | STOP | 0.8 | -3.25% | $-3.08 |
| 2026-09-24T15:01 | MINAUSDT | surge | STOP | 1.8 | -3.25% | $-3.00 |
| 2026-09-24T14:45 | BTCUSDT | bottom | TIME | 24.0 | +0.19% | $+0.18 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-24T14:45 | COMPUSDT | surge | 24.08 | 23.65 | -1.79% |
| 2026-09-24T15:01 | MORPHOUSDT | surge | 2.825 | 2.811 | -0.50% |
| 2026-09-24T15:34 | ENSUSDT | surge | 7.13 | 7.08 | -0.70% |
| 2026-09-24T15:51 | CAKEUSDT | surge | 2.758 | 2.741 | -0.62% |
| 2026-09-24T20:01 | AMDBUSDT | surge | 629.27 | 634.65 | +0.85% |
| 2026-09-24T20:19 | LINKUSDT | surge | 13.172 | 13.415 | +1.84% |
| 2026-09-25T01:44 | AXSUSDT | surge | 1.133 | 1.134 | +0.09% |
| 2026-09-25T01:44 | XLMUSDT | surge | 0.2185 | 0.222 | +1.60% |
| 2026-09-25T02:01 | ENAUSDT | surge | 0.2275 | 0.2273 | -0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
