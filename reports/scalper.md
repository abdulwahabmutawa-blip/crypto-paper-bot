# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T12:26:20+00:00 · runs 1838 · equity **$951.06** (-4.89%) · cash $0.00 · open 10/10 · round trips 653

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.06%/trade · realized $-47.96 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 555 | 54% | +0.01% | 50% | 42% | 7% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T11:52 | VELODROMEUSDT | surge | STOP | 1.5 | -3.25% | $-3.14 |
| 2026-09-26T11:35 | SPELLUSDT | surge | TARGET | 0.0 | +2.75% | $+2.66 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-25T16:15 | KORUBUSDT | surge | 21.59 | 21.49 | -0.46% |
| 2026-09-25T16:51 | SKHYBUSDT | surge | 191.35 | 191.49 | +0.07% |
| 2026-09-25T18:38 | ZKUSDT | surge | 0.01278 | 0.01291 | +1.02% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07874 | +1.38% |
| 2026-09-26T04:45 | INJUSDT | bottom | 7.814 | 7.777 | -0.47% |
| 2026-09-26T06:39 | BABYUSDT | surge | 0.01403 | 0.01405 | +0.14% |
| 2026-09-26T09:40 | STXUSDT | surge | 0.3439 | 0.3416 | -0.67% |
| 2026-09-26T11:35 | TNSRUSDT | surge | 0.0434 | 0.0427 | -1.61% |
| 2026-09-26T11:52 | RESOLVUSDT | surge | 0.02136 | 0.0213 | -0.28% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
