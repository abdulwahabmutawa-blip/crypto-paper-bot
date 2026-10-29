# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-29T20:32:56+00:00 · runs 4712 · equity **$592.93** (-40.71%) · cash $221.85 · open 6/10 · round trips 1678

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-404.11 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1464 | 48% | -0.28% | 46% | 47% | 7% |
| bottom | 214 | 43% | -0.49% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-29T20:14 | UNIUSDT | surge | STOP | 5.2 | -3.25% | $-1.85 |
| 2026-10-29T20:14 | BMNRBUSDT | surge | STOP | 5.2 | -3.25% | $-1.85 |
| 2026-10-29T20:14 | INJUSDT | surge | STOP | 5.5 | -3.25% | $-1.85 |
| 2026-10-29T20:14 | BEBUSDT | surge | STOP | 6.0 | -3.25% | $-1.89 |
| 2026-10-29T14:31 | SOXSBUSDT | surge | STOP | 12.5 | -3.25% | $-1.88 |
| 2026-10-29T14:13 | LSKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.60 |
| 2026-10-29T14:13 | AVAUSDT | surge | STOP | 1.0 | -3.25% | $-1.87 |
| 2026-10-29T14:09 | SPCXBUSDT | bottom | TIME | 24.0 | -0.94% | $-0.55 |
| 2026-10-29T13:36 | 牛来USDT | surge | TARGET | 0.5 | +2.75% | $+1.60 |
| 2026-10-29T13:03 | HUMAUSDT | surge | STOP | 0.0 | -3.25% | $-1.89 |
| 2026-10-29T12:47 | HUMAUSDT | surge | TARGET | 0.8 | +2.75% | $+1.56 |
| 2026-10-29T12:30 | BNBUSDT | surge | TIME | 24.0 | -2.32% | $-1.42 |
| 2026-10-29T11:41 | HUMAUSDT | surge | TARGET | 3.8 | +2.75% | $+1.65 |
| 2026-10-29T09:46 | AIUSDT | surge | STOP | 7.0 | -3.25% | $-1.87 |
| 2026-10-29T09:13 | LTCUSDT | surge | STOP | 16.5 | -3.25% | $-1.79 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-29T01:59 | HBARUSDT | bottom | 0.07428 | 0.07246 | -2.45% |
| 2026-10-29T02:48 | BTCUSDT | bottom | 79714 | 80330.7 | +0.77% |
| 2026-10-29T05:27 | 币安人生USDT | surge | 0.5351 | 0.5322 | -0.54% |
| 2026-10-29T13:36 | 牛来USDT | surge | 0.06099 | 0.06025 | -1.21% |
| 2026-10-29T14:09 | XRPUSDT | bottom | 1.291 | 1.2693 | -1.68% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
