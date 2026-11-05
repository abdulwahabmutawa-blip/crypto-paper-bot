# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-05T08:13:51+00:00 · runs 5238 · equity **$561.27** (-43.87%) · cash $0.00 · open 10/10 · round trips 1830

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-437.07 · worst day $-50.94 · trades/day 29.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1589 | 49% | -0.28% | 46% | 47% | 7% |
| bottom | 241 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-05T07:55 | STXUSDT | surge | STOP | 8.5 | -3.25% | $-1.71 |
| 2026-11-05T02:54 | BABABUSDT | surge | TARGET | 11.0 | +2.75% | $+1.46 |
| 2026-11-05T01:29 | MRNABUSDT | surge | TARGET | 4.0 | +2.75% | $+1.45 |
| 2026-11-04T23:14 | KMNOUSDT | surge | TARGET | 3.0 | +2.75% | $+1.41 |
| 2026-11-04T21:02 | MRNABUSDT | surge | TARGET | 4.2 | +2.75% | $+1.41 |
| 2026-11-04T20:09 | VETUSDT | surge | STOP | 4.2 | -3.25% | $-1.72 |
| 2026-11-04T18:57 | RAYUSDT | surge | TARGET | 3.2 | +2.75% | $+1.46 |
| 2026-11-04T16:35 | SUSDT | surge | STOP | 0.8 | -3.25% | $-1.72 |
| 2026-11-04T16:18 | MUBARAKUSDT | surge | STOP | 0.5 | -3.25% | $-1.72 |
| 2026-11-04T15:41 | STXUSDT | surge | TARGET | 2.8 | +2.75% | $+1.36 |
| 2026-11-04T15:41 | MUBARAKUSDT | surge | TARGET | 3.2 | +2.75% | $+1.44 |
| 2026-11-04T15:41 | TIAUSDT | surge | TARGET | 6.8 | +2.75% | $+1.44 |
| 2026-11-04T15:41 | METABUSDT | surge | TARGET | 6.8 | +2.75% | $+1.38 |
| 2026-11-04T15:41 | BABABUSDT | surge | TARGET | 7.5 | +2.75% | $+1.44 |
| 2026-11-04T15:41 | ARUSDT | surge | TARGET | 8.0 | +2.75% | $+1.43 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-04T15:41 | MSFTBUSDT | surge | 553.3 | 555.61 | +0.42% |
| 2026-11-04T15:41 | BNCBUSDT | surge | 5.1 | 5.02 | -1.57% |
| 2026-11-04T15:41 | LUNCUSDT | surge | 4.224e-05 | 4.173e-05 | -1.21% |
| 2026-11-04T15:41 | AMZNBUSDT | surge | 269.29 | 268.11 | -0.44% |
| 2026-11-04T16:18 | PENDLEUSDT | surge | 1.821 | 1.782 | -2.14% |
| 2026-11-04T18:57 | CAKEUSDT | surge | 2.039 | 2.004 | -1.72% |
| 2026-11-05T01:29 | NVDABUSDT | bottom | 199.06 | 198.6 | -0.23% |
| 2026-11-05T02:54 | BABABUSDT | surge | 109.24 | 111.11 | +1.71% |
| 2026-11-05T07:55 | 1000CATUSDT | surge | 0.0018 | 0.001837 | +2.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
