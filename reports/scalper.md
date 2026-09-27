# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T18:35:06+00:00 · runs 1948 · equity **$938.18** (-6.18%) · cash $0.00 · open 10/10 · round trips 706

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-61.64 · worst day $-50.94 · trades/day 30.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 603 | 53% | -0.02% | 50% | 43% | 7% |
| bottom | 103 | 45% | -0.42% | 41% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-27T14:27 | JASMYUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-27T13:54 | XPLUSDT | bottom | STOP | 12.8 | -3.25% | $-3.13 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3342 | -0.24% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12554 | +0.71% |
| 2026-09-27T10:01 | SOLUSDT | surge | 124.47 | 122.83 | -1.32% |
| 2026-09-27T12:58 | MMTUSDT | surge | 0.1833 | 0.1837 | +0.22% |
| 2026-09-27T14:43 | CAKEUSDT | surge | 2.844 | 2.801 | -1.51% |
| 2026-09-27T15:49 | HYPEUSDT | bottom | 91.19 | 91.97 | +0.86% |
| 2026-09-27T16:55 | ARBUSDT | bottom | 0.2201 | 0.2272 | +3.23% |
| 2026-09-27T18:00 | ARUSDT | surge | 5.102 | 5.028 | -1.45% |
| 2026-09-27T18:33 | PENDLEUSDT | surge | 2.679 | 2.666 | -0.49% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
