# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T15:39:01+00:00 · runs 363 · equity **$995.03** (-0.50%) · cash $0.00 · open 10/10 · round trips 129

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.03%/trade · realized $-4.33 · worst day $-18.97 · trades/day 25.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 76 | 55% | +0.09% | 50% | 39% | 11% |
| bottom | 53 | 47% | -0.20% | 45% | 43% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-09T15:36 | XTZUSDT | surge | STOP | 0.2 | -3.25% | $-3.29 |
| 2026-09-09T15:36 | MINAUSDT | surge | STOP | 1.0 | -3.25% | $-3.29 |
| 2026-09-09T15:36 | INTCBUSDT | surge | TIME | 24.0 | +1.00% | $+0.99 |
| 2026-09-09T15:13 | XTZUSDT | surge | TARGET | 0.8 | +2.75% | $+2.79 |
| 2026-09-09T15:13 | IOUSDT | surge | STOP | 2.8 | -3.25% | $-3.50 |
| 2026-09-09T15:13 | SPCXBUSDT | surge | STOP | 21.8 | -3.25% | $-3.18 |
| 2026-09-09T14:20 | DASHUSDT | surge | STOP | 5.5 | -3.25% | $-3.40 |
| 2026-09-09T14:02 | CHIPUSDT | surge | STOP | 2.2 | -3.25% | $-3.41 |
| 2026-09-09T14:02 | QQQBUSDT | bottom | TIME | 24.0 | -0.04% | $-0.04 |
| 2026-09-09T13:44 | TSLABUSDT | surge | TARGET | 23.5 | +2.75% | $+2.67 |
| 2026-09-09T12:16 | NEARUSDT | surge | TARGET | 0.5 | +2.75% | $+2.89 |
| 2026-09-09T11:38 | MINAUSDT | surge | STOP | 0.0 | -3.25% | $-3.17 |
| 2026-09-09T11:38 | ZECUSDT | surge | TARGET | 3.0 | +2.75% | $+3.09 |
| 2026-09-09T11:21 | ZKCUSDT | surge | TIME | 24.0 | -0.86% | $-0.84 |
| 2026-09-09T10:28 | NEARUSDT | surge | TARGET | 0.2 | +2.75% | $+2.63 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.07786 | -1.38% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 54.05 | +0.28% |
| 2026-09-09T10:28 | HOLOUSDT | surge | 0.0676 | 0.0662 | -2.07% |
| 2026-09-09T13:44 | NEARUSDT | surge | 2.59 | 2.571 | -0.73% |
| 2026-09-09T14:02 | LITEBUSDT | surge | 1011.88 | 1007.56 | -0.43% |
| 2026-09-09T15:13 | DODOUSDT | surge | 0.01839 | 0.01844 | +0.27% |
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1021.19 | -1.25% |
| 2026-09-09T15:36 | MRVLBUSDT | surge | 235.92 | 235.22 | -0.30% |
| 2026-09-09T15:36 | SKHYBUSDT | surge | 194.64 | 193.65 | -0.51% |
| 2026-09-09T15:36 | PHAUSDT | surge | 0.0289 | 0.0305 | +5.54% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
