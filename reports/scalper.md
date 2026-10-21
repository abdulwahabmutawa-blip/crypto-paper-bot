# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-21T20:02:55+00:00 · runs 4013 · equity **$682.50** (-31.75%) · cash $0.00 · open 10/10 · round trips 1456

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.25%/trade · realized $-312.89 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1274 | 49% | -0.24% | 47% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-21T16:48 | PENGUUSDT | surge | TARGET | 19.8 | +2.75% | $+1.94 |
| 2026-10-21T16:15 | OPNUSDT | surge | STOP | 0.2 | -3.25% | $-2.13 |
| 2026-10-21T16:15 | MAGICUSDT | surge | STOP | 0.8 | -3.25% | $-2.16 |
| 2026-10-21T16:15 | PROMUSDT | surge | TARGET | 2.0 | +2.75% | $+1.88 |
| 2026-10-21T15:59 | JTOUSDT | surge | TARGET | 24.0 | +2.75% | $+1.76 |
| 2026-10-21T15:42 | DASHUSDT | surge | TARGET | 1.5 | +2.75% | $+1.81 |
| 2026-10-21T15:25 | WUSDT | surge | TARGET | 0.5 | +2.75% | $+1.80 |
| 2026-10-21T15:25 | DOGEUSDT | surge | TARGET | 21.5 | +2.75% | $+1.76 |
| 2026-10-21T14:36 | RSRUSDT | surge | TIME | 24.0 | -2.07% | $-1.38 |
| 2026-10-21T14:03 | CRCLBUSDT | surge | TARGET | 23.5 | +2.75% | $+1.83 |
| 2026-10-21T13:46 | TSLABUSDT | surge | TARGET | 22.0 | +2.75% | $+1.76 |
| 2026-10-21T13:13 | WUSDT | surge | TARGET | 1.2 | +2.75% | $+1.74 |
| 2026-10-21T11:46 | BONKUSDT | surge | TARGET | 19.2 | +2.75% | $+1.69 |
| 2026-10-21T11:30 | BNCBUSDT | surge | TARGET | 3.2 | +2.75% | $+1.81 |
| 2026-10-21T08:14 | CFXUSDT | surge | TARGET | 16.2 | +2.75% | $+1.76 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-21T02:42 | SPCXBUSDT | surge | 161.76 | 158.78 | -1.84% |
| 2026-10-21T11:30 | LUMIAUSDT | surge | 0.0894 | 0.0885 | -1.01% |
| 2026-10-21T13:13 | SCUSDT | surge | 0.000906 | 0.000888 | -1.99% |
| 2026-10-21T15:25 | CRCLBUSDT | surge | 90.14 | 89.88 | -0.29% |
| 2026-10-21T15:42 | DASHUSDT | surge | 53.45 | 52.5 | -1.78% |
| 2026-10-21T16:15 | MSTRBUSDT | surge | 153.35 | 153.44 | +0.06% |
| 2026-10-21T16:15 | ACEUSDT | surge | 0.1574 | 0.1597 | +1.46% |
| 2026-10-21T16:15 | AAVEUSDT | surge | 158.89 | 157.53 | -0.86% |
| 2026-10-21T16:48 | DOGEUSDT | surge | 0.08348 | 0.08289 | -0.71% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
