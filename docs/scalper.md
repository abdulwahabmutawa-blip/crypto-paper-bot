# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T10:46:02+00:00 · runs 1133 · equity **$935.47** (-6.45%) · cash $0.00 · open 10/10 · round trips 385

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.18%/trade · realized $-71.67 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 303 | 52% | -0.09% | 48% | 43% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-18T10:44 | DODOUSDT | surge | TIME | 24.0 | +1.13% | $+0.97 |
| 2026-09-18T10:12 | RENDERUSDT | surge | TARGET | 8.5 | +2.75% | $+2.65 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-17T15:38 | INTCBUSDT | surge | 109.9 | 111.95 | +1.87% |
| 2026-09-18T01:20 | AXSUSDT | surge | 0.995 | 0.999 | +0.40% |
| 2026-09-18T03:31 | BCHUSDT | surge | 246.2 | 249.1 | +1.18% |
| 2026-09-18T04:24 | TRBUSDT | surge | 17.56 | 18.01 | +2.56% |
| 2026-09-18T04:41 | SEIUSDT | surge | 0.04638 | 0.04737 | +2.13% |
| 2026-09-18T07:24 | 币安人生USDT | surge | 0.5254 | 0.5152 | -1.94% |
| 2026-09-18T08:29 | AUSDT | surge | 0.0852 | 0.0859 | +0.82% |
| 2026-09-18T10:12 | ZKUSDT | surge | 0.01024 | 0.01024 | +0.00% |
| 2026-09-18T10:44 | BANKUSDT | surge | 0.0298 | 0.0299 | +0.34% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
