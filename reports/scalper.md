# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-04T00:55:51+00:00 · runs 2483 · equity **$856.71** (-14.33%) · cash $0.00 · open 10/10 · round trips 938

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-143.12 · worst day $-50.94 · trades/day 32.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 812 | 52% | -0.12% | 49% | 44% | 7% |
| bottom | 126 | 46% | -0.38% | 40% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-03T21:36 | TRBUSDT | surge | STOP | 3.8 | -3.25% | $-2.86 |
| 2026-10-03T20:30 | IOUSDT | surge | TARGET | 5.5 | +2.75% | $+2.36 |
| 2026-10-03T18:08 | STXUSDT | surge | STOP | 1.0 | -3.25% | $-2.79 |
| 2026-10-03T18:08 | CRCLBUSDT | bottom | TIME | 24.0 | +1.33% | $+1.13 |
| 2026-10-03T17:51 | SUPERUSDT | surge | STOP | 1.5 | -3.25% | $-3.21 |
| 2026-10-03T17:34 | JTOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.36 |
| 2026-10-03T17:17 | BNBUSDT | bottom | TARGET | 22.2 | +2.75% | $+2.29 |
| 2026-10-03T16:59 | STXUSDT | surge | TARGET | 2.5 | +2.75% | $+2.30 |
| 2026-10-03T16:42 | ZROUSDT | surge | STOP | 0.0 | -3.25% | $-2.88 |
| 2026-10-03T16:25 | AVAUSDT | surge | STOP | 0.5 | -3.25% | $-2.97 |
| 2026-10-03T16:08 | SPCXBUSDT | surge | TIME | 24.0 | +0.92% | $+0.90 |
| 2026-10-03T15:50 | ARUSDT | surge | STOP | 3.0 | -3.25% | $-2.64 |
| 2026-10-03T15:33 | TSLABUSDT | surge | TIME | 24.0 | -0.32% | $-0.30 |
| 2026-10-03T14:59 | SUPERUSDT | surge | TARGET | 0.8 | +2.75% | $+2.30 |
| 2026-10-03T13:27 | SYNUSDT | surge | STOP | 5.2 | -3.25% | $-2.65 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-03T01:28 | SNDKBUSDT | bottom | 1718.8 | 1716.47 | -0.14% |
| 2026-10-03T03:31 | INJUSDT | surge | 7.685 | 7.702 | +0.22% |
| 2026-10-03T15:50 | MORPHOUSDT | surge | 2.724 | 2.782 | +2.13% |
| 2026-10-03T17:17 | BNBUSDT | surge | 789.96 | 785.45 | -0.57% |
| 2026-10-03T17:51 | ATOMUSDT | surge | 1.733 | 1.715 | -1.04% |
| 2026-10-03T18:08 | ZKUSDT | surge | 0.01311 | 0.0132 | +0.69% |
| 2026-10-03T18:08 | OPUSDT | surge | 0.1355 | 0.1357 | +0.15% |
| 2026-10-03T20:30 | KAITOUSDT | surge | 0.3545 | 0.3467 | -2.20% |
| 2026-10-03T21:36 | DODOUSDT | surge | 0.01896 | 0.01914 | +0.95% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
