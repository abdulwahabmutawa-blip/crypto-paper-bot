# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-29T23:53:12+00:00 · runs 4724 · equity **$587.24** (-41.28%) · cash $445.31 · open 2/10 · round trips 1682

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-411.61 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1466 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 216 | 43% | -0.51% | 36% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-29T12:47 | HUMAUSDT | surge | TARGET | 0.8 | +2.75% | $+1.56 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-29T02:48 | BTCUSDT | bottom | 79714 | 78114 | -2.01% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
