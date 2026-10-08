# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T14:48:05+00:00 · runs 2867 · equity **$793.93** (-20.61%) · cash $0.00 · open 10/10 · round trips 1073

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-204.42 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 938 | 51% | -0.17% | 48% | 45% | 7% |
| bottom | 135 | 44% | -0.46% | 39% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-08T14:29 | PYTHUSDT | surge | TARGET | 5.2 | +2.75% | $+2.14 |
| 2026-10-08T14:29 | ATOMUSDT | surge | TARGET | 6.5 | +2.75% | $+2.22 |
| 2026-10-08T14:12 | TIAUSDT | surge | TARGET | 8.2 | +2.75% | $+2.14 |
| 2026-10-08T13:54 | MSTRBUSDT | bottom | STOP | 11.5 | -3.25% | $-2.58 |
| 2026-10-08T13:20 | ONDOUSDT | surge | TARGET | 4.0 | +2.75% | $+2.14 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T04:39 | NVDABUSDT | bottom | 237.11 | 236.89 | -0.09% |
| 2026-10-08T13:03 | LPTUSDT | surge | 1.843 | 1.796 | -2.55% |
| 2026-10-08T13:03 | ARKUSDT | surge | 0.2234 | 0.2218 | -0.72% |
| 2026-10-08T13:03 | APTUSDT | surge | 0.7864 | 0.7909 | +0.57% |
| 2026-10-08T13:20 | PARTIUSDT | surge | 0.0342 | 0.0341 | -0.29% |
| 2026-10-08T13:54 | AVNTUSDT | surge | 0.135 | 0.1382 | +2.37% |
| 2026-10-08T14:12 | ENJUSDT | surge | 0.03164 | 0.03174 | +0.32% |
| 2026-10-08T14:29 | SUPERUSDT | surge | 0.2405 | 0.2389 | -0.67% |
| 2026-10-08T14:29 | ATOMUSDT | surge | 1.829 | 1.811 | -0.98% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
