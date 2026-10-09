# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-09T08:43:14+00:00 · runs 2933 · equity **$763.56** (-23.64%) · cash $0.00 · open 10/10 · round trips 1096

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.24%/trade · realized $-238.19 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 958 | 50% | -0.21% | 47% | 46% | 7% |
| bottom | 138 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-09T08:41 | NMRUSDT | surge | STOP | 0.5 | -3.25% | $-2.51 |
| 2026-10-09T08:24 | ONEUSDT | surge | STOP | 5.8 | -3.25% | $-2.46 |
| 2026-10-09T08:07 | 牛来USDT | surge | STOP | 4.8 | -3.25% | $-2.46 |
| 2026-10-09T07:50 | ATOMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.01 |
| 2026-10-09T07:33 | METUSDT | bottom | TARGET | 2.5 | +2.75% | $+2.12 |
| 2026-10-09T07:16 | AEROUSDT | surge | STOP | 4.5 | -3.25% | $-2.46 |
| 2026-10-09T04:59 | NVDABUSDT | bottom | TIME | 24.0 | -2.02% | $-1.59 |
| 2026-10-09T02:28 | AEROUSDT | surge | TARGET | 5.8 | +2.75% | $+2.11 |
| 2026-10-09T00:52 | METUSDT | bottom | STOP | 4.0 | -3.25% | $-2.49 |
| 2026-10-09T00:36 | SCRUSDT | surge | STOP | 0.0 | -3.25% | $-2.43 |
| 2026-10-09T00:20 | PYTHUSDT | surge | STOP | 1.5 | -3.25% | $-2.46 |
| 2026-10-09T00:04 | TIAUSDT | surge | STOP | 1.0 | -3.25% | $-2.46 |
| 2026-10-08T23:48 | GTCUSDT | surge | TARGET | 0.0 | +2.75% | $+2.08 |
| 2026-10-08T22:21 | ONTUSDT | surge | STOP | 1.5 | -3.25% | $-2.49 |
| 2026-10-08T18:35 | ARKUSDT | surge | TARGET | 5.2 | +2.75% | $+2.12 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T20:37 | FILUSDT | surge | 1.0745 | 1.0792 | +0.44% |
| 2026-10-08T20:37 | TRXUSDT | bottom | 0.333 | 0.3324 | -0.18% |
| 2026-10-08T21:11 | MUBARAKUSDT | surge | 0.07694 | 0.07507 | -2.43% |
| 2026-10-09T00:52 | ALGOUSDT | bottom | 0.1177 | 0.1189 | +1.02% |
| 2026-10-09T02:12 | ONTUSDT | surge | 0.06075 | 0.06172 | +1.60% |
| 2026-10-09T07:50 | ATOMUSDT | surge | 1.954 | 1.95 | -0.20% |
| 2026-10-09T08:07 | API3USDT | surge | 0.3097 | 0.3142 | +1.45% |
| 2026-10-09T08:24 | BEAMXUSDT | surge | 0.002693 | 0.002697 | +0.15% |
| 2026-10-09T08:41 | APTUSDT | surge | 0.8194 | 0.8246 | +0.63% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
