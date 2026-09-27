# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T02:16:25+00:00 · runs 1889 · equity **$939.65** (-6.04%) · cash $0.00 · open 10/10 · round trips 676

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-62.28 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 577 | 54% | -0.01% | 50% | 42% | 7% |
| bottom | 99 | 43% | -0.49% | 39% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-27T00:59 | ESPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-27T00:41 | ESPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.58 |
| 2026-09-27T00:41 | TUSDT | surge | STOP | 0.0 | -3.25% | $-3.05 |
| 2026-09-27T00:24 | RUNEUSDT | surge | TARGET | 2.5 | +2.75% | $+2.42 |
| 2026-09-27T00:24 | ESPUSDT | surge | TARGET | 7.5 | +2.75% | $+2.61 |
| 2026-09-27T00:06 | GRAMUSDT | surge | TARGET | 3.5 | +2.75% | $+2.62 |
| 2026-09-26T23:13 | KMNOUSDT | surge | TARGET | 6.0 | +2.75% | $+2.53 |
| 2026-09-26T22:02 | KITEUSDT | surge | TARGET | 1.5 | +2.75% | $+2.62 |
| 2026-09-26T21:44 | LSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.96 |
| 2026-09-26T20:51 | WLDUSDT | surge | STOP | 1.8 | -3.25% | $-2.83 |
| 2026-09-26T20:51 | STXUSDT | surge | STOP | 11.0 | -3.25% | $-3.16 |
| 2026-09-26T20:51 | INJUSDT | bottom | STOP | 15.8 | -3.25% | $-3.18 |
| 2026-09-26T20:15 | ZENUSDT | surge | STOP | 3.5 | -3.25% | $-3.09 |
| 2026-09-26T20:15 | BABYUSDT | surge | STOP | 13.5 | -3.25% | $-3.32 |
| 2026-09-26T18:47 | OPGUSDT | surge | STOP | 3.5 | -3.25% | $-2.92 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07806 | +0.50% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 71.07 | -0.75% |
| 2026-09-26T20:51 | SEIUSDT | bottom | 0.0712 | 0.07274 | +2.16% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3332 | -0.54% |
| 2026-09-26T22:02 | SUPERUSDT | surge | 0.2006 | 0.2002 | -0.20% |
| 2026-09-26T23:13 | KITEUSDT | surge | 0.1508 | 0.1528 | +1.33% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1643.88 | -0.56% |
| 2026-09-27T00:41 | GRAMUSDT | surge | 1.605 | 1.601 | -0.25% |
| 2026-09-27T00:59 | XPLUSDT | bottom | 0.11061 | 0.11106 | +0.41% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
