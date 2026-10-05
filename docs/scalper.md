# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-05T04:23:20+00:00 · runs 2585 · equity **$844.22** (-15.58%) · cash $0.00 · open 10/10 · round trips 966

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-149.59 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 839 | 51% | -0.13% | 48% | 44% | 7% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-05T04:21 | ATOMUSDT | surge | STOP | 12.8 | -3.25% | $-2.63 |
| 2026-10-05T03:31 | VIRTUALUSDT | surge | TARGET | 8.8 | +2.75% | $+2.69 |
| 2026-10-05T03:31 | RUNEUSDT | surge | STOP | 9.8 | -3.25% | $-2.77 |
| 2026-10-05T00:04 | ROBOUSDT | surge | STOP | 7.8 | -3.25% | $-2.69 |
| 2026-10-04T23:15 | CHIPUSDT | surge | TARGET | 5.2 | +2.75% | $+2.34 |
| 2026-10-04T22:58 | ADAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.25 |
| 2026-10-04T22:09 | GUNUSDT | surge | STOP | 10.5 | -3.25% | $-2.75 |
| 2026-10-04T21:53 | DODOUSDT | surge | TIME | 24.0 | -2.04% | $-1.74 |
| 2026-10-04T18:37 | SENTUSDT | surge | STOP | 2.8 | -3.25% | $-3.28 |
| 2026-10-04T17:59 | CHIPUSDT | surge | TARGET | 1.5 | +2.75% | $+2.28 |
| 2026-10-04T17:43 | BNBUSDT | surge | TIME | 24.0 | -0.35% | $-0.30 |
| 2026-10-04T17:27 | BATUSDT | surge | STOP | 1.2 | -3.25% | $-2.73 |
| 2026-10-04T16:05 | NILUSDT | surge | TARGET | 5.0 | +2.75% | $+2.35 |
| 2026-10-04T16:05 | MORPHOUSDT | surge | TIME | 24.0 | -0.73% | $-0.57 |
| 2026-10-04T15:48 | BATUSDT | surge | TARGET | 3.8 | +2.75% | $+2.25 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-04T08:03 | ACEUSDT | surge | 0.1863 | 0.1887 | +1.29% |
| 2026-10-04T17:27 | BROCCOLI714USDT | surge | 0.02759 | 0.02695 | -2.32% |
| 2026-10-04T21:53 | SHIBUSDT | surge | 5.94e-06 | 5.9e-06 | -0.67% |
| 2026-10-04T22:58 | MSTRBUSDT | surge | 165.16 | 163.09 | -1.25% |
| 2026-10-04T23:15 | FLOKIUSDT | surge | 2.915e-05 | 2.872e-05 | -1.48% |
| 2026-10-05T00:04 | MEMEUSDT | surge | 0.000625 | 0.000613 | -1.92% |
| 2026-10-05T03:31 | ADAUSDT | surge | 0.2696 | 0.2653 | -1.59% |
| 2026-10-05T03:31 | LDOUSDT | surge | 0.4723 | 0.4687 | -0.76% |
| 2026-10-05T04:21 | GRTUSDT | surge | 0.02988 | 0.03033 | +1.51% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
