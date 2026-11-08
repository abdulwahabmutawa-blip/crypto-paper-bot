# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-08T12:43:31+00:00 · runs 5507 · equity **$521.49** (-47.85%) · cash $0.00 · open 10/10 · round trips 1887

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-475.25 · worst day $-50.94 · trades/day 29.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1638 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 249 | 42% | -0.57% | 35% | 45% | 20% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-07T19:16 | METUSDT | surge | TARGET | 0.2 | +2.75% | $+1.37 |
| 2026-11-07T18:59 | METUSDT | surge | TARGET | 0.5 | +2.75% | $+1.37 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-07T16:25 | STXUSDT | surge | 0.3433 | 0.3344 | -2.59% |
| 2026-11-07T19:16 | ETHFIUSDT | surge | 0.5924 | 0.5971 | +0.79% |
| 2026-11-08T01:34 | MSTRBUSDT | bottom | 126.98 | 128.39 | +1.11% |
| 2026-11-08T03:23 | ARBUSDT | surge | 0.1708 | 0.169 | -1.05% |
| 2026-11-08T03:23 | STRKUSDT | bottom | 0.03974 | 0.03896 | -1.96% |
| 2026-11-08T04:25 | DASHUSDT | surge | 47.81 | 46.67 | -2.38% |
| 2026-11-08T05:00 | HBARUSDT | bottom | 0.06644 | 0.06682 | +0.57% |
| 2026-11-08T11:20 | RSRUSDT | surge | 0.001656 | 0.001656 | +0.00% |
| 2026-11-08T12:25 | BEAMXUSDT | surge | 0.004201 | 0.004147 | -1.29% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
