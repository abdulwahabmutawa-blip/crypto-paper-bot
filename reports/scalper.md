# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-03T06:01:15+00:00 · runs 2414 · equity **$868.13** (-13.19%) · cash $0.00 · open 10/10 · round trips 919

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-131.76 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 795 | 52% | -0.10% | 49% | 44% | 7% |
| bottom | 124 | 45% | -0.42% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-02T16:08 | BATUSDT | surge | STOP | 0.8 | -3.25% | $-2.70 |
| 2026-10-02T15:52 | SKYUSDT | surge | TARGET | 2.2 | +2.75% | $+2.62 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-02T13:07 | DODOUSDT | surge | 0.01872 | 0.01837 | -1.87% |
| 2026-10-02T15:29 | TSLABUSDT | surge | 371.22 | 370.69 | -0.14% |
| 2026-10-02T15:52 | SPCXBUSDT | surge | 157.12 | 158.89 | +1.13% |
| 2026-10-02T17:48 | CRCLBUSDT | bottom | 80.95 | 81.66 | +0.88% |
| 2026-10-02T18:54 | BNBUSDT | bottom | 761.25 | 767.02 | +0.76% |
| 2026-10-03T01:28 | SNDKBUSDT | bottom | 1718.8 | 1717.53 | -0.07% |
| 2026-10-03T03:31 | AXSUSDT | surge | 1.279 | 1.264 | -1.17% |
| 2026-10-03T03:31 | INJUSDT | surge | 7.685 | 7.731 | +0.60% |
| 2026-10-03T05:43 | LPTUSDT | surge | 1.797 | 1.792 | -0.28% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
