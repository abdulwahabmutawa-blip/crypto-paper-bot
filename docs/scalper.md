# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T13:04:32+00:00 · runs 2181 · equity **$885.46** (-11.45%) · cash $0.00 · open 10/10 · round trips 822

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-123.69 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 704 | 52% | -0.11% | 49% | 45% | 7% |
| bottom | 118 | 46% | -0.36% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-30T03:52 | PUMPUSDT | surge | STOP | 7.8 | -3.25% | $-2.88 |
| 2026-09-30T03:17 | TRBUSDT | surge | STOP | 0.5 | -3.25% | $-3.17 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T15:13 | SKHYBUSDT | surge | 187.89 | 187.36 | -0.28% |
| 2026-09-29T15:31 | CHZUSDT | surge | 0.01635 | 0.01672 | +2.26% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 7.19 | +2.13% |
| 2026-09-30T01:32 | ASTERUSDT | surge | 0.7544 | 0.7697 | +2.03% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.72 | +2.26% |
| 2026-09-30T08:24 | AXSUSDT | surge | 1.166 | 1.177 | +0.94% |
| 2026-09-30T12:45 | REZUSDT | surge | 0.004604 | 0.004662 | +1.26% |
| 2026-09-30T13:02 | ZENUSDT | surge | 7.433 | 7.425 | -0.11% |
| 2026-09-30T13:02 | ENAUSDT | surge | 0.262 | 0.2617 | -0.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
