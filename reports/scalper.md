# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-23T21:36:37+00:00 · runs 4191 · equity **$654.00** (-34.60%) · cash $-0.00 · open 10/10 · round trips 1502

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-339.29 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1314 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 188 | 45% | -0.37% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-23T21:17 | LAUSDT | surge | STOP | 0.2 | -3.25% | $-2.13 |
| 2026-10-23T21:17 | SENTUSDT | surge | STOP | 3.2 | -3.25% | $-2.17 |
| 2026-10-23T20:53 | LAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.75 |
| 2026-10-23T20:36 | ARKMUSDT | surge | STOP | 0.8 | -3.25% | $-2.14 |
| 2026-10-23T19:43 | ACEUSDT | surge | STOP | 11.0 | -3.25% | $-2.21 |
| 2026-10-23T17:56 | BEAMXUSDT | surge | TARGET | 10.8 | +2.75% | $+1.79 |
| 2026-10-23T15:34 | COTIUSDT | surge | STOP | 0.2 | -3.25% | $-2.11 |
| 2026-10-23T15:11 | COTIUSDT | surge | TARGET | 4.5 | +2.75% | $+1.74 |
| 2026-10-23T13:01 | ARKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.84 |
| 2026-10-23T12:44 | ARKUSDT | surge | TARGET | 1.8 | +2.75% | $+1.79 |
| 2026-10-23T11:06 | STRKUSDT | bottom | STOP | 7.5 | -3.25% | $-2.07 |
| 2026-10-23T10:50 | ARKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.74 |
| 2026-10-23T10:34 | REZUSDT | surge | STOP | 2.8 | -3.25% | $-2.13 |
| 2026-10-23T10:18 | ARKUSDT | surge | TARGET | 0.2 | +2.75% | $+1.69 |
| 2026-10-23T09:45 | DASHUSDT | surge | STOP | 7.2 | -3.25% | $-2.07 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-23T02:23 | ATOMUSDT | surge | 1.766 | 1.743 | -1.30% |
| 2026-10-23T02:23 | RUNEUSDT | bottom | 0.642 | 0.634 | -1.25% |
| 2026-10-23T04:15 | BCHUSDT | surge | 284.8 | 284.4 | -0.14% |
| 2026-10-23T04:32 | BNCBUSDT | surge | 5.49 | 5.37 | -2.19% |
| 2026-10-23T11:06 | BOMEUSDT | surge | 0.0006433 | 0.000644 | +0.11% |
| 2026-10-23T13:01 | BONKUSDT | surge | 3.29e-06 | 3.18e-06 | -3.34% |
| 2026-10-23T15:34 | MSTRBUSDT | surge | 148.55 | 147.17 | -0.93% |
| 2026-10-23T21:17 | INITUSDT | surge | 0.15412 | 0.15329 | -0.54% |
| 2026-10-23T21:17 | WLFIUSDT | surge | 0.0548 | 0.0544 | -0.73% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
