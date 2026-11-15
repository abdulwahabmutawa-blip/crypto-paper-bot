# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-15T23:47:49+00:00 · runs 6098 · equity **$501.80** (-49.82%) · cash $0.00 · open 10/10 · round trips 2007

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-502.05 · worst day $-50.94 · trades/day 27.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1734 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 273 | 42% | -0.54% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-15T23:29 | TQQQBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.27 |
| 2026-11-15T23:29 | KORUBUSDT | surge | TARGET | 2.2 | +2.75% | $+1.24 |
| 2026-11-15T23:29 | NBISBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.25 |
| 2026-11-15T23:29 | SOXLBUSDT | surge | TARGET | 6.5 | +2.75% | $+1.24 |
| 2026-11-15T22:40 | LSKUSDT | surge | TARGET | 7.8 | +2.75% | $+1.24 |
| 2026-11-15T21:02 | WINUSDT | surge | STOP | 1.5 | -3.25% | $-1.48 |
| 2026-11-15T20:25 | PARTIUSDT | surge | STOP | 3.5 | -3.25% | $-1.47 |
| 2026-11-15T20:25 | KITEUSDT | surge | TARGET | 6.5 | +2.75% | $+1.24 |
| 2026-11-15T19:20 | FFUSDT | surge | STOP | 0.2 | -3.25% | $-1.50 |
| 2026-11-15T17:58 | SHELLUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.24 |
| 2026-11-15T17:26 | FFUSDT | surge | TARGET | 0.8 | +2.75% | $+1.24 |
| 2026-11-15T16:20 | PROMUSDT | surge | TARGET | 0.0 | +2.75% | $+1.23 |
| 2026-11-15T16:20 | FFUSDT | surge | TARGET | 3.0 | +2.75% | $+1.24 |
| 2026-11-15T14:58 | MEGAUSDT | surge | STOP | 1.5 | -3.25% | $-1.46 |
| 2026-11-15T09:31 | MEGAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.23 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T14:58 | TRXUSDT | bottom | 0.3057 | 0.3054 | -0.10% |
| 2026-11-15T16:20 | PROMUSDT | surge | 5.211 | 5.349 | +2.65% |
| 2026-11-15T19:20 | NVDABUSDT | surge | 164.87 | 165.76 | +0.54% |
| 2026-11-15T20:25 | SENTUSDT | surge | 0.01694 | 0.01686 | -0.47% |
| 2026-11-15T21:02 | SAGAUSDT | surge | 0.01416 | 0.01422 | +0.42% |
| 2026-11-15T23:29 | TQQQBUSDT | surge | 58.28 | 58.75 | +0.81% |
| 2026-11-15T23:29 | KORUBUSDT | surge | 7.58 | 7.82 | +3.17% |
| 2026-11-15T23:29 | SKHYBUSDT | surge | 132.44 | 134.07 | +1.23% |
| 2026-11-15T23:29 | NBISBUSDT | surge | 117.77 | 117.87 | +0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
