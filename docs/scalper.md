# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-09T05:35:54+00:00 · runs 2922 · equity **$766.35** (-23.36%) · cash $0.00 · open 10/10 · round trips 1090

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.24%/trade · realized $-232.45 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 953 | 50% | -0.20% | 47% | 45% | 7% |
| bottom | 137 | 44% | -0.49% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-09T04:59 | NVDABUSDT | bottom | TIME | 24.0 | -2.02% | $-1.59 |
| 2026-10-09T02:28 | AEROUSDT | surge | TARGET | 5.8 | +2.75% | $+2.11 |
| 2026-10-09T00:52 | METUSDT | bottom | STOP | 4.0 | -3.25% | $-2.49 |
| 2026-10-09T00:36 | SCRUSDT | surge | STOP | 0.0 | -3.25% | $-2.43 |
| 2026-10-09T00:20 | PYTHUSDT | surge | STOP | 1.5 | -3.25% | $-2.46 |
| 2026-10-09T00:04 | TIAUSDT | surge | STOP | 1.0 | -3.25% | $-2.46 |
| 2026-10-08T23:48 | GTCUSDT | surge | TARGET | 0.0 | +2.75% | $+2.08 |
| 2026-10-08T22:21 | ONTUSDT | surge | STOP | 1.5 | -3.25% | $-2.49 |
| 2026-10-08T18:35 | ARKUSDT | surge | TARGET | 5.2 | +2.75% | $+2.12 |
| 2026-10-08T15:54 | ONTUSDT | surge | STOP | 0.5 | -3.25% | $-2.42 |
| 2026-10-08T15:37 | ATOMUSDT | surge | STOP | 1.0 | -3.25% | $-2.65 |
| 2026-10-08T15:37 | SUPERUSDT | surge | STOP | 1.0 | -3.25% | $-2.65 |
| 2026-10-08T15:37 | ENJUSDT | surge | STOP | 1.2 | -3.25% | $-2.60 |
| 2026-10-08T15:37 | AVNTUSDT | surge | STOP | 1.5 | -3.25% | $-2.50 |
| 2026-10-08T15:37 | PARTIUSDT | surge | STOP | 2.0 | -3.25% | $-2.60 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T20:37 | FILUSDT | surge | 1.0745 | 1.0769 | +0.22% |
| 2026-10-08T20:37 | TRXUSDT | bottom | 0.333 | 0.3323 | -0.21% |
| 2026-10-08T21:11 | MUBARAKUSDT | surge | 0.07694 | 0.07597 | -1.26% |
| 2026-10-09T00:52 | ALGOUSDT | bottom | 0.1177 | 0.1205 | +2.38% |
| 2026-10-09T02:12 | ONTUSDT | surge | 0.06075 | 0.06019 | -0.92% |
| 2026-10-09T02:28 | ONEUSDT | surge | 0.0022 | 0.002163 | -1.68% |
| 2026-10-09T02:44 | AEROUSDT | surge | 0.8432 | 0.8327 | -1.25% |
| 2026-10-09T03:01 | 牛来USDT | surge | 0.07519 | 0.07544 | +0.33% |
| 2026-10-09T04:59 | METUSDT | bottom | 0.4358 | 0.4394 | +0.83% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
