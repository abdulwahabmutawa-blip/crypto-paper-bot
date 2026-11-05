# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-05T14:55:27+00:00 · runs 5260 · equity **$544.76** (-45.52%) · cash $150.57 · open 7/10 · round trips 1840

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.33%/trade · realized $-450.91 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1598 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 242 | 43% | -0.53% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-05T14:53 | NILUSDT | surge | STOP | 1.2 | -3.25% | $-1.66 |
| 2026-11-05T14:53 | INJUSDT | surge | STOP | 2.8 | -3.25% | $-1.61 |
| 2026-11-05T14:53 | NVDABUSDT | bottom | STOP | 13.2 | -3.25% | $-1.76 |
| 2026-11-05T14:53 | LUNCUSDT | surge | STOP | 23.0 | -3.25% | $-1.72 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-04T15:41 | MSFTBUSDT | surge | 553.3 | 546.8 | -1.17% |
| 2026-11-04T15:41 | AMZNBUSDT | surge | 269.29 | 264.36 | -1.83% |
| 2026-11-05T02:54 | BABABUSDT | surge | 109.24 | 107.06 | -2.00% |
| 2026-11-05T12:51 | NEARUSDT | bottom | 3.939 | 3.889 | -1.27% |
| 2026-11-05T12:51 | HYPEUSDT | bottom | 81.78 | 80.48 | -1.59% |
| 2026-11-05T14:53 | SUIUSDT | bottom | 0.8939 | 0.8904 | -0.39% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
