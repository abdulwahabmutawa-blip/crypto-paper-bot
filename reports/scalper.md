# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T23:50:44+00:00 · runs 1880 · equity **$938.39** (-6.16%) · cash $0.00 · open 10/10 · round trips 670

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-72.04 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 571 | 53% | -0.03% | 50% | 43% | 8% |
| bottom | 99 | 43% | -0.49% | 39% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T23:13 | KMNOUSDT | surge | TARGET | 6.0 | +2.75% | $+2.53 |
| 2026-09-26T22:02 | KITEUSDT | surge | TARGET | 1.5 | +2.75% | $+2.62 |
| 2026-09-26T21:44 | LSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.96 |
| 2026-09-26T20:51 | WLDUSDT | surge | STOP | 1.8 | -3.25% | $-2.83 |
| 2026-09-26T20:51 | STXUSDT | surge | STOP | 11.0 | -3.25% | $-3.16 |
| 2026-09-26T20:51 | INJUSDT | bottom | STOP | 15.8 | -3.25% | $-3.18 |
| 2026-09-26T20:15 | ZENUSDT | surge | STOP | 3.5 | -3.25% | $-3.09 |
| 2026-09-26T20:15 | BABYUSDT | surge | STOP | 13.5 | -3.25% | $-3.32 |
| 2026-09-26T18:47 | OPGUSDT | surge | STOP | 3.5 | -3.25% | $-2.92 |
| 2026-09-26T17:08 | SKHYBUSDT | surge | TIME | 24.0 | +0.05% | $+0.05 |
| 2026-09-26T16:36 | ZKUSDT | surge | TARGET | 21.8 | +2.75% | $+2.47 |
| 2026-09-26T16:36 | KORUBUSDT | surge | TIME | 24.0 | -0.39% | $-0.38 |
| 2026-09-26T16:19 | SPELLUSDT | surge | STOP | 0.2 | -3.25% | $-3.12 |
| 2026-09-26T15:46 | TNSRUSDT | surge | STOP | 4.0 | -3.25% | $-3.23 |
| 2026-09-26T15:13 | TLMUSDT | surge | STOP | 0.8 | -3.25% | $-3.02 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07818 | +0.66% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 71.8 | +0.27% |
| 2026-09-26T16:36 | ESPUSDT | surge | 0.1039 | 0.10454 | +0.62% |
| 2026-09-26T20:15 | GRAMUSDT | surge | 1.56 | 1.606 | +2.95% |
| 2026-09-26T20:51 | SEIUSDT | bottom | 0.0712 | 0.07203 | +1.17% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3343 | -0.21% |
| 2026-09-26T21:44 | RUNEUSDT | surge | 0.753 | 0.77 | +2.26% |
| 2026-09-26T22:02 | SUPERUSDT | surge | 0.2006 | 0.2044 | +1.89% |
| 2026-09-26T23:13 | KITEUSDT | surge | 0.1508 | 0.1531 | +1.53% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
