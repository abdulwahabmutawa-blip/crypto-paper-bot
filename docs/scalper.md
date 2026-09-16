# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-16T09:57:20+00:00 · runs 954 · equity **$880.41** (-11.96%) · cash $0.00 · open 10/10 · round trips 329

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.38%/trade · realized $-121.88 · worst day $-50.94 · trades/day 27.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 252 | 48% | -0.34% | 44% | 47% | 9% |
| bottom | 77 | 42% | -0.51% | 40% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-15T14:12 | SPCXBUSDT | surge | STOP | 21.8 | -3.25% | $-3.17 |
| 2026-09-15T13:33 | TUTUSDT | surge | TARGET | 2.8 | +2.75% | $+2.36 |
| 2026-09-15T13:16 | MINAUSDT | surge | STOP | 0.5 | -3.25% | $-2.80 |
| 2026-09-15T12:43 | SAGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.31 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T05:40 | SKHYBUSDT | surge | 178.8 | 181 | +1.23% |
| 2026-09-16T05:40 | HBARUSDT | bottom | 0.0746 | 0.07447 | -0.17% |
| 2026-09-16T06:13 | AAVEUSDT | bottom | 121.06 | 119.65 | -1.16% |
| 2026-09-16T07:08 | SOXLBUSDT | surge | 105.59 | 106.89 | +1.23% |
| 2026-09-16T07:24 | ZECUSDT | surge | 1185.93 | 1212.4 | +2.23% |
| 2026-09-16T08:48 | MARSCOINUSDT | surge | 0.0987 | 0.0997 | +1.01% |
| 2026-09-16T09:05 | PUNDIXUSDT | surge | 0.1232 | 0.1201 | -2.52% |
| 2026-09-16T09:55 | HEIUSDT | surge | 0.1187 | 0.1197 | +0.84% |
| 2026-09-16T09:55 | FFUSDT | bottom | 0.13714 | 0.13702 | -0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
