# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T13:55:33+00:00 · runs 1315 · equity **$911.29** (-8.87%) · cash $181.82 · open 8/10 · round trips 477

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.18%/trade · realized $-86.00 · worst day $-50.94 · trades/day 29.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 393 | 52% | -0.10% | 48% | 44% | 8% |
| bottom | 84 | 42% | -0.52% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T13:37 | STXUSDT | surge | STOP | 6.2 | -3.25% | $-3.11 |
| 2026-09-20T13:21 | SUSDT | surge | STOP | 0.5 | -3.25% | $-3.00 |
| 2026-09-20T13:04 | IOSTUSDT | surge | STOP | 0.2 | -3.25% | $-3.00 |
| 2026-09-20T12:31 | SAGAUSDT | surge | STOP | 0.0 | -3.25% | $-3.03 |
| 2026-09-20T12:15 | ACEUSDT | surge | TARGET | 1.0 | +2.75% | $+2.54 |
| 2026-09-20T10:20 | SUSDT | surge | STOP | 0.5 | -3.25% | $-3.09 |
| 2026-09-20T10:20 | MEGAUSDT | surge | STOP | 3.2 | -3.25% | $-3.03 |
| 2026-09-20T10:20 | JTOUSDT | surge | STOP | 3.2 | -3.25% | $-3.03 |
| 2026-09-20T09:42 | SUSDT | surge | TARGET | 0.0 | +2.75% | $+2.59 |
| 2026-09-20T09:09 | ZKUSDT | surge | STOP | 0.8 | -3.25% | $-3.25 |
| 2026-09-20T08:52 | USUALUSDT | surge | STOP | 0.2 | -3.25% | $-3.25 |
| 2026-09-20T08:52 | LDOUSDT | surge | STOP | 5.0 | -3.25% | $-2.99 |
| 2026-09-20T08:52 | DASHUSDT | bottom | STOP | 10.8 | -3.25% | $-3.10 |
| 2026-09-20T08:03 | ZKUSDT | surge | TARGET | 2.8 | +2.75% | $+2.80 |
| 2026-09-20T07:30 | CAKEUSDT | surge | STOP | 0.8 | -3.25% | $-3.22 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 108.18 | -1.95% |
| 2026-09-20T02:44 | XRPUSDT | bottom | 1.3972 | 1.3778 | -1.39% |
| 2026-09-20T08:52 | DOGEUSDT | bottom | 0.08475 | 0.085 | +0.29% |
| 2026-09-20T11:25 | CAKEUSDT | surge | 2.468 | 2.497 | +1.18% |
| 2026-09-20T11:25 | PROVEUSDT | surge | 0.2249 | 0.2232 | -0.76% |
| 2026-09-20T13:04 | NEARUSDT | surge | 3.721 | 3.677 | -1.18% |
| 2026-09-20T13:54 | MITOUSDT | surge | 0.01646 | 0.01661 | +0.91% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
