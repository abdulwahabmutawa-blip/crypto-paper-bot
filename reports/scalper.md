# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T17:15:15+00:00 · runs 715 · equity **$898.85** (-10.12%) · cash $0.00 · open 10/10 · round trips 256

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.40%/trade · realized $-99.41 · worst day $-50.94 · trades/day 28.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 190 | 46% | -0.40% | 43% | 48% | 9% |
| bottom | 66 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-13T17:13 | ARUSDT | surge | TARGET | 0.5 | +2.75% | $+2.48 |
| 2026-09-13T17:13 | ZAMAUSDT | surge | TIME | 24.0 | -0.52% | $-0.46 |
| 2026-09-13T16:40 | PYTHUSDT | surge | TIME | 24.0 | +1.26% | $+1.13 |
| 2026-09-13T16:24 | XTZUSDT | surge | TARGET | 1.8 | +2.75% | $+2.65 |
| 2026-09-13T15:47 | KNCUSDT | surge | STOP | 2.0 | -3.25% | $-3.11 |
| 2026-09-13T15:14 | DODOUSDT | surge | TARGET | 5.2 | +2.75% | $+2.37 |
| 2026-09-13T14:25 | FILUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-13T13:52 | GMTUSDT | surge | TARGET | 4.5 | +2.75% | $+2.51 |
| 2026-09-13T13:36 | GLMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.56 |
| 2026-09-13T13:19 | GLMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.50 |
| 2026-09-13T13:03 | GLMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.43 |
| 2026-09-13T12:30 | POLYXUSDT | surge | TARGET | 0.0 | +2.75% | $+2.36 |
| 2026-09-13T12:30 | GLMUSDT | surge | TARGET | 2.5 | +2.75% | $+2.37 |
| 2026-09-13T12:14 | POLYXUSDT | surge | TARGET | 0.8 | +2.75% | $+2.29 |
| 2026-09-13T11:08 | NEWTUSDT | surge | STOP | 2.8 | -3.25% | $-2.80 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.027 | +0.20% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 54.75 | -0.20% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.2754 | -0.11% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.3546 | +1.23% |
| 2026-09-13T15:14 | GMTUSDT | surge | 0.00796 | 0.00785 | -1.38% |
| 2026-09-13T15:47 | BABYUSDT | surge | 0.01255 | 0.01223 | -2.55% |
| 2026-09-13T16:24 | BATUSDT | surge | 0.0824 | 0.0821 | -0.36% |
| 2026-09-13T17:13 | XTZUSDT | surge | 0.2921 | 0.2912 | -0.31% |
| 2026-09-13T17:13 | SCRUSDT | surge | 0.02344 | 0.02382 | +1.62% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
