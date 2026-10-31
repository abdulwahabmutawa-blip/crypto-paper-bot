# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-31T06:16:50+00:00 · runs 4833 · equity **$587.91** (-41.21%) · cash $111.97 · open 8/10 · round trips 1692

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-413.07 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1474 | 49% | -0.28% | 46% | 47% | 7% |
| bottom | 218 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-31T05:59 | SPKUSDT | surge | TARGET | 1.2 | +2.75% | $+1.53 |
| 2026-10-31T04:05 | SPKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.52 |
| 2026-10-31T03:49 | OPUSDT | surge | STOP | 3.5 | -3.25% | $-1.81 |
| 2026-10-31T02:02 | HAEDALUSDT | surge | TARGET | 1.5 | +2.75% | $+1.53 |
| 2026-10-31T00:54 | TRXUSDT | bottom | STOP | 17.8 | -3.25% | $-1.81 |
| 2026-10-30T23:46 | OPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.52 |
| 2026-10-30T15:50 | XPLUSDT | surge | TARGET | 8.8 | +2.75% | $+1.53 |
| 2026-10-30T10:41 | WLFIUSDT | surge | STOP | 3.8 | -3.25% | $-1.81 |
| 2026-10-30T07:58 | RUNEUSDT | surge | STOP | 1.2 | -3.25% | $-1.81 |
| 2026-10-30T00:41 | BTCUSDT | bottom | STOP | 21.5 | -3.25% | $-1.85 |
| 2026-10-29T20:48 | XRPUSDT | bottom | STOP | 6.5 | -3.25% | $-1.89 |
| 2026-10-29T20:48 | 牛来USDT | surge | STOP | 7.0 | -3.25% | $-1.89 |
| 2026-10-29T20:48 | 币安人生USDT | surge | STOP | 15.2 | -3.25% | $-1.85 |
| 2026-10-29T20:48 | HBARUSDT | bottom | STOP | 18.8 | -3.25% | $-1.88 |
| 2026-10-29T20:14 | UNIUSDT | surge | STOP | 5.2 | -3.25% | $-1.85 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T23:29 | HYPEUSDT | bottom | 89.24 | 88.24 | -1.12% |
| 2026-10-30T23:46 | PENDLEUSDT | surge | 1.848 | 1.863 | +0.81% |
| 2026-10-31T04:05 | PEPEUSDT | bottom | 4.93e-06 | 4.97e-06 | +0.81% |
| 2026-10-31T04:54 | ARBUSDT | bottom | 0.16 | 0.1629 | +1.81% |
| 2026-10-31T05:10 | RADUSDT | surge | 0.244 | 0.245 | +0.41% |
| 2026-10-31T05:42 | GTCUSDT | surge | 0.23139 | 0.23136 | -0.01% |
| 2026-10-31T06:15 | SPKUSDT | surge | 0.020139 | 0.019947 | -0.95% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
