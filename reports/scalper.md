# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T08:46:27+00:00 · runs 3617 · equity **$696.17** (-30.38%) · cash $0.00 · open 10/10 · round trips 1326

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-299.48 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1157 | 49% | -0.24% | 47% | 46% | 7% |
| bottom | 169 | 45% | -0.41% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-17T08:45 | ERAUSDT | surge | TARGET | 6.8 | +2.75% | $+1.84 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02129 | -0.47% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 49.01 | -0.51% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 881.54 | +0.38% |
| 2026-10-17T03:05 | MINAUSDT | surge | 0.0777 | 0.0775 | -0.26% |
| 2026-10-17T06:52 | EIGENUSDT | surge | 0.2708 | 0.2708 | +0.00% |
| 2026-10-17T07:24 | NMRUSDT | surge | 12.34 | 12.19 | -1.22% |
| 2026-10-17T08:12 | SANDUSDT | surge | 0.05871 | 0.05737 | -2.28% |
| 2026-10-17T08:12 | NILUSDT | surge | 0.08826 | 0.0859 | -2.67% |
| 2026-10-17T08:45 | RSRUSDT | surge | 0.002047 | 0.002059 | +0.59% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
