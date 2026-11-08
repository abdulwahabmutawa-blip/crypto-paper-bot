# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-08T03:55:49+00:00 · runs 5472 · equity **$523.87** (-47.61%) · cash $0.00 · open 10/10 · round trips 1879

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-472.95 · worst day $-50.94 · trades/day 28.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1631 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 248 | 42% | -0.57% | 35% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-08T03:23 | FETUSDT | bottom | TIME | 24.0 | -1.89% | $-0.92 |
| 2026-11-08T02:52 | OPENUSDT | surge | STOP | 7.8 | -3.25% | $-1.62 |
| 2026-11-08T01:34 | MEGAUSDT | surge | STOP | 6.5 | -3.25% | $-1.62 |
| 2026-11-07T22:22 | METUSDT | surge | TARGET | 0.5 | +2.75% | $+1.39 |
| 2026-11-07T21:31 | XRPUSDT | bottom | TIME | 24.0 | -2.42% | $-1.25 |
| 2026-11-07T19:16 | METUSDT | surge | TARGET | 0.2 | +2.75% | $+1.37 |
| 2026-11-07T18:59 | METUSDT | surge | TARGET | 0.5 | +2.75% | $+1.37 |
| 2026-11-07T18:59 | 牛来USDT | surge | TARGET | 5.8 | +2.75% | $+1.30 |
| 2026-11-07T18:59 | BABABUSDT | surge | TIME | 24.0 | -0.41% | $-0.21 |
| 2026-11-07T18:25 | METUSDT | surge | TARGET | 4.2 | +2.75% | $+1.34 |
| 2026-11-07T15:54 | ERAUSDT | surge | STOP | 1.8 | -3.25% | $-1.58 |
| 2026-11-07T15:06 | STRKUSDT | surge | STOP | 5.8 | -3.25% | $-1.59 |
| 2026-11-07T13:47 | METUSDT | surge | TARGET | 0.2 | +2.75% | $+1.34 |
| 2026-11-07T13:47 | MITOUSDT | surge | STOP | 0.2 | -3.25% | $-1.58 |
| 2026-11-07T13:15 | METUSDT | surge | TARGET | 4.5 | +2.75% | $+1.35 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-07T04:59 | XLMUSDT | bottom | 0.1519 | 0.1505 | -0.92% |
| 2026-11-07T08:27 | NIGHTUSDT | surge | 0.04012 | 0.04014 | +0.05% |
| 2026-11-07T15:06 | RSRUSDT | surge | 0.00156 | 0.001566 | +0.38% |
| 2026-11-07T16:25 | STXUSDT | surge | 0.3433 | 0.3372 | -1.78% |
| 2026-11-07T19:16 | ETHFIUSDT | surge | 0.5924 | 0.5901 | -0.39% |
| 2026-11-07T22:22 | AEROUSDT | surge | 0.627 | 0.6093 | -2.82% |
| 2026-11-08T01:34 | MSTRBUSDT | bottom | 126.98 | 127.21 | +0.18% |
| 2026-11-08T03:23 | ARBUSDT | surge | 0.1708 | 0.1696 | -0.70% |
| 2026-11-08T03:23 | STRKUSDT | bottom | 0.03974 | 0.03958 | -0.40% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
