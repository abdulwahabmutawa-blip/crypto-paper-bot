# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T13:56:24+00:00 · runs 2184 · equity **$883.11** (-11.69%) · cash $0.00 · open 10/10 · round trips 824

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-118.93 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 706 | 52% | -0.11% | 49% | 44% | 7% |
| bottom | 118 | 46% | -0.36% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-30T13:37 | ENAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.31 |
| 2026-09-30T13:19 | ASTERUSDT | surge | TARGET | 11.5 | +2.75% | $+2.45 |
| 2026-09-30T13:02 | PROMUSDT | surge | STOP | 0.5 | -3.25% | $-2.77 |
| 2026-09-30T13:02 | CRCLBUSDT | bottom | TARGET | 18.8 | +2.75% | $+2.28 |
| 2026-09-30T12:45 | REZUSDT | surge | TARGET | 1.2 | +2.75% | $+2.34 |
| 2026-09-30T12:27 | RAREUSDT | surge | STOP | 2.0 | -3.25% | $-2.87 |
| 2026-09-30T11:22 | BERAUSDT | surge | STOP | 3.0 | -3.25% | $-2.86 |
| 2026-09-30T09:53 | XLMUSDT | bottom | TARGET | 16.0 | +2.75% | $+2.36 |
| 2026-09-30T08:24 | NOMUSDT | surge | STOP | 3.0 | -3.25% | $-2.97 |
| 2026-09-30T08:06 | KSMUSDT | surge | STOP | 0.0 | -3.25% | $-2.96 |
| 2026-09-30T07:48 | RAREUSDT | surge | STOP | 0.5 | -3.25% | $-3.05 |
| 2026-09-30T07:13 | COMPUSDT | surge | STOP | 2.8 | -3.25% | $-3.16 |
| 2026-09-30T05:38 | BERAUSDT | surge | TARGET | 1.5 | +2.75% | $+2.36 |
| 2026-09-30T05:03 | HUMAUSDT | surge | STOP | 1.5 | -3.25% | $-3.07 |
| 2026-09-30T04:27 | SPCXBUSDT | bottom | TIME | 24.0 | +2.19% | $+2.08 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 185.17 | -1.45% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01645 | +0.61% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 7.06 | +0.28% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.535 | +0.98% |
| 2026-09-30T08:24 | AXSUSDT | surge | 1.166 | 1.169 | +0.26% |
| 2026-09-30T12:45 | REZUSDT | surge | 0.004604 | 0.004618 | +0.30% |
| 2026-09-30T13:02 | ZENUSDT | surge | 7.433 | 7.499 | +0.89% |
| 2026-09-30T13:19 | ARKMUSDT | surge | 0.1385 | 0.1365 | -1.44% |
| 2026-09-30T13:37 | ENAUSDT | surge | 0.2689 | 0.2746 | +2.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
