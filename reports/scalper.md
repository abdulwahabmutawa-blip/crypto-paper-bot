# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T08:08:46+00:00 · runs 336 · equity **$1,008.59** (+0.86%) · cash $0.00 · open 10/10 · round trips 111

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean +0.03%/trade · realized $+2.15 · worst day $-18.97 · trades/day 22.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 59 | 58% | +0.22% | 53% | 37% | 10% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-09T08:07 | BNBUSDT | surge | TIME | 24.0 | -0.48% | $-0.49 |
| 2026-09-09T03:34 | ETCUSDT | surge | STOP | 0.5 | -3.25% | $-3.28 |
| 2026-09-09T02:59 | VETUSDT | surge | TARGET | 7.8 | +2.75% | $+2.70 |
| 2026-09-09T01:04 | SKHYBUSDT | surge | TIME | 24.0 | +1.51% | $+1.49 |
| 2026-09-09T00:47 | DOTUSDT | surge | STOP | 1.5 | -3.25% | $-3.68 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-08T11:07 | ZKCUSDT | surge | 0.0493 | 0.0492 | -0.20% |
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 719.82 | +0.35% |
| 2026-09-08T14:14 | TSLABUSDT | surge | 360.45 | 367.94 | +2.08% |
| 2026-09-08T15:19 | MRVLBUSDT | surge | 230.1 | 226.44 | -1.59% |
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 103.81 | +0.25% |
| 2026-09-08T17:18 | SPCXBUSDT | surge | 152.91 | 153 | +0.06% |
| 2026-09-09T00:47 | ATOMUSDT | surge | 1.851 | 1.902 | +2.76% |
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.0798 | +1.08% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 54.49 | +1.09% |
| 2026-09-09T08:07 | PHAUSDT | surge | 0.027 | 0.0271 | +0.37% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
