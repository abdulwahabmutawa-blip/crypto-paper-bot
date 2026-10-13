# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T06:19:28+00:00 · runs 3268 · equity **$750.92** (-24.91%) · cash $292.37 · open 6/10 · round trips 1220

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-246.50 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1070 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 150 | 44% | -0.49% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-13T05:23 | XAIUSDT | surge | STOP | 0.5 | -3.25% | $-2.39 |
| 2026-10-13T02:14 | ZROUSDT | bottom | TARGET | 0.2 | +2.75% | $+2.00 |
| 2026-10-13T01:57 | SKLUSDT | surge | TARGET | 0.0 | +2.75% | $+2.00 |
| 2026-10-13T00:14 | POLUSDT | bottom | STOP | 1.2 | -3.25% | $-2.35 |
| 2026-10-13T00:14 | AVAXUSDT | bottom | STOP | 2.0 | -3.25% | $-2.34 |
| 2026-10-13T00:14 | RENDERUSDT | surge | STOP | 3.2 | -3.25% | $-2.41 |
| 2026-10-12T23:38 | SOXSBUSDT | surge | TARGET | 7.0 | +2.75% | $+2.16 |
| 2026-10-12T22:45 | HYPEUSDT | bottom | STOP | 8.8 | -3.25% | $-2.45 |
| 2026-10-12T22:10 | FETUSDT | bottom | STOP | 7.0 | -3.25% | $-2.29 |
| 2026-10-12T21:52 | AAVEUSDT | bottom | STOP | 7.8 | -3.25% | $-2.45 |
| 2026-10-12T20:40 | BEAMXUSDT | surge | STOP | 0.5 | -3.25% | $-2.44 |
| 2026-10-12T19:46 | AXLUSDT | surge | STOP | 0.5 | -3.25% | $-2.44 |
| 2026-10-12T19:46 | STXUSDT | surge | TARGET | 0.2 | +2.75% | $+2.07 |
| 2026-10-12T19:46 | PIXELUSDT | surge | STOP | 0.8 | -3.25% | $-2.53 |
| 2026-10-12T18:53 | STXUSDT | surge | TARGET | 3.2 | +2.75% | $+1.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 162.64 | -2.14% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.1374 | -1.85% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3304 | +0.15% |
| 2026-10-13T01:39 | SOXSBUSDT | surge | 39.02 | 39.31 | +0.74% |
| 2026-10-13T06:17 | DODOUSDT | surge | 0.02046 | 0.02042 | -0.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
