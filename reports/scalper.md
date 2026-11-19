# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-19T14:45:37+00:00 · runs 6349 · equity **$488.96** (-51.10%) · cash $0.00 · open 10/10 · round trips 2099

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-510.74 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1808 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 291 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-19T07:04 | LUNAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.28 |
| 2026-11-19T06:48 | ZKPUSDT | bottom | STOP | 2.8 | -3.25% | $-1.47 |
| 2026-11-19T06:31 | CHIPUSDT | surge | TARGET | 2.5 | +2.75% | $+1.25 |
| 2026-11-19T06:14 | MEGAUSDT | surge | STOP | 2.0 | -3.25% | $-1.47 |
| 2026-11-19T05:57 | ZILUSDT | bottom | STOP | 1.8 | -3.25% | $-1.47 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-18T17:27 | PROMUSDT | surge | 5.559 | 5.549 | -0.18% |
| 2026-11-19T04:30 | BNCBUSDT | surge | 3.52 | 3.58 | +1.70% |
| 2026-11-19T07:21 | AMDBUSDT | surge | 546.1 | 549.76 | +0.67% |
| 2026-11-19T07:55 | PYTHUSDT | surge | 0.05705 | 0.05691 | -0.25% |
| 2026-11-19T08:29 | DRAMBUSDT | surge | 40.76 | 41.2 | +1.08% |
| 2026-11-19T08:46 | ZILUSDT | bottom | 0.000965 | 0.000955 | -1.04% |
| 2026-11-19T09:36 | RWUSDUSDT | bottom | 0.9999 | 1.0001 | +0.02% |
| 2026-11-19T13:40 | CHIPUSDT | surge | 0.03196 | 0.03114 | -2.57% |
| 2026-11-19T14:44 | PEPEUSDT | surge | 3.94e-06 | 3.93e-06 | -0.25% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
