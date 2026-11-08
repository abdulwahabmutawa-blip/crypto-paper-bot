# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-08T15:11:29+00:00 · runs 5516 · equity **$522.07** (-47.79%) · cash $0.00 · open 10/10 · round trips 1889

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-475.41 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1640 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 249 | 42% | -0.57% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-08T14:53 | RSRUSDT | surge | TARGET | 3.2 | +2.75% | $+1.36 |
| 2026-11-08T13:15 | STXUSDT | surge | STOP | 20.5 | -3.25% | $-1.53 |
| 2026-11-08T12:25 | BMTUSDT | surge | STOP | 0.8 | -3.25% | $-1.61 |
| 2026-11-08T11:20 | RSRUSDT | surge | TARGET | 3.8 | +2.75% | $+1.34 |
| 2026-11-08T10:14 | BMTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.32 |
| 2026-11-08T09:40 | BEAMXUSDT | surge | STOP | 0.8 | -3.25% | $-1.61 |
| 2026-11-08T08:38 | NIGHTUSDT | surge | TIME | 24.0 | -1.05% | $-0.52 |
| 2026-11-08T07:05 | RSRUSDT | surge | TARGET | 15.8 | +2.75% | $+1.30 |
| 2026-11-08T05:00 | XLMUSDT | bottom | TIME | 24.0 | -1.70% | $-0.83 |
| 2026-11-08T04:25 | AEROUSDT | surge | STOP | 5.8 | -3.25% | $-1.69 |
| 2026-11-08T03:23 | FETUSDT | bottom | TIME | 24.0 | -1.89% | $-0.92 |
| 2026-11-08T02:52 | OPENUSDT | surge | STOP | 7.8 | -3.25% | $-1.62 |
| 2026-11-08T01:34 | MEGAUSDT | surge | STOP | 6.5 | -3.25% | $-1.62 |
| 2026-11-07T22:22 | METUSDT | surge | TARGET | 0.5 | +2.75% | $+1.39 |
| 2026-11-07T21:31 | XRPUSDT | bottom | TIME | 24.0 | -2.42% | $-1.25 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-07T19:16 | ETHFIUSDT | surge | 0.5924 | 0.5939 | +0.25% |
| 2026-11-08T01:34 | MSTRBUSDT | bottom | 126.98 | 128.36 | +1.09% |
| 2026-11-08T03:23 | ARBUSDT | surge | 0.1708 | 0.17 | -0.47% |
| 2026-11-08T03:23 | STRKUSDT | bottom | 0.03974 | 0.03877 | -2.44% |
| 2026-11-08T04:25 | DASHUSDT | surge | 47.81 | 46.86 | -1.99% |
| 2026-11-08T05:00 | HBARUSDT | bottom | 0.06644 | 0.06648 | +0.06% |
| 2026-11-08T12:25 | BEAMXUSDT | surge | 0.004201 | 0.004117 | -2.00% |
| 2026-11-08T13:15 | PEPEUSDT | surge | 5.02e-06 | 5.09e-06 | +1.39% |
| 2026-11-08T14:53 | RSRUSDT | surge | 0.001685 | 0.001669 | -0.95% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
