# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T05:24:26+00:00 · runs 5148 · equity **$547.04** (-45.30%) · cash $0.00 · open 10/10 · round trips 1803

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-455.29 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1565 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 238 | 42% | -0.55% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-04T05:04 | SOXSBUSDT | surge | STOP | 0.0 | -3.25% | $-1.67 |
| 2026-11-04T04:29 | LSKUSDT | surge | TARGET | 1.0 | +2.75% | $+1.39 |
| 2026-11-04T03:20 | SOXSBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.39 |
| 2026-11-04T03:20 | AEROUSDT | surge | STOP | 5.2 | -3.25% | $-1.70 |
| 2026-11-04T03:20 | POLUSDT | surge | STOP | 8.2 | -3.25% | $-1.76 |
| 2026-11-04T01:48 | TRUMPUSDT | bottom | STOP | 1.0 | -3.25% | $-1.67 |
| 2026-11-04T01:15 | AMDBUSDT | surge | STOP | 0.8 | -3.25% | $-1.63 |
| 2026-11-04T00:58 | BEBUSDT | surge | STOP | 2.8 | -3.25% | $-1.70 |
| 2026-11-04T00:58 | ZROUSDT | surge | STOP | 7.5 | -3.25% | $-1.74 |
| 2026-11-04T00:41 | SNXXBUSDT | surge | STOP | 0.2 | -3.25% | $-1.75 |
| 2026-11-04T00:41 | PYTHUSDT | surge | STOP | 4.2 | -3.25% | $-1.76 |
| 2026-11-04T00:41 | BOMEUSDT | surge | STOP | 9.8 | -3.25% | $-1.68 |
| 2026-11-04T00:24 | WLFIUSDT | surge | STOP | 9.5 | -3.25% | $-1.68 |
| 2026-11-04T00:07 | XLMUSDT | bottom | TIME | 24.0 | -0.56% | $-0.30 |
| 2026-11-03T21:53 | RUNEUSDT | surge | STOP | 1.0 | -3.25% | $-1.70 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-03T06:36 | QQQBUSDT | bottom | 680.99 | 680.61 | -0.06% |
| 2026-11-04T00:41 | LINKUSDT | bottom | 10.925 | 10.959 | +0.31% |
| 2026-11-04T01:48 | HYPEUSDT | bottom | 81.77 | 84.36 | +3.17% |
| 2026-11-04T05:04 | RAYUSDT | surge | 1.5431 | 1.545 | +0.12% |
| 2026-11-04T05:04 | ONDOUSDT | surge | 0.3905 | 0.3912 | +0.18% |
| 2026-11-04T05:22 | AEROUSDT | surge | 0.6239 | 0.6243 | +0.06% |
| 2026-11-04T05:22 | BONKUSDT | surge | 2.9e-06 | 2.92e-06 | +0.69% |
| 2026-11-04T05:22 | ICPUSDT | surge | 2.485 | 2.497 | +0.48% |
| 2026-11-04T05:22 | AMDBUSDT | surge | 515.6 | 513.68 | -0.37% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
