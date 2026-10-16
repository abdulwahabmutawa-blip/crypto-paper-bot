# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-16T18:38:43+00:00 · runs 3564 · equity **$700.94** (-29.91%) · cash $138.33 · open 8/10 · round trips 1314

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-297.25 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1148 | 49% | -0.23% | 47% | 46% | 7% |
| bottom | 166 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-16T15:07 | TRUMPUSDT | surge | TIME | 24.0 | -1.59% | $-1.12 |
| 2026-10-16T15:07 | HYPEUSDT | surge | TIME | 24.0 | -0.91% | $-0.64 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T14:16 | OPENUSDT | surge | 0.0994 | 0.0977 | -1.71% |
| 2026-10-16T15:07 | APEUSDT | surge | 0.1529 | 0.1512 | -1.11% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02093 | -2.15% |
| 2026-10-16T17:09 | ZROUSDT | bottom | 2.008 | 2.029 | +1.05% |
| 2026-10-16T17:09 | AEROUSDT | bottom | 0.8661 | 0.8687 | +0.30% |
| 2026-10-16T17:44 | BCHUSDT | bottom | 272.8 | 274.4 | +0.59% |
| 2026-10-16T18:19 | SOXSBUSDT | surge | 48.02 | 48.26 | +0.50% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
