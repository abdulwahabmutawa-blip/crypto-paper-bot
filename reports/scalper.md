# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-23T14:42:09+00:00 · runs 1581 · equity **$941.53** (-5.85%) · cash $282.86 · open 7/10 · round trips 575

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-59.77 · worst day $-50.94 · trades/day 30.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 481 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 94 | 43% | -0.51% | 39% | 46% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-23T14:24 | HBARUSDT | bottom | STOP | 0.0 | -3.25% | $-3.18 |
| 2026-09-23T14:24 | ZROUSDT | surge | STOP | 0.0 | -3.25% | $-3.18 |
| 2026-09-23T14:24 | COTIUSDT | surge | STOP | 0.2 | -3.25% | $-3.28 |
| 2026-09-23T14:24 | PROVEUSDT | surge | STOP | 2.2 | -3.25% | $-3.02 |
| 2026-09-23T14:24 | LUNCUSDT | surge | STOP | 14.8 | -3.25% | $-3.12 |
| 2026-09-23T14:24 | SKHYBUSDT | surge | STOP | 23.5 | -3.25% | $-3.22 |
| 2026-09-23T14:07 | LUNAUSDT | surge | STOP | 14.2 | -3.25% | $-3.38 |
| 2026-09-23T14:07 | SOXLBUSDT | surge | STOP | 19.5 | -3.25% | $-3.19 |
| 2026-09-23T13:51 | SNXXBUSDT | surge | STOP | 0.0 | -3.25% | $-3.39 |
| 2026-09-23T13:35 | RAYUSDT | surge | TARGET | 0.0 | +2.75% | $+2.80 |
| 2026-09-23T13:18 | COTIUSDT | surge | TARGET | 0.0 | +2.75% | $+2.72 |
| 2026-09-23T13:02 | ICPUSDT | surge | STOP | 0.5 | -3.25% | $-3.22 |
| 2026-09-23T13:02 | SPCXBUSDT | bottom | TIME | 24.0 | +0.77% | $+0.78 |
| 2026-09-23T12:29 | 0GUSDT | surge | STOP | 0.8 | -3.25% | $-3.33 |
| 2026-09-23T11:48 | PEOPLEUSDT | surge | STOP | 13.8 | -3.25% | $-3.12 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-22T15:02 | SNDKBUSDT | surge | 1858.77 | 1831.92 | -1.44% |
| 2026-09-22T15:56 | MUBUSDT | surge | 1074.98 | 1076.96 | +0.18% |
| 2026-09-23T13:02 | SKYUSDT | surge | 0.07419 | 0.07441 | +0.30% |
| 2026-09-23T14:40 | BNBUSDT | bottom | 760.19 | 766.84 | +0.87% |
| 2026-09-23T14:40 | MSTRBUSDT | bottom | 162.61 | 164.26 | +1.01% |
| 2026-09-23T14:40 | BTCUSDT | bottom | 84041.7 | 84435.9 | +0.47% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
