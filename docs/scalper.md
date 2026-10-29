# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-29T19:00:26+00:00 · runs 4706 · equity **$599.13** (-40.09%) · cash $0.00 · open 10/10 · round trips 1674

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-396.66 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1460 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 214 | 43% | -0.49% | 36% | 44% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-29T07:43 | KATUSDT | surge | TARGET | 0.0 | +2.75% | $+1.61 |
| 2026-10-29T07:26 | KATUSDT | surge | TARGET | 3.8 | +2.75% | $+1.57 |
| 2026-10-29T02:48 | SOXLBUSDT | bottom | STOP | 0.8 | -3.25% | $-1.88 |
| 2026-10-29T02:15 | SNDKBUSDT | surge | STOP | 12.2 | -3.25% | $-1.91 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-29T01:59 | HBARUSDT | bottom | 0.07428 | 0.07306 | -1.64% |
| 2026-10-29T02:48 | BTCUSDT | bottom | 79714 | 80866 | +1.45% |
| 2026-10-29T05:27 | 币安人生USDT | surge | 0.5351 | 0.5373 | +0.41% |
| 2026-10-29T13:36 | 牛来USDT | surge | 0.06099 | 0.06057 | -0.69% |
| 2026-10-29T14:09 | BEBUSDT | surge | 225.94 | 219.96 | -2.65% |
| 2026-10-29T14:09 | XRPUSDT | bottom | 1.291 | 1.287 | -0.31% |
| 2026-10-29T14:31 | INJUSDT | surge | 8.058 | 7.994 | -0.79% |
| 2026-10-29T14:49 | BMNRBUSDT | surge | 21.93 | 21.61 | -1.46% |
| 2026-10-29T14:49 | UNIUSDT | surge | 7.307 | 7.19 | -1.60% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
