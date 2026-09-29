# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T14:58:00+00:00 · runs 2105 · equity **$927.69** (-7.23%) · cash $0.00 · open 10/10 · round trips 783

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-78.22 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 668 | 53% | -0.03% | 50% | 43% | 7% |
| bottom | 115 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29T14:55 | ALICEUSDT | surge | TARGET | 0.2 | +2.75% | $+2.23 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 148.75 | +2.00% |
| 2026-09-29T06:44 | CRVUSDT | surge | 0.3959 | 0.4079 | +3.03% |
| 2026-09-29T10:13 | ATOMUSDT | surge | 1.778 | 1.779 | +0.06% |
| 2026-09-29T12:29 | BABYUSDT | surge | 0.01387 | 0.01425 | +2.74% |
| 2026-09-29T12:29 | AAVEUSDT | surge | 171.83 | 174.49 | +1.55% |
| 2026-09-29T12:29 | COMPUSDT | surge | 25.37 | 25.05 | -1.26% |
| 2026-09-29T12:46 | COINBUSDT | surge | 197.33 | 192.8 | -2.30% |
| 2026-09-29T13:45 | BNCBUSDT | surge | 6.01 | 5.99 | -0.33% |
| 2026-09-29T14:55 | BONKUSDT | surge | 3.78e-06 | 3.8e-06 | +0.53% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
