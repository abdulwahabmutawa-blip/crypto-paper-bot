# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T07:44:34+00:00 · runs 5156 · equity **$553.26** (-44.67%) · cash $0.00 · open 10/10 · round trips 1809

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-451.27 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1569 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 240 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-04T01:15 | AMDBUSDT | surge | STOP | 0.8 | -3.25% | $-1.63 |
| 2026-11-04T00:58 | BEBUSDT | surge | STOP | 2.8 | -3.25% | $-1.70 |
| 2026-11-04T00:58 | ZROUSDT | surge | STOP | 7.5 | -3.25% | $-1.74 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-04T00:41 | LINKUSDT | bottom | 10.925 | 11.136 | +1.93% |
| 2026-11-04T05:04 | ONDOUSDT | surge | 0.3905 | 0.4008 | +2.64% |
| 2026-11-04T05:22 | AEROUSDT | surge | 0.6239 | 0.6286 | +0.75% |
| 2026-11-04T05:22 | ICPUSDT | surge | 2.485 | 2.535 | +2.01% |
| 2026-11-04T05:22 | AMDBUSDT | surge | 515.6 | 517.73 | +0.41% |
| 2026-11-04T06:32 | DOGEUSDT | surge | 0.07481 | 0.07505 | +0.32% |
| 2026-11-04T06:49 | ARUSDT | surge | 3.169 | 3.191 | +0.69% |
| 2026-11-04T07:07 | BABABUSDT | surge | 102.49 | 102.49 | +0.00% |
| 2026-11-04T07:42 | METABUSDT | surge | 621.26 | 621.74 | +0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
