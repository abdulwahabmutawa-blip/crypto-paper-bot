# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-26T07:52:54+00:00 · runs 6797 · equity **$489.07** (-51.09%) · cash $0.00 · open 10/10 · round trips 2225

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-509.63 · worst day $-50.94 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1911 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 314 | 43% | -0.50% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-26T02:00 | ATUSDT | surge | STOP | 0.5 | -3.25% | $-1.53 |
| 2026-11-26T01:25 | ATUSDT | surge | TARGET | 0.8 | +2.75% | $+1.26 |
| 2026-11-26T00:33 | XLMUSDT | surge | TARGET | 5.8 | +2.75% | $+1.22 |
| 2026-11-26T00:33 | WLDUSDT | surge | TARGET | 6.2 | +2.75% | $+1.22 |
| 2026-11-26T00:16 | TIAUSDT | surge | TARGET | 1.2 | +2.75% | $+1.23 |
| 2026-11-26T00:16 | DASHUSDT | surge | TARGET | 5.0 | +2.75% | $+1.22 |
| 2026-11-26T00:16 | BCHUSDT | surge | TARGET | 5.8 | +2.75% | $+1.22 |
| 2026-11-25T22:49 | PUMPUSDT | surge | TARGET | 1.5 | +2.75% | $+1.22 |
| 2026-11-25T22:49 | XPLUSDT | surge | TARGET | 2.0 | +2.75% | $+1.18 |
| 2026-11-25T19:14 | SUPERUSDT | surge | TARGET | 1.5 | +2.75% | $+1.18 |
| 2026-11-25T19:14 | GOOGLBUSDT | bottom | TARGET | 2.8 | +2.75% | $+1.19 |
| 2026-11-25T18:38 | QQQBUSDT | bottom | TARGET | 2.0 | +2.75% | $+1.19 |
| 2026-11-25T18:38 | NVDABUSDT | bottom | TARGET | 2.0 | +2.75% | $+1.19 |
| 2026-11-25T18:21 | WLFIUSDT | surge | TARGET | 1.8 | +2.75% | $+1.19 |
| 2026-11-25T18:03 | 牛来USDT | surge | TARGET | 1.5 | +2.75% | $+1.19 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-25T16:35 | SENTUSDT | surge | 0.02055 | 0.02063 | +0.39% |
| 2026-11-25T17:45 | STXUSDT | surge | 0.2623 | 0.2641 | +0.69% |
| 2026-11-25T19:14 | STRKUSDT | surge | 0.03085 | 0.03062 | -0.75% |
| 2026-11-25T22:49 | SUPERUSDT | surge | 0.1173 | 0.1187 | +1.19% |
| 2026-11-26T00:16 | RAYUSDT | surge | 1.3357 | 1.3203 | -1.15% |
| 2026-11-26T00:16 | NEARUSDT | surge | 3.094 | 3.059 | -1.13% |
| 2026-11-26T00:33 | EWYBUSDT | surge | 131.04 | 130.26 | -0.60% |
| 2026-11-26T00:33 | SKHYBUSDT | surge | 114.1 | 112.21 | -1.66% |
| 2026-11-26T02:00 | PUMPUSDT | surge | 0.002634 | 0.002639 | +0.19% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
