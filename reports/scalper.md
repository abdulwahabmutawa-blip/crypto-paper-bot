# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-16T14:37:02+00:00 · runs 971 · equity **$883.63** (-11.64%) · cash $0.00 · open 10/10 · round trips 338

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-110.47 · worst day $-50.94 · trades/day 28.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 260 | 49% | -0.27% | 45% | 46% | 8% |
| bottom | 78 | 41% | -0.55% | 40% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-16T14:34 | HEIUSDT | surge | TARGET | 0.0 | +2.75% | $+2.46 |
| 2026-09-16T14:17 | SOXLBUSDT | surge | TARGET | 7.0 | +2.75% | $+2.39 |
| 2026-09-16T13:59 | DASHUSDT | surge | TARGET | 2.0 | +2.75% | $+2.48 |
| 2026-09-16T13:59 | NEARUSDT | surge | TARGET | 3.0 | +2.75% | $+2.50 |
| 2026-09-16T13:24 | AAVEUSDT | bottom | STOP | 7.0 | -3.25% | $-2.85 |
| 2026-09-16T11:52 | ZECUSDT | surge | TARGET | 4.2 | +2.75% | $+2.42 |
| 2026-09-16T10:29 | HEIUSDT | surge | TARGET | 0.2 | +2.75% | $+2.45 |
| 2026-09-16T10:29 | MARSCOINUSDT | surge | TARGET | 1.2 | +2.75% | $+2.42 |
| 2026-09-16T10:12 | PUNDIXUSDT | surge | STOP | 0.8 | -3.25% | $-2.85 |
| 2026-09-16T09:55 | ACEUSDT | bottom | TARGET | 4.0 | +2.75% | $+2.41 |
| 2026-09-16T07:24 | ZECUSDT | surge | TARGET | 1.5 | +2.75% | $+2.41 |
| 2026-09-16T06:51 | HEMIUSDT | surge | STOP | 0.0 | -3.25% | $-2.85 |
| 2026-09-16T03:46 | GRAMUSDT | bottom | TIME | 24.0 | -2.34% | $-1.97 |
| 2026-09-16T03:29 | JSTUSDT | surge | TIME | 24.0 | +0.08% | $+0.07 |
| 2026-09-15T19:04 | BANKUSDT | bottom | STOP | 15.2 | -3.25% | $-2.74 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T05:40 | SKHYBUSDT | surge | 178.8 | 178.85 | +0.03% |
| 2026-09-16T05:40 | HBARUSDT | bottom | 0.0746 | 0.07278 | -2.44% |
| 2026-09-16T09:55 | FFUSDT | bottom | 0.13714 | 0.13648 | -0.48% |
| 2026-09-16T10:12 | INTCBUSDT | surge | 102.11 | 101.31 | -0.78% |
| 2026-09-16T10:45 | ZENUSDT | surge | 6.48 | 6.439 | -0.63% |
| 2026-09-16T13:24 | LAUSDT | surge | 0.0669 | 0.0664 | -0.75% |
| 2026-09-16T13:59 | BOMEUSDT | surge | 0.0008922 | 0.0008855 | -0.75% |
| 2026-09-16T13:59 | NEARUSDT | surge | 2.47 | 2.454 | -0.65% |
| 2026-09-16T14:34 | TSLABUSDT | surge | 363.68 | 362.99 | -0.19% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
