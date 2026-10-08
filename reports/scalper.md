# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T11:56:44+00:00 · runs 2857 · equity **$795.69** (-20.43%) · cash $0.00 · open 10/10 · round trips 1064

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-204.89 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 931 | 50% | -0.18% | 48% | 45% | 7% |
| bottom | 133 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-08T10:43 | BOMEUSDT | surge | TARGET | 3.0 | +2.75% | $+2.10 |
| 2026-10-08T08:49 | ERAUSDT | surge | STOP | 0.5 | -3.25% | $-2.44 |
| 2026-10-08T08:49 | ALGOUSDT | surge | TARGET | 1.0 | +2.75% | $+2.22 |
| 2026-10-08T08:01 | CVXUSDT | surge | STOP | 2.2 | -3.25% | $-2.53 |
| 2026-10-08T07:44 | PYTHUSDT | surge | TARGET | 1.8 | +2.75% | $+2.14 |
| 2026-10-08T07:44 | JTOUSDT | surge | TARGET | 4.0 | +2.75% | $+2.18 |
| 2026-10-08T07:28 | ERAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.04 |
| 2026-10-08T07:12 | WUSDT | surge | STOP | 0.0 | -3.25% | $-2.49 |
| 2026-10-08T06:39 | LDOUSDT | surge | STOP | 3.0 | -3.25% | $-2.58 |
| 2026-10-08T05:13 | CHIPUSDT | surge | STOP | 0.2 | -3.25% | $-2.55 |
| 2026-10-08T04:39 | ENAUSDT | bottom | STOP | 1.5 | -3.25% | $-2.58 |
| 2026-10-08T04:39 | BOMEUSDT | surge | STOP | 2.0 | -3.25% | $-2.58 |
| 2026-10-08T03:49 | CHIPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.18 |
| 2026-10-08T02:58 | OGNUSDT | surge | STOP | 0.8 | -3.25% | $-2.58 |
| 2026-10-08T02:58 | SPCXBUSDT | bottom | TIME | 24.0 | -0.34% | $-0.28 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T01:51 | LINKUSDT | bottom | 13.313 | 13.034 | -2.10% |
| 2026-10-08T02:08 | MSTRBUSDT | bottom | 153.72 | 150.95 | -1.80% |
| 2026-10-08T02:58 | CRVUSDT | surge | 0.3923 | 0.3859 | -1.63% |
| 2026-10-08T04:39 | NVDABUSDT | bottom | 237.11 | 235.21 | -0.80% |
| 2026-10-08T05:30 | TIAUSDT | surge | 0.479 | 0.4882 | +1.92% |
| 2026-10-08T07:44 | ATOMUSDT | surge | 1.779 | 1.808 | +1.63% |
| 2026-10-08T08:49 | PYTHUSDT | surge | 0.0749 | 0.07673 | +2.44% |
| 2026-10-08T09:06 | ONDOUSDT | surge | 0.4733 | 0.4837 | +2.20% |
| 2026-10-08T10:43 | ENSUSDT | surge | 6.66 | 6.59 | -1.05% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
