# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T23:28:32+00:00 · runs 1349 · equity **$923.32** (-7.67%) · cash $0.00 · open 10/10 · round trips 490

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-73.02 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 404 | 53% | -0.07% | 49% | 43% | 8% |
| bottom | 86 | 42% | -0.49% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T22:34 | KMNOUSDT | surge | TARGET | 1.0 | +2.75% | $+2.53 |
| 2026-09-20T21:59 | SOLUSDT | bottom | TIME | 24.0 | -0.66% | $-0.63 |
| 2026-09-20T21:18 | GRTUSDT | surge | STOP | 1.0 | -3.25% | $-3.09 |
| 2026-09-20T20:07 | CAKEUSDT | surge | TARGET | 8.5 | +2.75% | $+2.54 |
| 2026-09-20T18:19 | PROVEUSDT | surge | STOP | 1.0 | -3.25% | $-3.09 |
| 2026-09-20T18:19 | STRKUSDT | surge | TARGET | 1.2 | +2.75% | $+2.60 |
| 2026-09-20T17:07 | PROVEUSDT | surge | TARGET | 5.5 | +2.75% | $+2.54 |
| 2026-09-20T16:49 | CFGUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-20T16:49 | STRKUSDT | surge | TARGET | 0.0 | +2.75% | $+2.53 |
| 2026-09-20T16:49 | DOGEUSDT | bottom | TARGET | 7.8 | +2.75% | $+2.55 |
| 2026-09-20T16:13 | NEARUSDT | surge | TARGET | 2.8 | +2.75% | $+2.50 |
| 2026-09-20T15:55 | SAGAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.42 |
| 2026-09-20T14:27 | MITOUSDT | surge | STOP | 0.2 | -3.25% | $-2.95 |
| 2026-09-20T13:37 | STXUSDT | surge | STOP | 6.2 | -3.25% | $-3.11 |
| 2026-09-20T13:21 | SUSDT | surge | STOP | 0.5 | -3.25% | $-3.00 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-20T02:44 | XRPUSDT | bottom | 1.3972 | 1.4118 | +1.04% |
| 2026-09-20T14:10 | BNCBUSDT | surge | 6.68 | 6.57 | -1.65% |
| 2026-09-20T14:10 | TRXUSDT | surge | 0.3466 | 0.3426 | -1.15% |
| 2026-09-20T16:49 | ATOMUSDT | surge | 1.765 | 1.776 | +0.62% |
| 2026-09-20T16:49 | APTUSDT | surge | 0.747 | 0.742 | -0.67% |
| 2026-09-20T18:19 | RUNEUSDT | surge | 0.564 | 0.564 | +0.00% |
| 2026-09-20T18:19 | ALGOUSDT | surge | 0.1114 | 0.1094 | -1.80% |
| 2026-09-20T21:59 | SEIUSDT | surge | 0.05319 | 0.05346 | +0.51% |
| 2026-09-20T22:34 | ZROUSDT | surge | 1.177 | 1.167 | -0.85% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
