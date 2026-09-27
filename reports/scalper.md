# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T14:28:44+00:00 · runs 1933 · equity **$928.44** (-7.16%) · cash $0.00 · open 10/10 · round trips 693

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-61.52 · worst day $-50.94 · trades/day 30.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 592 | 54% | -0.01% | 50% | 42% | 7% |
| bottom | 101 | 44% | -0.49% | 40% | 46% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-27T04:28 | SKYUSDT | surge | TIME | 24.0 | -0.83% | $-0.80 |
| 2026-09-27T03:38 | WUSDT | surge | TARGET | 0.2 | +2.75% | $+2.49 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3335 | -0.45% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1627.9 | -1.53% |
| 2026-09-27T04:45 | REUSDT | surge | 0.5005 | 0.4929 | -1.52% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12537 | +0.57% |
| 2026-09-27T07:57 | BCHUSDT | surge | 343.4 | 334.2 | -2.68% |
| 2026-09-27T10:01 | SOLUSDT | surge | 124.47 | 122.01 | -1.98% |
| 2026-09-27T12:58 | MMTUSDT | surge | 0.1833 | 0.1827 | -0.33% |
| 2026-09-27T13:54 | OPNUSDT | surge | 0.0574 | 0.057 | -0.70% |
| 2026-09-27T14:27 | JASMYUSDT | surge | 0.00536 | 0.00526 | -1.87% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
