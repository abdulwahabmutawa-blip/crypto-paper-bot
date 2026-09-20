# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T22:19:09+00:00 · runs 1345 · equity **$925.00** (-7.50%) · cash $0.00 · open 10/10 · round trips 489

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-75.55 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 403 | 53% | -0.08% | 49% | 43% | 8% |
| bottom | 86 | 42% | -0.49% | 41% | 45% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-20T13:04 | IOSTUSDT | surge | STOP | 0.2 | -3.25% | $-3.00 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-20T02:44 | XRPUSDT | bottom | 1.3972 | 1.4087 | +0.82% |
| 2026-09-20T14:10 | BNCBUSDT | surge | 6.68 | 6.55 | -1.95% |
| 2026-09-20T14:10 | TRXUSDT | surge | 0.3466 | 0.343 | -1.04% |
| 2026-09-20T16:49 | ATOMUSDT | surge | 1.765 | 1.78 | +0.85% |
| 2026-09-20T16:49 | APTUSDT | surge | 0.747 | 0.742 | -0.67% |
| 2026-09-20T18:19 | RUNEUSDT | surge | 0.564 | 0.564 | +0.00% |
| 2026-09-20T18:19 | ALGOUSDT | surge | 0.1114 | 0.1106 | -0.72% |
| 2026-09-20T21:18 | KMNOUSDT | surge | 0.0321 | 0.0328 | +2.18% |
| 2026-09-20T21:59 | SEIUSDT | surge | 0.05319 | 0.05376 | +1.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
