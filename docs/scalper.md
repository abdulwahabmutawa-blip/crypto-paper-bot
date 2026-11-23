# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T01:54:41+00:00 · runs 6609 · equity **$480.11** (-51.99%) · cash $0.00 · open 10/10 · round trips 2149

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-517.12 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1850 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 299 | 43% | -0.45% | 37% | 43% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-23T01:53 | LISTAUSDT | surge | STOP | 0.0 | -3.25% | $-1.43 |
| 2026-11-23T01:53 | KITEUSDT | surge | TARGET | 17.2 | +2.75% | $+1.20 |
| 2026-11-23T01:36 | NBISBUSDT | surge | STOP | 1.0 | -3.25% | $-1.48 |
| 2026-11-23T00:28 | LISTAUSDT | surge | TARGET | 1.2 | +2.75% | $+1.22 |
| 2026-11-22T23:04 | SOXLBUSDT | surge | TARGET | 14.0 | +2.75% | $+1.18 |
| 2026-11-22T17:03 | KORUBUSDT | surge | TARGET | 7.0 | +2.75% | $+1.23 |
| 2026-11-22T17:03 | ETCUSDT | surge | TIME | 24.0 | +1.57% | $+0.67 |
| 2026-11-22T11:44 | ARUSDT | surge | TARGET | 2.8 | +2.75% | $+1.20 |
| 2026-11-22T10:19 | PYTHUSDT | surge | TARGET | 17.5 | +2.75% | $+1.17 |
| 2026-11-22T10:02 | SNXXBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.18 |
| 2026-11-22T10:02 | ICPUSDT | bottom | TARGET | 7.2 | +2.75% | $+1.17 |
| 2026-11-22T09:45 | RAREUSDT | bottom | TARGET | 1.2 | +2.75% | $+1.20 |
| 2026-11-22T09:07 | ERAUSDT | surge | TARGET | 5.0 | +2.75% | $+1.17 |
| 2026-11-22T08:50 | YBUSDT | bottom | TARGET | 3.0 | +2.75% | $+1.13 |
| 2026-11-22T08:50 | STXUSDT | surge | TARGET | 16.2 | +2.75% | $+1.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-22T09:07 | RENDERUSDT | surge | 1.337 | 1.322 | -1.12% |
| 2026-11-22T10:02 | EWYBUSDT | surge | 127.63 | 127.4 | -0.18% |
| 2026-11-22T10:02 | BONKUSDT | surge | 2.1e-06 | 2.05e-06 | -2.38% |
| 2026-11-22T10:19 | NVDABUSDT | surge | 132.81 | 132.64 | -0.13% |
| 2026-11-22T11:44 | TSLABUSDT | surge | 359.44 | 358.89 | -0.15% |
| 2026-11-22T17:03 | CAKEUSDT | surge | 1.524 | 1.518 | -0.39% |
| 2026-11-22T17:03 | INITUSDT | bottom | 0.08665 | 0.08617 | -0.55% |
| 2026-11-23T01:53 | SOXLBUSDT | surge | 34.84 | 34.54 | -0.86% |
| 2026-11-23T01:53 | SKHYBUSDT | surge | 111.81 | 111.22 | -0.53% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
