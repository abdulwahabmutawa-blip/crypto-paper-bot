# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T06:57:20+00:00 · runs 2838 · equity **$785.65** (-21.44%) · cash $0.00 · open 10/10 · round trips 1056

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.21%/trade · realized $-208.10 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 923 | 50% | -0.18% | 47% | 45% | 7% |
| bottom | 133 | 45% | -0.42% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-08T06:39 | LDOUSDT | surge | STOP | 3.0 | -3.25% | $-2.58 |
| 2026-10-08T05:13 | CHIPUSDT | surge | STOP | 0.2 | -3.25% | $-2.55 |
| 2026-10-08T04:39 | ENAUSDT | bottom | STOP | 1.5 | -3.25% | $-2.58 |
| 2026-10-08T04:39 | BOMEUSDT | surge | STOP | 2.0 | -3.25% | $-2.58 |
| 2026-10-08T03:49 | CHIPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.18 |
| 2026-10-08T02:58 | OGNUSDT | surge | STOP | 0.8 | -3.25% | $-2.58 |
| 2026-10-08T02:58 | SPCXBUSDT | bottom | TIME | 24.0 | -0.34% | $-0.28 |
| 2026-10-08T02:08 | TRXUSDT | bottom | TIME | 24.0 | +0.02% | $+0.01 |
| 2026-10-07T16:14 | AVAXUSDT | bottom | TARGET | 13.2 | +2.75% | $+2.24 |
| 2026-10-07T11:46 | STXUSDT | surge | STOP | 3.8 | -3.25% | $-2.62 |
| 2026-10-07T11:46 | ARKUSDT | surge | STOP | 4.2 | -3.25% | $-2.62 |
| 2026-10-07T09:43 | PARTIUSDT | surge | STOP | 1.8 | -3.25% | $-2.62 |
| 2026-10-07T09:43 | PUMPUSDT | surge | STOP | 2.0 | -3.25% | $-2.62 |
| 2026-10-07T08:13 | SYNUSDT | surge | STOP | 0.8 | -3.25% | $-2.61 |
| 2026-10-07T07:19 | PUMPUSDT | surge | TARGET | 1.8 | +2.75% | $+2.20 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T01:51 | LINKUSDT | bottom | 13.313 | 13.131 | -1.37% |
| 2026-10-08T02:08 | MSTRBUSDT | bottom | 153.72 | 152.02 | -1.11% |
| 2026-10-08T02:58 | CRVUSDT | surge | 0.3923 | 0.3906 | -0.43% |
| 2026-10-08T03:15 | JTOUSDT | surge | 0.5609 | 0.57 | +1.62% |
| 2026-10-08T04:39 | NVDABUSDT | bottom | 237.11 | 236.2 | -0.38% |
| 2026-10-08T05:30 | CVXUSDT | surge | 2.353 | 2.329 | -1.02% |
| 2026-10-08T05:30 | TIAUSDT | surge | 0.479 | 0.4807 | +0.35% |
| 2026-10-08T05:51 | PYTHUSDT | surge | 0.07422 | 0.07418 | -0.05% |
| 2026-10-08T06:55 | WUSDT | surge | 0.01754 | 0.01654 | -5.70% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
