# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T13:11:16+00:00 · runs 354 · equity **$1,005.31** (+0.53%) · cash $0.00 · open 10/10 · round trips 119

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 54% (break-even 54%) · mean +0.08%/trade · realized $+9.34 · worst day $-18.97 · trades/day 23.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 67 | 58% | +0.29% | 54% | 36% | 10% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-09T12:16 | NEARUSDT | surge | TARGET | 0.5 | +2.75% | $+2.89 |
| 2026-09-09T11:38 | MINAUSDT | surge | STOP | 0.0 | -3.25% | $-3.17 |
| 2026-09-09T11:38 | ZECUSDT | surge | TARGET | 3.0 | +2.75% | $+3.09 |
| 2026-09-09T11:21 | ZKCUSDT | surge | TIME | 24.0 | -0.86% | $-0.84 |
| 2026-09-09T10:28 | NEARUSDT | surge | TARGET | 0.2 | +2.75% | $+2.63 |
| 2026-09-09T10:10 | MRVLBUSDT | surge | STOP | 18.5 | -3.25% | $-3.22 |
| 2026-09-09T08:40 | PHAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.80 |
| 2026-09-09T08:23 | ATOMUSDT | surge | TARGET | 7.2 | +2.75% | $+3.01 |
| 2026-09-09T08:07 | BNBUSDT | surge | TIME | 24.0 | -0.48% | $-0.49 |
| 2026-09-09T03:34 | ETCUSDT | surge | STOP | 0.5 | -3.25% | $-3.28 |
| 2026-09-09T02:59 | VETUSDT | surge | TARGET | 7.8 | +2.75% | $+2.70 |
| 2026-09-09T01:04 | SKHYBUSDT | surge | TIME | 24.0 | +1.51% | $+1.49 |
| 2026-09-09T00:47 | DOTUSDT | surge | STOP | 1.5 | -3.25% | $-3.68 |
| 2026-09-08T23:09 | ATOMUSDT | surge | TARGET | 2.5 | +2.75% | $+3.03 |
| 2026-09-08T20:20 | DOTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.95 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 715.46 | -0.26% |
| 2026-09-08T14:14 | TSLABUSDT | surge | 360.45 | 364.62 | +1.16% |
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 102.12 | -1.38% |
| 2026-09-08T17:18 | SPCXBUSDT | surge | 152.91 | 151.8 | -0.73% |
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.07894 | -0.01% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 54.37 | +0.87% |
| 2026-09-09T08:40 | DASHUSDT | surge | 65.51 | 64.46 | -1.60% |
| 2026-09-09T10:28 | HOLOUSDT | surge | 0.0676 | 0.0668 | -1.18% |
| 2026-09-09T11:38 | CHIPUSDT | surge | 0.05885 | 0.05848 | -0.63% |
| 2026-09-09T12:16 | IOUSDT | surge | 0.1432 | 0.143 | -0.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
