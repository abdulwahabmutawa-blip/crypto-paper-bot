# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-28T00:39:42+00:00 · runs 6895 · equity **$492.82** (-50.72%) · cash $0.00 · open 10/10 · round trips 2264

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-508.29 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1944 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 320 | 43% | -0.45% | 38% | 43% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-27T19:18 | ATUSDT | surge | STOP | 0.8 | -3.25% | $-1.49 |
| 2026-11-27T19:18 | NOMUSDT | surge | STOP | 2.0 | -3.25% | $-1.49 |
| 2026-11-27T19:01 | MAGICUSDT | surge | STOP | 0.8 | -3.25% | $-1.47 |
| 2026-11-27T18:29 | SNDKBUSDT | surge | TARGET | 2.0 | +2.75% | $+1.24 |
| 2026-11-27T18:29 | SKYUSDT | bottom | TARGET | 2.8 | +2.75% | $+1.23 |
| 2026-11-27T18:29 | WIFUSDT | surge | TIME | 24.0 | +0.26% | $+0.12 |
| 2026-11-27T18:12 | THETAUSDT | surge | TIME | 24.0 | +0.71% | $+0.32 |
| 2026-11-27T17:07 | ANTBUSDT | surge | TARGET | 1.5 | +2.75% | $+1.23 |
| 2026-11-27T16:01 | HEIUSDT | surge | TARGET | 0.0 | +2.75% | $+1.20 |
| 2026-11-27T15:45 | TRXUSDT | bottom | TIME | 24.0 | -0.15% | $-0.07 |
| 2026-11-27T15:28 | GOOGLBUSDT | surge | STOP | 11.2 | -3.25% | $-1.56 |
| 2026-11-27T15:28 | SKHYBUSDT | surge | STOP | 11.0 | -3.25% | $-1.45 |
| 2026-11-27T15:28 | TQQQBUSDT | surge | STOP | 12.0 | -3.25% | $-1.47 |
| 2026-11-27T15:28 | DOTUSDT | surge | STOP | 19.2 | -3.25% | $-1.52 |
| 2026-11-27T04:15 | KORUBUSDT | surge | TARGET | 1.5 | +2.75% | $+1.24 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-27T02:34 | QQQBUSDT | surge | 647.34 | 650.21 | +0.44% |
| 2026-11-27T04:15 | SPCXBUSDT | surge | 133.15 | 132.18 | -0.73% |
| 2026-11-27T15:28 | TSLABUSDT | surge | 393.11 | 398.79 | +1.44% |
| 2026-11-27T15:28 | BCHUSDT | bottom | 204 | 208.3 | +2.11% |
| 2026-11-27T18:29 | RENDERUSDT | surge | 1.387 | 1.387 | +0.00% |
| 2026-11-27T18:29 | DRAMBUSDT | surge | 37.62 | 37.42 | -0.53% |
| 2026-11-27T19:01 | MUBUSDT | surge | 645.42 | 643.85 | -0.24% |
| 2026-11-27T19:18 | ANTBUSDT | surge | 91.18 | 91.12 | -0.07% |
| 2026-11-27T19:18 | NIGHTUSDT | surge | 0.05011 | 0.05015 | +0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
