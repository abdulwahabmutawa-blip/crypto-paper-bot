# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-19T09:21:49+00:00 · runs 6340 · equity **$488.81** (-51.12%) · cash $0.00 · open 10/10 · round trips 2096

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-511.79 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1806 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 290 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-19T04:30 | LUNCUSDT | surge | TARGET | 0.0 | +2.75% | $+1.28 |
| 2026-11-19T04:14 | LUNCUSDT | surge | TARGET | 0.2 | +2.75% | $+1.25 |
| 2026-11-19T03:57 | CHIPUSDT | surge | TARGET | 10.2 | +2.75% | $+1.20 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-18T17:11 | NVDABUSDT | bottom | 151.75 | 153.66 | +1.26% |
| 2026-11-18T17:27 | PROMUSDT | surge | 5.559 | 5.546 | -0.23% |
| 2026-11-18T17:43 | WCTUSDT | surge | 0.02981 | 0.02925 | -1.88% |
| 2026-11-19T04:30 | BNCBUSDT | surge | 3.52 | 3.54 | +0.57% |
| 2026-11-19T07:21 | AMDBUSDT | surge | 546.1 | 545.63 | -0.09% |
| 2026-11-19T07:55 | PYTHUSDT | surge | 0.05705 | 0.05668 | -0.65% |
| 2026-11-19T08:29 | DRAMBUSDT | surge | 40.76 | 40.8 | +0.10% |
| 2026-11-19T08:46 | STRKUSDT | surge | 0.0345 | 0.0355 | +2.90% |
| 2026-11-19T08:46 | ZILUSDT | bottom | 0.000965 | 0.000958 | -0.73% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
