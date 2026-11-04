# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-04T19:00:09+00:00 · runs 5190 · equity **$557.09** (-44.29%) · cash $0.00 · open 10/10 · round trips 1824

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-439.36 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1583 | 49% | -0.29% | 46% | 47% | 7% |
| bottom | 241 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-04T18:57 | RAYUSDT | surge | TARGET | 3.2 | +2.75% | $+1.46 |
| 2026-11-04T16:35 | SUSDT | surge | STOP | 0.8 | -3.25% | $-1.72 |
| 2026-11-04T16:18 | MUBARAKUSDT | surge | STOP | 0.5 | -3.25% | $-1.72 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-04T15:41 | VETUSDT | surge | 0.005945 | 0.005796 | -2.51% |
| 2026-11-04T15:41 | BABABUSDT | surge | 106.72 | 106.72 | +0.00% |
| 2026-11-04T15:41 | MSFTBUSDT | surge | 553.3 | 555.1 | +0.33% |
| 2026-11-04T15:41 | BNCBUSDT | surge | 5.1 | 5.02 | -1.57% |
| 2026-11-04T15:41 | LUNCUSDT | surge | 4.224e-05 | 4.154e-05 | -1.66% |
| 2026-11-04T15:41 | AMZNBUSDT | surge | 269.29 | 268.01 | -0.48% |
| 2026-11-04T16:18 | PENDLEUSDT | surge | 1.821 | 1.813 | -0.44% |
| 2026-11-04T16:35 | MRNABUSDT | surge | 247.16 | 246.01 | -0.47% |
| 2026-11-04T18:57 | CAKEUSDT | surge | 2.039 | 2.04 | +0.05% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
