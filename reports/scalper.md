# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-01T16:03:16+00:00 · runs 2276 · equity **$860.79** (-13.92%) · cash $0.00 · open 10/10 · round trips 865

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.17%/trade · realized $-144.27 · worst day $-50.94 · trades/day 32.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 746 | 51% | -0.14% | 48% | 45% | 7% |
| bottom | 119 | 46% | -0.35% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01T16:01 | HYPEUSDT | surge | STOP | 15.5 | -3.25% | $-2.71 |
| 2026-10-01T15:43 | MOVEUSDT | surge | TARGET | 1.0 | +2.75% | $+2.38 |
| 2026-10-01T15:43 | MEGAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.38 |
| 2026-10-01T15:43 | HEIUSDT | surge | STOP | 1.5 | -3.25% | $-2.76 |
| 2026-10-01T14:33 | OPNUSDT | surge | TARGET | 0.0 | +2.75% | $+2.38 |
| 2026-10-01T14:33 | TRBUSDT | surge | STOP | 0.5 | -3.25% | $-2.76 |
| 2026-10-01T14:33 | SPCXBUSDT | surge | TIME | 24.0 | +0.13% | $+0.12 |
| 2026-10-01T14:16 | GOOGLBUSDT | surge | TIME | 24.0 | -2.33% | $-2.06 |
| 2026-10-01T13:58 | OPNUSDT | surge | TARGET | 0.0 | +2.75% | $+2.25 |
| 2026-10-01T13:58 | SNDKBUSDT | surge | STOP | 7.5 | -3.25% | $-2.87 |
| 2026-10-01T13:41 | NIGHTUSDT | surge | STOP | 0.0 | -3.25% | $-2.75 |
| 2026-10-01T13:06 | ROBOUSDT | surge | STOP | 1.0 | -3.25% | $-2.71 |
| 2026-10-01T13:06 | SNXXBUSDT | surge | STOP | 7.8 | -3.25% | $-2.98 |
| 2026-10-01T12:13 | MEGAUSDT | surge | STOP | 0.5 | -3.25% | $-2.79 |
| 2026-10-01T11:56 | HUMAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.23 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T10:40 | POLUSDT | bottom | 0.11047 | 0.10869 | -1.61% |
| 2026-10-01T11:38 | KITEUSDT | surge | 0.1495 | 0.1515 | +1.34% |
| 2026-10-01T12:13 | UNIUSDT | surge | 9.062 | 9.108 | +0.51% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 5.98 | -0.83% |
| 2026-10-01T14:33 | MSTRBUSDT | surge | 157.17 | 156.75 | -0.27% |
| 2026-10-01T15:43 | ACEUSDT | surge | 0.19 | 0.192 | +1.05% |
| 2026-10-01T15:43 | MEGAUSDT | surge | 0.0498 | 0.05232 | +5.06% |
| 2026-10-01T15:43 | PEPEUSDT | surge | 4.39e-06 | 4.43e-06 | +0.91% |
| 2026-10-01T16:01 | AAVEUSDT | surge | 168.32 | 167.84 | -0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
