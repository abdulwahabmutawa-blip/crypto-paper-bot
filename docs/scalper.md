# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-12T01:49:31+00:00 · runs 5779 · equity **$503.70** (-49.63%) · cash $0.00 · open 10/10 · round trips 1968

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-495.89 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1704 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 264 | 42% | -0.55% | 36% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-11T14:29 | AVGOBUSDT | surge | TARGET | 12.8 | +2.75% | $+1.30 |
| 2026-11-11T12:25 | SOXLBUSDT | surge | TARGET | 3.5 | +2.75% | $+1.37 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-11T06:30 | EWYBUSDT | surge | 146.03 | 146.32 | +0.20% |
| 2026-11-11T16:45 | BNCBUSDT | surge | 4.71 | 4.62 | -1.91% |
| 2026-11-11T19:19 | QQQBUSDT | surge | 693.04 | 686.25 | -0.98% |
| 2026-11-11T21:18 | WLFIUSDT | bottom | 0.0465 | 0.0475 | +2.15% |
| 2026-11-11T23:06 | AMDBUSDT | surge | 572.98 | 574.86 | +0.33% |
| 2026-11-11T23:06 | SPCXBUSDT | bottom | 138.14 | 139.36 | +0.88% |
| 2026-11-11T23:06 | TAOUSDT | bottom | 216.3 | 216.5 | +0.09% |
| 2026-11-11T23:39 | GOOGLBUSDT | surge | 297.09 | 294.49 | -0.88% |
| 2026-11-11T23:39 | AVGOBUSDT | surge | 355.92 | 353.29 | -0.74% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
