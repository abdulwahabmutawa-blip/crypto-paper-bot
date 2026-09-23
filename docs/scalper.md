# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-23T09:11:10+00:00 · runs 1561 · equity **$978.48** (-2.15%) · cash $0.00 · open 10/10 · round trips 559

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean -0.03%/trade · realized $-23.99 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 467 | 55% | +0.06% | 51% | 41% | 8% |
| bottom | 92 | 42% | -0.49% | 40% | 46% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-22T16:49 | GIGGLEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.63 |
| 2026-09-22T16:13 | PROVEUSDT | bottom | STOP | 9.5 | -3.25% | $-3.21 |
| 2026-09-22T16:13 | AMDBUSDT | surge | TIME | 24.0 | +1.08% | $+1.02 |
| 2026-09-22T15:56 | ETCUSDT | surge | TARGET | 0.2 | +2.75% | $+2.65 |
| 2026-09-22T15:56 | TSLABUSDT | surge | TIME | 24.0 | +0.19% | $+0.16 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-22T12:53 | SPCXBUSDT | bottom | 152.07 | 154.34 | +1.49% |
| 2026-09-22T14:44 | SKHYBUSDT | surge | 194.89 | 191.21 | -1.89% |
| 2026-09-22T15:02 | SNDKBUSDT | surge | 1858.77 | 1879.96 | +1.14% |
| 2026-09-22T15:56 | MUBUSDT | surge | 1074.98 | 1093.07 | +1.68% |
| 2026-09-22T18:18 | SOXLBUSDT | surge | 149.09 | 149.2 | +0.07% |
| 2026-09-22T21:52 | PEOPLEUSDT | surge | 0.00956 | 0.0096 | +0.42% |
| 2026-09-22T23:19 | LUNCUSDT | surge | 5.67e-05 | 5.658e-05 | -0.21% |
| 2026-09-22T23:36 | LUNAUSDT | surge | 0.0565 | 0.0565 | +0.00% |
| 2026-09-23T09:09 | BBUSDT | surge | 0.0103 | 0.01029 | -0.10% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
