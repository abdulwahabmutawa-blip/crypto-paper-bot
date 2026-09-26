# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T08:19:04+00:00 · runs 1824 · equity **$952.24** (-4.78%) · cash $0.00 · open 10/10 · round trips 645

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.06%/trade · realized $-45.61 · worst day $-50.94 · trades/day 29.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 547 | 54% | +0.01% | 50% | 42% | 7% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T07:28 | RUNEUSDT | surge | TARGET | 2.5 | +2.75% | $+2.69 |
| 2026-09-26T06:39 | BABYUSDT | surge | TARGET | 0.2 | +2.75% | $+2.74 |
| 2026-09-26T06:07 | REZUSDT | surge | TARGET | 11.8 | +2.75% | $+2.66 |
| 2026-09-26T04:45 | PROMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.69 |
| 2026-09-26T04:45 | AVNTUSDT | surge | STOP | 0.2 | -3.25% | $-3.18 |
| 2026-09-26T04:29 | AVNTUSDT | surge | TARGET | 0.0 | +2.75% | $+2.64 |
| 2026-09-26T04:29 | PROMUSDT | surge | TARGET | 1.0 | +2.75% | $+2.61 |
| 2026-09-26T04:13 | SENTUSDT | surge | STOP | 1.0 | -3.25% | $-2.88 |
| 2026-09-26T04:13 | AVNTUSDT | surge | TARGET | 3.8 | +2.75% | $+2.84 |
| 2026-09-26T03:24 | RUNEUSDT | surge | TARGET | 5.2 | +2.75% | $+2.54 |
| 2026-09-26T02:47 | WLDUSDT | surge | STOP | 1.8 | -3.25% | $-2.97 |
| 2026-09-26T01:42 | VTHOUSDT | surge | TARGET | 11.8 | +2.75% | $+2.67 |
| 2026-09-26T00:53 | DODOUSDT | surge | STOP | 7.5 | -3.25% | $-3.07 |
| 2026-09-26T00:04 | MUBARAKUSDT | surge | TARGET | 4.0 | +2.75% | $+2.77 |
| 2026-09-25T21:55 | AEROUSDT | surge | TARGET | 1.2 | +2.75% | $+2.60 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-25T16:15 | KORUBUSDT | surge | 21.59 | 21.47 | -0.56% |
| 2026-09-25T16:51 | SKHYBUSDT | surge | 191.35 | 191.17 | -0.09% |
| 2026-09-25T18:38 | ZKUSDT | surge | 0.01278 | 0.01295 | +1.33% |
| 2026-09-25T21:55 | ZROUSDT | surge | 1.606 | 1.592 | -0.87% |
| 2026-09-26T01:42 | DOTUSDT | surge | 1.236 | 1.219 | -1.38% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07924 | +2.02% |
| 2026-09-26T04:45 | INJUSDT | bottom | 7.814 | 7.821 | +0.09% |
| 2026-09-26T06:39 | BABYUSDT | surge | 0.01403 | 0.01371 | -2.28% |
| 2026-09-26T07:28 | PROMUSDT | surge | 6.378 | 6.363 | -0.24% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
