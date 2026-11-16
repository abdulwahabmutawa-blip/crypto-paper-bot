# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-16T12:30:15+00:00 · runs 6145 · equity **$488.57** (-51.14%) · cash $135.09 · open 7/10 · round trips 2022

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-508.19 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1745 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 277 | 42% | -0.54% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-16T12:28 | NBISBUSDT | bottom | STOP | 4.5 | -3.25% | $-1.52 |
| 2026-11-16T12:28 | SOXSBUSDT | surge | TARGET | 6.2 | +2.75% | $+1.21 |
| 2026-11-16T12:28 | BMNRBUSDT | surge | STOP | 9.5 | -3.25% | $-1.50 |
| 2026-11-16T09:14 | SENTUSDT | surge | TARGET | 12.5 | +2.75% | $+1.24 |
| 2026-11-16T07:46 | ZROUSDT | bottom | TARGET | 6.2 | +2.75% | $+1.25 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T14:58 | TRXUSDT | bottom | 0.3057 | 0.304 | -0.56% |
| 2026-11-15T21:02 | SAGAUSDT | surge | 0.01416 | 0.01393 | -1.62% |
| 2026-11-16T01:24 | PROMUSDT | surge | 5.315 | 5.177 | -2.60% |
| 2026-11-16T02:01 | MSTRBUSDT | surge | 102.8 | 101.98 | -0.80% |
| 2026-11-16T07:11 | PEPEUSDT | bottom | 3.77e-06 | 3.74e-06 | -0.80% |
| 2026-11-16T09:30 | SENTUSDT | surge | 0.01735 | 0.01721 | -0.81% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
