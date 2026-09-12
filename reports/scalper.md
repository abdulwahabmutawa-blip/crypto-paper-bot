# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-12T17:54:48+00:00 · runs 630 · equity **$898.74** (-10.13%) · cash $0.00 · open 10/10 · round trips 221

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.48%/trade · realized $-102.78 · worst day $-50.94 · trades/day 27.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 156 | 44% | -0.53% | 40% | 50% | 10% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-12T17:52 | WLFIUSDT | surge | STOP | 0.8 | -3.25% | $-2.92 |
| 2026-09-12T17:16 | CHIPUSDT | surge | STOP | 0.8 | -3.25% | $-2.89 |
| 2026-09-12T16:53 | CFGUSDT | surge | STOP | 2.0 | -3.25% | $-2.92 |
| 2026-09-12T16:53 | KAITOUSDT | surge | TIME | 24.0 | -0.70% | $-0.66 |
| 2026-09-12T16:18 | ETHFIUSDT | surge | STOP | 1.5 | -3.25% | $-2.92 |
| 2026-09-12T16:18 | PLUMEUSDT | surge | TIME | 24.0 | +0.05% | $+0.04 |
| 2026-09-12T16:18 | SOXLBUSDT | surge | TIME | 24.0 | -0.85% | $-0.77 |
| 2026-09-12T16:00 | GOOGLBUSDT | surge | TIME | 24.0 | -0.75% | $-0.68 |
| 2026-09-12T14:13 | THEUSDT | surge | STOP | 2.8 | -3.25% | $-2.81 |
| 2026-09-12T14:13 | BTCUSDT | surge | TIME | 24.0 | -0.91% | $-0.82 |
| 2026-09-12T14:13 | AAPLBUSDT | surge | TIME | 24.0 | -0.21% | $-0.19 |
| 2026-09-12T13:55 | REZUSDT | surge | TARGET | 0.2 | +2.75% | $+2.53 |
| 2026-09-12T13:20 | POLUSDT | surge | TIME | 24.0 | +0.60% | $+0.55 |
| 2026-09-12T11:28 | ACEUSDT | surge | STOP | 8.8 | -3.25% | $-2.91 |
| 2026-09-12T10:53 | CAKEUSDT | surge | TARGET | 18.0 | +2.75% | $+2.57 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-11T20:35 | SPCXBUSDT | surge | 150.6 | 150.07 | -0.35% |
| 2026-09-12T10:53 | PROMUSDT | surge | 5.762 | 5.87 | +1.87% |
| 2026-09-12T14:31 | KAVAUSDT | surge | 0.07024 | 0.07023 | -0.01% |
| 2026-09-12T14:31 | NEIROUSDT | surge | 8.935e-05 | 8.985e-05 | +0.56% |
| 2026-09-12T16:00 | ORDIUSDT | surge | 4.305 | 4.228 | -1.79% |
| 2026-09-12T16:18 | PYTHUSDT | surge | 0.05484 | 0.05498 | +0.26% |
| 2026-09-12T16:18 | PENDLEUSDT | surge | 2.187 | 2.199 | +0.55% |
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.04908 | -0.06% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T17:52 | HEMIUSDT | surge | 0.007 | 0.00704 | +0.57% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
