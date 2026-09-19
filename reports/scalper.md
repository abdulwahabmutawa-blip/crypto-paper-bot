# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-19T22:51:29+00:00 · runs 1258 · equity **$944.95** (-5.51%) · cash $91.90 · open 9/10 · round trips 441

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.12%/trade · realized $-54.82 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 359 | 53% | -0.02% | 49% | 42% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-19T16:13 | IOSTUSDT | surge | STOP | 0.5 | -3.25% | $-2.97 |
| 2026-09-19T15:20 | BANKUSDT | surge | TARGET | 0.0 | +2.75% | $+2.34 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.008619 | -0.09% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.1551 | -1.52% |
| 2026-09-19T12:23 | TAOUSDT | surge | 267.9 | 264.8 | -1.16% |
| 2026-09-19T17:30 | 0GUSDT | surge | 0.2276 | 0.2273 | -0.13% |
| 2026-09-19T20:27 | HOMEUSDT | surge | 0.00654 | 0.00658 | +0.61% |
| 2026-09-19T21:20 | UNIUSDT | bottom | 8.594 | 8.619 | +0.29% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 110.69 | +0.33% |
| 2026-09-19T21:56 | DASHUSDT | bottom | 57.97 | 58.9 | +1.60% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
