# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-16T20:24:06+00:00 · runs 3571 · equity **$702.28** (-29.77%) · cash $0.00 · open 10/10 · round trips 1316

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-293.53 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1149 | 49% | -0.23% | 47% | 46% | 7% |
| bottom | 167 | 44% | -0.45% | 38% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-16T20:22 | SOXSBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.90 |
| 2026-10-16T20:22 | ZROUSDT | bottom | TARGET | 3.0 | +2.75% | $+1.82 |
| 2026-10-16T18:19 | SOXSBUSDT | surge | TARGET | 2.5 | +2.75% | $+1.88 |
| 2026-10-16T17:44 | NEARUSDT | bottom | TARGET | 0.2 | +2.75% | $+1.82 |
| 2026-10-16T17:44 | FILUSDT | surge | STOP | 1.0 | -3.25% | $-2.39 |
| 2026-10-16T17:27 | MSTRBUSDT | bottom | STOP | 1.2 | -3.25% | $-2.10 |
| 2026-10-16T17:27 | CRCLBUSDT | surge | STOP | 22.2 | -3.25% | $-2.36 |
| 2026-10-16T17:09 | DOTUSDT | surge | STOP | 1.8 | -3.25% | $-2.22 |
| 2026-10-16T17:09 | SEIUSDT | surge | STOP | 1.8 | -3.25% | $-2.22 |
| 2026-10-16T16:16 | LINKUSDT | surge | TIME | 24.0 | -1.52% | $-1.13 |
| 2026-10-16T15:59 | BEAMXUSDT | surge | STOP | 3.8 | -3.25% | $-2.17 |
| 2026-10-16T15:42 | PROMUSDT | bottom | STOP | 0.0 | -3.25% | $-2.18 |
| 2026-10-16T15:42 | DASHUSDT | surge | TIME | 24.0 | -0.19% | $-0.14 |
| 2026-10-16T15:25 | AXLUSDT | surge | STOP | 0.2 | -3.25% | $-2.25 |
| 2026-10-16T15:07 | TSLABUSDT | surge | STOP | 11.5 | -3.25% | $-2.20 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T14:16 | OPENUSDT | surge | 0.0994 | 0.0977 | -1.71% |
| 2026-10-16T15:07 | APEUSDT | surge | 0.1529 | 0.149 | -2.55% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02105 | -1.59% |
| 2026-10-16T17:09 | AEROUSDT | bottom | 0.8661 | 0.8704 | +0.50% |
| 2026-10-16T17:44 | BCHUSDT | bottom | 272.8 | 274.3 | +0.55% |
| 2026-10-16T19:18 | AUDIOUSDT | surge | 0.0164 | 0.01623 | -1.04% |
| 2026-10-16T20:06 | SEIUSDT | surge | 0.06587 | 0.06569 | -0.27% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 49.29 | +0.06% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 878.39 | +0.02% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
