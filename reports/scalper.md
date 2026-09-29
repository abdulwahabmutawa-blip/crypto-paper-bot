# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T11:23:29+00:00 · runs 2092 · equity **$920.39** (-7.96%) · cash $0.00 · open 10/10 · round trips 775

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-83.98 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 662 | 53% | -0.05% | 50% | 43% | 7% |
| bottom | 113 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-29T10:47 | ICPUSDT | surge | STOP | 2.8 | -3.25% | $-3.22 |
| 2026-09-29T10:13 | CELOUSDT | surge | STOP | 1.2 | -3.25% | $-3.22 |
| 2026-09-29T09:39 | CVXUSDT | surge | TARGET | 3.8 | +2.75% | $+2.37 |
| 2026-09-29T08:30 | CELOUSDT | surge | TARGET | 2.0 | +2.75% | $+2.65 |
| 2026-09-29T07:56 | AAVEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.65 |
| 2026-09-29T06:44 | CRVUSDT | surge | TARGET | 2.2 | +2.75% | $+2.61 |
| 2026-09-29T06:28 | PHAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.55 |
| 2026-09-29T06:28 | ICPUSDT | surge | TARGET | 2.0 | +2.75% | $+2.61 |
| 2026-09-29T05:55 | XLMUSDT | surge | STOP | 10.0 | -3.25% | $-3.11 |
| 2026-09-29T05:39 | DODOUSDT | surge | STOP | 13.8 | -3.25% | $-2.90 |
| 2026-09-29T04:01 | ICPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.62 |
| 2026-09-29T04:01 | MINAUSDT | surge | STOP | 4.5 | -3.25% | $-2.99 |
| 2026-09-29T04:01 | ALGOUSDT | surge | TARGET | 8.2 | +2.75% | $+2.63 |
| 2026-09-29T03:44 | CRVUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-29T02:55 | PROMUSDT | surge | STOP | 13.5 | -3.25% | $-3.03 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 230.43 | +1.11% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.13082 | +1.15% |
| 2026-09-28T23:32 | GRAMUSDT | bottom | 1.574 | 1.575 | +0.06% |
| 2026-09-29T02:55 | CRCLBUSDT | bottom | 85 | 86.66 | +1.95% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 146.97 | +0.78% |
| 2026-09-29T06:44 | CRVUSDT | surge | 0.3959 | 0.3938 | -0.53% |
| 2026-09-29T09:39 | 币安人生USDT | surge | 0.5147 | 0.511 | -0.72% |
| 2026-09-29T10:13 | ATOMUSDT | surge | 1.778 | 1.771 | -0.39% |
| 2026-09-29T10:47 | BABYUSDT | surge | 0.01356 | 0.01374 | +1.33% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
