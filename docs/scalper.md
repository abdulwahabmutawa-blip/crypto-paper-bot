# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-07T08:15:52+00:00 · runs 2756 · equity **$813.87** (-18.61%) · cash $158.34 · open 8/10 · round trips 1043

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.19%/trade · realized $-188.90 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 914 | 51% | -0.16% | 48% | 45% | 8% |
| bottom | 129 | 45% | -0.43% | 40% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-07T08:13 | SYNUSDT | surge | STOP | 0.8 | -3.25% | $-2.61 |
| 2026-10-07T07:19 | PUMPUSDT | surge | TARGET | 1.8 | +2.75% | $+2.20 |
| 2026-10-07T06:43 | ACEUSDT | surge | STOP | 1.2 | -3.25% | $-2.60 |
| 2026-10-07T06:43 | STXUSDT | surge | TARGET | 2.8 | +2.75% | $+2.24 |
| 2026-10-07T06:20 | MOVRUSDT | surge | STOP | 0.8 | -3.25% | $-2.60 |
| 2026-10-07T06:20 | PARTIUSDT | surge | TARGET | 1.2 | +2.75% | $+2.22 |
| 2026-10-07T06:02 | SANDUSDT | surge | STOP | 0.0 | -3.25% | $-2.69 |
| 2026-10-07T05:44 | SANDUSDT | surge | TARGET | 0.2 | +2.75% | $+2.22 |
| 2026-10-07T05:26 | RESOLVUSDT | surge | STOP | 0.8 | -3.25% | $-2.64 |
| 2026-10-07T04:51 | 牛来USDT | surge | STOP | 1.8 | -3.25% | $-2.64 |
| 2026-10-07T02:29 | MAGICUSDT | surge | STOP | 0.5 | -3.25% | $-2.95 |
| 2026-10-07T02:29 | ICPUSDT | bottom | STOP | 2.8 | -3.25% | $-2.55 |
| 2026-10-07T02:29 | DASHUSDT | bottom | STOP | 3.0 | -3.25% | $-2.83 |
| 2026-10-07T02:29 | WLFIUSDT | surge | STOP | 18.5 | -3.25% | $-2.48 |
| 2026-10-07T02:11 | RESOLVUSDT | surge | STOP | 1.0 | -3.25% | $-2.81 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-07T01:53 | TRXUSDT | bottom | 0.3352 | 0.3333 | -0.57% |
| 2026-10-07T02:47 | SPCXBUSDT | bottom | 168.44 | 169.15 | +0.42% |
| 2026-10-07T02:47 | AVAXUSDT | bottom | 11.021 | 11.257 | +2.14% |
| 2026-10-07T07:19 | ARKUSDT | surge | 0.2234 | 0.2262 | +1.25% |
| 2026-10-07T07:19 | PUMPUSDT | surge | 0.006597 | 0.006566 | -0.47% |
| 2026-10-07T07:55 | STXUSDT | surge | 0.4021 | 0.4012 | -0.22% |
| 2026-10-07T07:55 | PARTIUSDT | surge | 0.0349 | 0.0352 | +0.86% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
