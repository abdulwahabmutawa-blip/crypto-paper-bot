# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-01T18:14:07+00:00 · runs 2284 · equity **$864.10** (-13.59%) · cash $0.00 · open 10/10 · round trips 869

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-140.05 · worst day $-50.94 · trades/day 32.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 749 | 52% | -0.13% | 48% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01T17:36 | KITEUSDT | surge | TARGET | 5.8 | +2.75% | $+2.36 |
| 2026-10-01T17:18 | OPNUSDT | surge | TARGET | 0.0 | +2.75% | $+2.36 |
| 2026-10-01T17:00 | POLUSDT | bottom | STOP | 6.0 | -3.25% | $-2.89 |
| 2026-10-01T16:18 | MEGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T12:13 | UNIUSDT | surge | 9.062 | 9.086 | +0.26% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 5.98 | -0.83% |
| 2026-10-01T14:33 | MSTRBUSDT | surge | 157.17 | 159.01 | +1.17% |
| 2026-10-01T15:43 | ACEUSDT | surge | 0.19 | 0.1881 | -1.00% |
| 2026-10-01T15:43 | PEPEUSDT | surge | 4.39e-06 | 4.45e-06 | +1.37% |
| 2026-10-01T16:01 | AAVEUSDT | surge | 168.32 | 169.52 | +0.71% |
| 2026-10-01T16:18 | SKYUSDT | surge | 0.08117 | 0.08243 | +1.55% |
| 2026-10-01T17:18 | DYDXUSDT | surge | 0.14774 | 0.14957 | +1.24% |
| 2026-10-01T17:36 | SKHYBUSDT | surge | 188.77 | 189.31 | +0.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
