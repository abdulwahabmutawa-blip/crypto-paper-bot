# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-07T13:48:49+00:00 · runs 5418 · equity **$526.25** (-47.37%) · cash $0.00 · open 10/10 · round trips 1867

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-470.91 · worst day $-50.94 · trades/day 29.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1621 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 246 | 42% | -0.55% | 36% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-07T13:47 | METUSDT | surge | TARGET | 0.2 | +2.75% | $+1.34 |
| 2026-11-07T13:47 | MITOUSDT | surge | STOP | 0.2 | -3.25% | $-1.58 |
| 2026-11-07T13:15 | METUSDT | surge | TARGET | 4.5 | +2.75% | $+1.35 |
| 2026-11-07T13:15 | DASHUSDT | surge | STOP | 21.2 | -3.25% | $-1.58 |
| 2026-11-07T13:00 | MEGAUSDT | surge | STOP | 2.2 | -3.25% | $-1.58 |
| 2026-11-07T10:44 | RAYUSDT | surge | STOP | 19.0 | -3.25% | $-1.64 |
| 2026-11-07T08:44 | QNTUSDT | surge | STOP | 1.0 | -3.25% | $-1.61 |
| 2026-11-07T08:10 | ACTUSDT | surge | TARGET | 2.2 | +2.75% | $+1.35 |
| 2026-11-07T07:19 | QNTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.35 |
| 2026-11-07T04:59 | HUMAUSDT | bottom | TARGET | 3.5 | +2.75% | $+1.29 |
| 2026-11-07T04:43 | ACTUSDT | surge | TARGET | 5.0 | +2.75% | $+1.34 |
| 2026-11-07T03:54 | PYTHUSDT | surge | STOP | 12.2 | -3.25% | $-1.64 |
| 2026-11-07T03:54 | MUBARAKUSDT | surge | STOP | 12.2 | -3.25% | $-1.64 |
| 2026-11-07T03:06 | FILUSDT | surge | STOP | 11.5 | -3.25% | $-1.64 |
| 2026-11-07T01:29 | XTZUSDT | surge | STOP | 4.0 | -3.25% | $-1.58 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-06T18:58 | BABABUSDT | surge | 109.38 | 109.41 | +0.03% |
| 2026-11-06T21:23 | XRPUSDT | bottom | 1.1787 | 1.1658 | -1.09% |
| 2026-11-07T03:06 | FETUSDT | bottom | 0.1461 | 0.1458 | -0.21% |
| 2026-11-07T04:59 | XLMUSDT | bottom | 0.1519 | 0.1519 | +0.00% |
| 2026-11-07T08:27 | NIGHTUSDT | surge | 0.04012 | 0.03954 | -1.45% |
| 2026-11-07T09:02 | STRKUSDT | surge | 0.04196 | 0.04121 | -1.79% |
| 2026-11-07T13:00 | 牛来USDT | surge | 0.05725 | 0.05672 | -0.93% |
| 2026-11-07T13:47 | METUSDT | surge | 0.3074 | 0.3069 | -0.16% |
| 2026-11-07T13:47 | ERAUSDT | surge | 0.0747 | 0.0746 | -0.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
