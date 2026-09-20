# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T15:38:59+00:00 · runs 1322 · equity **$909.16** (-9.08%) · cash $0.00 · open 10/10 · round trips 478

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.18%/trade · realized $-88.95 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 394 | 52% | -0.11% | 48% | 44% | 8% |
| bottom | 84 | 42% | -0.52% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T14:27 | MITOUSDT | surge | STOP | 0.2 | -3.25% | $-2.95 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 108.24 | -1.89% |
| 2026-09-20T02:44 | XRPUSDT | bottom | 1.3972 | 1.3858 | -0.82% |
| 2026-09-20T08:52 | DOGEUSDT | bottom | 0.08475 | 0.08552 | +0.91% |
| 2026-09-20T11:25 | CAKEUSDT | surge | 2.468 | 2.468 | +0.00% |
| 2026-09-20T11:25 | PROVEUSDT | surge | 0.2249 | 0.2223 | -1.16% |
| 2026-09-20T13:04 | NEARUSDT | surge | 3.721 | 3.713 | -0.21% |
| 2026-09-20T14:10 | BNCBUSDT | surge | 6.68 | 6.52 | -2.40% |
| 2026-09-20T14:10 | TRXUSDT | surge | 0.3466 | 0.3446 | -0.58% |
| 2026-09-20T15:16 | SAGAUSDT | surge | 0.03089 | 0.03222 | +4.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
