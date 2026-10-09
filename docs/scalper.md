# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-09T13:09:27+00:00 · runs 2949 · equity **$769.21** (-23.08%) · cash $0.00 · open 10/10 · round trips 1103

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.23%/trade · realized $-228.40 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 965 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 138 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-09T12:49 | GRAMUSDT | surge | TARGET | 2.2 | +2.75% | $+2.11 |
| 2026-10-09T10:29 | ZKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.07 |
| 2026-10-09T10:29 | ONTUSDT | surge | TARGET | 8.0 | +2.75% | $+2.04 |
| 2026-10-09T10:06 | SUSDT | surge | TARGET | 1.0 | +2.75% | $+2.04 |
| 2026-10-09T10:06 | BEAMXUSDT | surge | TARGET | 1.5 | +2.75% | $+2.01 |
| 2026-10-09T10:06 | API3USDT | surge | TARGET | 1.8 | +2.75% | $+2.01 |
| 2026-10-09T08:58 | MUBARAKUSDT | surge | STOP | 11.8 | -3.25% | $-2.49 |
| 2026-10-09T08:41 | NMRUSDT | surge | STOP | 0.5 | -3.25% | $-2.51 |
| 2026-10-09T08:24 | ONEUSDT | surge | STOP | 5.8 | -3.25% | $-2.46 |
| 2026-10-09T08:07 | 牛来USDT | surge | STOP | 4.8 | -3.25% | $-2.46 |
| 2026-10-09T07:50 | ATOMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.01 |
| 2026-10-09T07:33 | METUSDT | bottom | TARGET | 2.5 | +2.75% | $+2.12 |
| 2026-10-09T07:16 | AEROUSDT | surge | STOP | 4.5 | -3.25% | $-2.46 |
| 2026-10-09T04:59 | NVDABUSDT | bottom | TIME | 24.0 | -2.02% | $-1.59 |
| 2026-10-09T02:28 | AEROUSDT | surge | TARGET | 5.8 | +2.75% | $+2.11 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T20:37 | FILUSDT | surge | 1.0745 | 1.0718 | -0.25% |
| 2026-10-08T20:37 | TRXUSDT | bottom | 0.333 | 0.333 | +0.00% |
| 2026-10-09T00:52 | ALGOUSDT | bottom | 0.1177 | 0.1181 | +0.34% |
| 2026-10-09T07:50 | ATOMUSDT | surge | 1.954 | 1.966 | +0.61% |
| 2026-10-09T08:41 | APTUSDT | surge | 0.8194 | 0.8103 | -1.11% |
| 2026-10-09T10:06 | API3USDT | surge | 0.318 | 0.3203 | +0.72% |
| 2026-10-09T10:06 | PROMUSDT | surge | 5.411 | 5.309 | -1.89% |
| 2026-10-09T10:29 | SUSDT | surge | 0.04508 | 0.04477 | -0.69% |
| 2026-10-09T12:49 | GRAMUSDT | surge | 1.493 | 1.48 | -0.87% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
