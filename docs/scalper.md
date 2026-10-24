# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-24T12:22:42+00:00 · runs 4244 · equity **$660.44** (-33.96%) · cash $0.00 · open 10/10 · round trips 1535

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-339.11 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1344 | 49% | -0.24% | 47% | 46% | 7% |
| bottom | 191 | 44% | -0.42% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-24T12:20 | VANAUSDT | surge | STOP | 1.8 | -3.25% | $-2.19 |
| 2026-10-24T10:19 | SAHARAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.83 |
| 2026-10-24T10:19 | VANAUSDT | surge | TARGET | 0.8 | +2.75% | $+1.87 |
| 2026-10-24T10:19 | REZUSDT | surge | STOP | 1.8 | -3.25% | $-2.16 |
| 2026-10-24T10:02 | HYPERUSDT | surge | TARGET | 9.8 | +2.75% | $+1.69 |
| 2026-10-24T09:44 | NILUSDT | surge | TARGET | 4.0 | +2.75% | $+1.78 |
| 2026-10-24T09:27 | BREVUSDT | surge | TARGET | 0.2 | +2.75% | $+1.82 |
| 2026-10-24T08:35 | REDUSDT | surge | STOP | 2.2 | -3.25% | $-2.22 |
| 2026-10-24T08:17 | TREEUSDT | surge | TARGET | 0.8 | +2.75% | $+1.78 |
| 2026-10-24T07:22 | TREEUSDT | surge | TARGET | 2.5 | +2.75% | $+1.78 |
| 2026-10-24T07:22 | KMNOUSDT | surge | STOP | 3.8 | -3.25% | $-2.10 |
| 2026-10-24T06:14 | REDUSDT | surge | TARGET | 0.0 | +2.75% | $+1.83 |
| 2026-10-24T05:57 | REDUSDT | surge | TARGET | 0.8 | +2.75% | $+1.78 |
| 2026-10-24T03:25 | KMNOUSDT | surge | TARGET | 4.8 | +2.75% | $+1.69 |
| 2026-10-24T03:08 | LAUSDT | surge | STOP | 1.0 | -3.25% | $-2.11 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 145.85 | -1.82% |
| 2026-10-23T23:01 | CRCLBUSDT | bottom | 85.12 | 85.17 | +0.06% |
| 2026-10-23T23:01 | LTCUSDT | bottom | 56.84 | 56.51 | -0.58% |
| 2026-10-23T23:01 | SNDKBUSDT | bottom | 1232.71 | 1240.46 | +0.63% |
| 2026-10-24T07:22 | PARTIUSDT | surge | 0.0351 | 0.0354 | +0.85% |
| 2026-10-24T10:02 | LUMIAUSDT | surge | 0.0766 | 0.0754 | -1.57% |
| 2026-10-24T10:19 | SAHARAUSDT | surge | 0.00829 | 0.00829 | +0.00% |
| 2026-10-24T10:19 | MIRAUSDT | surge | 0.0488 | 0.0488 | +0.00% |
| 2026-10-24T12:20 | WCTUSDT | surge | 0.03893 | 0.03957 | +1.64% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
