# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-03T18:29:39+00:00 · runs 5110 · equity **$562.11** (-43.79%) · cash $0.00 · open 10/10 · round trips 1783

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.33%/trade · realized $-439.91 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1548 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 235 | 42% | -0.54% | 36% | 46% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-03T17:00 | COWUSDT | surge | TIME | 24.0 | +0.00% | $+0.00 |
| 2026-11-03T17:00 | TSLABUSDT | surge | STOP | 23.8 | -3.25% | $-1.77 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-02T19:59 | FETUSDT | bottom | 0.1538 | 0.1545 | +0.46% |
| 2026-11-02T23:51 | XLMUSDT | bottom | 0.1628 | 0.1638 | +0.61% |
| 2026-11-03T06:36 | QQQBUSDT | bottom | 680.99 | 687.96 | +1.02% |
| 2026-11-03T14:41 | BOMEUSDT | surge | 0.0006236 | 0.0006241 | +0.08% |
| 2026-11-03T14:41 | WLFIUSDT | surge | 0.0518 | 0.0509 | -1.74% |
| 2026-11-03T14:41 | PUMPUSDT | surge | 0.004189 | 0.004257 | +1.62% |
| 2026-11-03T16:42 | BEBUSDT | surge | 214.5 | 214.92 | +0.20% |
| 2026-11-03T17:00 | KMNOUSDT | surge | 0.03366 | 0.03447 | +2.41% |
| 2026-11-03T17:00 | ZROUSDT | surge | 1.9 | 1.884 | -0.84% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
