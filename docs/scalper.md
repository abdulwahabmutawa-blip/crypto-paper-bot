# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T02:28:54+00:00 · runs 5138 · equity **$545.93** (-45.41%) · cash $151.34 · open 7/10 · round trips 1798

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-452.94 · worst day $-50.94 · trades/day 29.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1560 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 238 | 42% | -0.55% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-03T21:53 | BEBUSDT | surge | TARGET | 5.0 | +2.75% | $+1.45 |
| 2026-11-03T20:40 | SAGAUSDT | surge | STOP | 1.5 | -3.25% | $-1.76 |
| 2026-11-03T20:14 | FETUSDT | bottom | TIME | 24.0 | +0.01% | $+0.01 |
| 2026-11-03T18:45 | KMNOUSDT | surge | TARGET | 1.5 | +2.75% | $+1.48 |
| 2026-11-03T18:45 | PUMPUSDT | surge | TARGET | 4.0 | +2.75% | $+1.42 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-03T06:36 | QQQBUSDT | bottom | 680.99 | 673.49 | -1.10% |
| 2026-11-03T18:45 | POLUSDT | surge | 0.09274 | 0.09071 | -2.19% |
| 2026-11-03T21:53 | AEROUSDT | surge | 0.6215 | 0.6209 | -0.10% |
| 2026-11-04T00:41 | LINKUSDT | bottom | 10.925 | 10.833 | -0.84% |
| 2026-11-04T01:15 | SOXSBUSDT | surge | 56.76 | 57.72 | +1.69% |
| 2026-11-04T01:48 | HYPEUSDT | bottom | 81.77 | 82.16 | +0.48% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
