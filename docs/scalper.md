# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-22T00:26:59+00:00 · runs 4029 · equity **$675.25** (-32.47%) · cash $0.00 · open 10/10 · round trips 1459

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-319.28 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1277 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-21T23:33 | SCUSDT | surge | STOP | 10.2 | -3.25% | $-2.11 |
| 2026-10-21T23:10 | SPCXBUSDT | surge | STOP | 20.2 | -3.25% | $-2.09 |
| 2026-10-21T22:19 | DASHUSDT | surge | STOP | 6.5 | -3.25% | $-2.19 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-21T11:30 | LUMIAUSDT | surge | 0.0894 | 0.0882 | -1.34% |
| 2026-10-21T15:25 | CRCLBUSDT | surge | 90.14 | 89.4 | -0.82% |
| 2026-10-21T16:15 | MSTRBUSDT | surge | 153.35 | 152.18 | -0.76% |
| 2026-10-21T16:15 | ACEUSDT | surge | 0.1574 | 0.1569 | -0.32% |
| 2026-10-21T16:15 | AAVEUSDT | surge | 158.89 | 155.77 | -1.96% |
| 2026-10-21T16:48 | DOGEUSDT | surge | 0.08348 | 0.08211 | -1.64% |
| 2026-10-21T22:19 | QNTUSDT | surge | 209.61 | 206.58 | -1.45% |
| 2026-10-21T23:10 | TSLABUSDT | bottom | 375.06 | 375.19 | +0.03% |
| 2026-10-21T23:33 | INTCBUSDT | bottom | 91.03 | 91.18 | +0.16% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
