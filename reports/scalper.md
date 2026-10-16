# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-16T16:01:39+00:00 · runs 3555 · equity **$702.55** (-29.75%) · cash $0.00 · open 10/10 · round trips 1306

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-288.53 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1142 | 49% | -0.22% | 47% | 46% | 7% |
| bottom | 164 | 44% | -0.47% | 38% | 45% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-16T15:59 | BEAMXUSDT | surge | STOP | 3.8 | -3.25% | $-2.17 |
| 2026-10-16T15:42 | PROMUSDT | bottom | STOP | 0.0 | -3.25% | $-2.18 |
| 2026-10-16T15:42 | DASHUSDT | surge | TIME | 24.0 | -0.19% | $-0.14 |
| 2026-10-16T15:25 | AXLUSDT | surge | STOP | 0.2 | -3.25% | $-2.25 |
| 2026-10-16T15:07 | TSLABUSDT | surge | STOP | 11.5 | -3.25% | $-2.20 |
| 2026-10-16T15:07 | TRUMPUSDT | surge | TIME | 24.0 | -1.59% | $-1.12 |
| 2026-10-16T15:07 | HYPEUSDT | surge | TIME | 24.0 | -0.91% | $-0.64 |
| 2026-10-16T14:50 | BABYUSDT | surge | TIME | 24.0 | -1.92% | $-1.36 |
| 2026-10-16T14:16 | TRXUSDT | bottom | TIME | 24.0 | +1.60% | $+1.12 |
| 2026-10-16T12:10 | PROMUSDT | surge | STOP | 0.0 | -3.25% | $-2.24 |
| 2026-10-16T11:53 | APTUSDT | surge | TARGET | 6.0 | +2.75% | $+1.85 |
| 2026-10-16T05:31 | INITUSDT | surge | STOP | 0.5 | -3.25% | $-2.25 |
| 2026-10-16T04:57 | ZROUSDT | surge | TARGET | 0.8 | +2.75% | $+1.86 |
| 2026-10-16T03:50 | XPLUSDT | surge | STOP | 9.2 | -3.25% | $-2.27 |
| 2026-10-16T03:15 | PLUMEUSDT | surge | STOP | 2.5 | -3.25% | $-2.27 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-15T16:14 | LINKUSDT | surge | 12.558 | 12.321 | -1.89% |
| 2026-10-15T18:50 | CRCLBUSDT | surge | 85.89 | 84.28 | -1.87% |
| 2026-10-16T14:16 | OPENUSDT | surge | 0.0994 | 0.098 | -1.41% |
| 2026-10-16T15:07 | APEUSDT | surge | 0.1529 | 0.1518 | -0.72% |
| 2026-10-16T15:07 | SEIUSDT | surge | 0.06618 | 0.06435 | -2.77% |
| 2026-10-16T15:07 | DOTUSDT | surge | 1.198 | 1.172 | -2.17% |
| 2026-10-16T15:42 | SOXSBUSDT | surge | 46.77 | 46.77 | +0.00% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02146 | +0.33% |
| 2026-10-16T15:59 | MSTRBUSDT | bottom | 141.71 | 138.41 | -2.33% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
