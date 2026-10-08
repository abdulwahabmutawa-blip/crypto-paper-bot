# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-08T03:17:14+00:00 · runs 2824 · equity **$795.88** (-20.41%) · cash $79.29 · open 9/10 · round trips 1051

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
| 2026-10-08T01:51 | LINKUSDT | bottom | 13.313 | 13.166 | -1.10% |
| 2026-10-08T02:08 | MSTRBUSDT | bottom | 153.72 | 152.86 | -0.56% |
| 2026-10-08T02:25 | BOMEUSDT | surge | 0.001061 | 0.0010388 | -2.09% |
| 2026-10-08T02:58 | CRVUSDT | surge | 0.3923 | 0.3911 | -0.31% |
| 2026-10-08T02:58 | ENAUSDT | bottom | 0.2257 | 0.2233 | -1.06% |
| 2026-10-08T03:15 | JTOUSDT | surge | 0.5609 | 0.5589 | -0.36% |
| 2026-10-08T03:15 | CHIPUSDT | surge | 0.0537 | 0.05384 | +0.26% |
| 2026-10-08T03:15 | LDOUSDT | surge | 0.4624 | 0.4625 | +0.02% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
