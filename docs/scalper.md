# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-27T00:22:03+00:00 · runs 6830 · equity **$490.37** (-50.96%) · cash $0.00 · open 10/10 · round trips 2242

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-508.37 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1926 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 316 | 43% | -0.48% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-26T23:46 | SAGAUSDT | surge | STOP | 4.5 | -3.25% | $-1.47 |
| 2026-11-26T23:46 | SUPERUSDT | surge | TIME | 24.0 | -1.10% | $-0.49 |
| 2026-11-26T19:32 | FETUSDT | surge | TARGET | 1.0 | +2.75% | $+1.26 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-26T00:33 | EWYBUSDT | surge | 131.04 | 129.04 | -1.53% |
| 2026-11-26T15:19 | SKYUSDT | surge | 0.04609 | 0.04663 | +1.17% |
| 2026-11-26T15:19 | TRXUSDT | bottom | 0.3026 | 0.304 | +0.46% |
| 2026-11-26T17:51 | THETAUSDT | surge | 0.1357 | 0.1351 | -0.44% |
| 2026-11-26T18:25 | WIFUSDT | surge | 0.1387 | 0.136 | -1.95% |
| 2026-11-26T18:58 | SENTUSDT | surge | 0.02178 | 0.02156 | -1.01% |
| 2026-11-26T19:32 | DOTUSDT | surge | 0.676 | 0.675 | -0.15% |
| 2026-11-26T23:46 | TIAUSDT | bottom | 0.3353 | 0.3379 | +0.78% |
| 2026-11-26T23:46 | TRUMPUSDT | bottom | 0.863 | 0.863 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
