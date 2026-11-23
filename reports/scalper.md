# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-23T13:06:31+00:00 · runs 6643 · equity **$484.03** (-51.60%) · cash $0.00 · open 10/10 · round trips 2160

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-517.24 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1860 | 48% | -0.32% | 45% | 47% | 7% |
| bottom | 300 | 43% | -0.46% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-23T13:05 | AMDBUSDT | surge | STOP | 3.8 | -3.25% | $-1.44 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-22T17:03 | CAKEUSDT | surge | 1.524 | 1.541 | +1.12% |
| 2026-11-23T01:53 | SKHYBUSDT | surge | 111.81 | 112.03 | +0.20% |
| 2026-11-23T02:26 | XLMUSDT | bottom | 0.1263 | 0.1285 | +1.74% |
| 2026-11-23T06:26 | COINBUSDT | surge | 107.54 | 106.63 | -0.85% |
| 2026-11-23T09:14 | DRAMBUSDT | surge | 36.42 | 36.24 | -0.49% |
| 2026-11-23T12:16 | LUNCUSDT | surge | 4.234e-05 | 4.18e-05 | -1.28% |
| 2026-11-23T12:16 | GOOGLBUSDT | surge | 279.77 | 280.04 | +0.10% |
| 2026-11-23T12:49 | ALGOUSDT | surge | 0.0828 | 0.0843 | +1.81% |
| 2026-11-23T13:05 | QNTUSDT | surge | 157.17 | 157.88 | +0.45% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
