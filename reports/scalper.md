# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-28T16:33:11+00:00 · runs 6943 · equity **$486.73** (-51.33%) · cash $87.74 · open 8/10 · round trips 2273

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-511.45 · worst day $-50.94 · trades/day 26.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1952 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 321 | 44% | -0.44% | 38% | 43% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-28T15:59 | ATMUSDT | surge | STOP | 0.0 | -3.25% | $-1.45 |
| 2026-11-28T15:43 | NIGHTUSDT | surge | STOP | 0.8 | -3.25% | $-1.48 |
| 2026-11-28T15:43 | TSLABUSDT | surge | TIME | 24.0 | +1.17% | $+0.52 |
| 2026-11-28T14:55 | OPGUSDT | surge | STOP | 0.0 | -3.25% | $-1.48 |
| 2026-11-28T09:22 | NIGHTUSDT | surge | TARGET | 13.8 | +2.75% | $+1.22 |
| 2026-11-28T08:17 | RENDERUSDT | surge | STOP | 13.8 | -3.25% | $-1.49 |
| 2026-11-28T04:40 | SPCXBUSDT | surge | TIME | 24.0 | -0.83% | $-0.38 |
| 2026-11-28T04:23 | BCHUSDT | bottom | TARGET | 12.8 | +2.75% | $+1.23 |
| 2026-11-28T02:56 | QQQBUSDT | surge | TIME | 24.0 | +0.33% | $+0.15 |
| 2026-11-27T19:18 | ATUSDT | surge | STOP | 0.8 | -3.25% | $-1.49 |
| 2026-11-27T19:18 | NOMUSDT | surge | STOP | 2.0 | -3.25% | $-1.49 |
| 2026-11-27T19:01 | MAGICUSDT | surge | STOP | 0.8 | -3.25% | $-1.47 |
| 2026-11-27T18:29 | SNDKBUSDT | surge | TARGET | 2.0 | +2.75% | $+1.24 |
| 2026-11-27T18:29 | SKYUSDT | bottom | TARGET | 2.8 | +2.75% | $+1.23 |
| 2026-11-27T18:29 | WIFUSDT | surge | TIME | 24.0 | +0.26% | $+0.12 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-27T18:29 | DRAMBUSDT | surge | 37.62 | 37.25 | -0.98% |
| 2026-11-27T19:01 | MUBUSDT | surge | 645.42 | 640.09 | -0.83% |
| 2026-11-27T19:18 | ANTBUSDT | surge | 91.18 | 91.37 | +0.21% |
| 2026-11-28T14:39 | DODOUSDT | surge | 0.04201 | 0.04208 | +0.17% |
| 2026-11-28T14:39 | TLMUSDT | bottom | 0.000919 | 0.000906 | -1.41% |
| 2026-11-28T14:39 | HBARUSDT | bottom | 0.05271 | 0.0521 | -1.16% |
| 2026-11-28T14:55 | PEPEUSDT | bottom | 3.4e-06 | 3.4e-06 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
