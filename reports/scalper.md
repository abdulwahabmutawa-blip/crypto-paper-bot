# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T20:17:58+00:00 · runs 1868 · equity **$933.29** (-6.67%) · cash $0.00 · open 10/10 · round trips 664

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-65.08 · worst day $-50.94 · trades/day 30.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 566 | 53% | -0.03% | 50% | 43% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T20:15 | ZENUSDT | surge | STOP | 3.5 | -3.25% | $-3.09 |
| 2026-09-26T20:15 | BABYUSDT | surge | STOP | 13.5 | -3.25% | $-3.32 |
| 2026-09-26T18:47 | OPGUSDT | surge | STOP | 3.5 | -3.25% | $-2.92 |
| 2026-09-26T17:08 | SKHYBUSDT | surge | TIME | 24.0 | +0.05% | $+0.05 |
| 2026-09-26T16:36 | ZKUSDT | surge | TARGET | 21.8 | +2.75% | $+2.47 |
| 2026-09-26T16:36 | KORUBUSDT | surge | TIME | 24.0 | -0.39% | $-0.38 |
| 2026-09-26T16:19 | SPELLUSDT | surge | STOP | 0.2 | -3.25% | $-3.12 |
| 2026-09-26T15:46 | TNSRUSDT | surge | STOP | 4.0 | -3.25% | $-3.23 |
| 2026-09-26T15:13 | TLMUSDT | surge | STOP | 0.8 | -3.25% | $-3.02 |
| 2026-09-26T14:19 | TLMUSDT | surge | TARGET | 0.5 | +2.75% | $+2.49 |
| 2026-09-26T13:30 | RESOLVUSDT | surge | STOP | 1.5 | -3.25% | $-3.04 |
| 2026-09-26T11:52 | VELODROMEUSDT | surge | STOP | 1.5 | -3.25% | $-3.14 |
| 2026-09-26T11:35 | SPELLUSDT | surge | TARGET | 0.0 | +2.75% | $+2.66 |
| 2026-09-26T11:19 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.59 |
| 2026-09-26T10:13 | QNTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.59 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07719 | -0.62% |
| 2026-09-26T04:45 | INJUSDT | bottom | 7.814 | 7.677 | -1.75% |
| 2026-09-26T09:40 | STXUSDT | surge | 0.3439 | 0.3377 | -1.80% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 71.68 | +0.10% |
| 2026-09-26T16:36 | ESPUSDT | surge | 0.1039 | 0.10525 | +1.30% |
| 2026-09-26T17:08 | KMNOUSDT | surge | 0.04944 | 0.05008 | +1.29% |
| 2026-09-26T18:47 | WLDUSDT | surge | 0.5312 | 0.5319 | +0.13% |
| 2026-09-26T20:15 | GRAMUSDT | surge | 1.56 | 1.562 | +0.13% |
| 2026-09-26T20:15 | KITEUSDT | surge | 0.1478 | 0.1473 | -0.34% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
