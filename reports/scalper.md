# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T16:58:45+00:00 · runs 714 · equity **$890.92** (-10.91%) · cash $0.00 · open 10/10 · round trips 254

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.41%/trade · realized $-101.43 · worst day $-50.94 · trades/day 28.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 188 | 46% | -0.42% | 43% | 48% | 9% |
| bottom | 66 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-13T09:53 | API3USDT | surge | TARGET | 1.2 | +2.75% | $+2.37 |
| 2026-09-13T09:53 | WLDUSDT | bottom | STOP | 8.5 | -3.25% | $-2.83 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.04888 | -0.47% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.017 | -0.78% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 54.09 | -1.40% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.2742 | -0.54% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.348 | -0.66% |
| 2026-09-13T15:14 | GMTUSDT | surge | 0.00796 | 0.00782 | -1.76% |
| 2026-09-13T15:47 | BABYUSDT | surge | 0.01255 | 0.01219 | -2.87% |
| 2026-09-13T16:24 | BATUSDT | surge | 0.0824 | 0.0823 | -0.12% |
| 2026-09-13T16:40 | ARUSDT | surge | 2.713 | 2.715 | +0.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
