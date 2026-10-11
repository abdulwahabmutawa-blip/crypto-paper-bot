# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T13:44:59+00:00 · runs 3124 · equity **$771.24** (-22.88%) · cash $0.00 · open 10/10 · round trips 1161

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-226.01 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1019 | 50% | -0.18% | 47% | 45% | 8% |
| bottom | 142 | 44% | -0.44% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11T13:43 | ACHUSDT | surge | TARGET | 5.0 | +2.75% | $+2.11 |
| 2026-10-11T13:43 | AVAXUSDT | bottom | TARGET | 9.8 | +2.75% | $+2.02 |
| 2026-10-11T12:04 | DUSKUSDT | surge | TARGET | 15.8 | +2.75% | $+2.17 |
| 2026-10-11T10:42 | NEOUSDT | surge | STOP | 1.5 | -3.25% | $-2.55 |
| 2026-10-11T09:49 | MUBARAKUSDT | surge | STOP | 0.2 | -3.25% | $-2.53 |
| 2026-10-11T09:49 | BOMEUSDT | surge | TARGET | 0.8 | +2.75% | $+2.15 |
| 2026-10-11T09:16 | ARBUSDT | surge | TARGET | 2.2 | +2.75% | $+2.09 |
| 2026-10-11T08:59 | BOMEUSDT | surge | TARGET | 2.5 | +2.75% | $+2.18 |
| 2026-10-11T08:59 | WLDUSDT | surge | TIME | 24.0 | -0.83% | $-0.63 |
| 2026-10-11T08:22 | LAUSDT | surge | STOP | 1.8 | -3.25% | $-2.57 |
| 2026-10-11T06:54 | AXSUSDT | surge | TIME | 24.0 | -0.09% | $-0.07 |
| 2026-10-11T06:18 | LAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.33 |
| 2026-10-11T06:18 | ROSEUSDT | surge | STOP | 2.2 | -3.25% | $-2.39 |
| 2026-10-11T04:31 | ZKUSDT | surge | STOP | 0.0 | -3.25% | $-2.85 |
| 2026-10-11T04:14 | LAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.35 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.252 | -0.40% |
| 2026-10-11T03:38 | TRXUSDT | bottom | 0.3303 | 0.3306 | +0.09% |
| 2026-10-11T03:38 | ADAUSDT | bottom | 0.2473 | 0.2481 | +0.32% |
| 2026-10-11T09:49 | ARBUSDT | surge | 0.1995 | 0.1972 | -1.15% |
| 2026-10-11T09:49 | BIOUSDT | surge | 0.02956 | 0.02977 | +0.71% |
| 2026-10-11T10:42 | BOMEUSDT | surge | 0.0011399 | 0.0011067 | -2.91% |
| 2026-10-11T12:04 | 币安人生USDT | surge | 0.5913 | 0.5965 | +0.88% |
| 2026-10-11T13:43 | PLUMEUSDT | surge | 0.01985 | 0.01992 | +0.35% |
| 2026-10-11T13:43 | NILUSDT | surge | 0.0972 | 0.09569 | -1.55% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
