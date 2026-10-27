# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-27T14:57:25+00:00 · runs 4513 · equity **$623.74** (-37.63%) · cash $0.00 · open 10/10 · round trips 1617

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-377.92 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1409 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 208 | 44% | -0.45% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-27T14:55 | REZUSDT | surge | STOP | 0.2 | -3.25% | $-2.14 |
| 2026-10-27T14:19 | REZUSDT | surge | TARGET | 0.8 | +2.75% | $+1.76 |
| 2026-10-27T14:01 | SOXLBUSDT | surge | TARGET | 0.0 | +2.75% | $+1.53 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-26T14:52 | TSLABUSDT | surge | 395.32 | 402.72 | +1.87% |
| 2026-10-26T21:45 | RWUSDUSDT | bottom | 0.9998 | 0.9998 | +0.00% |
| 2026-10-27T00:23 | TQQQBUSDT | surge | 69.3 | 70.38 | +1.56% |
| 2026-10-27T01:31 | SKHYBUSDT | surge | 148.19 | 145.71 | -1.67% |
| 2026-10-27T03:48 | TRXUSDT | bottom | 0.3292 | 0.3281 | -0.33% |
| 2026-10-27T11:22 | AMDBUSDT | surge | 541.52 | 554.39 | +2.38% |
| 2026-10-27T13:44 | LSKUSDT | surge | 0.1694 | 0.1664 | -1.77% |
| 2026-10-27T14:01 | SNDKBUSDT | surge | 1299.08 | 1303.35 | +0.33% |
| 2026-10-27T14:55 | SENTUSDT | surge | 0.02269 | 0.02272 | +0.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
