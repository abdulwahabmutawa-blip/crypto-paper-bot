# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T14:04:22+00:00 · runs 357 · equity **$1,001.52** (+0.15%) · cash $0.00 · open 10/10 · round trips 122

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean +0.07%/trade · realized $+8.56 · worst day $-18.97 · trades/day 24.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 69 | 58% | +0.28% | 54% | 36% | 10% |
| bottom | 53 | 47% | -0.20% | 45% | 43% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-09T14:02 | CHIPUSDT | surge | STOP | 2.2 | -3.25% | $-3.41 |
| 2026-09-09T14:02 | QQQBUSDT | bottom | TIME | 24.0 | -0.04% | $-0.04 |
| 2026-09-09T13:44 | TSLABUSDT | surge | TARGET | 23.5 | +2.75% | $+2.67 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 105.45 | +1.83% |
| 2026-09-08T17:18 | SPCXBUSDT | surge | 152.91 | 151.39 | -0.99% |
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.07837 | -0.73% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 54.15 | +0.46% |
| 2026-09-09T08:40 | DASHUSDT | surge | 65.51 | 63.78 | -2.64% |
| 2026-09-09T10:28 | HOLOUSDT | surge | 0.0676 | 0.0663 | -1.92% |
| 2026-09-09T12:16 | IOUSDT | surge | 0.1432 | 0.141 | -1.54% |
| 2026-09-09T13:44 | NEARUSDT | surge | 2.59 | 2.568 | -0.85% |
| 2026-09-09T14:02 | XTZUSDT | surge | 0.264 | 0.2626 | -0.53% |
| 2026-09-09T14:02 | LITEBUSDT | surge | 1011.88 | 1012.83 | +0.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
