# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-27T17:08:27+00:00 · runs 6877 · equity **$494.80** (-50.52%) · cash $0.00 · open 10/10 · round trips 2257

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-506.73 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1938 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 319 | 43% | -0.46% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-27T17:07 | ANTBUSDT | surge | TARGET | 1.5 | +2.75% | $+1.23 |
| 2026-11-27T16:01 | HEIUSDT | surge | TARGET | 0.0 | +2.75% | $+1.20 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-26T17:51 | THETAUSDT | surge | 0.1357 | 0.1358 | +0.07% |
| 2026-11-26T18:25 | WIFUSDT | surge | 0.1387 | 0.14 | +0.94% |
| 2026-11-27T02:34 | QQQBUSDT | surge | 647.34 | 646.67 | -0.10% |
| 2026-11-27T04:15 | SPCXBUSDT | surge | 133.15 | 131.55 | -1.20% |
| 2026-11-27T15:28 | TSLABUSDT | surge | 393.11 | 399.28 | +1.57% |
| 2026-11-27T15:28 | SKYUSDT | bottom | 0.04544 | 0.04621 | +1.69% |
| 2026-11-27T15:28 | BCHUSDT | bottom | 204 | 204.9 | +0.44% |
| 2026-11-27T16:01 | SNDKBUSDT | surge | 83.51 | 83.74 | +0.28% |
| 2026-11-27T17:07 | NOMUSDT | surge | 0.001278 | 0.001275 | -0.23% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
