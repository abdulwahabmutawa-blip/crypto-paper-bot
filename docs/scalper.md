# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-24T14:39:31+00:00 · runs 6699 · equity **$481.99** (-51.80%) · cash $175.66 · open 6/10 · round trips 2191

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-517.18 · worst day $-50.94 · trades/day 27.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1886 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 305 | 43% | -0.49% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-24T14:37 | TRXUSDT | surge | TIME | 24.0 | -0.96% | $-0.44 |
| 2026-11-24T13:26 | INJUSDT | bottom | STOP | 9.5 | -3.25% | $-1.39 |
| 2026-11-24T12:33 | GOOGLBUSDT | surge | TIME | 24.0 | -0.33% | $-0.15 |
| 2026-11-24T10:11 | BABYUSDT | surge | TARGET | 3.5 | +2.75% | $+1.25 |
| 2026-11-24T10:11 | ZROUSDT | bottom | STOP | 6.0 | -3.25% | $-1.39 |
| 2026-11-24T10:11 | BEBUSDT | surge | STOP | 5.2 | -3.25% | $-1.44 |
| 2026-11-24T04:44 | BABYUSDT | surge | TARGET | 2.5 | +2.75% | $+1.22 |
| 2026-11-24T03:23 | PUMPUSDT | bottom | STOP | 3.0 | -3.25% | $-1.44 |
| 2026-11-24T02:51 | ZECUSDT | bottom | STOP | 2.5 | -3.25% | $-1.44 |
| 2026-11-24T00:09 | ALGOUSDT | surge | STOP | 4.2 | -3.25% | $-1.51 |
| 2026-11-24T00:09 | MORPHOUSDT | surge | STOP | 6.0 | -3.25% | $-1.47 |
| 2026-11-24T00:09 | ADAUSDT | surge | STOP | 5.0 | -3.25% | $-1.48 |
| 2026-11-24T00:09 | PENDLEUSDT | surge | STOP | 5.0 | -3.25% | $-1.48 |
| 2026-11-24T00:09 | NILUSDT | surge | STOP | 5.2 | -3.25% | $-1.48 |
| 2026-11-23T17:56 | SPCXBUSDT | surge | STOP | 3.0 | -3.25% | $-1.52 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-23T17:56 | METABUSDT | surge | 594.66 | 592.84 | -0.31% |
| 2026-11-23T17:56 | SPYBUSDT | surge | 722.28 | 715.58 | -0.93% |
| 2026-11-24T00:09 | ETHUSDT | bottom | 1710.65 | 1688.19 | -1.31% |
| 2026-11-24T11:58 | HBARUSDT | bottom | 0.05113 | 0.05101 | -0.23% |
| 2026-11-24T13:26 | AAVEUSDT | bottom | 93.51 | 94.39 | +0.94% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
