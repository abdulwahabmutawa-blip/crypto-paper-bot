# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-20T11:43:16+00:00 · runs 6411 · equity **$469.09** (-53.09%) · cash $303.05 · open 3/10 · round trips 2121

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.36%/trade · realized $-529.18 · worst day $-50.94 · trades/day 27.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1828 | 47% | -0.34% | 45% | 48% | 7% |
| bottom | 293 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-20T11:23 | RWUSDUSDT | bottom | TIME | 24.0 | -0.23% | $-0.11 |
| 2026-11-20T05:27 | NIGHTUSDT | surge | STOP | 1.2 | -3.25% | $-1.41 |
| 2026-11-20T04:54 | SNXUSDT | surge | STOP | 3.8 | -3.25% | $-1.41 |
| 2026-11-20T04:38 | HUMAUSDT | surge | STOP | 0.8 | -3.25% | $-1.41 |
| 2026-11-20T03:10 | BARDUSDT | surge | TARGET | 0.0 | +2.75% | $+1.19 |
| 2026-11-20T02:53 | SAPIENUSDT | surge | TARGET | 0.2 | +2.75% | $+1.18 |
| 2026-11-20T02:03 | KATUSDT | surge | STOP | 7.2 | -3.25% | $-1.44 |
| 2026-11-20T01:12 | ERAUSDT | surge | STOP | 6.8 | -3.25% | $-1.42 |
| 2026-11-19T21:50 | BABABUSDT | surge | STOP | 4.2 | -3.25% | $-1.41 |
| 2026-11-19T21:50 | BNCBUSDT | surge | STOP | 16.0 | -3.25% | $-1.55 |
| 2026-11-19T19:15 | HYPEUSDT | surge | STOP | 0.5 | -3.25% | $-1.44 |
| 2026-11-19T19:15 | USTCUSDT | surge | STOP | 2.0 | -3.25% | $-1.41 |
| 2026-11-19T18:43 | SAPIENUSDT | surge | TARGET | 0.0 | +2.75% | $+1.20 |
| 2026-11-19T17:39 | PROMUSDT | surge | TIME | 24.0 | -0.63% | $-0.27 |
| 2026-11-19T17:23 | PYTHUSDT | surge | STOP | 9.2 | -3.25% | $-1.48 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-19T15:47 | AAVEUSDT | bottom | 104.48 | 102.39 | -2.00% |
| 2026-11-19T16:03 | STRKUSDT | bottom | 0.0318 | 0.03109 | -2.23% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
