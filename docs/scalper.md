# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-26T19:17:14+00:00 · runs 6822 · equity **$492.45** (-50.76%) · cash $0.00 · open 10/10 · round trips 2239

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-507.66 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1923 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 316 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-26T18:58 | SENTUSDT | surge | TARGET | 3.0 | +2.75% | $+1.25 |
| 2026-11-26T18:42 | SAGAUSDT | surge | TARGET | 3.2 | +2.75% | $+1.21 |
| 2026-11-26T18:25 | SEIUSDT | surge | TARGET | 0.0 | +2.75% | $+1.21 |
| 2026-11-26T18:25 | WIFUSDT | surge | TARGET | 2.0 | +2.75% | $+1.24 |
| 2026-11-26T18:08 | STXUSDT | surge | TIME | 24.0 | -0.86% | $-0.38 |
| 2026-11-26T17:51 | MANTRAUSDT | bottom | TARGET | 2.2 | +2.75% | $+1.20 |
| 2026-11-26T16:10 | ZECUSDT | bottom | TARGET | 0.5 | +2.75% | $+1.20 |
| 2026-11-26T15:53 | SEIUSDT | surge | TARGET | 0.5 | +2.75% | $+1.21 |
| 2026-11-26T15:19 | PUMPUSDT | surge | STOP | 13.0 | -3.25% | $-1.48 |
| 2026-11-26T15:19 | NEARUSDT | surge | STOP | 14.8 | -3.25% | $-1.48 |
| 2026-11-26T15:19 | RAYUSDT | surge | STOP | 14.8 | -3.25% | $-1.48 |
| 2026-11-26T15:19 | STRKUSDT | surge | STOP | 20.0 | -3.25% | $-1.44 |
| 2026-11-26T15:01 | SKHYBUSDT | surge | STOP | 10.0 | -3.25% | $-1.48 |
| 2026-11-26T15:01 | SENTUSDT | surge | TARGET | 22.2 | +2.75% | $+1.19 |
| 2026-11-26T02:00 | ATUSDT | surge | STOP | 0.5 | -3.25% | $-1.53 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-25T22:49 | SUPERUSDT | surge | 0.1173 | 0.1171 | -0.17% |
| 2026-11-26T00:33 | EWYBUSDT | surge | 131.04 | 129.47 | -1.20% |
| 2026-11-26T15:19 | SKYUSDT | surge | 0.04609 | 0.04532 | -1.67% |
| 2026-11-26T15:19 | TRXUSDT | bottom | 0.3026 | 0.3036 | +0.33% |
| 2026-11-26T17:51 | THETAUSDT | surge | 0.1357 | 0.1352 | -0.37% |
| 2026-11-26T18:25 | WIFUSDT | surge | 0.1387 | 0.1399 | +0.87% |
| 2026-11-26T18:25 | FETUSDT | surge | 0.1177 | 0.1207 | +2.55% |
| 2026-11-26T18:42 | SAGAUSDT | surge | 0.01501 | 0.01482 | -1.27% |
| 2026-11-26T18:58 | SENTUSDT | surge | 0.02178 | 0.02201 | +1.06% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
