# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-16T07:31:08+00:00 · runs 6126 · equity **$490.73** (-50.93%) · cash $0.00 · open 10/10 · round trips 2017

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-508.88 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1742 | 48% | -0.33% | 46% | 48% | 7% |
| bottom | 275 | 42% | -0.54% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-16T07:11 | NIGHTUSDT | bottom | STOP | 4.0 | -3.25% | $-1.50 |
| 2026-11-16T06:03 | NVDABUSDT | surge | STOP | 10.5 | -3.25% | $-1.48 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T14:58 | TRXUSDT | bottom | 0.3057 | 0.3032 | -0.82% |
| 2026-11-15T20:25 | SENTUSDT | surge | 0.01694 | 0.01696 | +0.12% |
| 2026-11-15T21:02 | SAGAUSDT | surge | 0.01416 | 0.01402 | -0.99% |
| 2026-11-16T01:24 | PROMUSDT | surge | 5.315 | 5.284 | -0.58% |
| 2026-11-16T01:24 | ZROUSDT | bottom | 1.368 | 1.401 | +2.41% |
| 2026-11-16T02:01 | MSTRBUSDT | surge | 102.8 | 103.19 | +0.38% |
| 2026-11-16T02:36 | BMNRBUSDT | surge | 16.7 | 16.56 | -0.84% |
| 2026-11-16T06:03 | SOXSBUSDT | surge | 55.98 | 55.65 | -0.59% |
| 2026-11-16T07:11 | PEPEUSDT | bottom | 3.77e-06 | 3.77e-06 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
