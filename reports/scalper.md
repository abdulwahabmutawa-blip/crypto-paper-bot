# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-05T18:22:26+00:00 · runs 2631 · equity **$830.10** (-16.99%) · cash $0.00 · open 10/10 · round trips 976

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.18%/trade · realized $-166.62 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 849 | 51% | -0.15% | 48% | 45% | 7% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-05T17:11 | MSTRBUSDT | surge | STOP | 18.0 | -3.25% | $-2.74 |
| 2026-10-05T16:36 | PENGUUSDT | surge | STOP | 11.5 | -3.25% | $-2.73 |
| 2026-10-05T16:00 | EDUUSDT | surge | STOP | 0.0 | -3.25% | $-2.53 |
| 2026-10-05T15:43 | PENDLEUSDT | surge | STOP | 7.8 | -3.25% | $-2.61 |
| 2026-10-05T14:49 | VIRTUALUSDT | surge | STOP | 9.2 | -3.25% | $-2.64 |
| 2026-10-05T14:49 | LDOUSDT | surge | STOP | 11.0 | -3.25% | $-2.97 |
| 2026-10-05T07:55 | GRTUSDT | surge | TARGET | 3.2 | +2.75% | $+2.15 |
| 2026-10-05T05:29 | SCRUSDT | surge | STOP | 0.2 | -3.25% | $-2.73 |
| 2026-10-05T04:55 | BROCCOLI714USDT | surge | STOP | 11.2 | -3.25% | $-2.64 |
| 2026-10-05T04:55 | ACEUSDT | surge | TARGET | 20.5 | +2.75% | $+2.39 |
| 2026-10-05T04:21 | ATOMUSDT | surge | STOP | 12.8 | -3.25% | $-2.63 |
| 2026-10-05T03:31 | VIRTUALUSDT | surge | TARGET | 8.8 | +2.75% | $+2.69 |
| 2026-10-05T03:31 | RUNEUSDT | surge | STOP | 9.8 | -3.25% | $-2.77 |
| 2026-10-05T00:04 | ROBOUSDT | surge | STOP | 7.8 | -3.25% | $-2.69 |
| 2026-10-04T23:15 | CHIPUSDT | surge | TARGET | 5.2 | +2.75% | $+2.34 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-04T21:53 | SHIBUSDT | surge | 5.94e-06 | 5.88e-06 | -1.01% |
| 2026-10-04T23:15 | FLOKIUSDT | surge | 2.915e-05 | 2.89e-05 | -0.86% |
| 2026-10-05T00:04 | MEMEUSDT | surge | 0.000625 | 0.000612 | -2.08% |
| 2026-10-05T03:31 | ADAUSDT | surge | 0.2696 | 0.2651 | -1.67% |
| 2026-10-05T14:49 | SPCXBUSDT | surge | 166.62 | 167.75 | +0.68% |
| 2026-10-05T14:49 | FILUSDT | surge | 1.1008 | 1.107 | +0.56% |
| 2026-10-05T16:00 | WDCBUSDT | surge | 442.05 | 442.88 | +0.19% |
| 2026-10-05T16:36 | TSLABUSDT | surge | 378.15 | 379.7 | +0.41% |
| 2026-10-05T17:11 | PARTIUSDT | surge | 0.0312 | 0.0312 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
