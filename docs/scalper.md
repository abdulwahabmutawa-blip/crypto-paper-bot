# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-23T13:03:32+00:00 · runs 1575 · equity **$957.91** (-4.21%) · cash $0.00 · open 10/10 · round trips 564

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean -0.05%/trade · realized $-36.32 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 471 | 55% | +0.03% | 51% | 42% | 8% |
| bottom | 93 | 43% | -0.48% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-23T13:02 | ICPUSDT | surge | STOP | 0.5 | -3.25% | $-3.22 |
| 2026-09-23T13:02 | SPCXBUSDT | bottom | TIME | 24.0 | +0.77% | $+0.78 |
| 2026-09-23T12:29 | 0GUSDT | surge | STOP | 0.8 | -3.25% | $-3.33 |
| 2026-09-23T11:48 | PEOPLEUSDT | surge | STOP | 13.8 | -3.25% | $-3.12 |
| 2026-09-23T11:31 | BBUSDT | surge | STOP | 2.2 | -3.25% | $-3.44 |
| 2026-09-23T09:09 | CAKEUSDT | surge | STOP | 4.8 | -3.25% | $-3.56 |
| 2026-09-23T04:10 | TIAUSDT | surge | TARGET | 2.2 | +2.75% | $+2.93 |
| 2026-09-23T01:40 | ENSUSDT | surge | TARGET | 0.2 | +2.75% | $+2.85 |
| 2026-09-23T01:07 | PLUMEUSDT | surge | TARGET | 3.2 | +2.75% | $+2.77 |
| 2026-09-22T23:36 | ONDOUSDT | bottom | TARGET | 10.5 | +2.75% | $+2.78 |
| 2026-09-22T23:19 | TRBUSDT | surge | TARGET | 5.5 | +2.75% | $+2.57 |
| 2026-09-22T21:52 | QNTUSDT | surge | TARGET | 5.8 | +2.75% | $+2.57 |
| 2026-09-22T21:35 | ETCUSDT | surge | TARGET | 4.5 | +2.75% | $+2.70 |
| 2026-09-22T18:18 | KORUBUSDT | surge | TARGET | 2.0 | +2.75% | $+2.63 |
| 2026-09-22T17:43 | QQQBUSDT | surge | TIME | 24.0 | +0.62% | $+0.58 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-22T14:44 | SKHYBUSDT | surge | 194.89 | 190.3 | -2.36% |
| 2026-09-22T15:02 | SNDKBUSDT | surge | 1858.77 | 1873.25 | +0.78% |
| 2026-09-22T15:56 | MUBUSDT | surge | 1074.98 | 1086.95 | +1.11% |
| 2026-09-22T18:18 | SOXLBUSDT | surge | 149.09 | 146.68 | -1.62% |
| 2026-09-22T23:19 | LUNCUSDT | surge | 5.67e-05 | 5.586e-05 | -1.48% |
| 2026-09-22T23:36 | LUNAUSDT | surge | 0.0565 | 0.0558 | -1.24% |
| 2026-09-23T11:48 | PROVEUSDT | surge | 0.2371 | 0.2338 | -1.39% |
| 2026-09-23T13:02 | COTIUSDT | surge | 0.01701 | 0.01715 | +0.82% |
| 2026-09-23T13:02 | SKYUSDT | surge | 0.07419 | 0.07386 | -0.44% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
