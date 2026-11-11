# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-11T21:20:25+00:00 · runs 5765 · equity **$509.05** (-49.09%) · cash $0.00 · open 10/10 · round trips 1963

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-488.12 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1699 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 264 | 42% | -0.55% | 36% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-11T21:18 | OPENUSDT | surge | STOP | 9.2 | -3.25% | $-1.58 |
| 2026-11-11T19:53 | KITEUSDT | surge | STOP | 5.2 | -3.25% | $-1.58 |
| 2026-11-11T19:36 | PEPEUSDT | bottom | STOP | 9.5 | -3.25% | $-1.49 |
| 2026-11-11T19:19 | SXTUSDT | surge | STOP | 0.8 | -3.25% | $-1.54 |
| 2026-11-11T18:28 | GOOGLBUSDT | bottom | TARGET | 23.8 | +2.75% | $+1.27 |
| 2026-11-11T17:37 | BCHUSDT | bottom | TARGET | 23.0 | +2.75% | $+1.27 |
| 2026-11-11T16:45 | INTCBUSDT | surge | TARGET | 5.2 | +2.75% | $+1.29 |
| 2026-11-11T16:28 | INTWBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.41 |
| 2026-11-11T14:29 | AVGOBUSDT | surge | TARGET | 12.8 | +2.75% | $+1.30 |
| 2026-11-11T12:25 | SOXLBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.37 |
| 2026-11-11T11:50 | OPENUSDT | surge | TARGET | 1.0 | +2.75% | $+1.30 |
| 2026-11-11T11:15 | INTWBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.26 |
| 2026-11-11T10:40 | OPENUSDT | surge | TARGET | 14.5 | +2.75% | $+1.27 |
| 2026-11-11T10:05 | SKHYBUSDT | surge | TARGET | 8.0 | +2.75% | $+1.27 |
| 2026-11-11T09:47 | PHAUSDT | surge | STOP | 1.5 | -3.25% | $-1.47 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-11T06:30 | EWYBUSDT | surge | 146.03 | 148.33 | +1.58% |
| 2026-11-11T10:05 | HOMEUSDT | surge | 0.00556 | 0.00553 | -0.54% |
| 2026-11-11T16:28 | 0GUSDT | surge | 0.156 | 0.152 | -2.56% |
| 2026-11-11T16:45 | BNCBUSDT | surge | 4.71 | 4.67 | -0.85% |
| 2026-11-11T17:37 | INTCBUSDT | surge | 63.42 | 62.62 | -1.26% |
| 2026-11-11T19:19 | QQQBUSDT | surge | 693.04 | 690.21 | -0.41% |
| 2026-11-11T19:36 | TQQQBUSDT | surge | 60.96 | 60.37 | -0.97% |
| 2026-11-11T19:53 | INTWBUSDT | surge | 6.62 | 6.59 | -0.45% |
| 2026-11-11T21:18 | WLFIUSDT | bottom | 0.0465 | 0.0464 | -0.22% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
