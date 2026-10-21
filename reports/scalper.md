# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-21T14:54:15+00:00 · runs 3994 · equity **$686.55** (-31.35%) · cash $0.00 · open 10/10 · round trips 1448

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.26%/trade · realized $-319.54 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1266 | 49% | -0.25% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-21T14:36 | RSRUSDT | surge | TIME | 24.0 | -2.07% | $-1.38 |
| 2026-10-21T14:03 | CRCLBUSDT | surge | TARGET | 23.5 | +2.75% | $+1.83 |
| 2026-10-21T13:46 | TSLABUSDT | surge | TARGET | 22.0 | +2.75% | $+1.76 |
| 2026-10-21T13:13 | WUSDT | surge | TARGET | 1.2 | +2.75% | $+1.74 |
| 2026-10-21T11:46 | BONKUSDT | surge | TARGET | 19.2 | +2.75% | $+1.69 |
| 2026-10-21T11:30 | BNCBUSDT | surge | TARGET | 3.2 | +2.75% | $+1.81 |
| 2026-10-21T08:14 | CFXUSDT | surge | TARGET | 16.2 | +2.75% | $+1.76 |
| 2026-10-21T02:42 | RAYUSDT | surge | STOP | 7.8 | -3.25% | $-2.16 |
| 2026-10-20T20:52 | REZUSDT | surge | TARGET | 4.0 | +2.75% | $+1.89 |
| 2026-10-20T18:36 | ACEUSDT | surge | STOP | 1.2 | -3.25% | $-2.23 |
| 2026-10-20T17:31 | IOUSDT | surge | TARGET | 7.0 | +2.75% | $+1.71 |
| 2026-10-20T17:14 | THETAUSDT | surge | TARGET | 1.8 | +2.75% | $+1.83 |
| 2026-10-20T16:41 | COMPUSDT | surge | TARGET | 1.0 | +2.75% | $+1.83 |
| 2026-10-20T16:25 | BEAMXUSDT | surge | STOP | 3.0 | -3.25% | $-2.06 |
| 2026-10-20T15:34 | ICPUSDT | surge | STOP | 0.5 | -3.25% | $-2.25 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-20T15:34 | JTOUSDT | surge | 0.4772 | 0.4883 | +2.33% |
| 2026-10-20T17:31 | DOGEUSDT | surge | 0.08115 | 0.08303 | +2.32% |
| 2026-10-20T20:52 | PENGUUSDT | surge | 0.00803 | 0.008173 | +1.78% |
| 2026-10-21T02:42 | SPCXBUSDT | surge | 161.76 | 161.79 | +0.02% |
| 2026-10-21T11:30 | LUMIAUSDT | surge | 0.0894 | 0.0895 | +0.11% |
| 2026-10-21T13:13 | SCUSDT | surge | 0.000906 | 0.000903 | -0.33% |
| 2026-10-21T13:46 | DASHUSDT | surge | 52.31 | 52.94 | +1.20% |
| 2026-10-21T14:03 | PROMUSDT | surge | 5.546 | 5.594 | +0.87% |
| 2026-10-21T14:36 | WUSDT | surge | 0.0151 | 0.01524 | +0.93% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
