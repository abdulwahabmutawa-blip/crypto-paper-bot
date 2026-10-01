# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-01T11:04:42+00:00 · runs 2259 · equity **$863.55** (-13.65%) · cash $0.00 · open 10/10 · round trips 848

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-136.21 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 729 | 52% | -0.13% | 48% | 45% | 7% |
| bottom | 119 | 46% | -0.35% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01T10:40 | REUSDT | surge | STOP | 0.8 | -3.25% | $-2.98 |
| 2026-10-01T10:22 | ZENUSDT | surge | STOP | 21.0 | -3.25% | $-2.73 |
| 2026-10-01T09:30 | REUSDT | surge | TARGET | 0.8 | +2.75% | $+2.46 |
| 2026-10-01T08:37 | AXSUSDT | surge | TIME | 24.0 | -2.48% | $-2.19 |
| 2026-10-01T08:20 | ALGOUSDT | surge | STOP | 4.0 | -3.25% | $-3.00 |
| 2026-10-01T07:45 | SUSDT | surge | STOP | 7.0 | -3.25% | $-2.71 |
| 2026-10-01T06:00 | LINKUSDT | bottom | TIME | 24.0 | +0.31% | $+0.28 |
| 2026-10-01T05:00 | SOXLBUSDT | surge | TARGET | 1.8 | +2.75% | $+2.45 |
| 2026-10-01T04:07 | SNXXBUSDT | surge | TARGET | 12.2 | +2.75% | $+2.47 |
| 2026-10-01T03:13 | PROMUSDT | surge | STOP | 11.8 | -3.25% | $-2.99 |
| 2026-10-01T00:15 | STXUSDT | surge | STOP | 1.5 | -3.25% | $-2.86 |
| 2026-10-01T00:15 | HUMAUSDT | surge | STOP | 3.8 | -3.25% | $-2.74 |
| 2026-09-30T22:42 | STXUSDT | surge | TARGET | 1.8 | +2.75% | $+2.36 |
| 2026-09-30T20:41 | STXUSDT | surge | TARGET | 0.8 | +2.75% | $+2.30 |
| 2026-09-30T20:24 | BLURUSDT | surge | STOP | 0.0 | -3.25% | $-2.83 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-30T14:11 | GOOGLBUSDT | surge | 350.03 | 350.98 | +0.27% |
| 2026-09-30T14:29 | SPCXBUSDT | surge | 151.73 | 151.64 | -0.06% |
| 2026-10-01T00:15 | HYPEUSDT | surge | 90.39 | 89.61 | -0.86% |
| 2026-10-01T05:00 | SNXXBUSDT | surge | 17.38 | 17.32 | -0.35% |
| 2026-10-01T06:00 | SNDKBUSDT | surge | 1784.63 | 1767.15 | -0.98% |
| 2026-10-01T07:45 | MEGAUSDT | surge | 0.04587 | 0.04566 | -0.46% |
| 2026-10-01T08:37 | OPNUSDT | surge | 0.0602 | 0.0603 | +0.17% |
| 2026-10-01T10:22 | HUMAUSDT | surge | 0.03363 | 0.0343 | +1.99% |
| 2026-10-01T10:40 | POLUSDT | bottom | 0.11047 | 0.11057 | +0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
