# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T02:43:44+00:00 · runs 1102 · equity **$920.33** (-7.97%) · cash $0.00 · open 10/10 · round trips 376

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-87.28 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 294 | 51% | -0.15% | 47% | 44% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-18T02:42 | APTUSDT | surge | TARGET | 0.8 | +2.75% | $+2.66 |
| 2026-09-18T01:37 | APTUSDT | surge | TARGET | 0.8 | +2.75% | $+2.58 |
| 2026-09-18T01:20 | AXSUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-18T01:20 | PHAUSDT | surge | STOP | 0.8 | -3.25% | $-3.13 |
| 2026-09-18T01:20 | AUSDT | surge | TARGET | 7.8 | +2.75% | $+2.65 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-17T10:23 | DODOUSDT | surge | 0.01812 | 0.01836 | +1.32% |
| 2026-09-17T12:44 | CAKEUSDT | surge | 2.413 | 2.477 | +2.65% |
| 2026-09-17T14:28 | COINBUSDT | surge | 170.78 | 174.39 | +2.11% |
| 2026-09-17T15:38 | INTCBUSDT | surge | 109.9 | 109.47 | -0.39% |
| 2026-09-17T16:13 | BMNRBUSDT | surge | 23.97 | 24.18 | +0.88% |
| 2026-09-18T01:20 | AXSUSDT | surge | 0.995 | 0.993 | -0.20% |
| 2026-09-18T01:20 | AUSDT | surge | 0.0802 | 0.0807 | +0.62% |
| 2026-09-18T01:20 | RENDERUSDT | surge | 1.477 | 1.499 | +1.49% |
| 2026-09-18T02:42 | SEIUSDT | surge | 0.04496 | 0.04498 | +0.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
