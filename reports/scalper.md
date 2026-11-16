# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-16T04:04:34+00:00 · runs 6114 · equity **$493.29** (-50.67%) · cash $0.00 · open 10/10 · round trips 2015

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-505.90 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1741 | 48% | -0.33% | 46% | 48% | 7% |
| bottom | 274 | 42% | -0.53% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-16T02:36 | ASTERUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.25 |
| 2026-11-16T01:57 | TQQQBUSDT | surge | STOP | 2.2 | -3.25% | $-1.52 |
| 2026-11-16T01:24 | MUBUSDT | surge | STOP | 1.0 | -3.25% | $-1.54 |
| 2026-11-16T01:24 | DRAMBUSDT | surge | STOP | 1.0 | -3.25% | $-1.54 |
| 2026-11-16T01:24 | NBISBUSDT | surge | STOP | 1.8 | -3.25% | $-1.52 |
| 2026-11-16T01:24 | SKHYBUSDT | surge | STOP | 1.8 | -3.25% | $-1.52 |
| 2026-11-16T00:02 | KORUBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.29 |
| 2026-11-16T00:02 | PROMUSDT | surge | TARGET | 7.5 | +2.75% | $+1.24 |
| 2026-11-15T23:29 | TQQQBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.27 |
| 2026-11-15T23:29 | KORUBUSDT | surge | TARGET | 2.2 | +2.75% | $+1.24 |
| 2026-11-15T23:29 | NBISBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.25 |
| 2026-11-15T23:29 | SOXLBUSDT | surge | TARGET | 6.5 | +2.75% | $+1.24 |
| 2026-11-15T22:40 | LSKUSDT | surge | TARGET | 7.8 | +2.75% | $+1.24 |
| 2026-11-15T21:02 | WINUSDT | surge | STOP | 1.5 | -3.25% | $-1.48 |
| 2026-11-15T20:25 | PARTIUSDT | surge | STOP | 3.5 | -3.25% | $-1.47 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T14:58 | TRXUSDT | bottom | 0.3057 | 0.3044 | -0.43% |
| 2026-11-15T19:20 | NVDABUSDT | surge | 164.87 | 162.44 | -1.47% |
| 2026-11-15T20:25 | SENTUSDT | surge | 0.01694 | 0.01691 | -0.18% |
| 2026-11-15T21:02 | SAGAUSDT | surge | 0.01416 | 0.01419 | +0.21% |
| 2026-11-16T01:24 | PROMUSDT | surge | 5.315 | 5.336 | +0.40% |
| 2026-11-16T01:24 | ZROUSDT | bottom | 1.368 | 1.383 | +1.10% |
| 2026-11-16T02:01 | MSTRBUSDT | surge | 102.8 | 103.88 | +1.05% |
| 2026-11-16T02:36 | BMNRBUSDT | surge | 16.7 | 16.58 | -0.72% |
| 2026-11-16T02:54 | NIGHTUSDT | bottom | 0.04701 | 0.04621 | -1.70% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
