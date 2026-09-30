# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T07:50:48+00:00 · runs 2165 · equity **$883.21** (-11.68%) · cash $0.00 · open 10/10 · round trips 814

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-116.25 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 698 | 52% | -0.10% | 49% | 44% | 7% |
| bottom | 116 | 45% | -0.41% | 41% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-29T19:59 | SKYUSDT | surge | STOP | 1.0 | -3.25% | $-3.01 |
| 2026-09-29T19:59 | COTIUSDT | surge | STOP | 1.8 | -3.25% | $-2.95 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 186.68 | -0.64% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01638 | +0.18% |
| 2026-09-29T17:35 | XLMUSDT | bottom | 0.2216 | 0.2248 | +1.44% |
| 2026-09-29T18:10 | CRCLBUSDT | bottom | 83.55 | 84.08 | +0.63% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 6.98 | -0.85% |
| 2026-09-30T01:32 | ASTERUSDT | surge | 0.7544 | 0.7615 | +0.94% |
| 2026-09-30T05:03 | NOMUSDT | surge | 0.002164 | 0.002128 | -1.66% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.325 | -0.48% |
| 2026-09-30T07:48 | KSMUSDT | surge | 5.24 | 5.24 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
