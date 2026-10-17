# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T08:14:12+00:00 · runs 3615 · equity **$696.70** (-30.33%) · cash $0.00 · open 10/10 · round trips 1325

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.27%/trade · realized $-301.32 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1156 | 49% | -0.24% | 47% | 46% | 7% |
| bottom | 169 | 45% | -0.41% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-17T08:12 | BEAMXUSDT | surge | STOP | 9.8 | -3.25% | $-2.17 |
| 2026-10-17T08:12 | OPENUSDT | surge | STOP | 17.5 | -3.25% | $-2.32 |
| 2026-10-17T07:24 | RSRUSDT | surge | TARGET | 1.0 | +2.75% | $+1.87 |
| 2026-10-17T06:52 | PHAUSDT | surge | STOP | 3.2 | -3.25% | $-2.15 |
| 2026-10-17T06:13 | AEROUSDT | bottom | TARGET | 13.0 | +2.75% | $+1.82 |
| 2026-10-17T03:22 | APEUSDT | surge | STOP | 12.0 | -3.25% | $-2.22 |
| 2026-10-17T03:05 | BCHUSDT | bottom | TARGET | 9.2 | +2.75% | $+1.89 |
| 2026-10-17T01:37 | SEIUSDT | surge | STOP | 5.2 | -3.25% | $-2.25 |
| 2026-10-16T22:00 | AUDIOUSDT | surge | STOP | 2.5 | -3.25% | $-2.25 |
| 2026-10-16T20:22 | SOXSBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.90 |
| 2026-10-16T20:22 | ZROUSDT | bottom | TARGET | 3.0 | +2.75% | $+1.82 |
| 2026-10-16T18:19 | SOXSBUSDT | surge | TARGET | 2.5 | +2.75% | $+1.88 |
| 2026-10-16T17:44 | NEARUSDT | bottom | TARGET | 0.2 | +2.75% | $+1.82 |
| 2026-10-16T17:44 | FILUSDT | surge | STOP | 1.0 | -3.25% | $-2.39 |
| 2026-10-16T17:27 | MSTRBUSDT | bottom | STOP | 1.2 | -3.25% | $-2.10 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02144 | +0.23% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 49.04 | -0.45% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 881.83 | +0.41% |
| 2026-10-17T01:54 | ERAUSDT | surge | 0.0599 | 0.0595 | -0.67% |
| 2026-10-17T03:05 | MINAUSDT | surge | 0.0777 | 0.0771 | -0.77% |
| 2026-10-17T06:52 | EIGENUSDT | surge | 0.2708 | 0.2686 | -0.81% |
| 2026-10-17T07:24 | NMRUSDT | surge | 12.34 | 12.49 | +1.22% |
| 2026-10-17T08:12 | SANDUSDT | surge | 0.05871 | 0.058 | -1.21% |
| 2026-10-17T08:12 | NILUSDT | surge | 0.08826 | 0.0874 | -0.97% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
