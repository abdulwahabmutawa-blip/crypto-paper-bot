# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T15:43:55+00:00 · runs 5179 · equity **$562.43** (-43.76%) · cash $0.00 · open 10/10 · round trips 1821

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-437.37 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1580 | 49% | -0.28% | 46% | 47% | 7% |
| bottom | 241 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-04T15:41 | STXUSDT | surge | TARGET | 2.8 | +2.75% | $+1.36 |
| 2026-11-04T15:41 | MUBARAKUSDT | surge | TARGET | 3.2 | +2.75% | $+1.44 |
| 2026-11-04T15:41 | TIAUSDT | surge | TARGET | 6.8 | +2.75% | $+1.44 |
| 2026-11-04T15:41 | METABUSDT | surge | TARGET | 6.8 | +2.75% | $+1.38 |
| 2026-11-04T15:41 | BABABUSDT | surge | TARGET | 7.5 | +2.75% | $+1.44 |
| 2026-11-04T15:41 | ARUSDT | surge | TARGET | 8.0 | +2.75% | $+1.43 |
| 2026-11-04T15:41 | DOGEUSDT | surge | TARGET | 8.5 | +2.75% | $+1.44 |
| 2026-11-04T15:41 | AEROUSDT | surge | TARGET | 9.8 | +2.75% | $+1.40 |
| 2026-11-04T15:41 | LINKUSDT | bottom | TARGET | 14.0 | +2.75% | $+1.42 |
| 2026-11-04T12:23 | AMDBUSDT | surge | STOP | 6.8 | -3.25% | $-1.66 |
| 2026-11-04T12:06 | ICPUSDT | surge | TARGET | 6.5 | +2.75% | $+1.40 |
| 2026-11-04T08:22 | ONDOUSDT | surge | TARGET | 3.0 | +2.75% | $+1.40 |
| 2026-11-04T07:42 | LSKUSDT | surge | STOP | 0.5 | -3.25% | $-1.69 |
| 2026-11-04T07:07 | RAYUSDT | surge | TARGET | 1.8 | +2.75% | $+1.40 |
| 2026-11-04T06:49 | ZAMAUSDT | surge | TARGET | 1.0 | +2.75% | $+1.43 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-04T15:41 | VETUSDT | surge | 0.005945 | 0.005987 | +0.71% |
| 2026-11-04T15:41 | MUBARAKUSDT | surge | 0.04409 | 0.04392 | -0.39% |
| 2026-11-04T15:41 | BABABUSDT | surge | 106.72 | 106.88 | +0.15% |
| 2026-11-04T15:41 | SUSDT | surge | 0.04254 | 0.04227 | -0.63% |
| 2026-11-04T15:41 | MSFTBUSDT | surge | 553.3 | 556.12 | +0.51% |
| 2026-11-04T15:41 | BNCBUSDT | surge | 5.1 | 5.09 | -0.20% |
| 2026-11-04T15:41 | RAYUSDT | surge | 1.7339 | 1.7349 | +0.06% |
| 2026-11-04T15:41 | LUNCUSDT | surge | 4.224e-05 | 4.218e-05 | -0.14% |
| 2026-11-04T15:41 | AMZNBUSDT | surge | 269.29 | 268.09 | -0.45% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
