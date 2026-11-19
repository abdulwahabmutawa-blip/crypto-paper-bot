# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-19T19:16:21+00:00 · runs 6366 · equity **$475.73** (-52.43%) · cash $84.66 · open 8/10 · round trips 2111

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-521.39 · worst day $-50.94 · trades/day 27.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1819 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 292 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-19T19:15 | HYPEUSDT | surge | STOP | 0.5 | -3.25% | $-1.44 |
| 2026-11-19T19:15 | USTCUSDT | surge | STOP | 2.0 | -3.25% | $-1.41 |
| 2026-11-19T18:43 | SAPIENUSDT | surge | TARGET | 0.0 | +2.75% | $+1.20 |
| 2026-11-19T17:39 | PROMUSDT | surge | TIME | 24.0 | -0.63% | $-0.27 |
| 2026-11-19T17:23 | PYTHUSDT | surge | STOP | 9.2 | -3.25% | $-1.48 |
| 2026-11-19T16:19 | USTCUSDT | surge | TARGET | 0.5 | +2.75% | $+1.20 |
| 2026-11-19T16:03 | ZILUSDT | bottom | STOP | 7.0 | -3.25% | $-1.49 |
| 2026-11-19T15:47 | TSMBUSDT | surge | STOP | 0.5 | -3.25% | $-1.33 |
| 2026-11-19T15:47 | DRAMBUSDT | surge | STOP | 7.2 | -3.25% | $-1.33 |
| 2026-11-19T15:31 | PEPEUSDT | surge | STOP | 0.8 | -3.25% | $-1.46 |
| 2026-11-19T15:31 | AMDBUSDT | surge | STOP | 8.0 | -3.25% | $-1.46 |
| 2026-11-19T15:00 | CHIPUSDT | surge | STOP | 1.2 | -3.25% | $-1.37 |
| 2026-11-19T14:44 | NVDABUSDT | bottom | TARGET | 21.5 | +2.75% | $+1.20 |
| 2026-11-19T13:40 | WCTUSDT | surge | STOP | 18.8 | -3.25% | $-1.42 |
| 2026-11-19T09:36 | STRKUSDT | surge | TARGET | 0.5 | +2.75% | $+1.26 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-19T04:30 | BNCBUSDT | surge | 3.52 | 3.46 | -1.70% |
| 2026-11-19T09:36 | RWUSDUSDT | bottom | 0.9999 | 1 | +0.01% |
| 2026-11-19T15:31 | BABABUSDT | surge | 87.31 | 84.92 | -2.74% |
| 2026-11-19T15:47 | AAVEUSDT | bottom | 104.48 | 104.97 | +0.47% |
| 2026-11-19T16:03 | STRKUSDT | bottom | 0.0318 | 0.03149 | -0.97% |
| 2026-11-19T18:11 | ERAUSDT | surge | 0.0736 | 0.0725 | -1.49% |
| 2026-11-19T18:43 | KATUSDT | surge | 0.00319 | 0.00319 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
