# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-07T12:13:29+00:00 · runs 5412 · equity **$527.82** (-47.22%) · cash $0.00 · open 10/10 · round trips 1862

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-468.85 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1616 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 246 | 42% | -0.55% | 36% | 46% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-06T23:16 | FORMUSDT | surge | STOP | 7.8 | -3.25% | $-1.64 |
| 2026-11-06T21:23 | SPCXBUSDT | surge | TARGET | 5.8 | +2.75% | $+1.38 |
| 2026-11-06T21:07 | MRNABUSDT | surge | STOP | 2.0 | -3.25% | $-1.63 |
| 2026-11-06T18:58 | INTWBUSDT | surge | TARGET | 3.2 | +2.75% | $+1.38 |
| 2026-11-06T18:58 | WUSDT | surge | STOP | 3.2 | -3.25% | $-1.64 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-06T15:53 | DASHUSDT | surge | 47.87 | 46.83 | -2.17% |
| 2026-11-06T18:58 | BABABUSDT | surge | 109.38 | 109.47 | +0.08% |
| 2026-11-06T21:23 | XRPUSDT | bottom | 1.1787 | 1.1705 | -0.70% |
| 2026-11-07T03:06 | FETUSDT | bottom | 0.1461 | 0.1451 | -0.68% |
| 2026-11-07T04:59 | XLMUSDT | bottom | 0.1519 | 0.1527 | +0.53% |
| 2026-11-07T08:27 | NIGHTUSDT | surge | 0.04012 | 0.03963 | -1.22% |
| 2026-11-07T08:44 | METUSDT | surge | 0.2937 | 0.2992 | +1.87% |
| 2026-11-07T09:02 | STRKUSDT | surge | 0.04196 | 0.04098 | -2.34% |
| 2026-11-07T10:44 | MEGAUSDT | surge | 0.05056 | 0.04948 | -2.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
