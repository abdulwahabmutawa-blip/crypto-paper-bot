# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T01:35:04+00:00 · runs 3081 · equity **$777.76** (-22.22%) · cash $0.00 · open 10/10 · round trips 1140

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-219.72 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 999 | 50% | -0.17% | 48% | 45% | 8% |
| bottom | 141 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11T01:00 | LAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.07 |
| 2026-10-11T00:44 | LAUSDT | surge | TARGET | 12.5 | +2.75% | $+2.01 |
| 2026-10-10T22:49 | AAVEUSDT | surge | STOP | 16.0 | -3.25% | $-2.47 |
| 2026-10-10T21:44 | SUSDT | surge | TARGET | 0.2 | +2.75% | $+2.22 |
| 2026-10-10T21:06 | EIGENUSDT | surge | TARGET | 2.2 | +2.75% | $+2.23 |
| 2026-10-10T21:06 | INJUSDT | surge | TARGET | 3.8 | +2.75% | $+2.09 |
| 2026-10-10T20:01 | AEROUSDT | surge | TARGET | 5.0 | +2.75% | $+2.12 |
| 2026-10-10T18:38 | TIAUSDT | surge | TARGET | 1.8 | +2.75% | $+2.17 |
| 2026-10-10T17:14 | BABABUSDT | surge | TIME | 24.0 | -0.66% | $-0.50 |
| 2026-10-10T16:41 | CAKEUSDT | surge | TIME | 24.0 | -0.39% | $-0.31 |
| 2026-10-10T16:08 | MSTRBUSDT | surge | TIME | 24.0 | -1.07% | $-0.83 |
| 2026-10-10T14:51 | CRCLBUSDT | surge | TIME | 24.0 | -1.36% | $-1.06 |
| 2026-10-10T14:19 | TSLABUSDT | surge | TIME | 24.0 | -0.97% | $-0.71 |
| 2026-10-10T11:53 | RAYUSDT | bottom | TARGET | 12.8 | +2.75% | $+1.96 |
| 2026-10-10T08:43 | 币安人生USDT | surge | TARGET | 0.8 | +2.75% | $+2.03 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T06:41 | AXSUSDT | surge | 1.251 | 1.248 | -0.24% |
| 2026-10-10T08:43 | WLDUSDT | surge | 0.5538 | 0.5614 | +1.37% |
| 2026-10-10T14:19 | VTHOUSDT | surge | 0.000711 | 0.000697 | -1.97% |
| 2026-10-10T16:08 | 牛来USDT | surge | 0.08136 | 0.08099 | -0.45% |
| 2026-10-10T20:01 | DUSKUSDT | surge | 0.0863 | 0.0858 | -0.58% |
| 2026-10-10T21:06 | INJUSDT | surge | 7.725 | 7.743 | +0.23% |
| 2026-10-10T21:44 | ROSEUSDT | surge | 0.00866 | 0.00861 | -0.58% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.263 | +0.09% |
| 2026-10-11T01:00 | SUSDT | surge | 0.04825 | 0.04767 | -1.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
