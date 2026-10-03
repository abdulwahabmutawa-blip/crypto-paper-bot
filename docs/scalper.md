# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-03T11:27:28+00:00 · runs 2434 · equity **$863.40** (-13.66%) · cash $0.00 · open 10/10 · round trips 921

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-137.16 · worst day $-50.94 · trades/day 31.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 797 | 52% | -0.11% | 49% | 44% | 7% |
| bottom | 124 | 45% | -0.42% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-03T08:31 | LPTUSDT | surge | STOP | 2.8 | -3.25% | $-2.65 |
| 2026-10-03T07:54 | AXSUSDT | surge | STOP | 4.0 | -3.25% | $-2.74 |
| 2026-10-03T04:21 | PYTHUSDT | surge | STOP | 2.8 | -3.25% | $-2.74 |
| 2026-10-03T01:28 | XPLUSDT | bottom | TARGET | 6.2 | +2.75% | $+2.29 |
| 2026-10-02T20:33 | NMRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.29 |
| 2026-10-02T18:54 | PEPEUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | FETUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | VTHOUSDT | surge | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | CHIPUSDT | surge | STOP | 6.0 | -3.25% | $-2.90 |
| 2026-10-02T18:37 | DYDXUSDT | surge | STOP | 18.8 | -3.25% | $-2.82 |
| 2026-10-02T17:48 | WLDUSDT | surge | STOP | 0.8 | -3.25% | $-2.85 |
| 2026-10-02T17:48 | SKYUSDT | surge | STOP | 1.5 | -3.25% | $-2.62 |
| 2026-10-02T17:48 | CVXUSDT | surge | STOP | 11.2 | -3.25% | $-2.98 |
| 2026-10-02T17:48 | PLUMEUSDT | bottom | STOP | 16.8 | -3.25% | $-2.93 |
| 2026-10-02T16:58 | TRUMPUSDT | surge | STOP | 3.8 | -3.25% | $-2.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-02T13:07 | DODOUSDT | surge | 0.01872 | 0.01845 | -1.44% |
| 2026-10-02T15:29 | TSLABUSDT | surge | 371.22 | 370.96 | -0.07% |
| 2026-10-02T15:52 | SPCXBUSDT | surge | 157.12 | 159.05 | +1.23% |
| 2026-10-02T17:48 | CRCLBUSDT | bottom | 80.95 | 82.12 | +1.45% |
| 2026-10-02T18:54 | BNBUSDT | bottom | 761.25 | 769.17 | +1.04% |
| 2026-10-03T01:28 | SNDKBUSDT | bottom | 1718.8 | 1718.68 | -0.01% |
| 2026-10-03T03:31 | INJUSDT | surge | 7.685 | 7.587 | -1.28% |
| 2026-10-03T07:54 | SYNUSDT | surge | 0.18751 | 0.1849 | -1.39% |
| 2026-10-03T08:49 | RAYUSDT | surge | 2.021 | 2.0426 | +1.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
