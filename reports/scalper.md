# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T02:16:00+00:00 · runs 1801 · equity **$940.49** (-5.95%) · cash $0.00 · open 10/10 · round trips 634

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-57.98 · worst day $-50.94 · trades/day 28.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 536 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T01:42 | VTHOUSDT | surge | TARGET | 11.8 | +2.75% | $+2.67 |
| 2026-09-26T00:53 | DODOUSDT | surge | STOP | 7.5 | -3.25% | $-3.07 |
| 2026-09-26T00:04 | MUBARAKUSDT | surge | TARGET | 4.0 | +2.75% | $+2.77 |
| 2026-09-25T21:55 | AEROUSDT | surge | TARGET | 1.2 | +2.75% | $+2.60 |
| 2026-09-25T21:55 | BANKUSDT | surge | STOP | 15.0 | -3.25% | $-2.93 |
| 2026-09-25T20:25 | AMDBUSDT | surge | TIME | 24.0 | -0.02% | $-0.02 |
| 2026-09-25T19:49 | SUIUSDT | surge | TARGET | 4.8 | +2.75% | $+2.69 |
| 2026-09-25T18:38 | KMNOUSDT | surge | STOP | 2.5 | -3.25% | $-3.02 |
| 2026-09-25T18:02 | REZUSDT | surge | TARGET | 0.2 | +2.75% | $+2.59 |
| 2026-09-25T17:44 | REZUSDT | surge | TARGET | 3.5 | +2.75% | $+2.52 |
| 2026-09-25T17:08 | AEROUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-25T16:51 | JTOUSDT | surge | TARGET | 2.8 | +2.75% | $+2.52 |
| 2026-09-25T16:51 | BABYUSDT | surge | TARGET | 6.2 | +2.75% | $+2.40 |
| 2026-09-25T16:15 | NEARUSDT | surge | TARGET | 1.8 | +2.75% | $+2.62 |
| 2026-09-25T15:57 | ENSUSDT | surge | TIME | 24.0 | -1.23% | $-1.16 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-25T16:15 | KORUBUSDT | surge | 21.59 | 21.48 | -0.51% |
| 2026-09-25T16:51 | SKHYBUSDT | surge | 191.35 | 191.04 | -0.16% |
| 2026-09-25T18:02 | REZUSDT | surge | 0.004321 | 0.004298 | -0.53% |
| 2026-09-25T18:38 | ZKUSDT | surge | 0.01278 | 0.01283 | +0.39% |
| 2026-09-25T21:55 | RUNEUSDT | surge | 0.647 | 0.659 | +1.85% |
| 2026-09-25T21:55 | ZROUSDT | surge | 1.606 | 1.607 | +0.06% |
| 2026-09-26T00:04 | AVNTUSDT | surge | 0.1246 | 0.1246 | +0.00% |
| 2026-09-26T00:53 | WLDUSDT | surge | 0.4974 | 0.4896 | -1.57% |
| 2026-09-26T01:42 | DOTUSDT | surge | 1.236 | 1.223 | -1.05% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
