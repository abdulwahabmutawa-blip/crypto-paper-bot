# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-16T16:14:11+00:00 · runs 6150 · equity **$492.18** (-50.78%) · cash $0.00 · open 10/10 · round trips 2025

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-508.50 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1746 | 48% | -0.33% | 46% | 48% | 7% |
| bottom | 279 | 42% | -0.52% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-16T16:12 | PEPEUSDT | bottom | TARGET | 7.5 | +2.75% | $+1.23 |
| 2026-11-16T16:12 | TRXUSDT | bottom | TIME | 24.0 | -0.12% | $-0.05 |
| 2026-11-16T13:17 | PROMUSDT | surge | STOP | 11.8 | -3.25% | $-1.48 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T21:02 | SAGAUSDT | surge | 0.01416 | 0.01418 | +0.14% |
| 2026-11-16T02:01 | MSTRBUSDT | surge | 102.8 | 102.83 | +0.03% |
| 2026-11-16T09:30 | SENTUSDT | surge | 0.01735 | 0.01733 | -0.12% |
| 2026-11-16T12:45 | GRAMUSDT | bottom | 1.033 | 1.043 | +0.97% |
| 2026-11-16T13:33 | DODOUSDT | surge | 0.03287 | 0.03305 | +0.55% |
| 2026-11-16T16:12 | SOXSBUSDT | surge | 57.21 | 57.73 | +0.91% |
| 2026-11-16T16:12 | ZAMAUSDT | surge | 0.05507 | 0.05506 | -0.02% |
| 2026-11-16T16:12 | ATOMUSDT | surge | 1.329 | 1.323 | -0.45% |
| 2026-11-16T16:12 | ZROUSDT | surge | 1.453 | 1.446 | -0.48% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
