# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T05:40:24+00:00 · runs 2157 · equity **$890.11** (-10.99%) · cash $0.00 · open 10/10 · round trips 812

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.13%/trade · realized $-110.04 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 696 | 52% | -0.09% | 49% | 44% | 7% |
| bottom | 116 | 45% | -0.41% | 41% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-29T19:59 | SKYUSDT | surge | STOP | 1.0 | -3.25% | $-3.01 |
| 2026-09-29T19:59 | COTIUSDT | surge | STOP | 1.8 | -3.25% | $-2.95 |
| 2026-09-29T18:51 | SKYUSDT | surge | TARGET | 1.8 | +2.75% | $+2.48 |
| 2026-09-29T18:10 | ALICEUSDT | surge | STOP | 0.2 | -3.25% | $-2.79 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 186.63 | -0.67% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.0164 | +0.31% |
| 2026-09-29T17:35 | XLMUSDT | bottom | 0.2216 | 0.2228 | +0.54% |
| 2026-09-29T18:10 | CRCLBUSDT | bottom | 83.55 | 84.15 | +0.72% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 7.09 | +0.71% |
| 2026-09-30T01:32 | ASTERUSDT | surge | 0.7544 | 0.7614 | +0.93% |
| 2026-09-30T04:27 | COMPUSDT | surge | 26.11 | 25.63 | -1.84% |
| 2026-09-30T05:03 | NOMUSDT | surge | 0.002164 | 0.002156 | -0.37% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.413 | +0.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
