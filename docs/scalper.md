# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-22T01:52:30+00:00 · runs 6528 · equity **$471.27** (-52.87%) · cash $84.80 · open 8/10 · round trips 2128

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-531.01 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1833 | 48% | -0.34% | 45% | 48% | 7% |
| bottom | 295 | 43% | -0.50% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-22T01:15 | ETHFIUSDT | surge | TARGET | 8.0 | +2.75% | $+1.20 |
| 2026-11-22T00:40 | NIGHTUSDT | surge | STOP | 5.0 | -3.25% | $-1.34 |
| 2026-11-21T18:58 | USUALUSDT | surge | STOP | 2.5 | -3.25% | $-1.38 |
| 2026-11-21T17:11 | BEAMXUSDT | surge | TARGET | 0.2 | +2.75% | $+1.17 |
| 2026-11-21T13:53 | ORCAUSDT | surge | TARGET | 0.0 | +2.75% | $+1.17 |
| 2026-11-20T15:23 | STRKUSDT | bottom | STOP | 23.0 | -3.25% | $-1.36 |
| 2026-11-20T12:15 | AAVEUSDT | bottom | STOP | 20.2 | -3.25% | $-1.29 |
| 2026-11-20T11:23 | RWUSDUSDT | bottom | TIME | 24.0 | -0.23% | $-0.11 |
| 2026-11-20T05:27 | NIGHTUSDT | surge | STOP | 1.2 | -3.25% | $-1.41 |
| 2026-11-20T04:54 | SNXUSDT | surge | STOP | 3.8 | -3.25% | $-1.41 |
| 2026-11-20T04:38 | HUMAUSDT | surge | STOP | 0.8 | -3.25% | $-1.41 |
| 2026-11-20T03:10 | BARDUSDT | surge | TARGET | 0.0 | +2.75% | $+1.19 |
| 2026-11-20T02:53 | SAPIENUSDT | surge | TARGET | 0.2 | +2.75% | $+1.18 |
| 2026-11-20T02:03 | KATUSDT | surge | STOP | 7.2 | -3.25% | $-1.44 |
| 2026-11-20T01:12 | ERAUSDT | surge | STOP | 6.8 | -3.25% | $-1.42 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-21T16:17 | STXUSDT | surge | 0.2474 | 0.2527 | +2.14% |
| 2026-11-21T16:17 | RENDERUSDT | surge | 1.301 | 1.327 | +2.00% |
| 2026-11-21T16:17 | UNIUSDT | surge | 4.72 | 4.741 | +0.44% |
| 2026-11-21T16:17 | ETCUSDT | surge | 5.5 | 5.49 | -0.18% |
| 2026-11-21T16:35 | PYTHUSDT | surge | 0.04835 | 0.04896 | +1.26% |
| 2026-11-21T16:35 | ARUSDT | surge | 2.24 | 2.271 | +1.38% |
| 2026-11-21T16:53 | STRKUSDT | surge | 0.03068 | 0.03016 | -1.69% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
