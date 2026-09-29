# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T14:22:39+00:00 · runs 2103 · equity **$919.30** (-8.07%) · cash $0.00 · open 10/10 · round trips 782

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-80.45 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 667 | 53% | -0.04% | 50% | 43% | 7% |
| bottom | 115 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29T14:20 | GRAMUSDT | bottom | STOP | 14.5 | -3.25% | $-2.73 |
| 2026-09-29T13:45 | INITUSDT | surge | TARGET | 1.2 | +2.75% | $+2.58 |
| 2026-09-29T12:46 | 币安人生USDT | surge | STOP | 3.0 | -3.25% | $-2.88 |
| 2026-09-29T12:29 | BABYUSDT | surge | TARGET | 1.5 | +2.75% | $+2.64 |
| 2026-09-29T12:29 | CRCLBUSDT | bottom | TARGET | 9.5 | +2.75% | $+2.48 |
| 2026-09-29T12:29 | JSTUSDT | surge | TIME | 24.0 | +0.49% | $+0.45 |
| 2026-09-29T12:29 | NVDABUSDT | surge | TIME | 24.0 | +1.07% | $+0.98 |
| 2026-09-29T10:47 | ICPUSDT | surge | STOP | 2.8 | -3.25% | $-3.22 |
| 2026-09-29T10:13 | CELOUSDT | surge | STOP | 1.2 | -3.25% | $-3.22 |
| 2026-09-29T09:39 | CVXUSDT | surge | TARGET | 3.8 | +2.75% | $+2.37 |
| 2026-09-29T08:30 | CELOUSDT | surge | TARGET | 2.0 | +2.75% | $+2.65 |
| 2026-09-29T07:56 | AAVEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.65 |
| 2026-09-29T06:44 | CRVUSDT | surge | TARGET | 2.2 | +2.75% | $+2.61 |
| 2026-09-29T06:28 | PHAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.55 |
| 2026-09-29T06:28 | ICPUSDT | surge | TARGET | 2.0 | +2.75% | $+2.61 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 146.07 | +0.16% |
| 2026-09-29T06:44 | CRVUSDT | surge | 0.3959 | 0.3988 | +0.73% |
| 2026-09-29T10:13 | ATOMUSDT | surge | 1.778 | 1.766 | -0.67% |
| 2026-09-29T12:29 | BABYUSDT | surge | 0.01387 | 0.01411 | +1.73% |
| 2026-09-29T12:29 | AAVEUSDT | surge | 171.83 | 173.62 | +1.04% |
| 2026-09-29T12:29 | COMPUSDT | surge | 25.37 | 25.2 | -0.67% |
| 2026-09-29T12:46 | COINBUSDT | surge | 197.33 | 193.33 | -2.03% |
| 2026-09-29T13:45 | BNCBUSDT | surge | 6.01 | 5.99 | -0.33% |
| 2026-09-29T14:20 | ALICEUSDT | surge | 0.1666 | 0.1658 | -0.48% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
