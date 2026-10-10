# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-10T03:32:24+00:00 · runs 3003 · equity **$765.16** (-23.48%) · cash $0.00 · open 10/10 · round trips 1121

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.22%/trade · realized $-227.32 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 981 | 50% | -0.18% | 48% | 45% | 7% |
| bottom | 140 | 44% | -0.49% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-10T03:30 | WLFIUSDT | surge | TARGET | 6.5 | +2.75% | $+2.10 |
| 2026-10-09T22:51 | OPUSDT | surge | TARGET | 2.8 | +2.75% | $+1.91 |
| 2026-10-09T20:51 | TRXUSDT | bottom | TIME | 24.0 | -0.46% | $-0.35 |
| 2026-10-09T20:51 | FILUSDT | surge | TIME | 24.0 | +0.18% | $+0.14 |
| 2026-10-09T20:18 | GRAMUSDT | surge | STOP | 7.2 | -3.25% | $-2.56 |
| 2026-10-09T19:45 | POLUSDT | surge | STOP | 2.0 | -3.25% | $-2.33 |
| 2026-10-09T17:31 | ALGOUSDT | bottom | STOP | 16.5 | -3.25% | $-2.41 |
| 2026-10-09T16:58 | ATUSDT | surge | TARGET | 0.5 | +2.75% | $+2.05 |
| 2026-10-09T16:25 | ATOMUSDT | surge | TARGET | 8.2 | +2.75% | $+2.12 |
| 2026-10-09T16:08 | ZKUSDT | surge | TARGET | 1.8 | +2.75% | $+2.00 |
| 2026-10-09T15:45 | BATUSDT | surge | TARGET | 0.2 | +2.75% | $+2.08 |
| 2026-10-09T15:28 | API3USDT | surge | STOP | 0.8 | -3.25% | $-2.53 |
| 2026-10-09T14:35 | CRCLBUSDT | surge | TARGET | 0.0 | +2.75% | $+2.09 |
| 2026-10-09T14:35 | API3USDT | surge | TARGET | 0.0 | +2.75% | $+2.09 |
| 2026-10-09T14:17 | SUSDT | surge | STOP | 3.8 | -3.25% | $-2.50 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-09T14:00 | TSLABUSDT | surge | 385.25 | 383.05 | -0.57% |
| 2026-10-09T14:35 | CRCLBUSDT | surge | 86.8 | 85 | -2.07% |
| 2026-10-09T15:45 | MSTRBUSDT | surge | 157.49 | 154.27 | -2.04% |
| 2026-10-09T16:25 | CAKEUSDT | surge | 2.202 | 2.214 | +0.54% |
| 2026-10-09T16:58 | BABABUSDT | surge | 110.99 | 111.11 | +0.11% |
| 2026-10-09T20:18 | ATOMUSDT | surge | 2.037 | 1.983 | -2.65% |
| 2026-10-09T20:51 | CYBERUSDT | surge | 0.357 | 0.351 | -1.68% |
| 2026-10-09T22:51 | RAYUSDT | bottom | 2.3008 | 2.284 | -0.73% |
| 2026-10-10T03:30 | C98USDT | surge | 0.01858 | 0.01844 | -0.75% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
