# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T13:37:41+00:00 · runs 701 · equity **$888.56** (-11.14%) · cash $0.00 · open 10/10 · round trips 248

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.46%/trade · realized $-109.55 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 182 | 45% | -0.48% | 42% | 49% | 9% |
| bottom | 66 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-13T13:36 | GLMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.56 |
| 2026-09-13T13:19 | GLMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.50 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T16:18 | PYTHUSDT | surge | 0.05484 | 0.05484 | +0.00% |
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.04888 | -0.47% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.006 | -1.85% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 53.55 | -2.39% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.2701 | -2.03% |
| 2026-09-13T09:00 | GMTUSDT | surge | 0.00781 | 0.00802 | +2.69% |
| 2026-09-13T09:53 | DODOUSDT | surge | 0.01812 | 0.0183 | +0.99% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.3518 | +0.43% |
| 2026-09-13T13:36 | KNCUSDT | surge | 0.1469 | 0.1474 | +0.34% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
