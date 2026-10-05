# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-05T22:33:04+00:00 · runs 2646 · equity **$836.37** (-16.36%) · cash $0.00 · open 10/10 · round trips 982

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.18%/trade · realized $-165.93 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 855 | 51% | -0.15% | 48% | 45% | 7% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-05T22:14 | SHIBUSDT | surge | TIME | 24.0 | -0.76% | $-0.63 |
| 2026-10-05T20:35 | FILUSDT | surge | TARGET | 0.5 | +2.75% | $+2.17 |
| 2026-10-05T20:18 | SPCXBUSDT | surge | TARGET | 5.2 | +2.75% | $+2.30 |
| 2026-10-05T19:45 | PARTIUSDT | surge | STOP | 2.2 | -3.25% | $-2.65 |
| 2026-10-05T19:28 | EDUUSDT | surge | STOP | 0.0 | -3.25% | $-2.79 |
| 2026-10-05T19:11 | FILUSDT | surge | TARGET | 4.0 | +2.75% | $+2.30 |
| 2026-10-05T17:11 | MSTRBUSDT | surge | STOP | 18.0 | -3.25% | $-2.74 |
| 2026-10-05T16:36 | PENGUUSDT | surge | STOP | 11.5 | -3.25% | $-2.73 |
| 2026-10-05T16:00 | EDUUSDT | surge | STOP | 0.0 | -3.25% | $-2.53 |
| 2026-10-05T15:43 | PENDLEUSDT | surge | STOP | 7.8 | -3.25% | $-2.61 |
| 2026-10-05T14:49 | VIRTUALUSDT | surge | STOP | 9.2 | -3.25% | $-2.64 |
| 2026-10-05T14:49 | LDOUSDT | surge | STOP | 11.0 | -3.25% | $-2.97 |
| 2026-10-05T07:55 | GRTUSDT | surge | TARGET | 3.2 | +2.75% | $+2.15 |
| 2026-10-05T05:29 | SCRUSDT | surge | STOP | 0.2 | -3.25% | $-2.73 |
| 2026-10-05T04:55 | BROCCOLI714USDT | surge | STOP | 11.2 | -3.25% | $-2.64 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-04T23:15 | FLOKIUSDT | surge | 2.915e-05 | 2.939e-05 | +0.82% |
| 2026-10-05T00:04 | MEMEUSDT | surge | 0.000625 | 0.000626 | +0.16% |
| 2026-10-05T03:31 | ADAUSDT | surge | 0.2696 | 0.2726 | +1.11% |
| 2026-10-05T16:00 | WDCBUSDT | surge | 442.05 | 440.81 | -0.28% |
| 2026-10-05T16:36 | TSLABUSDT | surge | 378.15 | 379.27 | +0.30% |
| 2026-10-05T19:28 | MRNABUSDT | surge | 203.03 | 203.78 | +0.37% |
| 2026-10-05T20:18 | SPCXBUSDT | surge | 171.35 | 171.17 | -0.11% |
| 2026-10-05T20:35 | ICPUSDT | surge | 3.547 | 3.587 | +1.13% |
| 2026-10-05T22:14 | DIAUSDT | surge | 0.1825 | 0.1809 | -0.88% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
