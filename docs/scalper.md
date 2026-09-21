# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-21T04:23:56+00:00 · runs 1367 · equity **$924.24** (-7.58%) · cash $0.00 · open 10/10 · round trips 496

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-70.75 · worst day $-50.94 · trades/day 29.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 409 | 53% | -0.07% | 49% | 43% | 8% |
| bottom | 87 | 43% | -0.47% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-21T04:22 | MIRAUSDT | surge | TARGET | 2.0 | +2.75% | $+2.43 |
| 2026-09-21T02:55 | XRPUSDT | bottom | TIME | 24.0 | +0.85% | $+0.78 |
| 2026-09-21T02:03 | RENDERUSDT | surge | STOP | 2.2 | -3.25% | $-2.97 |
| 2026-09-21T01:11 | BNCBUSDT | surge | TARGET | 10.8 | +2.75% | $+2.50 |
| 2026-09-21T00:36 | SEIUSDT | surge | TARGET | 2.5 | +2.75% | $+2.60 |
| 2026-09-20T23:44 | ALGOUSDT | surge | STOP | 5.2 | -3.25% | $-3.07 |
| 2026-09-20T22:34 | KMNOUSDT | surge | TARGET | 1.0 | +2.75% | $+2.53 |
| 2026-09-20T21:59 | SOLUSDT | bottom | TIME | 24.0 | -0.66% | $-0.63 |
| 2026-09-20T21:18 | GRTUSDT | surge | STOP | 1.0 | -3.25% | $-3.09 |
| 2026-09-20T20:07 | CAKEUSDT | surge | TARGET | 8.5 | +2.75% | $+2.54 |
| 2026-09-20T18:19 | PROVEUSDT | surge | STOP | 1.0 | -3.25% | $-3.09 |
| 2026-09-20T18:19 | STRKUSDT | surge | TARGET | 1.2 | +2.75% | $+2.60 |
| 2026-09-20T17:07 | PROVEUSDT | surge | TARGET | 5.5 | +2.75% | $+2.54 |
| 2026-09-20T16:49 | CFGUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-20T16:49 | STRKUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-20T14:10 | TRXUSDT | surge | 0.3466 | 0.3431 | -1.01% |
| 2026-09-20T16:49 | ATOMUSDT | surge | 1.765 | 1.756 | -0.51% |
| 2026-09-20T16:49 | APTUSDT | surge | 0.747 | 0.74 | -0.94% |
| 2026-09-20T18:19 | RUNEUSDT | surge | 0.564 | 0.566 | +0.35% |
| 2026-09-20T22:34 | ZROUSDT | surge | 1.177 | 1.153 | -2.04% |
| 2026-09-21T00:36 | SOXLBUSDT | surge | 126.43 | 127.47 | +0.82% |
| 2026-09-21T01:11 | SNXXBUSDT | surge | 18.3 | 18.11 | -1.04% |
| 2026-09-21T02:55 | MUBUSDT | surge | 1027.56 | 1028.3 | +0.07% |
| 2026-09-21T04:22 | BERAUSDT | surge | 0.2296 | 0.227 | -1.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
