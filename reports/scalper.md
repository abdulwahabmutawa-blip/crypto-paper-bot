# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-19T15:49:05+00:00 · runs 6353 · equity **$479.15** (-52.09%) · cash $39.60 · open 9/10 · round trips 2104

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-517.70 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1813 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 291 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-19T07:38 | FUSDT | surge | STOP | 0.5 | -3.25% | $-1.42 |
| 2026-11-19T07:21 | ETHFIUSDT | surge | TARGET | 1.0 | +2.75% | $+1.21 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-18T17:27 | PROMUSDT | surge | 5.559 | 5.494 | -1.17% |
| 2026-11-19T04:30 | BNCBUSDT | surge | 3.52 | 3.52 | +0.00% |
| 2026-11-19T07:55 | PYTHUSDT | surge | 0.05705 | 0.05596 | -1.91% |
| 2026-11-19T08:46 | ZILUSDT | bottom | 0.000965 | 0.000935 | -3.11% |
| 2026-11-19T09:36 | RWUSDUSDT | bottom | 0.9999 | 1 | +0.01% |
| 2026-11-19T15:31 | BABABUSDT | surge | 87.31 | 86.91 | -0.46% |
| 2026-11-19T15:31 | USTCUSDT | surge | 0.00428 | 0.00425 | -0.70% |
| 2026-11-19T15:47 | AAVEUSDT | bottom | 104.48 | 104.87 | +0.37% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
