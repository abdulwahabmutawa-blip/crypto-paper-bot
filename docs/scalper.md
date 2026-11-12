# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-12T12:14:50+00:00 · runs 5813 · equity **$498.79** (-50.12%) · cash $0.00 · open 10/10 · round trips 1975

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-497.03 · worst day $-50.94 · trades/day 28.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1710 | 48% | -0.32% | 46% | 47% | 7% |
| bottom | 265 | 42% | -0.53% | 36% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-12T11:55 | SXTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.30 |
| 2026-11-12T11:55 | HAEDALUSDT | surge | STOP | 4.2 | -3.25% | $-1.47 |
| 2026-11-12T10:14 | ERAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.26 |
| 2026-11-12T07:57 | KITEUSDT | surge | STOP | 1.2 | -3.25% | $-1.54 |
| 2026-11-12T06:49 | EWYBUSDT | surge | TIME | 24.0 | -0.91% | $-0.42 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-11T19:19 | QQQBUSDT | surge | 693.04 | 686.38 | -0.96% |
| 2026-11-11T23:06 | AMDBUSDT | surge | 572.98 | 568.54 | -0.77% |
| 2026-11-11T23:06 | SPCXBUSDT | bottom | 138.14 | 140.11 | +1.43% |
| 2026-11-11T23:06 | TAOUSDT | bottom | 216.3 | 211.9 | -2.03% |
| 2026-11-11T23:39 | GOOGLBUSDT | surge | 297.09 | 293.54 | -1.19% |
| 2026-11-11T23:39 | AVGOBUSDT | surge | 355.92 | 351.15 | -1.34% |
| 2026-11-12T05:57 | MSTRBUSDT | bottom | 117.16 | 115.49 | -1.43% |
| 2026-11-12T11:55 | ONEUSDT | surge | 0.001701 | 0.001666 | -2.06% |
| 2026-11-12T11:55 | GRAMUSDT | surge | 1.253 | 1.245 | -0.64% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
