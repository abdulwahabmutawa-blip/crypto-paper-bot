# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-29T07:58:33+00:00 · runs 2080 · equity **$922.65** (-7.74%) · cash $0.00 · open 10/10 · round trips 771

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-82.56 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 658 | 53% | -0.04% | 50% | 43% | 7% |
| bottom | 113 | 44% | -0.44% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-29T02:39 | RUNEUSDT | surge | STOP | 6.8 | -3.25% | $-3.11 |
| 2026-09-28T23:32 | LINKUSDT | surge | TARGET | 3.5 | +2.75% | $+2.25 |
| 2026-09-28T23:15 | CRVUSDT | surge | TARGET | 1.5 | +2.75% | $+2.46 |
| 2026-09-28T21:35 | NMRUSDT | surge | STOP | 0.2 | -3.25% | $-3.01 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-28T12:08 | NVDABUSDT | surge | 227.9 | 230.25 | +1.03% |
| 2026-09-28T12:08 | JSTUSDT | surge | 0.12933 | 0.12997 | +0.49% |
| 2026-09-28T23:32 | GRAMUSDT | bottom | 1.574 | 1.587 | +0.83% |
| 2026-09-29T02:55 | CRCLBUSDT | bottom | 85 | 86.72 | +2.02% |
| 2026-09-29T04:01 | SPCXBUSDT | bottom | 145.83 | 146.5 | +0.46% |
| 2026-09-29T05:39 | CVXUSDT | surge | 2.268 | 2.274 | +0.26% |
| 2026-09-29T06:28 | CELOUSDT | surge | 0.10376 | 0.10481 | +1.01% |
| 2026-09-29T06:44 | CRVUSDT | surge | 0.3959 | 0.3971 | +0.30% |
| 2026-09-29T07:56 | ICPUSDT | surge | 3.386 | 3.364 | -0.65% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
