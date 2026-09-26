# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T11:20:42+00:00 · runs 1834 · equity **$958.01** (-4.20%) · cash $0.00 · open 10/10 · round trips 651

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.06%/trade · realized $-47.48 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 553 | 54% | +0.01% | 50% | 42% | 7% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T11:19 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.59 |
| 2026-09-26T10:13 | QNTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.59 |
| 2026-09-26T09:57 | ACEUSDT | surge | TARGET | 0.2 | +2.75% | $+2.46 |
| 2026-09-26T09:57 | DOTUSDT | surge | STOP | 8.0 | -3.25% | $-3.24 |
| 2026-09-26T09:40 | PROMUSDT | surge | STOP | 2.0 | -3.25% | $-3.26 |
| 2026-09-26T09:24 | ZROUSDT | surge | STOP | 11.2 | -3.25% | $-3.00 |
| 2026-09-26T07:28 | RUNEUSDT | surge | TARGET | 2.5 | +2.75% | $+2.69 |
| 2026-09-26T06:39 | BABYUSDT | surge | TARGET | 0.2 | +2.75% | $+2.74 |
| 2026-09-26T06:07 | REZUSDT | surge | TARGET | 11.8 | +2.75% | $+2.66 |
| 2026-09-26T04:45 | PROMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.69 |
| 2026-09-26T04:45 | AVNTUSDT | surge | STOP | 0.2 | -3.25% | $-3.18 |
| 2026-09-26T04:29 | AVNTUSDT | surge | TARGET | 0.0 | +2.75% | $+2.64 |
| 2026-09-26T04:29 | PROMUSDT | surge | TARGET | 1.0 | +2.75% | $+2.61 |
| 2026-09-26T04:13 | SENTUSDT | surge | STOP | 1.0 | -3.25% | $-2.88 |
| 2026-09-26T04:13 | AVNTUSDT | surge | TARGET | 3.8 | +2.75% | $+2.84 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-25T16:15 | KORUBUSDT | surge | 21.59 | 21.48 | -0.51% |
| 2026-09-25T16:51 | SKHYBUSDT | surge | 191.35 | 191.31 | -0.02% |
| 2026-09-25T18:38 | ZKUSDT | surge | 0.01278 | 0.01305 | +2.11% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07912 | +1.87% |
| 2026-09-26T04:45 | INJUSDT | bottom | 7.814 | 7.85 | +0.46% |
| 2026-09-26T06:39 | BABYUSDT | surge | 0.01403 | 0.01411 | +0.57% |
| 2026-09-26T09:40 | STXUSDT | surge | 0.3439 | 0.3414 | -0.73% |
| 2026-09-26T10:13 | VELODROMEUSDT | surge | 0.03868 | 0.03845 | -0.59% |
| 2026-09-26T11:19 | SPELLUSDT | surge | 0.0001093 | 0.0001122 | +2.65% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
