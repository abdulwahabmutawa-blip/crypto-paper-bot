# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-29T12:32:09+00:00 · runs 4683 · equity **$604.99** (-39.50%) · cash $173.70 · open 7/10 · round trips 1667

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-395.23 · worst day $-50.94 · trades/day 30.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1454 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 213 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-29T00:04 | DRAMBUSDT | surge | STOP | 5.0 | -3.25% | $-1.97 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-28T13:49 | SPCXBUSDT | bottom | 144.87 | 143.28 | -1.10% |
| 2026-10-29T01:59 | SOXSBUSDT | surge | 42.98 | 42.61 | -0.86% |
| 2026-10-29T01:59 | HBARUSDT | bottom | 0.07428 | 0.07384 | -0.59% |
| 2026-10-29T02:48 | BTCUSDT | bottom | 79714 | 80196.1 | +0.60% |
| 2026-10-29T05:27 | 币安人生USDT | surge | 0.5351 | 0.5374 | +0.43% |
| 2026-10-29T11:57 | HUMAUSDT | surge | 0.02906 | 0.02963 | +1.96% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
