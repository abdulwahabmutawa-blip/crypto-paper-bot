# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T01:56:10+00:00 · runs 3592 · equity **$699.20** (-30.08%) · cash $0.00 · open 10/10 · round trips 1318

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-298.02 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1151 | 49% | -0.24% | 47% | 46% | 7% |
| bottom | 167 | 44% | -0.45% | 38% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-17T01:37 | SEIUSDT | surge | STOP | 5.2 | -3.25% | $-2.25 |
| 2026-10-16T22:00 | AUDIOUSDT | surge | STOP | 2.5 | -3.25% | $-2.25 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T14:16 | OPENUSDT | surge | 0.0994 | 0.0976 | -1.81% |
| 2026-10-16T15:07 | APEUSDT | surge | 0.1529 | 0.1493 | -2.35% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02118 | -0.98% |
| 2026-10-16T17:09 | AEROUSDT | bottom | 0.8661 | 0.8743 | +0.95% |
| 2026-10-16T17:44 | BCHUSDT | bottom | 272.8 | 278.1 | +1.94% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 48.93 | -0.67% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 879.83 | +0.18% |
| 2026-10-16T22:00 | BEAMXUSDT | surge | 0.003005 | 0.002963 | -1.40% |
| 2026-10-17T01:54 | ERAUSDT | surge | 0.0599 | 0.06 | +0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
