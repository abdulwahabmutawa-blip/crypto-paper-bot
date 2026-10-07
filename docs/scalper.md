# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-07T04:53:37+00:00 · runs 2744 · equity **$815.38** (-18.46%) · cash $241.98 · open 7/10 · round trips 1034

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.19%/trade · realized $-184.62 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 905 | 51% | -0.16% | 48% | 45% | 8% |
| bottom | 129 | 45% | -0.43% | 40% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-07T04:51 | 牛来USDT | surge | STOP | 1.8 | -3.25% | $-2.64 |
| 2026-10-07T02:29 | MAGICUSDT | surge | STOP | 0.5 | -3.25% | $-2.95 |
| 2026-10-07T02:29 | ICPUSDT | bottom | STOP | 2.8 | -3.25% | $-2.55 |
| 2026-10-07T02:29 | DASHUSDT | bottom | STOP | 3.0 | -3.25% | $-2.83 |
| 2026-10-07T02:29 | WLFIUSDT | surge | STOP | 18.5 | -3.25% | $-2.48 |
| 2026-10-07T02:11 | RESOLVUSDT | surge | STOP | 1.0 | -3.25% | $-2.81 |
| 2026-10-07T02:11 | TRBUSDT | surge | STOP | 4.2 | -3.25% | $-2.79 |
| 2026-10-07T02:11 | TIAUSDT | surge | STOP | 6.8 | -3.25% | $-2.74 |
| 2026-10-07T02:11 | CRCLBUSDT | surge | STOP | 11.5 | -3.25% | $-2.70 |
| 2026-10-07T01:53 | INJUSDT | surge | STOP | 4.8 | -3.25% | $-2.73 |
| 2026-10-07T01:36 | MAGICUSDT | surge | TARGET | 3.2 | +2.75% | $+2.43 |
| 2026-10-07T00:54 | RESOLVUSDT | surge | TARGET | 3.8 | +2.75% | $+2.31 |
| 2026-10-06T23:25 | FILUSDT | surge | TIME | 24.0 | -2.03% | $-1.63 |
| 2026-10-06T23:08 | METUSDT | surge | STOP | 3.5 | -3.25% | $-2.93 |
| 2026-10-06T22:14 | MAGICUSDT | surge | TARGET | 0.5 | +2.75% | $+2.36 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-07T01:53 | TRXUSDT | bottom | 0.3352 | 0.3326 | -0.78% |
| 2026-10-07T02:47 | SPCXBUSDT | bottom | 168.44 | 169.74 | +0.77% |
| 2026-10-07T02:47 | AVAXUSDT | bottom | 11.021 | 11.072 | +0.46% |
| 2026-10-07T03:58 | STXUSDT | surge | 0.3916 | 0.3956 | +1.02% |
| 2026-10-07T04:16 | RESOLVUSDT | surge | 0.02253 | 0.02233 | -0.89% |
| 2026-10-07T04:51 | PARTIUSDT | surge | 0.0334 | 0.0332 | -0.60% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
