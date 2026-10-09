# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-09T20:20:13+00:00 · runs 2975 · equity **$765.89** (-23.41%) · cash $0.00 · open 10/10 · round trips 1117

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.23%/trade · realized $-231.11 · worst day $-50.94 · trades/day 31.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 978 | 50% | -0.19% | 48% | 45% | 7% |
| bottom | 139 | 44% | -0.49% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-09T14:17 | API3USDT | surge | TARGET | 4.0 | +2.75% | $+2.07 |
| 2026-10-09T14:00 | PROMUSDT | surge | STOP | 3.8 | -3.25% | $-2.45 |
| 2026-10-09T14:00 | APTUSDT | surge | STOP | 5.0 | -3.25% | $-2.42 |
| 2026-10-09T12:49 | GRAMUSDT | surge | TARGET | 2.2 | +2.75% | $+2.11 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T20:37 | FILUSDT | surge | 1.0745 | 1.0784 | +0.36% |
| 2026-10-08T20:37 | TRXUSDT | bottom | 0.333 | 0.3323 | -0.21% |
| 2026-10-09T14:00 | TSLABUSDT | surge | 385.25 | 382.73 | -0.65% |
| 2026-10-09T14:35 | CRCLBUSDT | surge | 86.8 | 84.68 | -2.44% |
| 2026-10-09T15:45 | MSTRBUSDT | surge | 157.49 | 154.59 | -1.84% |
| 2026-10-09T16:25 | CAKEUSDT | surge | 2.202 | 2.178 | -1.09% |
| 2026-10-09T16:58 | BABABUSDT | surge | 110.99 | 111.21 | +0.20% |
| 2026-10-09T19:45 | OPUSDT | surge | 0.1257 | 0.1271 | +1.11% |
| 2026-10-09T20:18 | ATOMUSDT | surge | 2.037 | 2.054 | +0.83% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
