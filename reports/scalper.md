# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-11T03:22:55+00:00 · runs 3088 · equity **$768.50** (-23.15%) · cash $0.00 · open 10/10 · round trips 1142

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-219.93 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1001 | 50% | -0.17% | 48% | 45% | 7% |
| bottom | 141 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-11T03:20 | ROSEUSDT | surge | TARGET | 5.5 | +2.75% | $+2.28 |
| 2026-10-11T03:03 | 牛来USDT | surge | STOP | 10.8 | -3.25% | $-2.49 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-10T06:41 | AXSUSDT | surge | 1.251 | 1.219 | -2.56% |
| 2026-10-10T08:43 | WLDUSDT | surge | 0.5538 | 0.5475 | -1.14% |
| 2026-10-10T14:19 | VTHOUSDT | surge | 0.000711 | 0.00069 | -2.95% |
| 2026-10-10T20:01 | DUSKUSDT | surge | 0.0863 | 0.0859 | -0.46% |
| 2026-10-10T21:06 | INJUSDT | surge | 7.725 | 7.505 | -2.85% |
| 2026-10-10T22:49 | CAKEUSDT | surge | 2.261 | 2.245 | -0.71% |
| 2026-10-11T01:00 | SUSDT | surge | 0.04825 | 0.04733 | -1.91% |
| 2026-10-11T03:03 | NEOUSDT | surge | 2.628 | 2.549 | -3.01% |
| 2026-10-11T03:20 | LAUSDT | surge | 0.0683 | 0.0685 | +0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
