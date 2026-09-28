# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-28T17:22:18+00:00 · runs 2033 · equity **$910.98** (-8.90%) · cash $0.00 · open 10/10 · round trips 750

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.12%/trade · realized $-91.74 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 639 | 53% | -0.06% | 49% | 44% | 7% |
| bottom | 111 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28T17:20 | LINKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.48 |
| 2026-09-28T16:47 | LINKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.37 |
| 2026-09-28T16:31 | ADAUSDT | bottom | TARGET | 1.2 | +2.75% | $+2.45 |
| 2026-09-28T15:58 | NMRUSDT | surge | STOP | 0.0 | -3.25% | $-2.90 |
| 2026-09-28T15:09 | ALGOUSDT | surge | STOP | 0.5 | -3.25% | $-2.93 |
| 2026-09-28T15:09 | IOTAUSDT | surge | STOP | 1.8 | -3.25% | $-3.03 |
| 2026-09-28T14:52 | DOTUSDT | bottom | STOP | 1.5 | -3.25% | $-3.03 |
| 2026-09-28T14:36 | HYPEUSDT | bottom | STOP | 22.5 | -3.25% | $-2.84 |
| 2026-09-28T14:03 | 牛来USDT | surge | STOP | 0.8 | -3.25% | $-3.03 |
| 2026-09-28T13:47 | ALGOUSDT | surge | TARGET | 0.0 | +2.75% | $+2.56 |
| 2026-09-28T13:14 | 牛来USDT | surge | TARGET | 0.2 | +2.75% | $+2.55 |
| 2026-09-28T12:41 | ADAUSDT | bottom | TARGET | 4.8 | +2.75% | $+2.53 |
| 2026-09-28T12:25 | MARSCOINUSDT | surge | TARGET | 0.0 | +2.75% | $+2.51 |
| 2026-09-28T08:49 | PROMUSDT | surge | STOP | 2.2 | -3.25% | $-2.99 |
| 2026-09-28T08:00 | HBARUSDT | surge | STOP | 0.5 | -3.25% | $-3.07 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T03:34 | MSTRBUSDT | bottom | 156.65 | 161.1 | +2.84% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 230.61 | +1.19% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.12963 | +0.23% |
| 2026-09-28T13:14 | PROMUSDT | surge | 6.412 | 6.326 | -1.34% |
| 2026-09-28T13:47 | NIGHTUSDT | surge | 0.02751 | 0.02753 | +0.07% |
| 2026-09-28T14:36 | WUSDT | bottom | 0.01377 | 0.01375 | -0.15% |
| 2026-09-28T15:42 | DODOUSDT | surge | 0.01887 | 0.01856 | -1.64% |
| 2026-09-28T16:47 | 牛来USDT | surge | 0.11532 | 0.11654 | +1.06% |
| 2026-09-28T17:20 | ALGOUSDT | surge | 0.1354 | 0.1362 | +0.59% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
