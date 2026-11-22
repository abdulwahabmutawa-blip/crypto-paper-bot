# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-22T08:51:56+00:00 · runs 6553 · equity **$475.58** (-52.44%) · cash $0.00 · open 10/10 · round trips 2136

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-526.80 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1839 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 297 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-22T08:50 | YBUSDT | bottom | TARGET | 3.0 | +2.75% | $+1.13 |
| 2026-11-22T08:50 | STXUSDT | surge | TARGET | 16.2 | +2.75% | $+1.17 |
| 2026-11-22T08:33 | ARUSDT | surge | TARGET | 15.8 | +2.75% | $+1.17 |
| 2026-11-22T08:16 | INJUSDT | bottom | TARGET | 4.2 | +2.75% | $+1.17 |
| 2026-11-22T08:16 | RENDERUSDT | surge | TARGET | 15.8 | +2.75% | $+1.17 |
| 2026-11-22T05:43 | UNIUSDT | surge | STOP | 13.0 | -3.25% | $-1.38 |
| 2026-11-22T03:58 | AIGENSYNUSDT | surge | TARGET | 0.5 | +2.75% | $+1.17 |
| 2026-11-22T03:58 | STRKUSDT | surge | STOP | 11.0 | -3.25% | $-1.38 |
| 2026-11-22T01:15 | ETHFIUSDT | surge | TARGET | 8.0 | +2.75% | $+1.20 |
| 2026-11-22T00:40 | NIGHTUSDT | surge | STOP | 5.0 | -3.25% | $-1.34 |
| 2026-11-21T18:58 | USUALUSDT | surge | STOP | 2.5 | -3.25% | $-1.38 |
| 2026-11-21T17:11 | BEAMXUSDT | surge | TARGET | 0.2 | +2.75% | $+1.17 |
| 2026-11-21T13:53 | ORCAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.17 |
| 2026-11-20T15:23 | STRKUSDT | bottom | STOP | 23.0 | -3.25% | $-1.36 |
| 2026-11-20T12:15 | AAVEUSDT | bottom | STOP | 20.2 | -3.25% | $-1.29 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-21T16:17 | ETCUSDT | surge | 5.5 | 5.48 | -0.36% |
| 2026-11-21T16:35 | PYTHUSDT | surge | 0.04835 | 0.04839 | +0.08% |
| 2026-11-22T02:42 | ICPUSDT | bottom | 1.885 | 1.913 | +1.49% |
| 2026-11-22T03:58 | ERAUSDT | surge | 0.0748 | 0.0768 | +2.67% |
| 2026-11-22T08:16 | KITEUSDT | surge | 0.1394 | 0.1401 | +0.50% |
| 2026-11-22T08:16 | RAREUSDT | bottom | 0.01357 | 0.01366 | +0.66% |
| 2026-11-22T08:33 | ARUSDT | surge | 2.31 | 2.309 | -0.04% |
| 2026-11-22T08:50 | SOXLBUSDT | surge | 33.5 | 33.51 | +0.03% |
| 2026-11-22T08:50 | SNXXBUSDT | surge | 1.84 | 1.85 | +0.54% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
