# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T07:57:41+00:00 · runs 4228 · equity **$653.44** (-34.66%) · cash $0.00 · open 10/10 · round trips 1526

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-343.30 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1335 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 191 | 44% | -0.42% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-24T07:22 | TREEUSDT | surge | TARGET | 2.5 | +2.75% | $+1.78 |
| 2026-10-24T07:22 | KMNOUSDT | surge | STOP | 3.8 | -3.25% | $-2.10 |
| 2026-10-24T06:14 | REDUSDT | surge | TARGET | 0.0 | +2.75% | $+1.83 |
| 2026-10-24T05:57 | REDUSDT | surge | TARGET | 0.8 | +2.75% | $+1.78 |
| 2026-10-24T03:25 | KMNOUSDT | surge | TARGET | 4.8 | +2.75% | $+1.69 |
| 2026-10-24T03:08 | LAUSDT | surge | STOP | 1.0 | -3.25% | $-2.11 |
| 2026-10-24T02:29 | KATUSDT | surge | TARGET | 0.0 | +2.75% | $+1.81 |
| 2026-10-24T02:12 | KATUSDT | surge | TARGET | 0.0 | +2.75% | $+1.78 |
| 2026-10-24T01:54 | LAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.77 |
| 2026-10-24T01:37 | LAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.72 |
| 2026-10-24T01:37 | AVAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.72 |
| 2026-10-24T01:37 | TREEUSDT | surge | TARGET | 0.5 | +2.75% | $+1.72 |
| 2026-10-24T00:45 | LAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.70 |
| 2026-10-24T00:28 | LAUSDT | surge | TARGET | 0.8 | +2.75% | $+1.69 |
| 2026-10-23T23:01 | GRAMUSDT | bottom | STOP | 0.5 | -3.25% | $-2.00 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 145.73 | -1.90% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 85.16 | +0.05% |
| 2026-10-23T23:01 | LTCUSDT | bottom | 56.84 | 56.62 | -0.39% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1237.42 | +0.38% |
| 2026-10-24T00:11 | HYPERUSDT | surge | 0.0649 | 0.0639 | -1.54% |
| 2026-10-24T05:23 | NILUSDT | surge | 0.08272 | 0.08372 | +1.21% |
| 2026-10-24T06:14 | REDUSDT | surge | 0.1536 | 0.1503 | -2.15% |
| 2026-10-24T07:22 | PARTIUSDT | surge | 0.0351 | 0.0347 | -1.14% |
| 2026-10-24T07:22 | TREEUSDT | surge | 0.0456 | 0.0458 | +0.44% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
