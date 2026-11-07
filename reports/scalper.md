# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-07T06:46:35+00:00 · runs 5392 · equity **$531.47** (-46.85%) · cash $48.95 · open 9/10 · round trips 1858

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-468.29 · worst day $-50.94 · trades/day 29.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1612 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 246 | 42% | -0.55% | 36% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-07T04:59 | HUMAUSDT | bottom | TARGET | 3.5 | +2.75% | $+1.29 |
| 2026-11-07T04:43 | ACTUSDT | surge | TARGET | 5.0 | +2.75% | $+1.34 |
| 2026-11-07T03:54 | PYTHUSDT | surge | STOP | 12.2 | -3.25% | $-1.64 |
| 2026-11-07T03:54 | MUBARAKUSDT | surge | STOP | 12.2 | -3.25% | $-1.64 |
| 2026-11-07T03:06 | FILUSDT | surge | STOP | 11.5 | -3.25% | $-1.64 |
| 2026-11-07T01:29 | XTZUSDT | surge | STOP | 4.0 | -3.25% | $-1.58 |
| 2026-11-06T23:16 | FORMUSDT | surge | STOP | 7.8 | -3.25% | $-1.64 |
| 2026-11-06T21:23 | SPCXBUSDT | surge | TARGET | 5.8 | +2.75% | $+1.38 |
| 2026-11-06T21:07 | MRNABUSDT | surge | STOP | 2.0 | -3.25% | $-1.63 |
| 2026-11-06T18:58 | INTWBUSDT | surge | TARGET | 3.2 | +2.75% | $+1.38 |
| 2026-11-06T18:58 | WUSDT | surge | STOP | 3.2 | -3.25% | $-1.64 |
| 2026-11-06T15:53 | NBISBUSDT | surge | STOP | 0.2 | -3.25% | $-1.64 |
| 2026-11-05T17:31 | SUIUSDT | bottom | STOP | 0.2 | -3.25% | $-1.63 |
| 2026-11-05T17:31 | HYPEUSDT | bottom | STOP | 2.2 | -3.25% | $-1.66 |
| 2026-11-05T17:31 | NEARUSDT | bottom | STOP | 2.2 | -3.25% | $-1.66 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-06T15:20 | RAYUSDT | surge | 1.8138 | 1.8011 | -0.70% |
| 2026-11-06T15:53 | DASHUSDT | surge | 47.87 | 47.05 | -1.71% |
| 2026-11-06T18:58 | BABABUSDT | surge | 109.38 | 109.43 | +0.05% |
| 2026-11-06T21:23 | XRPUSDT | bottom | 1.1787 | 1.1685 | -0.87% |
| 2026-11-07T03:06 | FETUSDT | bottom | 0.1461 | 0.1473 | +0.82% |
| 2026-11-07T04:59 | XLMUSDT | bottom | 0.1519 | 0.1536 | +1.12% |
| 2026-11-07T05:31 | ACTUSDT | surge | 0.01101 | 0.01105 | +0.36% |
| 2026-11-07T06:44 | QNTUSDT | surge | 198.6 | 199.63 | +0.52% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
