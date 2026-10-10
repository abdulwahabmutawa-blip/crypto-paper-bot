# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-10T17:50:48+00:00 · runs 3052 · equity **$766.30** (-23.37%) · cash $0.00 · open 10/10 · round trips 1132

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-232.16 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 991 | 50% | -0.19% | 47% | 45% | 8% |
| bottom | 141 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-10T17:14 | BABABUSDT | surge | TIME | 24.0 | -0.66% | $-0.50 |
| 2026-10-10T16:41 | CAKEUSDT | surge | TIME | 24.0 | -0.39% | $-0.31 |
| 2026-10-10T16:08 | MSTRBUSDT | surge | TIME | 24.0 | -1.07% | $-0.83 |
| 2026-10-10T14:51 | CRCLBUSDT | surge | TIME | 24.0 | -1.36% | $-1.06 |
| 2026-10-10T14:19 | TSLABUSDT | surge | TIME | 24.0 | -0.97% | $-0.71 |
| 2026-10-10T11:53 | RAYUSDT | bottom | TARGET | 12.8 | +2.75% | $+1.96 |
| 2026-10-10T08:43 | 币安人生USDT | surge | TARGET | 0.8 | +2.75% | $+2.03 |
| 2026-10-10T07:34 | CYBERUSDT | surge | STOP | 10.5 | -3.25% | $-2.48 |
| 2026-10-10T06:41 | ALTUSDT | surge | STOP | 2.0 | -3.25% | $-2.62 |
| 2026-10-10T06:41 | ATOMUSDT | surge | STOP | 10.0 | -3.25% | $-2.48 |
| 2026-10-10T04:22 | C98USDT | surge | TARGET | 0.5 | +2.75% | $+2.16 |
| 2026-10-10T03:30 | WLFIUSDT | surge | TARGET | 6.5 | +2.75% | $+2.10 |
| 2026-10-09T22:51 | OPUSDT | surge | TARGET | 2.8 | +2.75% | $+1.91 |
| 2026-10-09T20:51 | TRXUSDT | bottom | TIME | 24.0 | -0.46% | $-0.35 |
| 2026-10-09T20:51 | FILUSDT | surge | TIME | 24.0 | +0.18% | $+0.14 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T06:41 | AXSUSDT | surge | 1.251 | 1.261 | +0.80% |
| 2026-10-10T06:41 | AAVEUSDT | surge | 174.36 | 170.67 | -2.12% |
| 2026-10-10T08:43 | WLDUSDT | surge | 0.5538 | 0.5558 | +0.36% |
| 2026-10-10T11:53 | LAUSDT | surge | 0.0663 | 0.0651 | -1.81% |
| 2026-10-10T14:19 | VTHOUSDT | surge | 0.000711 | 0.000698 | -1.83% |
| 2026-10-10T14:51 | AEROUSDT | surge | 0.9046 | 0.8998 | -0.53% |
| 2026-10-10T16:08 | 牛来USDT | surge | 0.08136 | 0.08237 | +1.24% |
| 2026-10-10T16:41 | TIAUSDT | surge | 0.5053 | 0.5083 | +0.59% |
| 2026-10-10T17:14 | INJUSDT | surge | 7.489 | 7.569 | +1.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
