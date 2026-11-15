# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-15T14:14:45+00:00 · runs 6062 · equity **$490.67** (-50.93%) · cash $270.17 · open 4/10 · round trips 1993

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-508.58 · worst day $-50.94 · trades/day 27.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1721 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 272 | 42% | -0.55% | 35% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-15T09:31 | MEGAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.23 |
| 2026-11-15T06:07 | SPCXBUSDT | bottom | TIME | 24.0 | +0.32% | $+0.14 |
| 2026-11-15T06:07 | GOOGLBUSDT | bottom | TIME | 24.0 | -0.72% | $-0.33 |
| 2026-11-14T19:55 | WLFIUSDT | surge | STOP | 13.5 | -3.25% | $-1.47 |
| 2026-11-14T14:14 | FETUSDT | bottom | STOP | 8.2 | -3.25% | $-1.47 |
| 2026-11-14T06:26 | DODOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.24 |
| 2026-11-13T16:11 | TRXUSDT | bottom | TIME | 24.0 | -0.98% | $-0.44 |
| 2026-11-13T01:57 | OPENUSDT | surge | STOP | 12.2 | -3.25% | $-1.45 |
| 2026-11-12T23:56 | GOOGLBUSDT | surge | TIME | 24.0 | +1.24% | $+0.57 |
| 2026-11-12T19:50 | GRAMUSDT | surge | STOP | 6.2 | -3.25% | $-1.50 |
| 2026-11-12T19:50 | QQQBUSDT | surge | TIME | 24.0 | -0.77% | $-0.35 |
| 2026-11-12T14:48 | SPCXBUSDT | bottom | TARGET | 15.5 | +2.75% | $+1.27 |
| 2026-11-12T14:31 | MSTRBUSDT | bottom | STOP | 8.5 | -3.25% | $-1.54 |
| 2026-11-12T13:56 | ERAUSDT | surge | STOP | 0.2 | -3.25% | $-1.45 |
| 2026-11-12T13:56 | ONEUSDT | surge | STOP | 1.8 | -3.25% | $-1.50 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-15T13:02 | MEGAUSDT | surge | 0.05101 | 0.05019 | -1.61% |
| 2026-11-15T13:02 | FFUSDT | surge | 0.09635 | 0.09699 | +0.66% |
| 2026-11-15T13:37 | KITEUSDT | surge | 0.1381 | 0.1371 | -0.72% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
