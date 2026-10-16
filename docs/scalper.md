# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-16T15:09:50+00:00 · runs 3552 · equity **$709.33** (-29.07%) · cash $0.00 · open 10/10 · round trips 1302

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.25%/trade · realized $-281.80 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1139 | 50% | -0.22% | 47% | 46% | 7% |
| bottom | 163 | 44% | -0.46% | 38% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-16T00:30 | FFUSDT | surge | STOP | 8.8 | -3.25% | $-2.35 |
| 2026-10-15T18:50 | BCHUSDT | surge | TARGET | 3.8 | +2.75% | $+1.94 |
| 2026-10-15T18:16 | QQQBUSDT | bottom | TIME | 24.0 | -0.81% | $-0.57 |
| 2026-10-15T16:14 | CRVUSDT | surge | TARGET | 1.0 | +2.75% | $+2.00 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-15T15:22 | DASHUSDT | surge | 49.09 | 49.01 | -0.16% |
| 2026-10-15T16:14 | LINKUSDT | surge | 12.558 | 12.408 | -1.19% |
| 2026-10-15T18:50 | CRCLBUSDT | surge | 85.89 | 85.16 | -0.85% |
| 2026-10-16T12:10 | BEAMXUSDT | surge | 0.003026 | 0.002982 | -1.45% |
| 2026-10-16T14:16 | OPENUSDT | surge | 0.0994 | 0.0984 | -1.01% |
| 2026-10-16T14:50 | AXLUSDT | surge | 0.0578 | 0.0559 | -3.29% |
| 2026-10-16T15:07 | APEUSDT | surge | 0.1529 | 0.1505 | -1.57% |
| 2026-10-16T15:07 | SEIUSDT | surge | 0.06618 | 0.06493 | -1.89% |
| 2026-10-16T15:07 | DOTUSDT | surge | 1.198 | 1.182 | -1.34% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
