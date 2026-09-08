# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-08T15:04:42+00:00 · runs 272 · equity **$1,003.17** (+0.32%) · cash $0.00 · open 10/10 · round trips 99

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 54% (break-even 54%) · mean +0.03%/trade · realized $+2.17 · worst day $-18.97 · trades/day 24.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 47 | 60% | +0.28% | 55% | 38% | 6% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-08T10:17 | TSTUSDT | surge | STOP | 1.8 | -3.25% | $-3.22 |
| 2026-09-08T10:01 | MIRAUSDT | surge | STOP | 0.8 | -3.25% | $-3.21 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-07T17:10 | KAVAUSDT | surge | 0.05979 | 0.05904 | -1.25% |
| 2026-09-08T00:58 | SKHYBUSDT | surge | 184.72 | 187.14 | +1.31% |
| 2026-09-08T07:58 | BNBUSDT | surge | 756.19 | 752.09 | -0.54% |
| 2026-09-08T11:07 | ZKCUSDT | surge | 0.0493 | 0.0489 | -0.81% |
| 2026-09-08T13:08 | HEIUSDT | surge | 0.1439 | 0.1422 | -1.18% |
| 2026-09-08T13:57 | COTIUSDT | surge | 0.01804 | 0.01782 | -1.22% |
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 718.99 | +0.23% |
| 2026-09-08T14:14 | TSLABUSDT | surge | 360.45 | 365.7 | +1.46% |
| 2026-09-08T14:14 | DOGSUSDT | surge | 4.912e-05 | 5.044e-05 | +2.69% |
| 2026-09-08T15:03 | FFUSDT | surge | 0.14155 | 0.14221 | +0.47% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
