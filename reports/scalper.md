# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T19:26:31+00:00 · runs 723 · equity **$885.24** (-11.48%) · cash $0.00 · open 10/10 · round trips 260

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.42%/trade · realized $-106.11 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 194 | 46% | -0.43% | 42% | 48% | 9% |
| bottom | 66 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-13T18:52 | SCRUSDT | surge | STOP | 1.0 | -3.25% | $-2.98 |
| 2026-09-13T17:46 | BATUSDT | surge | STOP | 1.2 | -3.25% | $-3.22 |
| 2026-09-13T17:30 | SCRUSDT | surge | TARGET | 0.0 | +2.75% | $+2.50 |
| 2026-09-13T17:30 | BABYUSDT | surge | STOP | 1.5 | -3.25% | $-3.01 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.022 | -0.29% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 54.3 | -1.02% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.273 | -0.98% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.3509 | +0.17% |
| 2026-09-13T15:14 | GMTUSDT | surge | 0.00796 | 0.00776 | -2.51% |
| 2026-09-13T17:13 | XTZUSDT | surge | 0.2921 | 0.2886 | -1.20% |
| 2026-09-13T17:30 | MBLUSDT | surge | 0.00082 | 0.000803 | -2.07% |
| 2026-09-13T17:46 | ICPUSDT | surge | 2.784 | 2.779 | -0.18% |
| 2026-09-13T18:52 | ARUSDT | surge | 2.867 | 2.82 | -1.64% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
