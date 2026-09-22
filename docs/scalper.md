# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-22T23:55:17+00:00 · runs 1527 · equity **$980.50** (-1.95%) · cash $0.00 · open 10/10 · round trips 555

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean -0.04%/trade · realized $-28.98 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 463 | 55% | +0.05% | 51% | 41% | 8% |
| bottom | 92 | 42% | -0.49% | 40% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-22T23:36 | ONDOUSDT | bottom | TARGET | 10.5 | +2.75% | $+2.78 |
| 2026-09-22T23:19 | TRBUSDT | surge | TARGET | 5.5 | +2.75% | $+2.57 |
| 2026-09-22T21:52 | QNTUSDT | surge | TARGET | 5.8 | +2.75% | $+2.57 |
| 2026-09-22T21:35 | ETCUSDT | surge | TARGET | 4.5 | +2.75% | $+2.70 |
| 2026-09-22T18:18 | KORUBUSDT | surge | TARGET | 2.0 | +2.75% | $+2.63 |
| 2026-09-22T17:43 | QQQBUSDT | surge | TIME | 24.0 | +0.62% | $+0.58 |
| 2026-09-22T16:49 | GIGGLEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.63 |
| 2026-09-22T16:13 | PROVEUSDT | bottom | STOP | 9.5 | -3.25% | $-3.21 |
| 2026-09-22T16:13 | AMDBUSDT | surge | TIME | 24.0 | +1.08% | $+1.02 |
| 2026-09-22T15:56 | ETCUSDT | surge | TARGET | 0.2 | +2.75% | $+2.65 |
| 2026-09-22T15:56 | TSLABUSDT | surge | TIME | 24.0 | +0.19% | $+0.16 |
| 2026-09-22T15:20 | KITEUSDT | surge | TARGET | 4.5 | +2.75% | $+2.58 |
| 2026-09-22T15:02 | MARSCOINUSDT | surge | STOP | 0.0 | -3.25% | $-3.22 |
| 2026-09-22T14:44 | TSTUSDT | surge | STOP | 1.0 | -3.25% | $-3.38 |
| 2026-09-22T14:44 | TUTUSDT | surge | STOP | 1.5 | -3.25% | $-3.29 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-22T12:53 | SPCXBUSDT | bottom | 152.07 | 154.21 | +1.41% |
| 2026-09-22T14:44 | SKHYBUSDT | surge | 194.89 | 196.16 | +0.65% |
| 2026-09-22T15:02 | SNDKBUSDT | surge | 1858.77 | 1895.53 | +1.98% |
| 2026-09-22T15:56 | MUBUSDT | surge | 1074.98 | 1097.7 | +2.11% |
| 2026-09-22T18:18 | SOXLBUSDT | surge | 149.09 | 152.62 | +2.37% |
| 2026-09-22T21:35 | PLUMEUSDT | surge | 0.01614 | 0.01633 | +1.18% |
| 2026-09-22T21:52 | PEOPLEUSDT | surge | 0.00956 | 0.0096 | +0.42% |
| 2026-09-22T23:19 | LUNCUSDT | surge | 5.67e-05 | 5.659e-05 | -0.19% |
| 2026-09-22T23:36 | LUNAUSDT | surge | 0.0565 | 0.0564 | -0.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
