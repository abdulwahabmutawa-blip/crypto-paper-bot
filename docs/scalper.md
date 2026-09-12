# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-12T21:30:15+00:00 · runs 642 · equity **$893.72** (-10.63%) · cash $0.00 · open 10/10 · round trips 226

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.45%/trade · realized $-98.71 · worst day $-50.94 · trades/day 28.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 161 | 45% | -0.49% | 41% | 49% | 10% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-12T21:28 | KAVAUSDT | surge | TARGET | 6.8 | +2.75% | $+2.47 |
| 2026-09-12T20:51 | SPCXBUSDT | surge | TIME | 24.0 | -0.57% | $-0.51 |
| 2026-09-12T20:15 | HEMIUSDT | surge | TARGET | 2.0 | +2.75% | $+2.39 |
| 2026-09-12T18:46 | ORDIUSDT | surge | STOP | 2.5 | -3.25% | $-2.93 |
| 2026-09-12T18:28 | PROMUSDT | surge | TARGET | 7.2 | +2.75% | $+2.65 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T14:31 | NEIROUSDT | surge | 8.935e-05 | 8.769e-05 | -1.86% |
| 2026-09-12T16:18 | PYTHUSDT | surge | 0.05484 | 0.0553 | +0.84% |
| 2026-09-12T16:18 | PENDLEUSDT | surge | 2.187 | 2.188 | +0.05% |
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.04843 | -1.38% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T18:28 | JTOUSDT | surge | 0.4519 | 0.4404 | -2.54% |
| 2026-09-12T18:46 | PARTIUSDT | surge | 0.0242 | 0.0239 | -1.24% |
| 2026-09-12T20:15 | PUMPUSDT | surge | 0.003852 | 0.003864 | +0.31% |
| 2026-09-12T20:51 | INJUSDT | surge | 6.063 | 6.031 | -0.53% |
| 2026-09-12T21:28 | HEMIUSDT | surge | 0.00728 | 0.00715 | -1.79% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
