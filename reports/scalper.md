# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-19T13:05:27+00:00 · runs 3808 · equity **$679.81** (-32.02%) · cash $0.00 · open 10/10 · round trips 1401

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-324.45 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1223 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 178 | 45% | -0.36% | 39% | 42% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-19T11:54 | NBISBUSDT | surge | TARGET | 10.5 | +2.75% | $+1.80 |
| 2026-10-19T10:46 | EWYBUSDT | surge | TARGET | 9.0 | +2.75% | $+1.80 |
| 2026-10-19T10:46 | DRAMBUSDT | surge | TARGET | 10.2 | +2.75% | $+1.80 |
| 2026-10-19T03:17 | MSTRBUSDT | surge | TIME | 24.0 | +2.22% | $+1.38 |
| 2026-10-19T02:24 | TQQQBUSDT | surge | TARGET | 3.8 | +2.75% | $+1.75 |
| 2026-10-19T01:49 | SKHYBUSDT | surge | TARGET | 2.5 | +2.75% | $+1.80 |
| 2026-10-19T01:49 | TRXUSDT | bottom | TIME | 24.0 | -0.61% | $-0.39 |
| 2026-10-19T01:32 | EWYBUSDT | surge | TARGET | 3.0 | +2.75% | $+1.75 |
| 2026-10-19T01:14 | INTCBUSDT | surge | TARGET | 2.8 | +2.75% | $+1.75 |
| 2026-10-19T00:21 | SOXLBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.75 |
| 2026-10-19T00:21 | KORUBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.75 |
| 2026-10-18T23:11 | RUNEUSDT | surge | TARGET | 0.5 | +2.75% | $+1.75 |
| 2026-10-18T22:18 | SANDUSDT | bottom | TARGET | 0.5 | +2.75% | $+1.75 |
| 2026-10-18T22:18 | UNIUSDT | bottom | TARGET | 1.5 | +2.75% | $+1.73 |
| 2026-10-18T22:18 | SOXSBUSDT | surge | STOP | 3.5 | -3.25% | $-2.02 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-18T22:18 | QQQBUSDT | surge | 713.34 | 719.74 | +0.90% |
| 2026-10-19T00:21 | TSLABUSDT | surge | 359.63 | 356.02 | -1.00% |
| 2026-10-19T01:49 | SKHYBUSDT | surge | 139.41 | 143 | +2.58% |
| 2026-10-19T01:49 | MUBUSDT | surge | 897.99 | 913.18 | +1.69% |
| 2026-10-19T02:24 | TQQQBUSDT | surge | 70.62 | 70.92 | +0.42% |
| 2026-10-19T03:17 | AAOIBUSDT | surge | 79.21 | 79.47 | +0.33% |
| 2026-10-19T10:46 | ATOMUSDT | surge | 1.743 | 1.766 | +1.32% |
| 2026-10-19T10:46 | RAYUSDT | surge | 1.9318 | 1.926 | -0.30% |
| 2026-10-19T11:54 | NBISBUSDT | surge | 176.15 | 177.19 | +0.59% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
