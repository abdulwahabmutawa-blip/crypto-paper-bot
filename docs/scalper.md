# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-08T16:10:10+00:00 · runs 276 · equity **$1,003.83** (+0.38%) · cash $0.00 · open 10/10 · round trips 101

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean +0.02%/trade · realized $+1.54 · worst day $-18.97 · trades/day 25.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 49 | 59% | +0.26% | 55% | 39% | 6% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-08T15:19 | DOGSUSDT | surge | TARGET | 1.0 | +2.75% | $+2.67 |
| 2026-09-08T15:19 | COTIUSDT | surge | STOP | 1.2 | -3.25% | $-3.30 |
| 2026-09-08T15:03 | PROMUSDT | surge | TARGET | 1.0 | +2.75% | $+2.79 |
| 2026-09-08T14:14 | VETUSDT | surge | STOP | 1.2 | -3.25% | $-3.10 |
| 2026-09-08T14:14 | ETCUSDT | surge | TARGET | 5.8 | +2.75% | $+2.72 |
| 2026-09-08T13:57 | BICOUSDT | surge | STOP | 0.2 | -3.25% | $-3.32 |
| 2026-09-08T13:57 | SCRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.81 |
| 2026-09-08T13:57 | LINKUSDT | bottom | STOP | 16.0 | -3.25% | $-3.38 |
| 2026-09-08T13:24 | MINAUSDT | surge | TIME | 24.0 | +0.85% | $+0.86 |
| 2026-09-08T13:24 | ZKPUSDT | surge | TIME | 24.0 | +0.78% | $+0.79 |
| 2026-09-08T13:08 | SAHARAUSDT | surge | TARGET | 2.2 | +2.75% | $+2.72 |
| 2026-09-08T12:35 | ATOMUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-08T11:30 | MOVRUSDT | surge | STOP | 0.8 | -3.25% | $-3.12 |
| 2026-09-08T11:07 | VETUSDT | surge | TARGET | 0.8 | +2.75% | $+2.63 |
| 2026-09-08T10:34 | MEGAUSDT | surge | STOP | 2.5 | -3.25% | $-3.32 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-07T17:10 | KAVAUSDT | surge | 0.05979 | 0.05868 | -1.86% |
| 2026-09-08T00:58 | SKHYBUSDT | surge | 184.72 | 188.6 | +2.10% |
| 2026-09-08T07:58 | BNBUSDT | surge | 756.19 | 754.73 | -0.19% |
| 2026-09-08T11:07 | ZKCUSDT | surge | 0.0493 | 0.0487 | -1.22% |
| 2026-09-08T13:08 | HEIUSDT | surge | 0.1439 | 0.1421 | -1.25% |
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 719.79 | +0.34% |
| 2026-09-08T14:14 | TSLABUSDT | surge | 360.45 | 367.51 | +1.96% |
| 2026-09-08T15:03 | FFUSDT | surge | 0.14155 | 0.14244 | +0.63% |
| 2026-09-08T15:19 | MRVLBUSDT | surge | 230.1 | 231.28 | +0.51% |
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 104.93 | +1.33% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
