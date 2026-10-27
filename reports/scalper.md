# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-27T13:46:17+00:00 · runs 4509 · equity **$624.68** (-37.53%) · cash $0.00 · open 10/10 · round trips 1614

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-379.08 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1406 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 208 | 44% | -0.45% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-27T13:44 | AIUSDT | surge | TIME | 24.0 | +0.26% | $+0.16 |
| 2026-10-27T13:44 | CELOUSDT | surge | TIME | 24.0 | -0.31% | $-0.16 |
| 2026-10-27T13:26 | SENTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.72 |
| 2026-10-27T12:15 | HAEDALUSDT | surge | TARGET | 0.5 | +2.75% | $+1.67 |
| 2026-10-27T11:22 | ZROUSDT | bottom | TARGET | 7.0 | +2.75% | $+1.61 |
| 2026-10-27T11:22 | BEBUSDT | surge | TARGET | 18.2 | +2.75% | $+1.64 |
| 2026-10-27T04:06 | IOSTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.57 |
| 2026-10-27T03:48 | CFGUSDT | surge | TIME | 24.0 | -3.05% | $-1.80 |
| 2026-10-27T03:14 | KORUBUSDT | surge | STOP | 0.8 | -3.25% | $-1.92 |
| 2026-10-27T02:06 | BNBUSDT | bottom | TIME | 24.0 | +0.91% | $+0.53 |
| 2026-10-27T01:31 | PHAUSDT | surge | STOP | 15.0 | -3.25% | $-1.95 |
| 2026-10-27T00:23 | SKHYBUSDT | surge | TARGET | 22.5 | +2.75% | $+1.68 |
| 2026-10-26T21:45 | HAEDALUSDT | surge | TARGET | 0.0 | +2.75% | $+1.62 |
| 2026-10-26T21:28 | CRVUSDT | surge | STOP | 11.2 | -3.25% | $-1.98 |
| 2026-10-26T16:54 | MUBARAKUSDT | surge | STOP | 17.8 | -3.25% | $-2.00 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-26T14:52 | TSLABUSDT | surge | 395.32 | 403.35 | +2.03% |
| 2026-10-26T21:45 | RWUSDUSDT | bottom | 0.9998 | 0.9998 | +0.00% |
| 2026-10-27T00:23 | TQQQBUSDT | surge | 69.3 | 70.07 | +1.11% |
| 2026-10-27T01:31 | SKHYBUSDT | surge | 148.19 | 145.93 | -1.53% |
| 2026-10-27T03:48 | TRXUSDT | bottom | 0.3292 | 0.3284 | -0.24% |
| 2026-10-27T11:22 | AMDBUSDT | surge | 541.52 | 553.16 | +2.15% |
| 2026-10-27T13:26 | REZUSDT | surge | 0.005195 | 0.005258 | +1.21% |
| 2026-10-27T13:44 | LSKUSDT | surge | 0.1694 | 0.1678 | -0.94% |
| 2026-10-27T13:44 | SOXLBUSDT | surge | 94.98 | 97.22 | +2.36% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
