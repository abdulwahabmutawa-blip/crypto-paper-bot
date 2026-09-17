# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-17T12:46:32+00:00 · runs 1052 · equity **$900.49** (-9.95%) · cash $0.00 · open 10/10 · round trips 359

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-103.05 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 277 | 50% | -0.22% | 46% | 45% | 8% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-17T12:44 | KORUBUSDT | surge | TARGET | 11.0 | +2.75% | $+2.40 |
| 2026-09-17T12:27 | AEROUSDT | surge | TARGET | 11.5 | +2.75% | $+2.47 |
| 2026-09-17T11:17 | THEUSDT | surge | TARGET | 0.0 | +2.75% | $+2.41 |
| 2026-09-17T10:59 | GRAMUSDT | bottom | TARGET | 15.2 | +2.75% | $+2.34 |
| 2026-09-17T10:23 | INTCBUSDT | surge | TIME | 24.0 | +1.27% | $+1.08 |
| 2026-09-17T01:19 | RAYUSDT | surge | TARGET | 5.8 | +2.75% | $+2.34 |
| 2026-09-17T00:44 | DASHUSDT | surge | TARGET | 3.8 | +2.75% | $+2.41 |
| 2026-09-17T00:26 | NEARUSDT | surge | TARGET | 3.2 | +2.75% | $+2.67 |
| 2026-09-17T00:26 | ASTERUSDT | surge | TARGET | 5.2 | +2.75% | $+2.51 |
| 2026-09-16T20:59 | NEARUSDT | surge | TARGET | 2.5 | +2.75% | $+2.60 |
| 2026-09-16T20:42 | INJUSDT | bottom | TARGET | 0.8 | +2.75% | $+2.34 |
| 2026-09-16T19:35 | LITEBUSDT | surge | STOP | 1.2 | -3.25% | $-2.83 |
| 2026-09-16T19:35 | FFUSDT | bottom | STOP | 9.5 | -3.25% | $-2.89 |
| 2026-09-16T19:18 | SKHYBUSDT | surge | STOP | 13.5 | -3.25% | $-2.85 |
| 2026-09-16T18:45 | ZENUSDT | surge | STOP | 0.2 | -3.25% | $-3.07 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T14:34 | TSLABUSDT | surge | 363.68 | 365.27 | +0.44% |
| 2026-09-16T15:10 | SPCXBUSDT | surge | 152.08 | 154.05 | +1.30% |
| 2026-09-16T15:45 | NVDABUSDT | surge | 216.32 | 218.52 | +1.02% |
| 2026-09-17T00:26 | WLDUSDT | surge | 0.3733 | 0.3753 | +0.54% |
| 2026-09-17T00:26 | TRUMPUSDT | surge | 1.932 | 1.958 | +1.35% |
| 2026-09-17T10:23 | DODOUSDT | surge | 0.01812 | 0.018 | -0.66% |
| 2026-09-17T11:17 | GALAUSDT | surge | 0.001735 | 0.001733 | -0.12% |
| 2026-09-17T12:27 | PROVEUSDT | surge | 0.1906 | 0.1911 | +0.26% |
| 2026-09-17T12:44 | CAKEUSDT | surge | 2.413 | 2.408 | -0.21% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
