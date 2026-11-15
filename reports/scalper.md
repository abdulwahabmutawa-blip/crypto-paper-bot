# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-15T18:00:11+00:00 · runs 6076 · equity **$492.60** (-50.74%) · cash $138.20 · open 7/10 · round trips 1998

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-505.09 · worst day $-50.94 · trades/day 27.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1725 | 48% | -0.33% | 46% | 48% | 7% |
| bottom | 273 | 42% | -0.54% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-15T17:58 | SHELLUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.24 |
| 2026-11-15T17:26 | FFUSDT | surge | TARGET | 0.8 | +2.75% | $+1.24 |
| 2026-11-15T16:20 | PROMUSDT | surge | TARGET | 0.0 | +2.75% | $+1.23 |
| 2026-11-15T16:20 | FFUSDT | surge | TARGET | 3.0 | +2.75% | $+1.24 |
| 2026-11-15T14:58 | MEGAUSDT | surge | STOP | 1.5 | -3.25% | $-1.46 |
| 2026-11-15T09:31 | MEGAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.23 |
| 2026-11-15T06:07 | SPCXBUSDT | bottom | TIME | 24.0 | +0.32% | $+0.14 |
| 2026-11-15T06:07 | GOOGLBUSDT | bottom | TIME | 24.0 | -0.72% | $-0.33 |
| 2026-11-14T19:55 | WLFIUSDT | surge | STOP | 13.5 | -3.25% | $-1.47 |
| 2026-11-14T14:14 | FETUSDT | bottom | STOP | 8.2 | -3.25% | $-1.47 |
| 2026-11-14T06:26 | DODOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.24 |
| 2026-11-13T16:11 | TRXUSDT | bottom | TIME | 24.0 | -0.98% | $-0.44 |
| 2026-11-13T01:57 | OPENUSDT | surge | STOP | 12.2 | -3.25% | $-1.45 |
| 2026-11-12T23:56 | GOOGLBUSDT | surge | TIME | 24.0 | +1.24% | $+0.57 |
| 2026-11-12T19:50 | GRAMUSDT | surge | STOP | 6.2 | -3.25% | $-1.50 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T13:37 | KITEUSDT | surge | 0.1381 | 0.1384 | +0.22% |
| 2026-11-15T14:30 | LSKUSDT | surge | 0.148 | 0.1453 | -1.82% |
| 2026-11-15T14:58 | TRXUSDT | bottom | 0.3057 | 0.3054 | -0.10% |
| 2026-11-15T16:20 | PROMUSDT | surge | 5.211 | 5.177 | -0.65% |
| 2026-11-15T16:37 | PARTIUSDT | surge | 0.0357 | 0.0355 | -0.56% |
| 2026-11-15T16:53 | SOXLBUSDT | surge | 56.36 | 55.12 | -2.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
