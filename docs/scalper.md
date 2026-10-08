# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T13:05:23+00:00 · runs 2861 · equity **$789.79** (-21.02%) · cash $0.00 · open 10/10 · round trips 1068

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-210.48 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 934 | 50% | -0.18% | 48% | 45% | 7% |
| bottom | 134 | 45% | -0.44% | 39% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-08T13:03 | LPTUSDT | surge | TARGET | 0.5 | +2.75% | $+2.11 |
| 2026-10-08T13:03 | ENSUSDT | surge | STOP | 2.2 | -3.25% | $-2.55 |
| 2026-10-08T13:03 | LINKUSDT | bottom | STOP | 11.0 | -3.25% | $-2.57 |
| 2026-10-08T12:29 | CRVUSDT | surge | STOP | 9.2 | -3.25% | $-2.58 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T02:08 | MSTRBUSDT | bottom | 153.72 | 149.83 | -2.53% |
| 2026-10-08T04:39 | NVDABUSDT | bottom | 237.11 | 235.43 | -0.71% |
| 2026-10-08T05:30 | TIAUSDT | surge | 0.479 | 0.4818 | +0.58% |
| 2026-10-08T07:44 | ATOMUSDT | surge | 1.779 | 1.806 | +1.52% |
| 2026-10-08T08:49 | PYTHUSDT | surge | 0.0749 | 0.07499 | +0.12% |
| 2026-10-08T09:06 | ONDOUSDT | surge | 0.4733 | 0.4801 | +1.44% |
| 2026-10-08T13:03 | LPTUSDT | surge | 1.843 | 1.843 | +0.00% |
| 2026-10-08T13:03 | ARKUSDT | surge | 0.2234 | 0.2236 | +0.09% |
| 2026-10-08T13:03 | APTUSDT | surge | 0.7864 | 0.7851 | -0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
