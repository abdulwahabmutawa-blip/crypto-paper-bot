# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-29T12:48:35+00:00 · runs 4684 · equity **$605.16** (-39.48%) · cash $116.09 · open 8/10 · round trips 1668

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-393.67 · worst day $-50.94 · trades/day 30.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1455 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 213 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-29T12:47 | HUMAUSDT | surge | TARGET | 0.8 | +2.75% | $+1.56 |
| 2026-10-29T12:30 | BNBUSDT | surge | TIME | 24.0 | -2.32% | $-1.42 |
| 2026-10-29T11:41 | HUMAUSDT | surge | TARGET | 3.8 | +2.75% | $+1.65 |
| 2026-10-29T09:46 | AIUSDT | surge | STOP | 7.0 | -3.25% | $-1.87 |
| 2026-10-29T09:13 | LTCUSDT | surge | STOP | 16.5 | -3.25% | $-1.79 |
| 2026-10-29T07:43 | KATUSDT | surge | TARGET | 0.0 | +2.75% | $+1.61 |
| 2026-10-29T07:26 | KATUSDT | surge | TARGET | 3.8 | +2.75% | $+1.57 |
| 2026-10-29T02:48 | SOXLBUSDT | bottom | STOP | 0.8 | -3.25% | $-1.88 |
| 2026-10-29T02:15 | SNDKBUSDT | surge | STOP | 12.2 | -3.25% | $-1.91 |
| 2026-10-29T01:59 | ETHFIUSDT | surge | STOP | 1.2 | -3.25% | $-1.95 |
| 2026-10-29T01:59 | INJUSDT | surge | STOP | 1.5 | -3.25% | $-1.91 |
| 2026-10-29T01:59 | PUMPUSDT | surge | STOP | 3.0 | -3.25% | $-1.84 |
| 2026-10-29T01:59 | RAYUSDT | surge | STOP | 4.8 | -3.25% | $-1.88 |
| 2026-10-29T01:59 | EWYBUSDT | surge | TIME | 24.0 | -1.65% | $-1.06 |
| 2026-10-29T00:37 | TIAUSDT | surge | STOP | 4.0 | -3.25% | $-2.02 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-28T13:49 | SPCXBUSDT | bottom | 144.87 | 143.02 | -1.28% |
| 2026-10-29T01:59 | SOXSBUSDT | surge | 42.98 | 42.72 | -0.60% |
| 2026-10-29T01:59 | HBARUSDT | bottom | 0.07428 | 0.07403 | -0.34% |
| 2026-10-29T02:48 | BTCUSDT | bottom | 79714 | 80044 | +0.41% |
| 2026-10-29T05:27 | 币安人生USDT | surge | 0.5351 | 0.537 | +0.36% |
| 2026-10-29T12:47 | 牛来USDT | surge | 0.06037 | 0.06014 | -0.38% |
| 2026-10-29T12:47 | HUMAUSDT | surge | 0.02995 | 0.0299 | -0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
