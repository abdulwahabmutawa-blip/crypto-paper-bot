# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-12T23:41:04+00:00 · runs 3245 · equity **$751.79** (-24.82%) · cash $225.26 · open 7/10 · round trips 1214

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.22%/trade · realized $-241.01 · worst day $-50.94 · trades/day 31.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1067 | 50% | -0.19% | 48% | 45% | 7% |
| bottom | 147 | 44% | -0.48% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-12T23:38 | SOXSBUSDT | surge | TARGET | 7.0 | +2.75% | $+2.16 |
| 2026-10-12T22:45 | HYPEUSDT | bottom | STOP | 8.8 | -3.25% | $-2.45 |
| 2026-10-12T22:10 | FETUSDT | bottom | STOP | 7.0 | -3.25% | $-2.29 |
| 2026-10-12T21:52 | AAVEUSDT | bottom | STOP | 7.8 | -3.25% | $-2.45 |
| 2026-10-12T20:40 | BEAMXUSDT | surge | STOP | 0.5 | -3.25% | $-2.44 |
| 2026-10-12T19:46 | AXLUSDT | surge | STOP | 0.5 | -3.25% | $-2.44 |
| 2026-10-12T19:46 | STXUSDT | surge | TARGET | 0.2 | +2.75% | $+2.07 |
| 2026-10-12T19:46 | PIXELUSDT | surge | STOP | 0.8 | -3.25% | $-2.53 |
| 2026-10-12T18:53 | STXUSDT | surge | TARGET | 3.2 | +2.75% | $+1.94 |
| 2026-10-12T18:36 | BEAMXUSDT | surge | TARGET | 0.2 | +2.75% | $+2.11 |
| 2026-10-12T17:12 | MORPHOUSDT | surge | STOP | 14.0 | -3.25% | $-2.52 |
| 2026-10-12T16:06 | PYTHUSDT | surge | TARGET | 1.8 | +2.75% | $+2.00 |
| 2026-10-12T15:49 | DODOUSDT | surge | TARGET | 1.0 | +2.75% | $+2.33 |
| 2026-10-12T15:49 | XLMUSDT | surge | TIME | 24.0 | -2.68% | $-2.14 |
| 2026-10-12T14:59 | RENDERUSDT | surge | STOP | 5.2 | -3.25% | $-2.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 162.84 | -2.02% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.13782 | -1.55% |
| 2026-10-12T20:57 | RENDERUSDT | surge | 2.113 | 2.076 | -1.75% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3291 | -0.24% |
| 2026-10-12T22:10 | AVAXUSDT | bottom | 10.349 | 10.157 | -1.86% |
| 2026-10-12T22:45 | POLUSDT | bottom | 0.10018 | 0.09792 | -2.26% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
