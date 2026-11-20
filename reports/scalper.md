# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-20T01:14:28+00:00 · runs 6379 · equity **$473.57** (-52.64%) · cash $171.89 · open 6/10 · round trips 2114

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-525.77 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1822 | 48% | -0.34% | 45% | 48% | 7% |
| bottom | 292 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-20T01:12 | ERAUSDT | surge | STOP | 6.8 | -3.25% | $-1.42 |
| 2026-11-19T21:50 | BABABUSDT | surge | STOP | 4.2 | -3.25% | $-1.41 |
| 2026-11-19T21:50 | BNCBUSDT | surge | STOP | 16.0 | -3.25% | $-1.55 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-19T09:36 | RWUSDUSDT | bottom | 0.9999 | 1 | +0.01% |
| 2026-11-19T15:47 | AAVEUSDT | bottom | 104.48 | 104.52 | +0.04% |
| 2026-11-19T16:03 | STRKUSDT | bottom | 0.0318 | 0.03185 | +0.16% |
| 2026-11-19T18:43 | KATUSDT | surge | 0.00319 | 0.00314 | -1.57% |
| 2026-11-20T00:56 | SNXUSDT | surge | 0.1669 | 0.1667 | -0.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
