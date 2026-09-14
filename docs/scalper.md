# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-14T00:09:09+00:00 · runs 741 · equity **$876.82** (-12.32%) · cash $260.29 · open 7/10 · round trips 270

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.48%/trade · realized $-123.28 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 201 | 45% | -0.47% | 42% | 49% | 9% |
| bottom | 69 | 42% | -0.51% | 41% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-14T00:07 | PUMPUSDT | bottom | STOP | 1.8 | -3.25% | $-2.78 |
| 2026-09-13T22:29 | ALGOUSDT | surge | STOP | 0.8 | -3.25% | $-2.94 |
| 2026-09-13T22:29 | DOTUSDT | bottom | TIME | 24.0 | -2.30% | $-2.20 |
| 2026-09-13T22:13 | ARUSDT | surge | STOP | 3.2 | -3.25% | $-2.88 |
| 2026-09-13T22:13 | MBLUSDT | surge | TARGET | 4.5 | +2.75% | $+2.52 |
| 2026-09-13T22:13 | STXUSDT | surge | STOP | 18.5 | -3.25% | $-2.72 |
| 2026-09-13T22:13 | DASHUSDT | bottom | STOP | 23.5 | -3.25% | $-2.74 |
| 2026-09-13T21:36 | XTZUSDT | surge | STOP | 0.8 | -3.25% | $-3.04 |
| 2026-09-13T20:30 | XTZUSDT | surge | TARGET | 3.2 | +2.75% | $+2.50 |
| 2026-09-13T19:41 | GMTUSDT | surge | STOP | 4.2 | -3.25% | $-2.88 |
| 2026-09-13T18:52 | SCRUSDT | surge | STOP | 1.0 | -3.25% | $-2.98 |
| 2026-09-13T17:46 | BATUSDT | surge | STOP | 1.2 | -3.25% | $-3.22 |
| 2026-09-13T17:30 | SCRUSDT | surge | TARGET | 0.0 | +2.75% | $+2.50 |
| 2026-09-13T17:30 | BABYUSDT | surge | STOP | 1.5 | -3.25% | $-3.01 |
| 2026-09-13T17:13 | ARUSDT | surge | TARGET | 0.5 | +2.75% | $+2.48 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.3463 | -1.14% |
| 2026-09-13T17:46 | ICPUSDT | surge | 2.784 | 2.793 | +0.32% |
| 2026-09-13T19:41 | CAKEUSDT | surge | 2.269 | 2.235 | -1.50% |
| 2026-09-13T22:13 | SAGAUSDT | bottom | 0.01706 | 0.01728 | +1.29% |
| 2026-09-13T22:29 | PEPEUSDT | bottom | 3.36e-06 | 3.4e-06 | +1.19% |
| 2026-09-14T00:07 | TRXUSDT | bottom | 0.3384 | 0.3381 | -0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
