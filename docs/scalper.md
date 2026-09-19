# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-19T21:40:26+00:00 · runs 1254 · equity **$938.91** (-6.11%) · cash $0.00 · open 10/10 · round trips 438

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-45.33 · worst day $-50.94 · trades/day 29.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 356 | 54% | +0.00% | 49% | 41% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-19T15:20 | AVAXUSDT | surge | TARGET | 2.2 | +2.75% | $+2.55 |
| 2026-09-19T15:03 | HOMEUSDT | surge | STOP | 4.0 | -3.25% | $-2.86 |
| 2026-09-19T12:59 | AVAXUSDT | surge | TARGET | 0.2 | +2.75% | $+2.48 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.008652 | +0.29% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.1542 | -2.10% |
| 2026-09-19T12:23 | TAOUSDT | surge | 267.9 | 261.7 | -2.31% |
| 2026-09-19T17:30 | 0GUSDT | surge | 0.2276 | 0.2263 | -0.57% |
| 2026-09-19T20:09 | FLOKIUSDT | surge | 2.663e-05 | 2.6e-05 | -2.37% |
| 2026-09-19T20:27 | HOMEUSDT | surge | 0.00654 | 0.00642 | -1.83% |
| 2026-09-19T20:45 | BERAUSDT | surge | 0.2195 | 0.2133 | -2.82% |
| 2026-09-19T20:45 | PEPEUSDT | surge | 4.23e-06 | 4.07e-06 | -3.78% |
| 2026-09-19T21:20 | UNIUSDT | bottom | 8.594 | 8.535 | -0.69% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
