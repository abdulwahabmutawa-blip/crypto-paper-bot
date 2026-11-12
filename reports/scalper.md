# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-12T06:16:49+00:00 · runs 5796 · equity **$501.26** (-49.87%) · cash $0.00 · open 10/10 · round trips 1970

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-496.16 · worst day $-50.94 · trades/day 28.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1705 | 48% | -0.32% | 46% | 48% | 7% |
| bottom | 265 | 42% | -0.53% | 36% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-12T05:57 | WLFIUSDT | bottom | TARGET | 8.2 | +2.75% | $+1.29 |
| 2026-11-12T05:23 | BNCBUSDT | surge | STOP | 12.2 | -3.25% | $-1.57 |
| 2026-11-11T23:23 | HOMEUSDT | surge | STOP | 13.0 | -3.25% | $-1.55 |
| 2026-11-11T23:06 | INTWBUSDT | surge | STOP | 2.5 | -3.25% | $-1.53 |
| 2026-11-11T23:06 | TQQQBUSDT | surge | STOP | 3.0 | -3.25% | $-1.44 |
| 2026-11-11T23:06 | INTCBUSDT | surge | STOP | 4.8 | -3.25% | $-1.54 |
| 2026-11-11T23:06 | 0GUSDT | surge | STOP | 5.8 | -3.25% | $-1.71 |
| 2026-11-11T21:18 | OPENUSDT | surge | STOP | 9.2 | -3.25% | $-1.58 |
| 2026-11-11T19:53 | KITEUSDT | surge | STOP | 5.2 | -3.25% | $-1.58 |
| 2026-11-11T19:36 | PEPEUSDT | bottom | STOP | 9.5 | -3.25% | $-1.49 |
| 2026-11-11T19:19 | SXTUSDT | surge | STOP | 0.8 | -3.25% | $-1.54 |
| 2026-11-11T18:28 | GOOGLBUSDT | bottom | TARGET | 23.8 | +2.75% | $+1.27 |
| 2026-11-11T17:37 | BCHUSDT | bottom | TARGET | 23.0 | +2.75% | $+1.27 |
| 2026-11-11T16:45 | INTCBUSDT | surge | TARGET | 5.2 | +2.75% | $+1.29 |
| 2026-11-11T16:28 | INTWBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.41 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-11T06:30 | EWYBUSDT | surge | 146.03 | 145.95 | -0.05% |
| 2026-11-11T19:19 | QQQBUSDT | surge | 693.04 | 684.34 | -1.26% |
| 2026-11-11T23:06 | AMDBUSDT | surge | 572.98 | 564.14 | -1.54% |
| 2026-11-11T23:06 | SPCXBUSDT | bottom | 138.14 | 139.19 | +0.76% |
| 2026-11-11T23:06 | TAOUSDT | bottom | 216.3 | 214.5 | -0.83% |
| 2026-11-11T23:39 | GOOGLBUSDT | surge | 297.09 | 294.79 | -0.77% |
| 2026-11-11T23:39 | AVGOBUSDT | surge | 355.92 | 349.8 | -1.72% |
| 2026-11-12T05:57 | MSTRBUSDT | bottom | 117.16 | 117.52 | +0.31% |
| 2026-11-12T06:15 | KITEUSDT | surge | 0.1275 | 0.1269 | -0.47% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
