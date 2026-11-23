# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T09:50:12+00:00 · runs 6638 · equity **$483.71** (-51.63%) · cash $0.00 · open 10/10 · round trips 2155

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-518.83 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1855 | 48% | -0.32% | 45% | 48% | 7% |
| bottom | 300 | 43% | -0.46% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-23T09:14 | NVDABUSDT | surge | TARGET | 22.8 | +2.75% | $+1.20 |
| 2026-11-23T09:14 | RENDERUSDT | surge | TIME | 24.0 | +0.27% | $+0.12 |
| 2026-11-23T08:24 | BONKUSDT | surge | TARGET | 22.0 | +2.75% | $+1.21 |
| 2026-11-23T06:26 | BMTUSDT | surge | STOP | 3.5 | -3.25% | $-1.37 |
| 2026-11-23T02:43 | SOXLBUSDT | surge | STOP | 0.8 | -3.25% | $-1.42 |
| 2026-11-23T02:26 | INITUSDT | bottom | STOP | 9.0 | -3.25% | $-1.45 |
| 2026-11-23T01:53 | LISTAUSDT | surge | STOP | 0.0 | -3.25% | $-1.43 |
| 2026-11-23T01:53 | KITEUSDT | surge | TARGET | 17.2 | +2.75% | $+1.20 |
| 2026-11-23T01:36 | NBISBUSDT | surge | STOP | 1.0 | -3.25% | $-1.48 |
| 2026-11-23T00:28 | LISTAUSDT | surge | TARGET | 1.2 | +2.75% | $+1.22 |
| 2026-11-22T23:04 | SOXLBUSDT | surge | TARGET | 14.0 | +2.75% | $+1.18 |
| 2026-11-22T17:03 | KORUBUSDT | surge | TARGET | 7.0 | +2.75% | $+1.23 |
| 2026-11-22T17:03 | ETCUSDT | surge | TIME | 24.0 | +1.57% | $+0.67 |
| 2026-11-22T11:44 | ARUSDT | surge | TARGET | 2.8 | +2.75% | $+1.20 |
| 2026-11-22T10:19 | PYTHUSDT | surge | TARGET | 17.5 | +2.75% | $+1.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-22T10:02 | EWYBUSDT | surge | 127.63 | 128.87 | +0.97% |
| 2026-11-22T11:44 | TSLABUSDT | surge | 359.44 | 362.22 | +0.77% |
| 2026-11-22T17:03 | CAKEUSDT | surge | 1.524 | 1.538 | +0.92% |
| 2026-11-23T01:53 | SKHYBUSDT | surge | 111.81 | 113.5 | +1.51% |
| 2026-11-23T02:26 | XLMUSDT | bottom | 0.1263 | 0.1282 | +1.50% |
| 2026-11-23T06:26 | COINBUSDT | surge | 107.54 | 107.42 | -0.11% |
| 2026-11-23T08:24 | BLURUSDT | surge | 0.008 | 0.00801 | +0.12% |
| 2026-11-23T09:14 | AMDBUSDT | surge | 451.83 | 450.44 | -0.31% |
| 2026-11-23T09:14 | DRAMBUSDT | surge | 36.42 | 36.56 | +0.38% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
