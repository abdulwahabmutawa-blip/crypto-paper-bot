# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T12:55:27+00:00 · runs 3121 · equity **$768.95** (-23.10%) · cash $0.00 · open 10/10 · round trips 1159

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.22%/trade · realized $-230.14 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1018 | 50% | -0.18% | 47% | 45% | 8% |
| bottom | 141 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-11T03:38 | NEOUSDT | surge | STOP | 0.2 | -3.25% | $-2.41 |
| 2026-10-11T03:38 | SUSDT | surge | STOP | 2.2 | -3.25% | $-2.51 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.256 | -0.22% |
| 2026-10-11T03:38 | TRXUSDT | bottom | 0.3303 | 0.3306 | +0.09% |
| 2026-10-11T03:38 | AVAXUSDT | bottom | 10.234 | 10.503 | +2.63% |
| 2026-10-11T03:38 | ADAUSDT | bottom | 0.2473 | 0.2475 | +0.08% |
| 2026-10-11T08:22 | ACHUSDT | surge | 0.00617 | 0.0061 | -1.13% |
| 2026-10-11T09:49 | ARBUSDT | surge | 0.1995 | 0.198 | -0.75% |
| 2026-10-11T09:49 | BIOUSDT | surge | 0.02956 | 0.0295 | -0.20% |
| 2026-10-11T10:42 | BOMEUSDT | surge | 0.0011399 | 0.0011236 | -1.43% |
| 2026-10-11T12:04 | 币安人生USDT | surge | 0.5913 | 0.5905 | -0.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
