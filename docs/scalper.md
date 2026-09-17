# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-17T11:19:31+00:00 · runs 1047 · equity **$892.24** (-10.78%) · cash $0.00 · open 10/10 · round trips 357

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-107.93 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 275 | 49% | -0.24% | 46% | 46% | 8% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-16T18:28 | NEARUSDT | surge | TARGET | 4.2 | +2.75% | $+2.56 |
| 2026-09-16T18:28 | ZENUSDT | surge | TARGET | 7.2 | +2.75% | $+2.50 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T14:34 | TSLABUSDT | surge | 363.68 | 362.6 | -0.30% |
| 2026-09-16T15:10 | SPCXBUSDT | surge | 152.08 | 153.36 | +0.84% |
| 2026-09-16T15:45 | NVDABUSDT | surge | 216.32 | 216.76 | +0.20% |
| 2026-09-17T00:26 | WLDUSDT | surge | 0.3733 | 0.3722 | -0.29% |
| 2026-09-17T00:26 | TRUMPUSDT | surge | 1.932 | 1.944 | +0.62% |
| 2026-09-17T00:44 | AEROUSDT | surge | 0.5507 | 0.5518 | +0.20% |
| 2026-09-17T01:19 | KORUBUSDT | surge | 19.19 | 19.26 | +0.36% |
| 2026-09-17T10:23 | DODOUSDT | surge | 0.01812 | 0.01791 | -1.16% |
| 2026-09-17T11:17 | GALAUSDT | surge | 0.001735 | 0.00173 | -0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
