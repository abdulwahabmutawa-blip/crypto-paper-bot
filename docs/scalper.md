# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-30T07:27:33+00:00 · runs 4753 · equity **$584.09** (-41.59%) · cash $277.98 · open 5/10 · round trips 1683

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-413.46 · worst day $-50.94 · trades/day 30.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1466 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 217 | 42% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-30T00:41 | BTCUSDT | bottom | STOP | 21.5 | -3.25% | $-1.85 |
| 2026-10-29T20:48 | XRPUSDT | bottom | STOP | 6.5 | -3.25% | $-1.89 |
| 2026-10-29T20:48 | 牛来USDT | surge | STOP | 7.0 | -3.25% | $-1.89 |
| 2026-10-29T20:48 | 币安人生USDT | surge | STOP | 15.2 | -3.25% | $-1.85 |
| 2026-10-29T20:48 | HBARUSDT | bottom | STOP | 18.8 | -3.25% | $-1.88 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T06:15 | XPLUSDT | surge | 0.07677 | 0.07668 | -0.12% |
| 2026-10-30T06:32 | RUNEUSDT | surge | 0.687 | 0.673 | -2.04% |
| 2026-10-30T06:32 | WLFIUSDT | surge | 0.0521 | 0.0514 | -1.34% |
| 2026-10-30T06:48 | TRXUSDT | bottom | 0.3341 | 0.3311 | -0.90% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
