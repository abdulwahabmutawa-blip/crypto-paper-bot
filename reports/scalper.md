# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-26T15:03:28+00:00 · runs 6807 · equity **$484.85** (-51.51%) · cash $0.00 · open 10/10 · round trips 2227

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-509.92 · worst day $-50.94 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1913 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 314 | 43% | -0.50% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-26T15:01 | SKHYBUSDT | surge | STOP | 10.0 | -3.25% | $-1.48 |
| 2026-11-26T15:01 | SENTUSDT | surge | TARGET | 22.2 | +2.75% | $+1.19 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-25T17:45 | STXUSDT | surge | 0.2623 | 0.2632 | +0.34% |
| 2026-11-25T19:14 | STRKUSDT | surge | 0.03085 | 0.03027 | -1.88% |
| 2026-11-25T22:49 | SUPERUSDT | surge | 0.1173 | 0.1177 | +0.34% |
| 2026-11-26T00:16 | RAYUSDT | surge | 1.3357 | 1.2888 | -3.51% |
| 2026-11-26T00:16 | NEARUSDT | surge | 3.094 | 3.028 | -2.13% |
| 2026-11-26T00:33 | EWYBUSDT | surge | 131.04 | 129.34 | -1.30% |
| 2026-11-26T02:00 | PUMPUSDT | surge | 0.002634 | 0.002563 | -2.70% |
| 2026-11-26T15:01 | SAGAUSDT | surge | 0.01438 | 0.0143 | -0.56% |
| 2026-11-26T15:01 | SEIUSDT | surge | 0.03709 | 0.03704 | -0.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
