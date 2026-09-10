# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T15:49:25+00:00 · runs 448 · equity **$934.60** (-6.54%) · cash $188.68 · open 8/10 · round trips 159

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 46% (break-even 54%) · mean -0.40%/trade · realized $-63.29 · worst day $-41.53 · trades/day 26.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 102 | 47% | -0.41% | 43% | 49% | 8% |
| bottom | 57 | 44% | -0.39% | 42% | 46% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-10T15:48 | SAGAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.56 |
| 2026-09-10T13:09 | FFUSDT | surge | STOP | 1.2 | -3.25% | $-3.01 |
| 2026-09-10T13:09 | RUNEUSDT | surge | STOP | 2.0 | -3.25% | $-3.01 |
| 2026-09-10T13:09 | ENAUSDT | bottom | STOP | 9.0 | -3.25% | $-3.11 |
| 2026-09-10T13:09 | MSTRBUSDT | bottom | STOP | 16.8 | -3.25% | $-3.13 |
| 2026-09-10T12:51 | ETHFIUSDT | surge | STOP | 0.8 | -3.25% | $-3.01 |
| 2026-09-10T12:51 | SKHYBUSDT | surge | STOP | 21.0 | -3.25% | $-3.20 |
| 2026-09-10T12:51 | MUBUSDT | surge | STOP | 21.5 | -3.25% | $-3.29 |
| 2026-09-10T12:16 | INTCBUSDT | surge | STOP | 19.2 | -3.25% | $-3.18 |
| 2026-09-10T12:16 | MRVLBUSDT | surge | STOP | 20.2 | -3.25% | $-3.20 |
| 2026-09-10T10:49 | VETUSDT | surge | STOP | 3.5 | -3.25% | $-3.11 |
| 2026-09-10T10:15 | REUSDT | surge | STOP | 0.0 | -3.25% | $-3.05 |
| 2026-09-10T09:57 | RAYUSDT | surge | STOP | 0.2 | -3.25% | $-3.06 |
| 2026-09-10T09:40 | DODOUSDT | surge | TARGET | 0.0 | +2.75% | $+2.59 |
| 2026-09-10T09:22 | CKBUSDT | surge | STOP | 0.5 | -3.25% | $-3.11 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 91.46 | -0.17% |
| 2026-09-10T14:59 | METUSDT | surge | 0.217 | 0.2175 | +0.23% |
| 2026-09-10T14:59 | INJUSDT | bottom | 5.885 | 5.843 | -0.71% |
| 2026-09-10T14:59 | DOTUSDT | bottom | 1.083 | 1.086 | +0.28% |
| 2026-09-10T15:15 | RUNEUSDT | surge | 0.503 | 0.5 | -0.60% |
| 2026-09-10T15:31 | FFUSDT | surge | 0.1649 | 0.16563 | +0.44% |
| 2026-09-10T15:31 | AAPLBUSDT | surge | 323.88 | 320.74 | -0.97% |
| 2026-09-10T15:31 | VETUSDT | surge | 0.008236 | 0.008174 | -0.75% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
