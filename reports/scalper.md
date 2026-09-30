# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T09:01:53+00:00 · runs 2169 · equity **$880.99** (-11.90%) · cash $0.00 · open 10/10 · round trips 816

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-122.18 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 700 | 52% | -0.10% | 49% | 44% | 7% |
| bottom | 116 | 45% | -0.41% | 41% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-29T21:08 | MOVRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.54 |
| 2026-09-29T20:16 | ICPUSDT | surge | TARGET | 3.2 | +2.75% | $+2.48 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 186.38 | -0.80% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01648 | +0.80% |
| 2026-09-29T17:35 | XLMUSDT | bottom | 0.2216 | 0.2245 | +1.31% |
| 2026-09-29T18:10 | CRCLBUSDT | bottom | 83.55 | 83.86 | +0.37% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 6.98 | -0.85% |
| 2026-09-30T01:32 | ASTERUSDT | surge | 0.7544 | 0.7671 | +1.68% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.308 | -0.60% |
| 2026-09-30T08:06 | BERAUSDT | surge | 0.2535 | 0.2563 | +1.10% |
| 2026-09-30T08:24 | AXSUSDT | surge | 1.166 | 1.174 | +0.69% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
