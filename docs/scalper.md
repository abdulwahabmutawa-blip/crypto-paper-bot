# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T01:06:01+00:00 · runs 1096 · equity **$911.18** (-8.88%) · cash $0.00 · open 10/10 · round trips 371

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-94.63 · worst day $-50.94 · trades/day 26.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 289 | 51% | -0.18% | 46% | 45% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-18T00:32 | KORUBUSDT | surge | STOP | 7.8 | -3.25% | $-3.05 |
| 2026-09-18T00:32 | TRUMPUSDT | surge | TIME | 24.0 | +0.37% | $+0.36 |
| 2026-09-18T00:15 | ROSEUSDT | surge | STOP | 0.2 | -3.25% | $-3.23 |
| 2026-09-17T23:59 | WLDUSDT | surge | TARGET | 23.5 | +2.75% | $+2.66 |
| 2026-09-17T17:29 | PROVEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.58 |
| 2026-09-17T16:30 | PROVEUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-17T16:30 | GALAUSDT | surge | TARGET | 4.8 | +2.75% | $+2.47 |
| 2026-09-17T16:13 | NVDABUSDT | surge | TIME | 24.0 | +1.04% | $+0.86 |
| 2026-09-17T15:38 | EDENUSDT | surge | STOP | 0.5 | -3.25% | $-3.03 |
| 2026-09-17T15:38 | PROVEUSDT | surge | TARGET | 3.0 | +2.75% | $+2.54 |
| 2026-09-17T14:46 | TSLABUSDT | surge | TIME | 24.0 | +1.51% | $+1.39 |
| 2026-09-17T14:28 | SPCXBUSDT | surge | TARGET | 23.0 | +2.75% | $+2.34 |
| 2026-09-17T12:44 | KORUBUSDT | surge | TARGET | 11.0 | +2.75% | $+2.40 |
| 2026-09-17T12:27 | AEROUSDT | surge | TARGET | 11.5 | +2.75% | $+2.47 |
| 2026-09-17T11:17 | THEUSDT | surge | TARGET | 0.0 | +2.75% | $+2.41 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-17T10:23 | DODOUSDT | surge | 0.01812 | 0.01829 | +0.94% |
| 2026-09-17T12:44 | CAKEUSDT | surge | 2.413 | 2.432 | +0.79% |
| 2026-09-17T14:28 | COINBUSDT | surge | 170.78 | 173.27 | +1.46% |
| 2026-09-17T15:38 | INTCBUSDT | surge | 109.9 | 109.15 | -0.68% |
| 2026-09-17T16:13 | BMNRBUSDT | surge | 23.97 | 23.92 | -0.21% |
| 2026-09-17T17:29 | AUSDT | surge | 0.0776 | 0.0798 | +2.84% |
| 2026-09-18T00:15 | PHAUSDT | surge | 0.0314 | 0.031 | -1.27% |
| 2026-09-18T00:32 | APTUSDT | surge | 0.597 | 0.605 | +1.34% |
| 2026-09-18T00:48 | AXSUSDT | surge | 0.976 | 0.987 | +1.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
