# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T15:51:04+00:00 · runs 2108 · equity **$908.27** (-9.17%) · cash $0.00 · open 10/10 · round trips 790

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-87.66 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 675 | 53% | -0.05% | 50% | 43% | 7% |
| bottom | 115 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29T15:31 | ALICEUSDT | surge | STOP | 0.2 | -3.25% | $-3.03 |
| 2026-09-29T15:31 | BONKUSDT | surge | STOP | 0.5 | -3.25% | $-2.71 |
| 2026-09-29T15:31 | COMPUSDT | surge | STOP | 3.0 | -3.25% | $-3.05 |
| 2026-09-29T15:13 | BNCBUSDT | surge | STOP | 1.2 | -3.25% | $-3.13 |
| 2026-09-29T15:13 | COINBUSDT | surge | STOP | 2.2 | -3.25% | $-2.78 |
| 2026-09-29T15:13 | BABYUSDT | surge | TARGET | 2.5 | +2.75% | $+2.58 |
| 2026-09-29T15:13 | CRVUSDT | surge | TARGET | 8.2 | +2.75% | $+2.69 |
| 2026-09-29T14:55 | ALICEUSDT | surge | TARGET | 0.2 | +2.75% | $+2.23 |
| 2026-09-29T14:20 | GRAMUSDT | bottom | STOP | 14.5 | -3.25% | $-2.73 |
| 2026-09-29T13:45 | INITUSDT | surge | TARGET | 1.2 | +2.75% | $+2.58 |
| 2026-09-29T12:46 | 币安人生USDT | surge | STOP | 3.0 | -3.25% | $-2.88 |
| 2026-09-29T12:29 | BABYUSDT | surge | TARGET | 1.5 | +2.75% | $+2.64 |
| 2026-09-29T12:29 | CRCLBUSDT | bottom | TARGET | 9.5 | +2.75% | $+2.48 |
| 2026-09-29T12:29 | JSTUSDT | surge | TIME | 24.0 | +0.49% | $+0.45 |
| 2026-09-29T12:29 | NVDABUSDT | surge | TIME | 24.0 | +1.07% | $+0.98 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 148.24 | +1.65% |
| 2026-09-29T10:13 | ATOMUSDT | surge | 1.778 | 1.748 | -1.69% |
| 2026-09-29T12:29 | AAVEUSDT | surge | 171.83 | 170.97 | -0.50% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 187.24 | -0.35% |
| 2026-09-29T15:13 | REUSDT | surge | 0.5002 | 0.4901 | -2.02% |
| 2026-09-29T15:13 | SPKUSDT | surge | 0.024311 | 0.02389 | -1.73% |
| 2026-09-29T15:31 | NIGHTUSDT | surge | 0.03196 | 0.03186 | -0.31% |
| 2026-09-29T15:31 | JASMYUSDT | surge | 0.00532 | 0.00535 | +0.56% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01636 | +0.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
