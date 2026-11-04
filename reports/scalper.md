# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T13:50:12+00:00 · runs 5178 · equity **$552.58** (-44.74%) · cash $-0.00 · open 10/10 · round trips 1812

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.33%/trade · realized $-450.12 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1572 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 240 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-04T12:23 | AMDBUSDT | surge | STOP | 6.8 | -3.25% | $-1.66 |
| 2026-11-04T12:06 | ICPUSDT | surge | TARGET | 6.5 | +2.75% | $+1.40 |
| 2026-11-04T08:22 | ONDOUSDT | surge | TARGET | 3.0 | +2.75% | $+1.40 |
| 2026-11-04T07:42 | LSKUSDT | surge | STOP | 0.5 | -3.25% | $-1.69 |
| 2026-11-04T07:07 | RAYUSDT | surge | TARGET | 1.8 | +2.75% | $+1.40 |
| 2026-11-04T06:49 | ZAMAUSDT | surge | TARGET | 1.0 | +2.75% | $+1.43 |
| 2026-11-04T06:49 | QQQBUSDT | bottom | TIME | 24.0 | +0.16% | $+0.08 |
| 2026-11-04T06:32 | BONKUSDT | surge | TARGET | 1.0 | +2.75% | $+1.40 |
| 2026-11-04T05:39 | HYPEUSDT | bottom | TARGET | 3.5 | +2.75% | $+1.39 |
| 2026-11-04T05:04 | SOXSBUSDT | surge | STOP | 0.0 | -3.25% | $-1.67 |
| 2026-11-04T04:29 | LSKUSDT | surge | TARGET | 1.0 | +2.75% | $+1.39 |
| 2026-11-04T03:20 | SOXSBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.39 |
| 2026-11-04T03:20 | AEROUSDT | surge | STOP | 5.2 | -3.25% | $-1.70 |
| 2026-11-04T03:20 | POLUSDT | surge | STOP | 8.2 | -3.25% | $-1.76 |
| 2026-11-04T01:48 | TRUMPUSDT | bottom | STOP | 1.0 | -3.25% | $-1.67 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-04T00:41 | LINKUSDT | bottom | 10.925 | 11.151 | +2.07% |
| 2026-11-04T05:22 | AEROUSDT | surge | 0.6239 | 0.6246 | +0.11% |
| 2026-11-04T06:32 | DOGEUSDT | surge | 0.07481 | 0.07479 | -0.03% |
| 2026-11-04T06:49 | ARUSDT | surge | 3.169 | 3.16 | -0.28% |
| 2026-11-04T07:07 | BABABUSDT | surge | 102.49 | 105.13 | +2.58% |
| 2026-11-04T07:42 | METABUSDT | surge | 621.26 | 627.24 | +0.96% |
| 2026-11-04T08:22 | TIAUSDT | surge | 0.449 | 0.442 | -1.56% |
| 2026-11-04T12:06 | MUBARAKUSDT | surge | 0.0427 | 0.04321 | +1.19% |
| 2026-11-04T12:23 | STXUSDT | surge | 0.345 | 0.3457 | +0.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
