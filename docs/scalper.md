# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-22T10:04:27+00:00 · runs 6558 · equity **$481.40** (-51.86%) · cash $0.00 · open 10/10 · round trips 2140

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.35%/trade · realized $-522.09 · worst day $-50.94 · trades/day 27.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1841 | 48% | -0.33% | 45% | 48% | 7% |
| bottom | 299 | 43% | -0.45% | 37% | 43% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-22T10:02 | SNXXBUSDT | surge | TARGET | 1.0 | +2.75% | $+1.18 |
| 2026-11-22T10:02 | ICPUSDT | bottom | TARGET | 7.2 | +2.75% | $+1.17 |
| 2026-11-22T09:45 | RAREUSDT | bottom | TARGET | 1.2 | +2.75% | $+1.20 |
| 2026-11-22T09:07 | ERAUSDT | surge | TARGET | 5.0 | +2.75% | $+1.17 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-21T16:17 | ETCUSDT | surge | 5.5 | 5.56 | +1.09% |
| 2026-11-21T16:35 | PYTHUSDT | surge | 0.04835 | 0.04918 | +1.72% |
| 2026-11-22T08:16 | KITEUSDT | surge | 0.1394 | 0.1424 | +2.15% |
| 2026-11-22T08:33 | ARUSDT | surge | 2.31 | 2.349 | +1.69% |
| 2026-11-22T08:50 | SOXLBUSDT | surge | 33.5 | 33.84 | +1.01% |
| 2026-11-22T09:07 | RENDERUSDT | surge | 1.337 | 1.344 | +0.52% |
| 2026-11-22T09:45 | KORUBUSDT | surge | 5.18 | 5.2 | +0.39% |
| 2026-11-22T10:02 | EWYBUSDT | surge | 127.63 | 127.58 | -0.04% |
| 2026-11-22T10:02 | BONKUSDT | surge | 2.1e-06 | 2.09e-06 | -0.48% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
