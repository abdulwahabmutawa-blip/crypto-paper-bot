# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-16T08:00:02+00:00 · runs 947 · equity **$875.23** (-12.48%) · cash $263.53 · open 7/10 · round trips 328

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.39%/trade · realized $-124.29 · worst day $-50.94 · trades/day 27.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 252 | 48% | -0.34% | 44% | 47% | 9% |
| bottom | 76 | 41% | -0.55% | 39% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-15T12:27 | VTHOUSDT | surge | TARGET | 0.0 | +2.75% | $+2.42 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-16T05:40 | SKHYBUSDT | surge | 178.8 | 180.23 | +0.80% |
| 2026-09-16T05:40 | ACEUSDT | bottom | 0.15 | 0.15 | +0.00% |
| 2026-09-16T05:40 | HBARUSDT | bottom | 0.0746 | 0.07446 | -0.19% |
| 2026-09-16T06:13 | AAVEUSDT | bottom | 121.06 | 119.43 | -1.35% |
| 2026-09-16T07:08 | SOXLBUSDT | surge | 105.59 | 106.38 | +0.75% |
| 2026-09-16T07:24 | ZECUSDT | surge | 1185.93 | 1179.43 | -0.55% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
