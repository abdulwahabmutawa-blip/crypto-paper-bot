# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T11:42:16+00:00 · runs 2178 · equity **$880.01** (-12.00%) · cash $0.00 · open 10/10 · round trips 818

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-122.68 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 701 | 52% | -0.11% | 49% | 45% | 7% |
| bottom | 117 | 45% | -0.39% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-30T11:22 | BERAUSDT | surge | STOP | 3.0 | -3.25% | $-2.86 |
| 2026-09-30T09:53 | XLMUSDT | bottom | TARGET | 16.0 | +2.75% | $+2.36 |
| 2026-09-30T08:24 | NOMUSDT | surge | STOP | 3.0 | -3.25% | $-2.97 |
| 2026-09-30T08:06 | KSMUSDT | surge | STOP | 0.0 | -3.25% | $-2.96 |
| 2026-09-30T07:48 | RAREUSDT | surge | STOP | 0.5 | -3.25% | $-3.05 |
| 2026-09-30T07:13 | COMPUSDT | surge | STOP | 2.8 | -3.25% | $-3.16 |
| 2026-09-30T05:38 | BERAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.36 |
| 2026-09-30T05:03 | HUMAUSDT | surge | STOP | 1.5 | -3.25% | $-3.07 |
| 2026-09-30T04:27 | SPCXBUSDT | bottom | TIME | 24.0 | +2.19% | $+2.08 |
| 2026-09-30T03:52 | PUMPUSDT | surge | STOP | 7.8 | -3.25% | $-2.88 |
| 2026-09-30T03:17 | TRBUSDT | surge | STOP | 0.5 | -3.25% | $-3.17 |
| 2026-09-30T02:42 | TRBUSDT | surge | TARGET | 5.0 | +2.75% | $+2.61 |
| 2026-09-30T01:32 | PHAUSDT | surge | STOP | 0.0 | -3.25% | $-2.99 |
| 2026-09-30T01:14 | PHAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.46 |
| 2026-09-29T23:42 | NIGHTUSDT | surge | TARGET | 7.8 | +2.75% | $+2.40 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 185.78 | -1.12% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01657 | +1.35% |
| 2026-09-29T18:10 | CRCLBUSDT | bottom | 83.55 | 84.33 | +0.93% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 7.07 | +0.43% |
| 2026-09-30T01:32 | ASTERUSDT | surge | 0.7544 | 0.7587 | +0.57% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.416 | +0.15% |
| 2026-09-30T08:24 | AXSUSDT | surge | 1.166 | 1.17 | +0.34% |
| 2026-09-30T09:53 | RAREUSDT | surge | 0.01867 | 0.01848 | -1.02% |
| 2026-09-30T11:22 | REZUSDT | surge | 0.004457 | 0.004528 | +1.59% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
