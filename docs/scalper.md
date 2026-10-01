# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-01T14:18:15+00:00 · runs 2270 · equity **$852.92** (-14.71%) · cash $0.00 · open 10/10 · round trips 858

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.17%/trade · realized $-143.30 · worst day $-50.94 · trades/day 31.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 739 | 51% | -0.14% | 48% | 45% | 7% |
| bottom | 119 | 46% | -0.35% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01T14:16 | GOOGLBUSDT | surge | TIME | 24.0 | -2.33% | $-2.06 |
| 2026-10-01T13:58 | OPNUSDT | surge | TARGET | 0.0 | +2.75% | $+2.25 |
| 2026-10-01T13:58 | SNDKBUSDT | surge | STOP | 7.5 | -3.25% | $-2.87 |
| 2026-10-01T13:41 | NIGHTUSDT | surge | STOP | 0.0 | -3.25% | $-2.75 |
| 2026-10-01T13:06 | ROBOUSDT | surge | STOP | 1.0 | -3.25% | $-2.71 |
| 2026-10-01T13:06 | SNXXBUSDT | surge | STOP | 7.8 | -3.25% | $-2.98 |
| 2026-10-01T12:13 | MEGAUSDT | surge | STOP | 0.5 | -3.25% | $-2.79 |
| 2026-10-01T11:56 | HUMAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.23 |
| 2026-10-01T11:38 | OPNUSDT | surge | TARGET | 2.8 | +2.75% | $+2.37 |
| 2026-10-01T11:38 | MEGAUSDT | surge | TARGET | 3.5 | +2.75% | $+2.22 |
| 2026-10-01T10:40 | REUSDT | surge | STOP | 0.8 | -3.25% | $-2.98 |
| 2026-10-01T10:22 | ZENUSDT | surge | STOP | 21.0 | -3.25% | $-2.73 |
| 2026-10-01T09:30 | REUSDT | surge | TARGET | 0.8 | +2.75% | $+2.46 |
| 2026-10-01T08:37 | AXSUSDT | surge | TIME | 24.0 | -2.48% | $-2.19 |
| 2026-10-01T08:20 | ALGOUSDT | surge | STOP | 4.0 | -3.25% | $-3.00 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-30T14:29 | SPCXBUSDT | surge | 151.73 | 152.3 | +0.38% |
| 2026-10-01T00:15 | HYPEUSDT | surge | 90.39 | 89.21 | -1.31% |
| 2026-10-01T10:40 | POLUSDT | bottom | 0.11047 | 0.10886 | -1.46% |
| 2026-10-01T11:38 | KITEUSDT | surge | 0.1495 | 0.1514 | +1.27% |
| 2026-10-01T12:13 | UNIUSDT | surge | 9.062 | 9.101 | +0.43% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 6 | -0.50% |
| 2026-10-01T13:58 | HEIUSDT | surge | 0.1558 | 0.1529 | -1.86% |
| 2026-10-01T13:58 | TRBUSDT | surge | 21.53 | 21.09 | -2.04% |
| 2026-10-01T14:16 | OPNUSDT | surge | 0.0623 | 0.0627 | +0.64% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
