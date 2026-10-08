# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T03:00:18+00:00 · runs 2823 · equity **$799.51** (-20.05%) · cash $317.18 · open 6/10 · round trips 1051

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.20%/trade · realized $-199.99 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 919 | 50% | -0.18% | 48% | 45% | 8% |
| bottom | 132 | 45% | -0.40% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-08T02:58 | OGNUSDT | surge | STOP | 0.8 | -3.25% | $-2.58 |
| 2026-10-08T02:58 | SPCXBUSDT | bottom | TIME | 24.0 | -0.34% | $-0.28 |
| 2026-10-08T02:08 | TRXUSDT | bottom | TIME | 24.0 | +0.02% | $+0.01 |
| 2026-10-07T16:14 | AVAXUSDT | bottom | TARGET | 13.2 | +2.75% | $+2.24 |
| 2026-10-07T11:46 | STXUSDT | surge | STOP | 3.8 | -3.25% | $-2.62 |
| 2026-10-07T11:46 | ARKUSDT | surge | STOP | 4.2 | -3.25% | $-2.62 |
| 2026-10-07T09:43 | PARTIUSDT | surge | STOP | 1.8 | -3.25% | $-2.62 |
| 2026-10-07T09:43 | PUMPUSDT | surge | STOP | 2.0 | -3.25% | $-2.62 |
| 2026-10-07T08:13 | SYNUSDT | surge | STOP | 0.8 | -3.25% | $-2.61 |
| 2026-10-07T07:19 | PUMPUSDT | surge | TARGET | 1.8 | +2.75% | $+2.20 |
| 2026-10-07T06:43 | ACEUSDT | surge | STOP | 1.2 | -3.25% | $-2.60 |
| 2026-10-07T06:43 | STXUSDT | surge | TARGET | 2.8 | +2.75% | $+2.24 |
| 2026-10-07T06:20 | MOVRUSDT | surge | STOP | 0.8 | -3.25% | $-2.60 |
| 2026-10-07T06:20 | PARTIUSDT | surge | TARGET | 1.2 | +2.75% | $+2.22 |
| 2026-10-07T06:02 | SANDUSDT | surge | STOP | 0.0 | -3.25% | $-2.69 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T01:51 | LINKUSDT | bottom | 13.313 | 13.265 | -0.36% |
| 2026-10-08T02:08 | MSTRBUSDT | bottom | 153.72 | 153.95 | +0.15% |
| 2026-10-08T02:25 | BOMEUSDT | surge | 0.001061 | 0.0010485 | -1.18% |
| 2026-10-08T02:58 | CRVUSDT | surge | 0.3923 | 0.3951 | +0.71% |
| 2026-10-08T02:58 | ENAUSDT | bottom | 0.2257 | 0.2258 | +0.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
