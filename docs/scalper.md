# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T08:19:12+00:00 · runs 4230 · equity **$654.82** (-34.52%) · cash $0.00 · open 10/10 · round trips 1527

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-341.53 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1336 | 49% | -0.25% | 47% | 46% | 7% |
| bottom | 191 | 44% | -0.42% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-24T08:17 | TREEUSDT | surge | TARGET | 0.8 | +2.75% | $+1.78 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 145.96 | -1.74% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 84.99 | -0.15% |
| 2026-10-23T23:01 | LTCUSDT | bottom | 56.84 | 56.69 | -0.26% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1237.61 | +0.40% |
| 2026-10-24T00:11 | HYPERUSDT | surge | 0.0649 | 0.0643 | -0.92% |
| 2026-10-24T05:23 | NILUSDT | surge | 0.08272 | 0.08294 | +0.27% |
| 2026-10-24T06:14 | REDUSDT | surge | 0.1536 | 0.1496 | -2.60% |
| 2026-10-24T07:22 | PARTIUSDT | surge | 0.0351 | 0.0347 | -1.14% |
| 2026-10-24T08:17 | REZUSDT | surge | 0.00446 | 0.004485 | +0.56% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
