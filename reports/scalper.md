# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-08T23:59:50+00:00 · runs 306 · equity **$1,006.29** (+0.63%) · cash $0.00 · open 10/10 · round trips 106

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 54% (break-even 54%) · mean +0.05%/trade · realized $+5.40 · worst day $-18.97 · trades/day 26.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 54 | 59% | +0.30% | 56% | 37% | 7% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-08T23:09 | ATOMUSDT | surge | TARGET | 2.5 | +2.75% | $+3.03 |
| 2026-09-08T20:20 | DOTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.95 |
| 2026-09-08T19:46 | FFUSDT | surge | TARGET | 4.5 | +2.75% | $+2.87 |
| 2026-09-08T19:13 | HEIUSDT | surge | STOP | 5.8 | -3.25% | $-3.30 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-08T00:58 | SKHYBUSDT | surge | 184.72 | 184.61 | -0.06% |
| 2026-09-08T07:58 | BNBUSDT | surge | 756.19 | 752.43 | -0.50% |
| 2026-09-08T11:07 | ZKCUSDT | surge | 0.0493 | 0.0495 | +0.41% |
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 717.66 | +0.05% |
| 2026-09-08T14:14 | TSLABUSDT | surge | 360.45 | 366.46 | +1.67% |
| 2026-09-08T15:19 | MRVLBUSDT | surge | 230.1 | 224.59 | -2.39% |
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 103.92 | +0.36% |
| 2026-09-08T17:18 | SPCXBUSDT | surge | 152.91 | 152.88 | -0.02% |
| 2026-09-08T19:13 | VETUSDT | surge | 0.007951 | 0.008067 | +1.46% |
| 2026-09-08T23:09 | DOTUSDT | surge | 1.247 | 1.247 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
