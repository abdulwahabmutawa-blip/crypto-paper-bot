# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T13:04:55+00:00 · runs 699 · equity **$882.13** (-11.79%) · cash $0.00 · open 10/10 · round trips 246

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.48%/trade · realized $-114.61 · worst day $-50.94 · trades/day 27.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 180 | 44% | -0.52% | 41% | 50% | 9% |
| bottom | 66 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-13T13:03 | GLMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.43 |
| 2026-09-13T12:30 | POLYXUSDT | surge | TARGET | 0.0 | +2.75% | $+2.36 |
| 2026-09-13T12:30 | GLMUSDT | surge | TARGET | 2.5 | +2.75% | $+2.37 |
| 2026-09-13T12:14 | POLYXUSDT | surge | TARGET | 0.8 | +2.75% | $+2.29 |
| 2026-09-13T11:08 | NEWTUSDT | surge | STOP | 2.8 | -3.25% | $-2.80 |
| 2026-09-13T09:53 | API3USDT | surge | TARGET | 1.2 | +2.75% | $+2.37 |
| 2026-09-13T09:53 | WLDUSDT | bottom | STOP | 8.5 | -3.25% | $-2.83 |
| 2026-09-13T09:00 | ORDIUSDT | surge | STOP | 6.2 | -3.25% | $-3.07 |
| 2026-09-13T08:24 | CVCUSDT | surge | STOP | 0.2 | -3.25% | $-2.89 |
| 2026-09-13T08:06 | PENDLEUSDT | surge | STOP | 15.5 | -3.25% | $-2.89 |
| 2026-09-13T07:48 | NEWTUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
| 2026-09-13T07:13 | PUMPUSDT | surge | STOP | 10.5 | -3.25% | $-2.91 |
| 2026-09-13T03:40 | SAGAUSDT | surge | STOP | 0.0 | -3.25% | $-2.81 |
| 2026-09-13T03:24 | INJUSDT | surge | STOP | 6.2 | -3.25% | $-2.91 |
| 2026-09-13T02:19 | KAVAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.52 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T16:18 | PYTHUSDT | surge | 0.05484 | 0.05479 | -0.09% |
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.04886 | -0.51% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.011 | -1.37% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 53.95 | -1.66% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.2718 | -1.41% |
| 2026-09-13T09:00 | GMTUSDT | surge | 0.00781 | 0.00785 | +0.51% |
| 2026-09-13T09:53 | DODOUSDT | surge | 0.01812 | 0.01816 | +0.22% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.3488 | -0.43% |
| 2026-09-13T13:03 | GLMUSDT | surge | 0.1235 | 0.1247 | +0.97% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
