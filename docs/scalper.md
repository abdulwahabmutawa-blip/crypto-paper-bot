# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-16T12:46:06+00:00 · runs 3543 · equity **$725.42** (-27.46%) · cash $0.00 · open 10/10 · round trips 1297

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.25%/trade · realized $-277.60 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1135 | 50% | -0.21% | 47% | 46% | 7% |
| bottom | 162 | 44% | -0.47% | 38% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-16T12:10 | PROMUSDT | surge | STOP | 0.0 | -3.25% | $-2.24 |
| 2026-10-16T11:53 | APTUSDT | surge | TARGET | 6.0 | +2.75% | $+1.85 |
| 2026-10-16T05:31 | INITUSDT | surge | STOP | 0.5 | -3.25% | $-2.25 |
| 2026-10-16T04:57 | ZROUSDT | surge | TARGET | 0.8 | +2.75% | $+1.86 |
| 2026-10-16T03:50 | XPLUSDT | surge | STOP | 9.2 | -3.25% | $-2.27 |
| 2026-10-16T03:15 | PLUMEUSDT | surge | STOP | 2.5 | -3.25% | $-2.27 |
| 2026-10-16T00:30 | FFUSDT | surge | STOP | 8.8 | -3.25% | $-2.35 |
| 2026-10-15T18:50 | BCHUSDT | surge | TARGET | 3.8 | +2.75% | $+1.94 |
| 2026-10-15T18:16 | QQQBUSDT | bottom | TIME | 24.0 | -0.81% | $-0.57 |
| 2026-10-15T16:14 | CRVUSDT | surge | TARGET | 1.0 | +2.75% | $+2.00 |
| 2026-10-15T15:22 | XRPUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.93 |
| 2026-10-15T15:22 | XPLUSDT | surge | TARGET | 1.0 | +2.75% | $+1.93 |
| 2026-10-15T15:05 | ZAMAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.94 |
| 2026-10-15T14:30 | RLCUSDT | surge | TARGET | 0.0 | +2.75% | $+1.93 |
| 2026-10-15T07:14 | SOXSBUSDT | surge | TARGET | 6.0 | +2.75% | $+1.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-15T14:08 | TRXUSDT | bottom | 0.3298 | 0.3356 | +1.76% |
| 2026-10-15T14:30 | BABYUSDT | surge | 0.01258 | 0.01244 | -1.11% |
| 2026-10-15T14:47 | HYPEUSDT | surge | 80.78 | 81.49 | +0.88% |
| 2026-10-15T14:47 | TRUMPUSDT | surge | 1.866 | 1.88 | +0.75% |
| 2026-10-15T15:22 | DASHUSDT | surge | 49.09 | 50.22 | +2.30% |
| 2026-10-15T16:14 | LINKUSDT | surge | 12.558 | 12.622 | +0.51% |
| 2026-10-15T18:50 | CRCLBUSDT | surge | 85.89 | 85.11 | -0.91% |
| 2026-10-16T03:15 | TSLABUSDT | surge | 373.97 | 374.42 | +0.12% |
| 2026-10-16T12:10 | BEAMXUSDT | surge | 0.003026 | 0.003024 | -0.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
