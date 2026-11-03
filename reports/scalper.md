# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-03T16:44:54+00:00 · runs 5104 · equity **$560.86** (-43.91%) · cash $0.00 · open 10/10 · round trips 1781

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-438.14 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1546 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 235 | 42% | -0.54% | 36% | 46% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-03T16:42 | BABABUSDT | surge | STOP | 23.5 | -3.25% | $-1.77 |
| 2026-11-03T14:41 | CHIPUSDT | surge | TARGET | 1.5 | +2.75% | $+1.38 |
| 2026-11-03T14:41 | RUNEUSDT | surge | TARGET | 5.0 | +2.75% | $+1.38 |
| 2026-11-03T14:41 | WLFIUSDT | surge | TARGET | 7.8 | +2.75% | $+1.39 |
| 2026-11-03T12:03 | STRKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.34 |
| 2026-11-03T10:25 | MEGAUSDT | surge | STOP | 2.8 | -3.25% | $-1.64 |
| 2026-11-03T05:29 | 1000CATUSDT | bottom | STOP | 0.5 | -3.25% | $-1.64 |
| 2026-11-03T04:56 | MEGAUSDT | surge | STOP | 6.8 | -3.25% | $-1.74 |
| 2026-11-03T03:48 | HAEDALUSDT | surge | STOP | 3.5 | -3.25% | $-1.76 |
| 2026-11-03T03:14 | PROMUSDT | bottom | STOP | 19.8 | -3.25% | $-1.60 |
| 2026-11-03T01:50 | SOXSBUSDT | surge | STOP | 3.8 | -3.25% | $-1.74 |
| 2026-11-02T23:51 | KORUBUSDT | bottom | TARGET | 2.2 | +2.75% | $+1.47 |
| 2026-11-02T20:48 | TQQQBUSDT | bottom | STOP | 1.5 | -3.25% | $-1.76 |
| 2026-11-02T20:48 | SPCXBUSDT | surge | STOP | 3.8 | -3.25% | $-1.77 |
| 2026-11-02T19:59 | HOTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.49 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-02T16:59 | TSLABUSDT | surge | 410.69 | 398.61 | -2.94% |
| 2026-11-02T16:59 | COWUSDT | surge | 0.1187 | 0.1194 | +0.59% |
| 2026-11-02T19:59 | FETUSDT | bottom | 0.1538 | 0.1552 | +0.91% |
| 2026-11-02T23:51 | XLMUSDT | bottom | 0.1628 | 0.1633 | +0.31% |
| 2026-11-03T06:36 | QQQBUSDT | bottom | 680.99 | 686.27 | +0.78% |
| 2026-11-03T14:41 | BOMEUSDT | surge | 0.0006236 | 0.0006237 | +0.02% |
| 2026-11-03T14:41 | WLFIUSDT | surge | 0.0518 | 0.0512 | -1.16% |
| 2026-11-03T14:41 | PUMPUSDT | surge | 0.004189 | 0.004207 | +0.43% |
| 2026-11-03T16:42 | BEBUSDT | surge | 214.5 | 212.86 | -0.76% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
