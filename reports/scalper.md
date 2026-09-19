# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-19T20:11:48+00:00 · runs 1249 · equity **$953.26** (-4.67%) · cash $0.00 · open 10/10 · round trips 434

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-45.25 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 352 | 54% | +0.01% | 50% | 41% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-19T20:09 | ONDOUSDT | surge | STOP | 2.8 | -3.25% | $-3.19 |
| 2026-09-19T17:48 | PROVEUSDT | surge | TARGET | 12.8 | +2.75% | $+2.62 |
| 2026-09-19T17:30 | PHAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.43 |
| 2026-09-19T17:30 | NILUSDT | surge | TARGET | 1.0 | +2.75% | $+2.43 |
| 2026-09-19T17:06 | MUBUSDT | surge | TIME | 24.0 | +0.98% | $+0.95 |
| 2026-09-19T16:31 | ALLOUSDT | surge | STOP | 1.0 | -3.25% | $-2.97 |
| 2026-09-19T16:13 | IOSTUSDT | surge | STOP | 0.5 | -3.25% | $-2.97 |
| 2026-09-19T15:20 | BANKUSDT | surge | TARGET | 0.0 | +2.75% | $+2.34 |
| 2026-09-19T15:20 | AVAXUSDT | surge | TARGET | 2.2 | +2.75% | $+2.55 |
| 2026-09-19T15:03 | HOMEUSDT | surge | STOP | 4.0 | -3.25% | $-2.86 |
| 2026-09-19T12:59 | AVAXUSDT | surge | TARGET | 0.2 | +2.75% | $+2.48 |
| 2026-09-19T12:41 | INJUSDT | surge | TARGET | 1.5 | +2.75% | $+2.42 |
| 2026-09-19T12:23 | ENAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
| 2026-09-19T11:30 | DODOUSDT | surge | TIME | 24.0 | -0.80% | $-0.69 |
| 2026-09-19T10:49 | ACHUSDT | surge | STOP | 1.0 | -3.25% | $-3.05 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-18T20:06 | SNDKBUSDT | surge | 1790.7 | 1784.43 | -0.35% |
| 2026-09-18T20:42 | SENTUSDT | surge | 0.01781 | 0.018 | +1.07% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.00875 | +1.43% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.1556 | -1.21% |
| 2026-09-19T12:23 | TAOUSDT | surge | 267.9 | 262.2 | -2.13% |
| 2026-09-19T17:30 | NEIROUSDT | surge | 9.668e-05 | 9.517e-05 | -1.56% |
| 2026-09-19T17:30 | 0GUSDT | surge | 0.2276 | 0.2262 | -0.62% |
| 2026-09-19T17:48 | PHAUSDT | surge | 0.0355 | 0.0361 | +1.69% |
| 2026-09-19T20:09 | FLOKIUSDT | surge | 2.663e-05 | 2.662e-05 | -0.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
