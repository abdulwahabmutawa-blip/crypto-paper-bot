# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-27T15:46:35+00:00 · runs 6872 · equity **$492.93** (-50.71%) · cash $0.00 · open 10/10 · round trips 2255

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-509.16 · worst day $-50.94 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1936 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 319 | 43% | -0.46% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-27T15:45 | TRXUSDT | bottom | TIME | 24.0 | -0.15% | $-0.07 |
| 2026-11-27T15:28 | GOOGLBUSDT | surge | STOP | 11.2 | -3.25% | $-1.56 |
| 2026-11-27T15:28 | SKHYBUSDT | surge | STOP | 11.0 | -3.25% | $-1.45 |
| 2026-11-27T15:28 | TQQQBUSDT | surge | STOP | 12.0 | -3.25% | $-1.47 |
| 2026-11-27T15:28 | DOTUSDT | surge | STOP | 19.2 | -3.25% | $-1.52 |
| 2026-11-27T04:15 | KORUBUSDT | surge | TARGET | 1.5 | +2.75% | $+1.24 |
| 2026-11-27T03:58 | SENTUSDT | surge | TARGET | 9.0 | +2.75% | $+1.28 |
| 2026-11-27T03:42 | SNDKBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.19 |
| 2026-11-27T02:34 | TRUMPUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.21 |
| 2026-11-27T02:34 | TIAUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.21 |
| 2026-11-27T02:34 | SKYUSDT | surge | TARGET | 11.0 | +2.75% | $+1.20 |
| 2026-11-27T01:44 | SOPHUSDT | surge | STOP | 0.5 | -3.25% | $-1.46 |
| 2026-11-27T00:54 | EWYBUSDT | surge | TIME | 24.0 | -1.35% | $-0.61 |
| 2026-11-26T23:46 | SAGAUSDT | surge | STOP | 4.5 | -3.25% | $-1.47 |
| 2026-11-26T23:46 | SUPERUSDT | surge | TIME | 24.0 | -1.10% | $-0.49 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-26T17:51 | THETAUSDT | surge | 0.1357 | 0.1361 | +0.29% |
| 2026-11-26T18:25 | WIFUSDT | surge | 0.1387 | 0.138 | -0.50% |
| 2026-11-27T02:34 | QQQBUSDT | surge | 647.34 | 646.74 | -0.09% |
| 2026-11-27T04:15 | SPCXBUSDT | surge | 133.15 | 132.06 | -0.82% |
| 2026-11-27T15:28 | ANTBUSDT | surge | 88.36 | 90.22 | +2.11% |
| 2026-11-27T15:28 | TSLABUSDT | surge | 393.11 | 399.91 | +1.73% |
| 2026-11-27T15:28 | SKYUSDT | bottom | 0.04544 | 0.04617 | +1.61% |
| 2026-11-27T15:28 | BCHUSDT | bottom | 204 | 205.3 | +0.64% |
| 2026-11-27T15:45 | HEIUSDT | surge | 0.0825 | 0.0823 | -0.24% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
