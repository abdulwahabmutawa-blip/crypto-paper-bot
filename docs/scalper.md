# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-19T17:08:34+00:00 · runs 6358 · equity **$476.66** (-52.33%) · cash $43.33 · open 9/10 · round trips 2106

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-517.99 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1814 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 292 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-19T08:46 | STRKUSDT | surge | TARGET | 0.8 | +2.75% | $+1.25 |
| 2026-11-19T08:46 | KORUBUSDT | surge | TARGET | 2.5 | +2.75% | $+1.21 |
| 2026-11-19T08:29 | CHIPUSDT | surge | STOP | 0.8 | -3.25% | $-1.38 |
| 2026-11-19T07:55 | LUNAUSDT | surge | STOP | 0.5 | -3.25% | $-1.55 |
| 2026-11-19T07:55 | EWYBUSDT | surge | TIME | 24.0 | +0.78% | $+0.35 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-18T17:27 | PROMUSDT | surge | 5.559 | 5.513 | -0.83% |
| 2026-11-19T04:30 | BNCBUSDT | surge | 3.52 | 3.44 | -2.27% |
| 2026-11-19T07:55 | PYTHUSDT | surge | 0.05705 | 0.05555 | -2.63% |
| 2026-11-19T09:36 | RWUSDUSDT | bottom | 0.9999 | 1 | +0.01% |
| 2026-11-19T15:31 | BABABUSDT | surge | 87.31 | 85.75 | -1.79% |
| 2026-11-19T15:47 | AAVEUSDT | bottom | 104.48 | 103.66 | -0.78% |
| 2026-11-19T16:03 | STRKUSDT | bottom | 0.0318 | 0.03134 | -1.45% |
| 2026-11-19T16:51 | USTCUSDT | surge | 0.00427 | 0.00417 | -2.34% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
