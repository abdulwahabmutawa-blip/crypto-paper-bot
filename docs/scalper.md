# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-28T14:54:20+00:00 · runs 2024 · equity **$900.11** (-9.99%) · cash $90.06 · open 9/10 · round trips 744

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.12%/trade · realized $-90.19 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 634 | 53% | -0.06% | 50% | 43% | 7% |
| bottom | 110 | 44% | -0.47% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28T14:52 | DOTUSDT | bottom | STOP | 1.5 | -3.25% | $-3.03 |
| 2026-09-28T14:36 | HYPEUSDT | bottom | STOP | 22.5 | -3.25% | $-2.84 |
| 2026-09-28T14:03 | 牛来USDT | surge | STOP | 0.8 | -3.25% | $-3.03 |
| 2026-09-28T13:47 | ALGOUSDT | surge | TARGET | 0.0 | +2.75% | $+2.56 |
| 2026-09-28T13:14 | 牛来USDT | surge | TARGET | 0.2 | +2.75% | $+2.55 |
| 2026-09-28T12:41 | ADAUSDT | bottom | TARGET | 4.8 | +2.75% | $+2.53 |
| 2026-09-28T12:25 | MARSCOINUSDT | surge | TARGET | 0.0 | +2.75% | $+2.51 |
| 2026-09-28T08:49 | PROMUSDT | surge | STOP | 2.2 | -3.25% | $-2.99 |
| 2026-09-28T08:00 | HBARUSDT | surge | STOP | 0.5 | -3.25% | $-3.07 |
| 2026-09-28T07:44 | BABYUSDT | bottom | STOP | 4.2 | -3.25% | $-2.75 |
| 2026-09-28T07:28 | MUBARAKUSDT | surge | STOP | 0.2 | -3.25% | $-3.06 |
| 2026-09-28T07:28 | HBARUSDT | surge | TARGET | 5.0 | +2.75% | $+2.66 |
| 2026-09-28T06:55 | PUMPUSDT | surge | STOP | 5.5 | -3.25% | $-3.40 |
| 2026-09-28T05:45 | ONDOUSDT | surge | STOP | 1.0 | -3.25% | $-2.97 |
| 2026-09-28T05:45 | SEIUSDT | surge | STOP | 1.8 | -3.25% | $-3.07 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T03:34 | MSTRBUSDT | bottom | 156.65 | 155.45 | -0.77% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 229.34 | +0.63% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.13143 | +1.62% |
| 2026-09-28T13:14 | IOTAUSDT | surge | 0.054 | 0.0523 | -3.15% |
| 2026-09-28T13:14 | PROMUSDT | surge | 6.412 | 6.358 | -0.84% |
| 2026-09-28T13:47 | NIGHTUSDT | surge | 0.02751 | 0.02708 | -1.56% |
| 2026-09-28T14:19 | ALGOUSDT | surge | 0.1338 | 0.1276 | -4.63% |
| 2026-09-28T14:36 | WUSDT | bottom | 0.01377 | 0.0135 | -1.96% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
