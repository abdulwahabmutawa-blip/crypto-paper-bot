# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-09T15:15:19+00:00 · runs 361 · equity **$995.49** (-0.45%) · cash $0.00 · open 10/10 · round trips 126

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean +0.01%/trade · realized $+1.26 · worst day $-18.97 · trades/day 25.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 73 | 56% | +0.17% | 52% | 38% | 10% |
| bottom | 53 | 47% | -0.20% | 45% | 43% | 11% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-09T10:10 | MRVLBUSDT | surge | STOP | 18.5 | -3.25% | $-3.22 |
| 2026-09-09T08:40 | PHAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.80 |
| 2026-09-09T08:23 | ATOMUSDT | surge | TARGET | 7.2 | +2.75% | $+3.01 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-08T15:19 | INTCBUSDT | surge | 103.55 | 105.1 | +1.50% |
| 2026-09-09T01:04 | HBARUSDT | bottom | 0.07895 | 0.07816 | -1.00% |
| 2026-09-09T03:34 | LTCUSDT | bottom | 53.9 | 53.93 | +0.06% |
| 2026-09-09T10:28 | HOLOUSDT | surge | 0.0676 | 0.0662 | -2.07% |
| 2026-09-09T13:44 | NEARUSDT | surge | 2.59 | 2.581 | -0.35% |
| 2026-09-09T14:02 | LITEBUSDT | surge | 1011.88 | 1013.78 | +0.19% |
| 2026-09-09T14:20 | MINAUSDT | surge | 0.0932 | 0.0917 | -1.61% |
| 2026-09-09T15:13 | DODOUSDT | surge | 0.01839 | 0.01838 | -0.05% |
| 2026-09-09T15:13 | XTZUSDT | surge | 0.2737 | 0.2707 | -1.10% |
| 2026-09-09T15:13 | MUBUSDT | surge | 1034.11 | 1020.58 | -1.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
