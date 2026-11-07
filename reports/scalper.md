# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-07T21:50:01+00:00 · runs 5448 · equity **$525.96** (-47.40%) · cash $0.00 · open 10/10 · round trips 1875

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-470.17 · worst day $-50.94 · trades/day 29.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1628 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 247 | 42% | -0.56% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-07T13:15 | DASHUSDT | surge | STOP | 21.2 | -3.25% | $-1.58 |
| 2026-11-07T13:00 | MEGAUSDT | surge | STOP | 2.2 | -3.25% | $-1.58 |
| 2026-11-07T10:44 | RAYUSDT | surge | STOP | 19.0 | -3.25% | $-1.64 |
| 2026-11-07T08:44 | QNTUSDT | surge | STOP | 1.0 | -3.25% | $-1.61 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-07T03:06 | FETUSDT | bottom | 0.1461 | 0.1431 | -2.05% |
| 2026-11-07T04:59 | XLMUSDT | bottom | 0.1519 | 0.1503 | -1.05% |
| 2026-11-07T08:27 | NIGHTUSDT | surge | 0.04012 | 0.03982 | -0.75% |
| 2026-11-07T15:06 | RSRUSDT | surge | 0.00156 | 0.001546 | -0.90% |
| 2026-11-07T16:25 | STXUSDT | surge | 0.3433 | 0.339 | -1.25% |
| 2026-11-07T18:59 | OPENUSDT | surge | 0.0906 | 0.0893 | -1.43% |
| 2026-11-07T18:59 | MEGAUSDT | surge | 0.05089 | 0.04979 | -2.16% |
| 2026-11-07T19:16 | ETHFIUSDT | surge | 0.5924 | 0.5932 | +0.14% |
| 2026-11-07T21:31 | METUSDT | surge | 0.3242 | 0.3291 | +1.51% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
