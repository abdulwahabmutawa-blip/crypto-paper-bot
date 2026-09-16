# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-16T13:09:02+00:00 · runs 966 · equity **$878.02** (-12.20%) · cash $0.00 · open 10/10 · round trips 333

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-117.45 · worst day $-50.94 · trades/day 27.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 256 | 48% | -0.32% | 45% | 47% | 9% |
| bottom | 77 | 42% | -0.51% | 40% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-15T18:29 | DODOUSDT | surge | STOP | 14.2 | -3.25% | $-3.01 |
| 2026-09-15T17:38 | METABUSDT | surge | TIME | 24.0 | +0.08% | $+0.07 |
| 2026-09-15T16:12 | SKHYBUSDT | surge | STOP | 2.2 | -3.25% | $-2.79 |
| 2026-09-15T15:03 | TUTUSDT | surge | TARGET | 1.2 | +2.75% | $+2.36 |
| 2026-09-15T15:03 | INJUSDT | bottom | STOP | 2.5 | -3.25% | $-2.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T05:40 | SKHYBUSDT | surge | 178.8 | 179.94 | +0.64% |
| 2026-09-16T05:40 | HBARUSDT | bottom | 0.0746 | 0.07387 | -0.98% |
| 2026-09-16T06:13 | AAVEUSDT | bottom | 121.06 | 117.45 | -2.98% |
| 2026-09-16T07:08 | SOXLBUSDT | surge | 105.59 | 106.59 | +0.95% |
| 2026-09-16T09:55 | FFUSDT | bottom | 0.13714 | 0.13626 | -0.64% |
| 2026-09-16T10:12 | INTCBUSDT | surge | 102.11 | 100.62 | -1.46% |
| 2026-09-16T10:45 | NEARUSDT | surge | 2.428 | 2.471 | +1.77% |
| 2026-09-16T10:45 | ZENUSDT | surge | 6.48 | 6.389 | -1.40% |
| 2026-09-16T11:52 | DASHUSDT | surge | 53.88 | 53.31 | -1.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
