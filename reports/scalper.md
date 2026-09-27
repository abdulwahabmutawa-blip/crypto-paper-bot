# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T15:01:38+00:00 · runs 1935 · equity **$923.12** (-7.69%) · cash $0.00 · open 10/10 · round trips 695

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-67.89 · worst day $-50.94 · trades/day 30.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 594 | 53% | -0.02% | 50% | 43% | 7% |
| bottom | 101 | 44% | -0.49% | 40% | 46% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-27T14:43 | JASMYUSDT | surge | STOP | 0.0 | -3.25% | $-3.10 |
| 2026-09-27T14:43 | BCHUSDT | surge | STOP | 6.8 | -3.25% | $-3.27 |
| 2026-09-27T14:27 | JASMYUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-27T13:54 | XPLUSDT | bottom | STOP | 12.8 | -3.25% | $-3.13 |
| 2026-09-27T13:21 | ZROUSDT | surge | STOP | 4.8 | -3.25% | $-3.12 |
| 2026-09-27T12:58 | JASMYUSDT | surge | TARGET | 1.5 | +2.75% | $+2.47 |
| 2026-09-27T11:12 | DASHUSDT | surge | STOP | 18.5 | -3.25% | $-3.02 |
| 2026-09-27T10:01 | MOVRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.55 |
| 2026-09-27T09:26 | STXUSDT | surge | STOP | 3.5 | -3.25% | $-3.12 |
| 2026-09-27T08:15 | PYTHUSDT | surge | TARGET | 2.2 | +2.75% | $+2.57 |
| 2026-09-27T07:57 | SUPERUSDT | surge | TARGET | 9.5 | +2.75% | $+2.70 |
| 2026-09-27T05:52 | SEIUSDT | bottom | TARGET | 8.8 | +2.75% | $+2.50 |
| 2026-09-27T05:36 | CFGUSDT | surge | STOP | 1.0 | -3.25% | $-3.09 |
| 2026-09-27T05:36 | PYTHUSDT | surge | TARGET | 2.5 | +2.75% | $+2.67 |
| 2026-09-27T04:45 | KITEUSDT | surge | STOP | 1.0 | -3.25% | $-3.03 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3337 | -0.39% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1598.18 | -3.32% |
| 2026-09-27T04:45 | REUSDT | surge | 0.5005 | 0.4896 | -2.18% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12535 | +0.55% |
| 2026-09-27T10:01 | SOLUSDT | surge | 124.47 | 121.7 | -2.23% |
| 2026-09-27T12:58 | MMTUSDT | surge | 0.1833 | 0.1822 | -0.60% |
| 2026-09-27T13:54 | OPNUSDT | surge | 0.0574 | 0.0567 | -1.22% |
| 2026-09-27T14:43 | CAKEUSDT | surge | 2.844 | 2.799 | -1.58% |
| 2026-09-27T14:43 | PUMPUSDT | surge | 0.004707 | 0.004775 | +1.44% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
