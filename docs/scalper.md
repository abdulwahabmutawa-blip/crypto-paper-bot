# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T13:56:46+00:00 · runs 2864 · equity **$791.62** (-20.84%) · cash $0.00 · open 10/10 · round trips 1070

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-210.92 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 935 | 50% | -0.18% | 48% | 45% | 7% |
| bottom | 135 | 44% | -0.46% | 39% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-08T06:39 | LDOUSDT | surge | STOP | 3.0 | -3.25% | $-2.58 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T04:39 | NVDABUSDT | bottom | 237.11 | 234.11 | -1.27% |
| 2026-10-08T05:30 | TIAUSDT | surge | 0.479 | 0.4935 | +3.03% |
| 2026-10-08T07:44 | ATOMUSDT | surge | 1.779 | 1.819 | +2.25% |
| 2026-10-08T08:49 | PYTHUSDT | surge | 0.0749 | 0.0761 | +1.60% |
| 2026-10-08T13:03 | LPTUSDT | surge | 1.843 | 1.811 | -1.74% |
| 2026-10-08T13:03 | ARKUSDT | surge | 0.2234 | 0.224 | +0.27% |
| 2026-10-08T13:03 | APTUSDT | surge | 0.7864 | 0.7878 | +0.18% |
| 2026-10-08T13:20 | PARTIUSDT | surge | 0.0342 | 0.0337 | -1.46% |
| 2026-10-08T13:54 | AVNTUSDT | surge | 0.135 | 0.1355 | +0.37% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
