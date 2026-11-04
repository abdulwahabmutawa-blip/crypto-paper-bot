# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T00:43:10+00:00 · runs 5131 · equity **$547.92** (-45.21%) · cash $51.52 · open 9/10 · round trips 1794

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-446.19 · worst day $-50.94 · trades/day 29.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1557 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 237 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-03T17:00 | COWUSDT | surge | TIME | 24.0 | +0.00% | $+0.00 |
| 2026-11-03T17:00 | TSLABUSDT | surge | STOP | 23.8 | -3.25% | $-1.77 |
| 2026-11-03T16:42 | BABABUSDT | surge | STOP | 23.5 | -3.25% | $-1.77 |
| 2026-11-03T14:41 | CHIPUSDT | surge | TARGET | 1.5 | +2.75% | $+1.38 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-03T06:36 | QQQBUSDT | bottom | 680.99 | 680.88 | -0.02% |
| 2026-11-03T17:00 | ZROUSDT | surge | 1.9 | 1.844 | -2.95% |
| 2026-11-03T18:45 | POLUSDT | surge | 0.09274 | 0.09103 | -1.84% |
| 2026-11-03T21:53 | BEBUSDT | surge | 222.62 | 215.65 | -3.13% |
| 2026-11-03T21:53 | AEROUSDT | surge | 0.6215 | 0.6146 | -1.11% |
| 2026-11-04T00:24 | AMDBUSDT | surge | 515.65 | 506.87 | -1.70% |
| 2026-11-04T00:41 | TRUMPUSDT | bottom | 1.544 | 1.545 | +0.06% |
| 2026-11-04T00:41 | LINKUSDT | bottom | 10.925 | 10.871 | -0.49% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
