# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-08T13:42:50+00:00 · runs 267 · equity **$992.30** (-0.77%) · cash $0.00 · open 10/10 · round trips 93

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 54% (break-even 54%) · mean +0.05%/trade · realized $+3.64 · worst day $-18.97 · trades/day 23.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 42 | 60% | +0.27% | 55% | 38% | 7% |
| bottom | 51 | 49% | -0.14% | 47% | 43% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-08T13:24 | MINAUSDT | surge | TIME | 24.0 | +0.85% | $+0.86 |
| 2026-09-08T13:24 | ZKPUSDT | surge | TIME | 24.0 | +0.78% | $+0.79 |
| 2026-09-08T13:08 | SAHARAUSDT | surge | TARGET | 2.2 | +2.75% | $+2.72 |
| 2026-09-08T12:35 | ATOMUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-08T11:30 | MOVRUSDT | surge | STOP | 0.8 | -3.25% | $-3.12 |
| 2026-09-08T11:07 | VETUSDT | surge | TARGET | 0.8 | +2.75% | $+2.63 |
| 2026-09-08T10:34 | MEGAUSDT | surge | STOP | 2.5 | -3.25% | $-3.32 |
| 2026-09-08T10:17 | TSTUSDT | surge | STOP | 1.8 | -3.25% | $-3.22 |
| 2026-09-08T10:01 | MIRAUSDT | surge | STOP | 0.8 | -3.25% | $-3.21 |
| 2026-09-08T09:05 | KAITOUSDT | surge | STOP | 1.0 | -3.25% | $-3.32 |
| 2026-09-08T08:15 | 1000CATUSDT | surge | TARGET | 0.0 | +2.75% | $+2.81 |
| 2026-09-08T08:15 | HBARUSDT | surge | STOP | 12.0 | -3.25% | $-3.13 |
| 2026-09-08T07:58 | MEGAUSDT | surge | TARGET | 1.2 | +2.75% | $+2.73 |
| 2026-09-08T07:58 | CAKEUSDT | surge | TARGET | 1.5 | +2.75% | $+2.63 |
| 2026-09-08T07:58 | KAITOUSDT | surge | TARGET | 2.0 | +2.75% | $+2.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-07T17:10 | KAVAUSDT | surge | 0.05979 | 0.059 | -1.32% |
| 2026-09-07T21:35 | LINKUSDT | bottom | 12.761 | 12.344 | -3.27% |
| 2026-09-08T00:58 | SKHYBUSDT | surge | 184.72 | 185.3 | +0.31% |
| 2026-09-08T07:58 | BNBUSDT | surge | 756.19 | 743.78 | -1.64% |
| 2026-09-08T08:15 | ETCUSDT | surge | 8.08 | 8.14 | +0.74% |
| 2026-09-08T11:07 | ZKCUSDT | surge | 0.0493 | 0.0491 | -0.41% |
| 2026-09-08T12:35 | VETUSDT | surge | 0.00783 | 0.007687 | -1.83% |
| 2026-09-08T13:08 | HEIUSDT | surge | 0.1439 | 0.1428 | -0.76% |
| 2026-09-08T13:24 | SCRUSDT | surge | 0.0232 | 0.02345 | +1.08% |
| 2026-09-08T13:24 | BICOUSDT | surge | 0.02422 | 0.02323 | -4.09% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
