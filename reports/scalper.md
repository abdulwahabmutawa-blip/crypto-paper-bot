# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T14:13:51+00:00 · runs 2865 · equity **$796.78** (-20.32%) · cash $0.00 · open 10/10 · round trips 1071

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-208.78 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 936 | 51% | -0.17% | 48% | 45% | 7% |
| bottom | 135 | 44% | -0.46% | 39% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-08T07:28 | ERAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.04 |
| 2026-10-08T07:12 | WUSDT | surge | STOP | 0.0 | -3.25% | $-2.49 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T04:39 | NVDABUSDT | bottom | 237.11 | 235.81 | -0.55% |
| 2026-10-08T07:44 | ATOMUSDT | surge | 1.779 | 1.829 | +2.81% |
| 2026-10-08T08:49 | PYTHUSDT | surge | 0.0749 | 0.07786 | +3.95% |
| 2026-10-08T13:03 | LPTUSDT | surge | 1.843 | 1.825 | -0.98% |
| 2026-10-08T13:03 | ARKUSDT | surge | 0.2234 | 0.2247 | +0.58% |
| 2026-10-08T13:03 | APTUSDT | surge | 0.7864 | 0.7948 | +1.07% |
| 2026-10-08T13:20 | PARTIUSDT | surge | 0.0342 | 0.0337 | -1.46% |
| 2026-10-08T13:54 | AVNTUSDT | surge | 0.135 | 0.1359 | +0.67% |
| 2026-10-08T14:12 | ENJUSDT | surge | 0.03164 | 0.03195 | +0.98% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
