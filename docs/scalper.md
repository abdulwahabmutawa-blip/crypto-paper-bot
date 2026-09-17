# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-17T16:14:58+00:00 · runs 1064 · equity **$910.46** (-8.95%) · cash $0.00 · open 10/10 · round trips 364

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-98.97 · worst day $-50.94 · trades/day 28.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 282 | 50% | -0.20% | 46% | 45% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-17T16:13 | NVDABUSDT | surge | TIME | 24.0 | +1.04% | $+0.86 |
| 2026-09-17T15:38 | EDENUSDT | surge | STOP | 0.5 | -3.25% | $-3.03 |
| 2026-09-17T15:38 | PROVEUSDT | surge | TARGET | 3.0 | +2.75% | $+2.54 |
| 2026-09-17T14:46 | TSLABUSDT | surge | TIME | 24.0 | +1.51% | $+1.39 |
| 2026-09-17T14:28 | SPCXBUSDT | surge | TARGET | 23.0 | +2.75% | $+2.34 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-17T00:26 | WLDUSDT | surge | 0.3733 | 0.3761 | +0.75% |
| 2026-09-17T00:26 | TRUMPUSDT | surge | 1.932 | 1.954 | +1.14% |
| 2026-09-17T10:23 | DODOUSDT | surge | 0.01812 | 0.01807 | -0.28% |
| 2026-09-17T11:17 | GALAUSDT | surge | 0.001735 | 0.001809 | +4.27% |
| 2026-09-17T12:44 | CAKEUSDT | surge | 2.413 | 2.418 | +0.21% |
| 2026-09-17T14:28 | COINBUSDT | surge | 170.78 | 170 | -0.46% |
| 2026-09-17T15:38 | PROVEUSDT | surge | 0.1964 | 0.2019 | +2.80% |
| 2026-09-17T15:38 | INTCBUSDT | surge | 109.9 | 111.08 | +1.07% |
| 2026-09-17T16:13 | BMNRBUSDT | surge | 23.97 | 24.15 | +0.75% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
