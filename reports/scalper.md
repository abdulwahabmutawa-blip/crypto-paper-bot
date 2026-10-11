# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T15:08:06+00:00 · runs 3127 · equity **$779.17** (-22.08%) · cash $0.00 · open 10/10 · round trips 1166

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-224.47 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1024 | 50% | -0.18% | 48% | 45% | 8% |
| bottom | 142 | 44% | -0.44% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11T15:06 | IOUSDT | surge | TARGET | 0.5 | +2.75% | $+2.16 |
| 2026-10-11T15:06 | NILUSDT | surge | STOP | 0.8 | -3.25% | $-2.51 |
| 2026-10-11T14:16 | PLUMEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.12 |
| 2026-10-11T14:00 | 币安人生USDT | surge | TARGET | 1.8 | +2.75% | $+2.23 |
| 2026-10-11T14:00 | BOMEUSDT | surge | STOP | 3.0 | -3.25% | $-2.46 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.261 | +0.00% |
| 2026-10-11T03:38 | TRXUSDT | bottom | 0.3303 | 0.3303 | +0.00% |
| 2026-10-11T03:38 | ADAUSDT | bottom | 0.2473 | 0.249 | +0.69% |
| 2026-10-11T09:49 | ARBUSDT | surge | 0.1995 | 0.1988 | -0.35% |
| 2026-10-11T09:49 | BIOUSDT | surge | 0.02956 | 0.02995 | +1.32% |
| 2026-10-11T14:00 | MEGAUSDT | surge | 0.04439 | 0.04564 | +2.82% |
| 2026-10-11T14:16 | PLUMEUSDT | surge | 0.02052 | 0.02003 | -2.39% |
| 2026-10-11T15:06 | ALGOUSDT | surge | 0.1215 | 0.1243 | +2.30% |
| 2026-10-11T15:06 | ATOMUSDT | surge | 2.017 | 2.024 | +0.35% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
