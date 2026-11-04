# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T00:09:32+00:00 · runs 5129 · equity **$557.40** (-44.26%) · cash $0.00 · open 10/10 · round trips 1790

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-439.32 · worst day $-50.94 · trades/day 29.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1553 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 237 | 42% | -0.54% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-03T14:41 | RUNEUSDT | surge | TARGET | 5.0 | +2.75% | $+1.38 |
| 2026-11-03T14:41 | WLFIUSDT | surge | TARGET | 7.8 | +2.75% | $+1.39 |
| 2026-11-03T12:03 | STRKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.34 |
| 2026-11-03T10:25 | MEGAUSDT | surge | STOP | 2.8 | -3.25% | $-1.64 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-03T06:36 | QQQBUSDT | bottom | 680.99 | 687.79 | +1.00% |
| 2026-11-03T14:41 | BOMEUSDT | surge | 0.0006236 | 0.0006111 | -2.00% |
| 2026-11-03T14:41 | WLFIUSDT | surge | 0.0518 | 0.0513 | -0.97% |
| 2026-11-03T17:00 | ZROUSDT | surge | 1.9 | 1.874 | -1.37% |
| 2026-11-03T18:45 | POLUSDT | surge | 0.09274 | 0.09198 | -0.82% |
| 2026-11-03T20:14 | PYTHUSDT | surge | 0.06578 | 0.06462 | -1.76% |
| 2026-11-03T21:53 | BEBUSDT | surge | 222.62 | 220.8 | -0.82% |
| 2026-11-03T21:53 | AEROUSDT | surge | 0.6215 | 0.6252 | +0.60% |
| 2026-11-04T00:07 | SNXXBUSDT | surge | 6.53 | 6.53 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
