# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T02:16:14+00:00 · runs 3254 · equity **$752.56** (-24.74%) · cash $367.85 · open 5/10 · round trips 1219

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.22%/trade · realized $-244.11 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1069 | 50% | -0.19% | 48% | 45% | 7% |
| bottom | 150 | 44% | -0.49% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-12T18:36 | BEAMXUSDT | surge | TARGET | 0.2 | +2.75% | $+2.11 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 161.89 | -2.59% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.13741 | -1.84% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3296 | -0.09% |
| 2026-10-13T01:39 | SOXSBUSDT | surge | 39.02 | 39.1 | +0.21% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
