# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-04T10:00:25+00:00 · runs 2516 · equity **$856.45** (-14.36%) · cash $0.00 · open 10/10 · round trips 944

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-140.67 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 817 | 52% | -0.12% | 49% | 44% | 7% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-04T09:42 | METUSDT | surge | STOP | 7.8 | -3.25% | $-2.73 |
| 2026-10-04T09:25 | IOTAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.34 |
| 2026-10-04T08:36 | WUSDT | surge | TARGET | 4.5 | +2.75% | $+2.28 |
| 2026-10-04T08:03 | ZKUSDT | surge | TARGET | 13.8 | +2.75% | $+2.32 |
| 2026-10-04T03:55 | INJUSDT | surge | TIME | 24.0 | -1.69% | $-1.43 |
| 2026-10-04T01:33 | SNDKBUSDT | bottom | TIME | 24.0 | -0.40% | $-0.34 |
| 2026-10-03T21:36 | TRBUSDT | surge | STOP | 3.8 | -3.25% | $-2.86 |
| 2026-10-03T20:30 | IOUSDT | surge | TARGET | 5.5 | +2.75% | $+2.36 |
| 2026-10-03T18:08 | STXUSDT | surge | STOP | 1.0 | -3.25% | $-2.79 |
| 2026-10-03T18:08 | CRCLBUSDT | bottom | TIME | 24.0 | +1.33% | $+1.13 |
| 2026-10-03T17:51 | SUPERUSDT | surge | STOP | 1.5 | -3.25% | $-3.21 |
| 2026-10-03T17:34 | JTOUSDT | surge | TARGET | 0.8 | +2.75% | $+2.36 |
| 2026-10-03T17:17 | BNBUSDT | bottom | TARGET | 22.2 | +2.75% | $+2.29 |
| 2026-10-03T16:59 | STXUSDT | surge | TARGET | 2.5 | +2.75% | $+2.30 |
| 2026-10-03T16:42 | ZROUSDT | surge | STOP | 0.0 | -3.25% | $-2.88 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-03T15:50 | MORPHOUSDT | surge | 2.724 | 2.754 | +1.10% |
| 2026-10-03T17:17 | BNBUSDT | surge | 789.96 | 791.65 | +0.21% |
| 2026-10-03T17:51 | ATOMUSDT | surge | 1.733 | 1.753 | +1.15% |
| 2026-10-03T18:08 | OPUSDT | surge | 0.1355 | 0.1334 | -1.55% |
| 2026-10-03T20:30 | KAITOUSDT | surge | 0.3545 | 0.3454 | -2.57% |
| 2026-10-03T21:36 | DODOUSDT | surge | 0.01896 | 0.01863 | -1.74% |
| 2026-10-04T08:03 | ACEUSDT | surge | 0.1863 | 0.1882 | +1.02% |
| 2026-10-04T09:25 | IOTAUSDT | surge | 0.0607 | 0.0596 | -1.81% |
| 2026-10-04T09:42 | RUNEUSDT | surge | 0.782 | 0.789 | +0.90% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
