# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-15T21:36:34+00:00 · runs 3489 · equity **$734.26** (-26.57%) · cash $0.00 · open 10/10 · round trips 1290

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.24%/trade · realized $-269.92 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1128 | 50% | -0.21% | 47% | 45% | 7% |
| bottom | 162 | 44% | -0.47% | 38% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-15T18:50 | BCHUSDT | surge | TARGET | 3.8 | +2.75% | $+1.94 |
| 2026-10-15T18:16 | QQQBUSDT | bottom | TIME | 24.0 | -0.81% | $-0.57 |
| 2026-10-15T16:14 | CRVUSDT | surge | TARGET | 1.0 | +2.75% | $+2.00 |
| 2026-10-15T15:22 | XRPUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.93 |
| 2026-10-15T15:22 | XPLUSDT | surge | TARGET | 1.0 | +2.75% | $+1.93 |
| 2026-10-15T15:05 | ZAMAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.94 |
| 2026-10-15T14:30 | RLCUSDT | surge | TARGET | 0.0 | +2.75% | $+1.93 |
| 2026-10-15T07:14 | SOXSBUSDT | surge | TARGET | 6.0 | +2.75% | $+1.94 |
| 2026-10-15T02:32 | DUSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.31 |
| 2026-10-15T02:32 | SOLUSDT | bottom | STOP | 13.0 | -3.25% | $-2.30 |
| 2026-10-15T02:32 | BNBUSDT | bottom | STOP | 13.2 | -3.25% | $-2.29 |
| 2026-10-15T01:23 | MEGAUSDT | surge | TARGET | 4.0 | +2.75% | $+1.95 |
| 2026-10-15T00:49 | WCTUSDT | surge | STOP | 1.2 | -3.25% | $-2.31 |
| 2026-10-14T22:30 | SOXSBUSDT | surge | TARGET | 2.8 | +2.75% | $+1.94 |
| 2026-10-14T20:44 | AXLUSDT | surge | STOP | 3.0 | -3.25% | $-2.39 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-15T14:08 | TRXUSDT | bottom | 0.3298 | 0.3324 | +0.79% |
| 2026-10-15T14:30 | BABYUSDT | surge | 0.01258 | 0.0127 | +0.95% |
| 2026-10-15T14:47 | HYPEUSDT | surge | 80.78 | 82.19 | +1.75% |
| 2026-10-15T14:47 | TRUMPUSDT | surge | 1.866 | 1.888 | +1.18% |
| 2026-10-15T15:22 | DASHUSDT | surge | 49.09 | 49.84 | +1.53% |
| 2026-10-15T15:22 | FFUSDT | surge | 0.11541 | 0.11474 | -0.58% |
| 2026-10-15T16:14 | LINKUSDT | surge | 12.558 | 12.538 | -0.16% |
| 2026-10-15T18:16 | XPLUSDT | surge | 0.08608 | 0.08608 | +0.00% |
| 2026-10-15T18:50 | CRCLBUSDT | surge | 85.89 | 86.27 | +0.44% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
