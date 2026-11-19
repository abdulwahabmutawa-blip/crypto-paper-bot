# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-19T07:40:33+00:00 · runs 6334 · equity **$488.08** (-51.19%) · cash $0.00 · open 10/10 · round trips 2091

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-511.66 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1801 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 290 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-19T02:37 | ICPUSDT | bottom | TARGET | 9.2 | +2.75% | $+1.20 |
| 2026-11-19T01:01 | TLMUSDT | bottom | TARGET | 7.8 | +2.75% | $+1.20 |
| 2026-11-19T00:45 | AMDBUSDT | surge | TARGET | 7.0 | +2.75% | $+1.20 |
| 2026-11-19T00:14 | AVGOBUSDT | surge | TIME | 24.0 | +1.44% | $+0.67 |
| 2026-11-18T16:38 | ZBTUSDT | surge | STOP | 1.2 | -3.25% | $-1.40 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-18T07:30 | EWYBUSDT | surge | 138.73 | 140.18 | +1.05% |
| 2026-11-18T17:11 | NVDABUSDT | bottom | 151.75 | 153.28 | +1.01% |
| 2026-11-18T17:27 | PROMUSDT | surge | 5.559 | 5.566 | +0.13% |
| 2026-11-18T17:43 | WCTUSDT | surge | 0.02981 | 0.02931 | -1.68% |
| 2026-11-19T04:30 | BNCBUSDT | surge | 3.52 | 3.51 | -0.28% |
| 2026-11-19T06:14 | KORUBUSDT | surge | 7.03 | 7.16 | +1.85% |
| 2026-11-19T07:04 | LUNAUSDT | surge | 0.0355 | 0.035 | -1.41% |
| 2026-11-19T07:21 | AMDBUSDT | surge | 546.1 | 546.39 | +0.05% |
| 2026-11-19T07:38 | CHIPUSDT | surge | 0.03169 | 0.03131 | -1.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
