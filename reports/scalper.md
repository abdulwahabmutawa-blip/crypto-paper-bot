# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-06T07:16:02+00:00 · runs 2673 · equity **$824.35** (-17.57%) · cash $0.00 · open 10/10 · round trips 991

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.19%/trade · realized $-174.79 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 864 | 51% | -0.16% | 48% | 45% | 8% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-05T20:18 | SPCXBUSDT | surge | TARGET | 5.2 | +2.75% | $+2.30 |
| 2026-10-05T19:45 | PARTIUSDT | surge | STOP | 2.2 | -3.25% | $-2.65 |
| 2026-10-05T19:28 | EDUUSDT | surge | STOP | 0.0 | -3.25% | $-2.79 |
| 2026-10-05T19:11 | FILUSDT | surge | TARGET | 4.0 | +2.75% | $+2.30 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-05T16:00 | WDCBUSDT | surge | 442.05 | 440.88 | -0.26% |
| 2026-10-05T16:36 | TSLABUSDT | surge | 378.15 | 380.48 | +0.62% |
| 2026-10-05T19:28 | MRNABUSDT | surge | 203.03 | 205.86 | +1.39% |
| 2026-10-05T20:18 | SPCXBUSDT | surge | 171.35 | 173.19 | +1.07% |
| 2026-10-05T23:04 | FILUSDT | surge | 1.179 | 1.1965 | +1.48% |
| 2026-10-06T03:44 | SENTUSDT | surge | 0.02544 | 0.02534 | -0.39% |
| 2026-10-06T03:44 | PARTIUSDT | surge | 0.0323 | 0.0323 | +0.00% |
| 2026-10-06T06:56 | ACEUSDT | surge | 0.1927 | 0.1924 | -0.16% |
| 2026-10-06T07:14 | VTHOUSDT | surge | 0.000777 | 0.000738 | -5.02% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
