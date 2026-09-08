# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-08T18:58:14+00:00 · runs 287 · equity **$1,000.74** (+0.07%) · cash $0.00 · open 10/10 · round trips 102

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean +0.01%/trade · realized $-0.14 · worst day $-18.97 · trades/day 25.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 50 | 58% | +0.22% | 54% | 38% | 8% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-08T17:18 | KAVAUSDT | surge | TIME | 24.0 | -1.69% | $-1.68 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-08T00:58 | SKHYBUSDT | surge | 184.72 | 187.05 | +1.26% |
| 2026-09-08T07:58 | BNBUSDT | surge | 756.19 | 748.94 | -0.96% |
| 2026-09-08T11:07 | ZKCUSDT | surge | 0.0493 | 0.0486 | -1.42% |
| 2026-09-08T13:08 | HEIUSDT | surge | 0.1439 | 0.1395 | -3.06% |
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 719.49 | +0.30% |
| 2026-09-08T14:14 | TSLABUSDT | surge | 360.45 | 366.85 | +1.78% |
| 2026-09-08T15:03 | FFUSDT | surge | 0.14155 | 0.14394 | +1.69% |
| 2026-09-08T15:19 | MRVLBUSDT | surge | 230.1 | 228.42 | -0.73% |
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 105.23 | +1.62% |
| 2026-09-08T17:18 | SPCXBUSDT | surge | 152.91 | 153.61 | +0.46% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
