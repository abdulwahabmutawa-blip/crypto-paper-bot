# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T20:20:09+00:00 · runs 1955 · equity **$935.46** (-6.45%) · cash $0.00 · open 10/10 · round trips 708

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-62.38 · worst day $-50.94 · trades/day 30.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 604 | 53% | -0.03% | 50% | 43% | 7% |
| bottom | 104 | 45% | -0.39% | 41% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-27T19:45 | ARUSDT | surge | STOP | 1.5 | -3.25% | $-3.36 |
| 2026-09-27T18:55 | ARBUSDT | bottom | TARGET | 1.8 | +2.75% | $+2.62 |
| 2026-09-27T18:33 | XVGUSDT | surge | STOP | 2.0 | -3.25% | $-3.26 |
| 2026-09-27T18:00 | NOMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.76 |
| 2026-09-27T17:44 | NOMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.69 |
| 2026-09-27T17:27 | NOMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.62 |
| 2026-09-27T16:55 | AMPUSDT | bottom | TARGET | 0.5 | +2.75% | $+2.68 |
| 2026-09-27T16:55 | OPNUSDT | surge | STOP | 2.8 | -3.25% | $-3.03 |
| 2026-09-27T16:22 | WUSDT | surge | TARGET | 0.5 | +2.75% | $+2.68 |
| 2026-09-27T16:05 | PUMPUSDT | surge | TARGET | 1.2 | +2.75% | $+2.61 |
| 2026-09-27T15:49 | REUSDT | surge | STOP | 10.8 | -3.25% | $-2.93 |
| 2026-09-27T15:33 | AMPUSDT | bottom | TARGET | 0.0 | +2.75% | $+2.61 |
| 2026-09-27T15:16 | ZECUSDT | surge | STOP | 15.0 | -3.25% | $-3.19 |
| 2026-09-27T14:43 | JASMYUSDT | surge | STOP | 0.0 | -3.25% | $-3.10 |
| 2026-09-27T14:43 | BCHUSDT | surge | STOP | 6.8 | -3.25% | $-3.27 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.334 | -0.30% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12538 | +0.58% |
| 2026-09-27T10:01 | SOLUSDT | surge | 124.47 | 123.35 | -0.90% |
| 2026-09-27T12:58 | MMTUSDT | surge | 0.1833 | 0.1823 | -0.55% |
| 2026-09-27T14:43 | CAKEUSDT | surge | 2.844 | 2.798 | -1.62% |
| 2026-09-27T15:49 | HYPEUSDT | bottom | 91.19 | 91.94 | +0.82% |
| 2026-09-27T18:33 | PENDLEUSDT | surge | 2.679 | 2.68 | +0.04% |
| 2026-09-27T18:55 | PUMPUSDT | surge | 0.004974 | 0.004959 | -0.30% |
| 2026-09-27T19:45 | JASMYUSDT | surge | 0.00527 | 0.00527 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
