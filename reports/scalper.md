# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-06T10:11:23+00:00 · runs 2683 · equity **$826.17** (-17.38%) · cash $0.00 · open 10/10 · round trips 995

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.19%/trade · realized $-175.54 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 868 | 51% | -0.16% | 48% | 45% | 8% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-06T09:34 | LPTUSDT | surge | STOP | 1.0 | -3.25% | $-2.81 |
| 2026-10-06T08:24 | SENTUSDT | surge | TARGET | 4.5 | +2.75% | $+2.32 |
| 2026-10-06T07:49 | PARTIUSDT | surge | TARGET | 4.0 | +2.75% | $+2.32 |
| 2026-10-06T07:31 | VTHOUSDT | surge | STOP | 0.0 | -3.25% | $-2.57 |
| 2026-10-06T07:14 | VTHOUSDT | surge | TARGET | 1.8 | +2.75% | $+2.11 |
| 2026-10-06T06:56 | CHIPUSDT | surge | TARGET | 3.0 | +2.75% | $+2.32 |
| 2026-10-06T05:12 | SUSDT | surge | STOP | 4.8 | -3.25% | $-2.58 |
| 2026-10-06T03:44 | ORDIUSDT | surge | STOP | 4.0 | -3.25% | $-2.83 |
| 2026-10-06T03:44 | ICPUSDT | surge | STOP | 7.0 | -3.25% | $-2.63 |
| 2026-10-06T03:44 | ADAUSDT | surge | TIME | 24.0 | -1.55% | $-1.42 |
| 2026-10-06T00:13 | MEMEUSDT | surge | TIME | 24.0 | -0.89% | $-0.71 |
| 2026-10-05T23:37 | FLOKIUSDT | surge | TIME | 24.0 | -0.49% | $-0.43 |
| 2026-10-05T23:04 | DIAUSDT | surge | STOP | 0.8 | -3.25% | $-2.69 |
| 2026-10-05T22:14 | SHIBUSDT | surge | TIME | 24.0 | -0.76% | $-0.63 |
| 2026-10-05T20:35 | FILUSDT | surge | TARGET | 0.5 | +2.75% | $+2.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-05T16:00 | WDCBUSDT | surge | 442.05 | 432.12 | -2.25% |
| 2026-10-05T16:36 | TSLABUSDT | surge | 378.15 | 381.32 | +0.84% |
| 2026-10-05T19:28 | MRNABUSDT | surge | 203.03 | 204.88 | +0.91% |
| 2026-10-05T20:18 | SPCXBUSDT | surge | 171.35 | 173.21 | +1.09% |
| 2026-10-05T23:04 | FILUSDT | surge | 1.179 | 1.1716 | -0.63% |
| 2026-10-06T06:56 | ACEUSDT | surge | 0.1927 | 0.1954 | +1.40% |
| 2026-10-06T07:31 | WLFIUSDT | surge | 0.0564 | 0.0568 | +0.71% |
| 2026-10-06T07:49 | GRAMUSDT | surge | 1.573 | 1.564 | -0.57% |
| 2026-10-06T09:34 | C98USDT | surge | 0.01841 | 0.01847 | +0.33% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
