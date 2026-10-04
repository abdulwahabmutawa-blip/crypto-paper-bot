# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-04T23:32:44+00:00 · runs 2567 · equity **$851.17** (-14.88%) · cash $0.00 · open 10/10 · round trips 962

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-144.18 · worst day $-50.94 · trades/day 32.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 835 | 52% | -0.12% | 49% | 44% | 7% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-04T15:32 | SENTUSDT | surge | TARGET | 1.2 | +2.75% | $+2.70 |
| 2026-10-04T15:15 | IOTAUSDT | surge | STOP | 0.2 | -3.25% | $-2.71 |
| 2026-10-04T14:59 | RUNEUSDT | surge | TARGET | 5.2 | +2.75% | $+2.24 |
| 2026-10-04T14:09 | ATOMUSDT | surge | TARGET | 20.0 | +2.75% | $+2.63 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-04T08:03 | ACEUSDT | surge | 0.1863 | 0.1883 | +1.07% |
| 2026-10-04T15:15 | ATOMUSDT | surge | 1.787 | 1.753 | -1.90% |
| 2026-10-04T16:05 | ROBOUSDT | surge | 0.00882 | 0.0086 | -2.49% |
| 2026-10-04T17:27 | BROCCOLI714USDT | surge | 0.02759 | 0.02759 | +0.00% |
| 2026-10-04T17:43 | RUNEUSDT | surge | 0.811 | 0.798 | -1.60% |
| 2026-10-04T18:37 | VIRTUALUSDT | surge | 0.849 | 0.8463 | -0.32% |
| 2026-10-04T21:53 | SHIBUSDT | surge | 5.94e-06 | 5.92e-06 | -0.34% |
| 2026-10-04T22:58 | MSTRBUSDT | surge | 165.16 | 165.19 | +0.02% |
| 2026-10-04T23:15 | FLOKIUSDT | surge | 2.915e-05 | 2.914e-05 | -0.03% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
