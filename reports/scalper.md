# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-10T12:53:39+00:00 · runs 437 · equity **$934.00** (-6.60%) · cash $472.63 · open 5/10 · round trips 154

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-53.59 · worst day $-31.83 · trades/day 25.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 99 | 47% | -0.39% | 43% | 48% | 8% |
| bottom | 55 | 45% | -0.29% | 44% | 44% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-10T03:56 | LTCUSDT | bottom | TIME | 24.0 | -2.09% | $-2.04 |
| 2026-09-10T03:21 | SAHARAUSDT | surge | STOP | 0.0 | -3.25% | $-3.15 |
| 2026-09-10T02:05 | MINAUSDT | surge | STOP | 1.5 | -3.25% | $-3.25 |
| 2026-09-10T00:37 | SAHARAUSDT | surge | STOP | 2.0 | -3.25% | $-3.14 |
| 2026-09-10T00:20 | MINAUSDT | surge | TARGET | 0.0 | +2.75% | $+2.72 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T20:03 | MSTRBUSDT | bottom | 132.71 | 128.47 | -3.19% |
| 2026-09-09T22:17 | CRCLBUSDT | bottom | 91.62 | 89.91 | -1.87% |
| 2026-09-10T03:56 | ENAUSDT | bottom | 0.1503 | 0.147 | -2.20% |
| 2026-09-10T10:49 | RUNEUSDT | surge | 0.498 | 0.483 | -3.01% |
| 2026-09-10T11:41 | FFUSDT | surge | 0.15745 | 0.15296 | -2.85% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
