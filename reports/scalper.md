# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T11:50:00+00:00 · runs 1923 · equity **$935.38** (-6.46%) · cash $0.00 · open 10/10 · round trips 689

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-60.29 · worst day $-50.94 · trades/day 30.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 589 | 53% | -0.01% | 50% | 42% | 7% |
| bottom | 100 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-27T03:05 | GRAMUSDT | surge | STOP | 2.2 | -3.25% | $-3.05 |
| 2026-09-27T02:48 | KITEUSDT | surge | TARGET | 3.5 | +2.75% | $+2.60 |
| 2026-09-27T00:59 | ESPUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-27T00:41 | ESPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.58 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3343 | -0.21% |
| 2026-09-27T00:06 | ZECUSDT | surge | 1653.12 | 1658.45 | +0.32% |
| 2026-09-27T00:59 | XPLUSDT | bottom | 0.11061 | 0.11057 | -0.04% |
| 2026-09-27T04:45 | REUSDT | surge | 0.5005 | 0.4977 | -0.56% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.1254 | +0.59% |
| 2026-09-27T07:57 | BCHUSDT | surge | 343.4 | 338.1 | -1.54% |
| 2026-09-27T08:15 | ZROUSDT | surge | 1.659 | 1.633 | -1.57% |
| 2026-09-27T10:01 | SOLUSDT | surge | 124.47 | 123.78 | -0.55% |
| 2026-09-27T11:12 | JASMYUSDT | surge | 0.00505 | 0.005 | -0.99% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
