# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T05:27:18+00:00 · runs 3095 · equity **$769.62** (-23.04%) · cash $0.00 · open 10/10 · round trips 1148

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.22%/trade · realized $-230.32 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1007 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 141 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11T04:31 | ZKUSDT | surge | STOP | 0.0 | -3.25% | $-2.85 |
| 2026-10-11T04:14 | LAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.35 |
| 2026-10-11T03:38 | NEOUSDT | surge | STOP | 0.2 | -3.25% | $-2.41 |
| 2026-10-11T03:38 | SUSDT | surge | STOP | 2.2 | -3.25% | $-2.51 |
| 2026-10-11T03:38 | INJUSDT | surge | STOP | 6.2 | -3.25% | $-2.63 |
| 2026-10-11T03:38 | VTHOUSDT | surge | STOP | 13.0 | -3.25% | $-2.34 |
| 2026-10-11T03:20 | ROSEUSDT | surge | TARGET | 5.5 | +2.75% | $+2.28 |
| 2026-10-11T03:03 | 牛来USDT | surge | STOP | 10.8 | -3.25% | $-2.49 |
| 2026-10-11T01:00 | LAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.07 |
| 2026-10-11T00:44 | LAUSDT | surge | TARGET | 12.5 | +2.75% | $+2.01 |
| 2026-10-10T22:49 | AAVEUSDT | surge | STOP | 16.0 | -3.25% | $-2.47 |
| 2026-10-10T21:44 | SUSDT | surge | TARGET | 0.2 | +2.75% | $+2.22 |
| 2026-10-10T21:06 | EIGENUSDT | surge | TARGET | 2.2 | +2.75% | $+2.23 |
| 2026-10-10T21:06 | INJUSDT | surge | TARGET | 3.8 | +2.75% | $+2.09 |
| 2026-10-10T20:01 | AEROUSDT | surge | TARGET | 5.0 | +2.75% | $+2.12 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T06:41 | AXSUSDT | surge | 1.251 | 1.238 | -1.04% |
| 2026-10-10T08:43 | WLDUSDT | surge | 0.5538 | 0.5574 | +0.65% |
| 2026-10-10T20:01 | DUSKUSDT | surge | 0.0863 | 0.086 | -0.35% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.252 | -0.40% |
| 2026-10-11T03:38 | TRXUSDT | bottom | 0.3303 | 0.3307 | +0.12% |
| 2026-10-11T03:38 | AVAXUSDT | bottom | 10.234 | 10.29 | +0.55% |
| 2026-10-11T03:38 | ADAUSDT | bottom | 0.2473 | 0.2479 | +0.24% |
| 2026-10-11T03:56 | ROSEUSDT | surge | 0.00879 | 0.00866 | -1.48% |
| 2026-10-11T04:31 | LAUSDT | surge | 0.0695 | 0.0705 | +1.44% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
