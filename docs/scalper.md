# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-15T22:09:18+00:00 · runs 6092 · equity **$491.92** (-50.81%) · cash $0.00 · open 10/10 · round trips 2002

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-508.30 · worst day $-50.94 · trades/day 27.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1729 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 273 | 42% | -0.54% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-15T06:07 | SPCXBUSDT | bottom | TIME | 24.0 | +0.32% | $+0.14 |
| 2026-11-15T06:07 | GOOGLBUSDT | bottom | TIME | 24.0 | -0.72% | $-0.33 |
| 2026-11-14T19:55 | WLFIUSDT | surge | STOP | 13.5 | -3.25% | $-1.47 |
| 2026-11-14T14:14 | FETUSDT | bottom | STOP | 8.2 | -3.25% | $-1.47 |
| 2026-11-14T06:26 | DODOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.24 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T14:30 | LSKUSDT | surge | 0.148 | 0.1478 | -0.14% |
| 2026-11-15T14:58 | TRXUSDT | bottom | 0.3057 | 0.3051 | -0.20% |
| 2026-11-15T16:20 | PROMUSDT | surge | 5.211 | 5.255 | +0.84% |
| 2026-11-15T16:53 | SOXLBUSDT | surge | 56.36 | 56.94 | +1.03% |
| 2026-11-15T19:20 | NVDABUSDT | surge | 164.87 | 164.5 | -0.22% |
| 2026-11-15T19:36 | NBISBUSDT | surge | 113.18 | 114.42 | +1.10% |
| 2026-11-15T20:25 | SENTUSDT | surge | 0.01694 | 0.01683 | -0.65% |
| 2026-11-15T20:45 | KORUBUSDT | surge | 7.4 | 7.39 | -0.14% |
| 2026-11-15T21:02 | SAGAUSDT | surge | 0.01416 | 0.01399 | -1.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
