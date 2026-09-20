# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T00:35:15+00:00 · runs 1265 · equity **$955.11** (-4.49%) · cash $0.00 · open 10/10 · round trips 443

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.10%/trade · realized $-49.63 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 361 | 54% | -0.01% | 49% | 42% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T00:17 | HOMEUSDT | surge | TARGET | 3.8 | +2.75% | $+2.70 |
| 2026-09-20T00:17 | 0GUSDT | surge | TARGET | 6.5 | +2.75% | $+2.50 |
| 2026-09-19T22:13 | FLOKIUSDT | surge | STOP | 2.0 | -3.25% | $-3.09 |
| 2026-09-19T21:56 | PEPEUSDT | surge | STOP | 0.8 | -3.25% | $-3.20 |
| 2026-09-19T21:56 | BERAUSDT | surge | STOP | 0.8 | -3.25% | $-3.20 |
| 2026-09-19T21:20 | NEIROUSDT | surge | STOP | 3.5 | -3.25% | $-2.95 |
| 2026-09-19T20:45 | PHAUSDT | surge | TARGET | 2.5 | +2.75% | $+2.70 |
| 2026-09-19T20:45 | SENTUSDT | surge | TIME | 24.0 | +0.82% | $+0.78 |
| 2026-09-19T20:27 | SNDKBUSDT | surge | TIME | 24.0 | -0.61% | $-0.60 |
| 2026-09-19T20:09 | ONDOUSDT | surge | STOP | 2.8 | -3.25% | $-3.19 |
| 2026-09-19T17:48 | PROVEUSDT | surge | TARGET | 12.8 | +2.75% | $+2.62 |
| 2026-09-19T17:30 | PHAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.43 |
| 2026-09-19T17:30 | NILUSDT | surge | TARGET | 1.0 | +2.75% | $+2.43 |
| 2026-09-19T17:06 | MUBUSDT | surge | TIME | 24.0 | +0.98% | $+0.95 |
| 2026-09-19T16:31 | ALLOUSDT | surge | STOP | 1.0 | -3.25% | $-2.97 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.008676 | +0.57% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.156 | -0.95% |
| 2026-09-19T12:23 | TAOUSDT | surge | 267.9 | 266.1 | -0.67% |
| 2026-09-19T21:20 | UNIUSDT | bottom | 8.594 | 8.667 | +0.85% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 111.05 | +0.65% |
| 2026-09-19T21:56 | DASHUSDT | bottom | 57.97 | 58.47 | +0.86% |
| 2026-09-19T23:28 | SEIUSDT | surge | 0.04964 | 0.04947 | -0.34% |
| 2026-09-20T00:17 | ZILUSDT | surge | 0.00361 | 0.003705 | +2.63% |
| 2026-09-20T00:17 | ALGOUSDT | surge | 0.1045 | 0.106 | +1.44% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
