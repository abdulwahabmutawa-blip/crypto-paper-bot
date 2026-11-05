# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-05T12:53:41+00:00 · runs 5253 · equity **$554.88** (-44.51%) · cash $50.94 · open 9/10 · round trips 1836

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-444.17 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1595 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 241 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-05T12:51 | AEROUSDT | surge | STOP | 3.8 | -3.25% | $-1.65 |
| 2026-11-05T12:51 | CAKEUSDT | surge | STOP | 17.8 | -3.25% | $-1.77 |
| 2026-11-05T12:51 | BNCBUSDT | surge | STOP | 21.0 | -3.25% | $-1.72 |
| 2026-11-05T11:59 | PENDLEUSDT | surge | STOP | 19.5 | -3.25% | $-1.66 |
| 2026-11-05T08:45 | 1000CATUSDT | surge | STOP | 0.0 | -3.25% | $-1.70 |
| 2026-11-05T08:28 | 1000CATUSDT | surge | TARGET | 0.2 | +2.75% | $+1.40 |
| 2026-11-05T07:55 | STXUSDT | surge | STOP | 8.5 | -3.25% | $-1.71 |
| 2026-11-05T02:54 | BABABUSDT | surge | TARGET | 11.0 | +2.75% | $+1.46 |
| 2026-11-05T01:29 | MRNABUSDT | surge | TARGET | 4.0 | +2.75% | $+1.45 |
| 2026-11-04T23:14 | KMNOUSDT | surge | TARGET | 3.0 | +2.75% | $+1.41 |
| 2026-11-04T21:02 | MRNABUSDT | surge | TARGET | 4.2 | +2.75% | $+1.41 |
| 2026-11-04T20:09 | VETUSDT | surge | STOP | 4.2 | -3.25% | $-1.72 |
| 2026-11-04T18:57 | RAYUSDT | surge | TARGET | 3.2 | +2.75% | $+1.46 |
| 2026-11-04T16:35 | SUSDT | surge | STOP | 0.8 | -3.25% | $-1.72 |
| 2026-11-04T16:18 | MUBARAKUSDT | surge | STOP | 0.5 | -3.25% | $-1.72 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-04T15:41 | MSFTBUSDT | surge | 553.3 | 556.81 | +0.63% |
| 2026-11-04T15:41 | LUNCUSDT | surge | 4.224e-05 | 4.156e-05 | -1.61% |
| 2026-11-04T15:41 | AMZNBUSDT | surge | 269.29 | 270.94 | +0.61% |
| 2026-11-05T01:29 | NVDABUSDT | bottom | 199.06 | 196.62 | -1.23% |
| 2026-11-05T02:54 | BABABUSDT | surge | 109.24 | 110.78 | +1.41% |
| 2026-11-05T11:59 | INJUSDT | surge | 8.43 | 8.275 | -1.84% |
| 2026-11-05T12:51 | NEARUSDT | bottom | 3.939 | 3.944 | +0.13% |
| 2026-11-05T12:51 | HYPEUSDT | bottom | 81.78 | 81.75 | -0.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
