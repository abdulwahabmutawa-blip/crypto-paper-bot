# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T09:20:10+00:00 · runs 1127 · equity **$932.54** (-6.75%) · cash $0.00 · open 10/10 · round trips 383

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.19%/trade · realized $-75.29 · worst day $-50.94 · trades/day 27.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 301 | 52% | -0.10% | 48% | 44% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-18T08:29 | BMNRBUSDT | surge | TARGET | 16.0 | +2.75% | $+2.28 |
| 2026-09-18T07:24 | REZUSDT | surge | STOP | 1.2 | -3.25% | $-3.04 |
| 2026-09-18T05:46 | 币安人生USDT | surge | TARGET | 2.0 | +2.75% | $+2.50 |
| 2026-09-18T04:41 | AUSDT | surge | TARGET | 3.0 | +2.75% | $+2.65 |
| 2026-09-18T04:24 | SEIUSDT | surge | TARGET | 1.5 | +2.75% | $+2.73 |
| 2026-09-18T03:31 | COINBUSDT | surge | TARGET | 13.0 | +2.75% | $+2.40 |
| 2026-09-18T03:31 | CAKEUSDT | surge | TARGET | 14.8 | +2.75% | $+2.47 |
| 2026-09-18T02:42 | APTUSDT | surge | TARGET | 0.8 | +2.75% | $+2.66 |
| 2026-09-18T01:37 | APTUSDT | surge | TARGET | 0.8 | +2.75% | $+2.58 |
| 2026-09-18T01:20 | AXSUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-18T01:20 | PHAUSDT | surge | STOP | 0.8 | -3.25% | $-3.13 |
| 2026-09-18T01:20 | AUSDT | surge | TARGET | 7.8 | +2.75% | $+2.65 |
| 2026-09-18T00:32 | KORUBUSDT | surge | STOP | 7.8 | -3.25% | $-3.05 |
| 2026-09-18T00:32 | TRUMPUSDT | surge | TIME | 24.0 | +0.37% | $+0.36 |
| 2026-09-18T00:15 | ROSEUSDT | surge | STOP | 0.2 | -3.25% | $-3.23 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-17T10:23 | DODOUSDT | surge | 0.01812 | 0.01817 | +0.28% |
| 2026-09-17T15:38 | INTCBUSDT | surge | 109.9 | 111.45 | +1.41% |
| 2026-09-18T01:20 | AXSUSDT | surge | 0.995 | 1 | +0.50% |
| 2026-09-18T01:20 | RENDERUSDT | surge | 1.477 | 1.513 | +2.44% |
| 2026-09-18T03:31 | BCHUSDT | surge | 246.2 | 249.2 | +1.22% |
| 2026-09-18T04:24 | TRBUSDT | surge | 17.56 | 17.77 | +1.20% |
| 2026-09-18T04:41 | SEIUSDT | surge | 0.04638 | 0.04691 | +1.14% |
| 2026-09-18T07:24 | 币安人生USDT | surge | 0.5254 | 0.5167 | -1.66% |
| 2026-09-18T08:29 | AUSDT | surge | 0.0852 | 0.0867 | +1.76% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
