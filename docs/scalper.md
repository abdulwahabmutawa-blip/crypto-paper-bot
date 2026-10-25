# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-25T03:57:20+00:00 · runs 4301 · equity **$646.17** (-35.38%) · cash $0.00 · open 10/10 · round trips 1551

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-356.75 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1355 | 49% | -0.26% | 47% | 46% | 7% |
| bottom | 196 | 43% | -0.46% | 38% | 44% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-25T01:55 | ZBTUSDT | bottom | STOP | 1.2 | -3.25% | $-1.96 |
| 2026-10-25T00:27 | SAHARAUSDT | surge | STOP | 0.5 | -3.25% | $-2.02 |
| 2026-10-25T00:27 | TREEUSDT | bottom | STOP | 0.8 | -3.25% | $-2.02 |
| 2026-10-24T23:22 | SNDKBUSDT | bottom | TIME | 24.0 | -0.14% | $-0.08 |
| 2026-10-24T23:22 | CRCLBUSDT | bottom | TIME | 24.0 | -0.13% | $-0.08 |
| 2026-10-24T21:29 | CVXUSDT | surge | TARGET | 0.8 | +2.75% | $+1.73 |
| 2026-10-24T17:43 | ZBTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.72 |
| 2026-10-24T16:15 | PARTIUSDT | surge | STOP | 8.8 | -3.25% | $-2.10 |
| 2026-10-24T15:39 | OPENUSDT | surge | STOP | 0.2 | -3.25% | $-2.06 |
| 2026-10-24T15:39 | LTCUSDT | bottom | STOP | 16.2 | -3.25% | $-1.99 |
| 2026-10-24T14:28 | MIRAUSDT | surge | STOP | 4.0 | -3.25% | $-2.19 |
| 2026-10-24T14:28 | MSTRBUSDT | surge | STOP | 22.8 | -3.25% | $-2.05 |
| 2026-10-24T13:47 | SAHARAUSDT | surge | STOP | 3.2 | -3.25% | $-2.19 |
| 2026-10-24T13:12 | WCTUSDT | surge | STOP | 0.0 | -3.25% | $-2.08 |
| 2026-10-24T12:55 | WCTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.79 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-24T16:50 | AIUSDT | bottom | 0.0193 | 0.0195 | +1.04% |
| 2026-10-24T19:52 | SOXLBUSDT | surge | 84.51 | 85.26 | +0.89% |
| 2026-10-24T19:52 | BNCBUSDT | surge | 5.44 | 5.6 | +2.94% |
| 2026-10-24T21:45 | ORCAUSDT | surge | 1.791 | 1.784 | -0.39% |
| 2026-10-24T22:02 | CVXUSDT | surge | 2.51 | 2.511 | +0.04% |
| 2026-10-24T23:22 | STRKUSDT | bottom | 0.0465 | 0.04669 | +0.41% |
| 2026-10-24T23:55 | CHIPUSDT | surge | 0.04556 | 0.04484 | -1.58% |
| 2026-10-25T01:00 | NILUSDT | surge | 0.08692 | 0.08825 | +1.53% |
| 2026-10-25T01:55 | ASTERUSDT | surge | 0.712 | 0.7108 | -0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
