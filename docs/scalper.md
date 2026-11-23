# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T12:50:39+00:00 · runs 6642 · equity **$482.31** (-51.77%) · cash $0.00 · open 10/10 · round trips 2159

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-515.80 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1859 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 300 | 43% | -0.46% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-23T12:49 | LSKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.24 |
| 2026-11-23T12:16 | BLURUSDT | surge | TARGET | 1.8 | +2.75% | $+1.24 |
| 2026-11-23T12:16 | TSLABUSDT | surge | TIME | 24.0 | +0.29% | $+0.13 |
| 2026-11-23T12:16 | EWYBUSDT | surge | TIME | 24.0 | +0.94% | $+0.41 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-22T17:03 | CAKEUSDT | surge | 1.524 | 1.539 | +0.98% |
| 2026-11-23T01:53 | SKHYBUSDT | surge | 111.81 | 110.87 | -0.84% |
| 2026-11-23T02:26 | XLMUSDT | bottom | 0.1263 | 0.1281 | +1.43% |
| 2026-11-23T06:26 | COINBUSDT | surge | 107.54 | 106.43 | -1.03% |
| 2026-11-23T09:14 | AMDBUSDT | surge | 451.83 | 439.89 | -2.64% |
| 2026-11-23T09:14 | DRAMBUSDT | surge | 36.42 | 35.92 | -1.37% |
| 2026-11-23T12:16 | LUNCUSDT | surge | 4.234e-05 | 4.217e-05 | -0.40% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 278.24 | -0.55% |
| 2026-11-23T12:49 | ALGOUSDT | surge | 0.0828 | 0.0829 | +0.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
