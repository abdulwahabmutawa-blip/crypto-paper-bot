# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-06T21:23:22+00:00 · runs 2718 · equity **$834.64** (-16.54%) · cash $0.00 · open 10/10 · round trips 1017

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-159.50 · worst day $-50.94 · trades/day 31.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 890 | 51% | -0.13% | 48% | 44% | 8% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-06T20:45 | MARSCOINUSDT | surge | STOP | 3.2 | -3.25% | $-2.76 |
| 2026-10-06T20:45 | SPCXBUSDT | surge | TIME | 24.0 | -0.06% | $-0.05 |
| 2026-10-06T19:15 | RESOLVUSDT | surge | TARGET | 1.5 | +2.75% | $+2.41 |
| 2026-10-06T19:10 | FLUXUSDT | surge | STOP | 0.0 | -3.25% | $-2.83 |
| 2026-10-06T18:53 | MIRAUSDT | surge | STOP | 0.5 | -3.25% | $-2.93 |
| 2026-10-06T18:01 | MIRAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.41 |
| 2026-10-06T17:43 | FLUXUSDT | surge | TARGET | 0.8 | +2.75% | $+2.36 |
| 2026-10-06T17:43 | MIRAUSDT | surge | TARGET | 2.5 | +2.75% | $+2.33 |
| 2026-10-06T17:26 | TRBUSDT | surge | STOP | 0.8 | -3.25% | $-2.86 |
| 2026-10-06T16:51 | METUSDT | surge | TARGET | 0.2 | +2.75% | $+2.42 |
| 2026-10-06T16:51 | TSLABUSDT | surge | TIME | 24.0 | +0.41% | $+0.33 |
| 2026-10-06T16:17 | TRBUSDT | surge | TARGET | 1.0 | +2.75% | $+2.33 |
| 2026-10-06T16:17 | ACEUSDT | surge | TARGET | 9.2 | +2.75% | $+2.38 |
| 2026-10-06T15:07 | TRBUSDT | surge | TARGET | 0.5 | +2.75% | $+2.29 |
| 2026-10-06T15:07 | ALICEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.24 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-05T23:04 | FILUSDT | surge | 1.179 | 1.1625 | -1.40% |
| 2026-10-06T07:31 | WLFIUSDT | surge | 0.0564 | 0.0564 | +0.00% |
| 2026-10-06T07:49 | GRAMUSDT | surge | 1.573 | 1.526 | -2.99% |
| 2026-10-06T14:15 | CRCLBUSDT | surge | 86.06 | 84.55 | -1.75% |
| 2026-10-06T16:51 | MAGICUSDT | surge | 0.0673 | 0.068 | +1.04% |
| 2026-10-06T19:10 | TIAUSDT | surge | 0.483 | 0.4818 | -0.25% |
| 2026-10-06T19:15 | METUSDT | surge | 0.3358 | 0.3305 | -1.58% |
| 2026-10-06T20:45 | RESOLVUSDT | surge | 0.02178 | 0.02175 | -0.14% |
| 2026-10-06T20:45 | INJUSDT | surge | 8.085 | 8.1 | +0.19% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
