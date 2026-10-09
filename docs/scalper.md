# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-09T00:05:33+00:00 · runs 2901 · equity **$769.62** (-23.04%) · cash $151.09 · open 8/10 · round trips 1085

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-225.59 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 950 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 135 | 44% | -0.46% | 39% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-08T15:37 | APTUSDT | surge | STOP | 2.2 | -3.25% | $-2.50 |
| 2026-10-08T15:03 | LPTUSDT | surge | STOP | 1.8 | -3.25% | $-2.50 |
| 2026-10-08T14:29 | PYTHUSDT | surge | TARGET | 5.2 | +2.75% | $+2.14 |
| 2026-10-08T14:29 | ATOMUSDT | surge | TARGET | 6.5 | +2.75% | $+2.22 |
| 2026-10-08T14:12 | TIAUSDT | surge | TARGET | 8.2 | +2.75% | $+2.14 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T04:39 | NVDABUSDT | bottom | 237.11 | 231 | -2.58% |
| 2026-10-08T20:37 | AEROUSDT | surge | 0.8244 | 0.8324 | +0.97% |
| 2026-10-08T20:37 | FILUSDT | surge | 1.0745 | 1.073 | -0.14% |
| 2026-10-08T20:37 | TRXUSDT | bottom | 0.333 | 0.3327 | -0.09% |
| 2026-10-08T20:37 | METUSDT | bottom | 0.4396 | 0.4376 | -0.45% |
| 2026-10-08T21:11 | MUBARAKUSDT | surge | 0.07694 | 0.07619 | -0.97% |
| 2026-10-08T22:38 | PYTHUSDT | surge | 0.08358 | 0.08111 | -2.96% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
