# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-07T01:56:02+00:00 · runs 2734 · equity **$829.89** (-17.01%) · cash $0.00 · open 10/10 · round trips 1025

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-160.13 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 898 | 51% | -0.13% | 48% | 44% | 8% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-07T01:53 | INJUSDT | surge | STOP | 4.8 | -3.25% | $-2.73 |
| 2026-10-07T01:36 | MAGICUSDT | surge | TARGET | 3.2 | +2.75% | $+2.43 |
| 2026-10-07T00:54 | RESOLVUSDT | surge | TARGET | 3.8 | +2.75% | $+2.31 |
| 2026-10-06T23:25 | FILUSDT | surge | TIME | 24.0 | -2.03% | $-1.63 |
| 2026-10-06T23:08 | METUSDT | surge | STOP | 3.5 | -3.25% | $-2.93 |
| 2026-10-06T22:14 | MAGICUSDT | surge | TARGET | 0.5 | +2.75% | $+2.36 |
| 2026-10-06T21:39 | MAGICUSDT | surge | TARGET | 4.5 | +2.75% | $+2.36 |
| 2026-10-06T21:39 | GRAMUSDT | surge | STOP | 13.5 | -3.25% | $-2.81 |
| 2026-10-06T20:45 | MARSCOINUSDT | surge | STOP | 3.2 | -3.25% | $-2.76 |
| 2026-10-06T20:45 | SPCXBUSDT | surge | TIME | 24.0 | -0.06% | $-0.05 |
| 2026-10-06T19:15 | RESOLVUSDT | surge | TARGET | 1.5 | +2.75% | $+2.41 |
| 2026-10-06T19:10 | FLUXUSDT | surge | STOP | 0.0 | -3.25% | $-2.83 |
| 2026-10-06T18:53 | MIRAUSDT | surge | STOP | 0.5 | -3.25% | $-2.93 |
| 2026-10-06T18:01 | MIRAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.41 |
| 2026-10-06T17:43 | FLUXUSDT | surge | TARGET | 0.8 | +2.75% | $+2.36 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-06T07:31 | WLFIUSDT | surge | 0.0564 | 0.056 | -0.71% |
| 2026-10-06T14:15 | CRCLBUSDT | surge | 86.06 | 83.81 | -2.61% |
| 2026-10-06T19:10 | TIAUSDT | surge | 0.483 | 0.4777 | -1.10% |
| 2026-10-06T21:39 | TRBUSDT | surge | 22.71 | 22.35 | -1.59% |
| 2026-10-06T23:08 | DASHUSDT | bottom | 55.52 | 54.93 | -1.06% |
| 2026-10-06T23:25 | ICPUSDT | bottom | 3.381 | 3.318 | -1.86% |
| 2026-10-07T00:54 | RESOLVUSDT | surge | 0.02248 | 0.02205 | -1.91% |
| 2026-10-07T01:36 | MAGICUSDT | surge | 0.0727 | 0.072 | -0.96% |
| 2026-10-07T01:53 | TRXUSDT | bottom | 0.3352 | 0.3349 | -0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
