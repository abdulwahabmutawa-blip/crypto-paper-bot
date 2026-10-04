# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-04T15:50:20+00:00 · runs 2538 · equity **$857.46** (-14.25%) · cash $0.00 · open 10/10 · round trips 952

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-142.03 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 825 | 52% | -0.12% | 49% | 44% | 7% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-04T15:48 | BATUSDT | surge | TARGET | 3.8 | +2.75% | $+2.25 |
| 2026-10-04T15:32 | SENTUSDT | surge | TARGET | 1.2 | +2.75% | $+2.70 |
| 2026-10-04T15:15 | IOTAUSDT | surge | STOP | 0.2 | -3.25% | $-2.71 |
| 2026-10-04T14:59 | RUNEUSDT | surge | TARGET | 5.2 | +2.75% | $+2.24 |
| 2026-10-04T14:09 | ATOMUSDT | surge | TARGET | 20.0 | +2.75% | $+2.63 |
| 2026-10-04T11:54 | OPUSDT | surge | STOP | 17.5 | -3.25% | $-2.74 |
| 2026-10-04T11:21 | IOTAUSDT | surge | STOP | 1.8 | -3.25% | $-2.85 |
| 2026-10-04T10:48 | KAITOUSDT | surge | STOP | 14.0 | -3.25% | $-2.87 |
| 2026-10-04T09:42 | METUSDT | surge | STOP | 7.8 | -3.25% | $-2.73 |
| 2026-10-04T09:25 | IOTAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.34 |
| 2026-10-04T08:36 | WUSDT | surge | TARGET | 4.5 | +2.75% | $+2.28 |
| 2026-10-04T08:03 | ZKUSDT | surge | TARGET | 13.8 | +2.75% | $+2.32 |
| 2026-10-04T03:55 | INJUSDT | surge | TIME | 24.0 | -1.69% | $-1.43 |
| 2026-10-04T01:33 | SNDKBUSDT | bottom | TIME | 24.0 | -0.40% | $-0.34 |
| 2026-10-03T21:36 | TRBUSDT | surge | STOP | 3.8 | -3.25% | $-2.86 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-03T15:50 | MORPHOUSDT | surge | 2.724 | 2.71 | -0.51% |
| 2026-10-03T17:17 | BNBUSDT | surge | 789.96 | 787.75 | -0.28% |
| 2026-10-03T21:36 | DODOUSDT | surge | 0.01896 | 0.01869 | -1.42% |
| 2026-10-04T08:03 | ACEUSDT | surge | 0.1863 | 0.1873 | +0.54% |
| 2026-10-04T10:48 | NILUSDT | surge | 0.08754 | 0.08994 | +2.74% |
| 2026-10-04T11:21 | GUNUSDT | surge | 0.00341 | 0.00337 | -1.17% |
| 2026-10-04T15:15 | ATOMUSDT | surge | 1.787 | 1.774 | -0.73% |
| 2026-10-04T15:32 | SENTUSDT | surge | 0.0243 | 0.02431 | +0.04% |
| 2026-10-04T15:48 | BATUSDT | surge | 0.1082 | 0.1083 | +0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
