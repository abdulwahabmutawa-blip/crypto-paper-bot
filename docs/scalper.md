# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-02T17:01:07+00:00 · runs 5032 · equity **$570.57** (-42.94%) · cash $0.00 · open 10/10 · round trips 1758

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-426.78 · worst day $-50.94 · trades/day 29.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1529 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 229 | 43% | -0.50% | 37% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-02T16:59 | MEGAUSDT | surge | STOP | 0.8 | -3.25% | $-1.60 |
| 2026-11-02T16:59 | MITOUSDT | surge | TARGET | 2.2 | +2.75% | $+1.47 |
| 2026-11-02T16:59 | KORUBUSDT | surge | STOP | 8.0 | -3.25% | $-1.86 |
| 2026-11-02T16:59 | CRCLBUSDT | surge | STOP | 9.5 | -3.25% | $-2.05 |
| 2026-11-02T16:59 | SKHYBUSDT | surge | STOP | 15.2 | -3.25% | $-1.81 |
| 2026-11-02T16:59 | CELOUSDT | bottom | STOP | 22.8 | -3.25% | $-1.83 |
| 2026-11-02T12:26 | SOXLBUSDT | surge | STOP | 7.2 | -3.25% | $-1.66 |
| 2026-11-02T10:13 | ONDOUSDT | bottom | STOP | 17.2 | -3.25% | $-1.79 |
| 2026-11-02T07:11 | NIGHTUSDT | surge | STOP | 14.2 | -3.25% | $-1.65 |
| 2026-11-02T06:35 | INTCBUSDT | surge | TIME | 24.0 | +0.51% | $+0.29 |
| 2026-11-02T05:10 | RADUSDT | bottom | TIME | 24.0 | -0.66% | $-0.42 |
| 2026-11-02T04:53 | TRUMPUSDT | surge | STOP | 5.2 | -3.25% | $-1.71 |
| 2026-11-02T01:32 | INTWBUSDT | surge | TARGET | 19.2 | +2.75% | $+1.55 |
| 2026-11-02T01:15 | KORUBUSDT | surge | TARGET | 0.8 | +2.75% | $+1.49 |
| 2026-11-02T00:19 | MITOUSDT | surge | TARGET | 2.5 | +2.75% | $+1.45 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-01T23:29 | SEIUSDT | surge | 0.04825 | 0.0475 | -1.55% |
| 2026-11-02T01:32 | DRAMBUSDT | surge | 49.57 | 48.3 | -2.56% |
| 2026-11-02T07:11 | PROMUSDT | bottom | 5.468 | 5.424 | -0.80% |
| 2026-11-02T16:59 | TSLABUSDT | surge | 410.69 | 411.76 | +0.26% |
| 2026-11-02T16:59 | BABABUSDT | surge | 103.32 | 103.46 | +0.14% |
| 2026-11-02T16:59 | MSTRBUSDT | surge | 136.3 | 135.02 | -0.94% |
| 2026-11-02T16:59 | SPCXBUSDT | surge | 140.88 | 141 | +0.09% |
| 2026-11-02T16:59 | COWUSDT | surge | 0.1187 | 0.1194 | +0.59% |
| 2026-11-02T16:59 | MUBUSDT | bottom | 861.83 | 861.32 | -0.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
