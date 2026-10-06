# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-06T14:51:58+00:00 · runs 2695 · equity **$835.66** (-16.43%) · cash $0.00 · open 10/10 · round trips 1002

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.18%/trade · realized $-169.56 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 875 | 51% | -0.15% | 48% | 44% | 8% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-06T14:15 | MRNABUSDT | surge | STOP | 0.0 | -3.25% | $-2.77 |
| 2026-10-06T14:15 | C98USDT | surge | TARGET | 0.2 | +2.75% | $+2.24 |
| 2026-10-06T13:57 | MRNABUSDT | surge | TARGET | 18.2 | +2.75% | $+2.28 |
| 2026-10-06T13:39 | C98USDT | surge | TARGET | 0.5 | +2.75% | $+2.00 |
| 2026-10-06T13:39 | TRBUSDT | surge | TARGET | 1.0 | +2.75% | $+2.36 |
| 2026-10-06T11:54 | WDCBUSDT | surge | STOP | 19.5 | -3.25% | $-2.44 |
| 2026-10-06T11:19 | C98USDT | surge | TARGET | 1.5 | +2.75% | $+2.30 |
| 2026-10-06T09:34 | LPTUSDT | surge | STOP | 1.0 | -3.25% | $-2.81 |
| 2026-10-06T08:24 | SENTUSDT | surge | TARGET | 4.5 | +2.75% | $+2.32 |
| 2026-10-06T07:49 | PARTIUSDT | surge | TARGET | 4.0 | +2.75% | $+2.32 |
| 2026-10-06T07:31 | VTHOUSDT | surge | STOP | 0.0 | -3.25% | $-2.57 |
| 2026-10-06T07:14 | VTHOUSDT | surge | TARGET | 1.8 | +2.75% | $+2.11 |
| 2026-10-06T06:56 | CHIPUSDT | surge | TARGET | 3.0 | +2.75% | $+2.32 |
| 2026-10-06T05:12 | SUSDT | surge | STOP | 4.8 | -3.25% | $-2.58 |
| 2026-10-06T03:44 | ORDIUSDT | surge | STOP | 4.0 | -3.25% | $-2.83 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-05T16:36 | TSLABUSDT | surge | 378.15 | 380.77 | +0.69% |
| 2026-10-05T20:18 | SPCXBUSDT | surge | 171.35 | 175.01 | +2.14% |
| 2026-10-05T23:04 | FILUSDT | surge | 1.179 | 1.1623 | -1.42% |
| 2026-10-06T06:56 | ACEUSDT | surge | 0.1927 | 0.1973 | +2.39% |
| 2026-10-06T07:31 | WLFIUSDT | surge | 0.0564 | 0.0564 | +0.00% |
| 2026-10-06T07:49 | GRAMUSDT | surge | 1.573 | 1.565 | -0.51% |
| 2026-10-06T13:39 | ALICEUSDT | surge | 0.1912 | 0.1948 | +1.88% |
| 2026-10-06T14:15 | TRBUSDT | surge | 21.87 | 22.25 | +1.74% |
| 2026-10-06T14:15 | CRCLBUSDT | surge | 86.06 | 85.39 | -0.78% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
