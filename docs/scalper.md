# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T13:46:40+00:00 · runs 356 · equity **$1,003.64** (+0.36%) · cash $0.00 · open 10/10 · round trips 120

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 54% (break-even 54%) · mean +0.10%/trade · realized $+12.01 · worst day $-18.97 · trades/day 24.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 68 | 59% | +0.33% | 54% | 35% | 10% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-09T00:47 | DOTUSDT | surge | STOP | 1.5 | -3.25% | $-3.68 |
| 2026-09-08T23:09 | ATOMUSDT | surge | TARGET | 2.5 | +2.75% | $+3.03 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 716.55 | -0.11% |
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 104.45 | +0.87% |
| 2026-09-08T17:18 | SPCXBUSDT | surge | 152.91 | 152.09 | -0.54% |
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.07856 | -0.49% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 54 | +0.19% |
| 2026-09-09T08:40 | DASHUSDT | surge | 65.51 | 64.22 | -1.97% |
| 2026-09-09T10:28 | HOLOUSDT | surge | 0.0676 | 0.0664 | -1.78% |
| 2026-09-09T11:38 | CHIPUSDT | surge | 0.05885 | 0.05736 | -2.53% |
| 2026-09-09T12:16 | IOUSDT | surge | 0.1432 | 0.1414 | -1.26% |
| 2026-09-09T13:44 | NEARUSDT | surge | 2.59 | 2.578 | -0.46% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
