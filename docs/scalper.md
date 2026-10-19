# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-19T16:10:05+00:00 · runs 3819 · equity **$679.12** (-32.09%) · cash $0.00 · open 10/10 · round trips 1407

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.28%/trade · realized $-325.43 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1229 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 178 | 45% | -0.36% | 39% | 42% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-19T15:50 | MRVLBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.74 |
| 2026-10-19T15:33 | MUBUSDT | surge | TARGET | 13.5 | +2.75% | $+1.79 |
| 2026-10-19T15:16 | KATUSDT | surge | STOP | 1.0 | -3.25% | $-2.05 |
| 2026-10-19T13:54 | NBISBUSDT | surge | STOP | 1.8 | -3.25% | $-2.18 |
| 2026-10-19T13:54 | AAOIBUSDT | surge | STOP | 10.2 | -3.25% | $-2.07 |
| 2026-10-19T13:37 | SKHYBUSDT | surge | TARGET | 11.5 | +2.75% | $+1.79 |
| 2026-10-19T11:54 | NBISBUSDT | surge | TARGET | 10.5 | +2.75% | $+1.80 |
| 2026-10-19T10:46 | EWYBUSDT | surge | TARGET | 9.0 | +2.75% | $+1.80 |
| 2026-10-19T10:46 | DRAMBUSDT | surge | TARGET | 10.2 | +2.75% | $+1.80 |
| 2026-10-19T03:17 | MSTRBUSDT | surge | TIME | 24.0 | +2.22% | $+1.38 |
| 2026-10-19T02:24 | TQQQBUSDT | surge | TARGET | 3.8 | +2.75% | $+1.75 |
| 2026-10-19T01:49 | SKHYBUSDT | surge | TARGET | 2.5 | +2.75% | $+1.80 |
| 2026-10-19T01:49 | TRXUSDT | bottom | TIME | 24.0 | -0.61% | $-0.39 |
| 2026-10-19T01:32 | EWYBUSDT | surge | TARGET | 3.0 | +2.75% | $+1.75 |
| 2026-10-19T01:14 | INTCBUSDT | surge | TARGET | 2.8 | +2.75% | $+1.75 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-18T22:18 | QQQBUSDT | surge | 713.34 | 722.71 | +1.31% |
| 2026-10-19T00:21 | TSLABUSDT | surge | 359.63 | 367.9 | +2.30% |
| 2026-10-19T02:24 | TQQQBUSDT | surge | 70.62 | 71.78 | +1.64% |
| 2026-10-19T10:46 | ATOMUSDT | surge | 1.743 | 1.78 | +2.12% |
| 2026-10-19T10:46 | RAYUSDT | surge | 1.9318 | 1.9191 | -0.66% |
| 2026-10-19T13:37 | BNCBUSDT | surge | 4.7 | 4.73 | +0.64% |
| 2026-10-19T15:16 | GOOGLBUSDT | surge | 346.27 | 345.53 | -0.21% |
| 2026-10-19T15:33 | AMDBUSDT | surge | 553.18 | 548.84 | -0.78% |
| 2026-10-19T15:50 | MORPHOUSDT | surge | 2.53 | 2.545 | +0.59% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
