# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-24T05:55:10+00:00 · runs 1639 · equity **$932.99** (-6.70%) · cash $563.13 · open 4/10 · round trips 581

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.11%/trade · realized $-67.85 · worst day $-50.94 · trades/day 30.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 487 | 53% | -0.03% | 49% | 43% | 8% |
| bottom | 94 | 43% | -0.51% | 39% | 46% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-23T21:33 | RAYUSDT | surge | STOP | 1.5 | -3.25% | $-3.07 |
| 2026-09-23T16:19 | SKYUSDT | surge | STOP | 3.0 | -3.25% | $-3.21 |
| 2026-09-23T16:02 | MUBUSDT | surge | TIME | 24.0 | -0.14% | $-0.13 |
| 2026-09-23T15:46 | NEARUSDT | surge | STOP | 0.5 | -3.25% | $-3.07 |
| 2026-09-23T15:30 | RAYUSDT | surge | TARGET | 0.0 | +2.75% | $+2.60 |
| 2026-09-23T15:13 | SNDKBUSDT | surge | TIME | 24.0 | -1.24% | $-1.19 |
| 2026-09-23T14:24 | HBARUSDT | bottom | STOP | 0.0 | -3.25% | $-3.18 |
| 2026-09-23T14:24 | ZROUSDT | surge | STOP | 0.0 | -3.25% | $-3.18 |
| 2026-09-23T14:24 | COTIUSDT | surge | STOP | 0.2 | -3.25% | $-3.28 |
| 2026-09-23T14:24 | PROVEUSDT | surge | STOP | 2.2 | -3.25% | $-3.02 |
| 2026-09-23T14:24 | LUNCUSDT | surge | STOP | 14.8 | -3.25% | $-3.12 |
| 2026-09-23T14:24 | SKHYBUSDT | surge | STOP | 23.5 | -3.25% | $-3.22 |
| 2026-09-23T14:07 | LUNAUSDT | surge | STOP | 14.2 | -3.25% | $-3.38 |
| 2026-09-23T14:07 | SOXLBUSDT | surge | STOP | 19.5 | -3.25% | $-3.19 |
| 2026-09-23T13:51 | SNXXBUSDT | surge | STOP | 0.0 | -3.25% | $-3.39 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-23T14:40 | BNBUSDT | bottom | 760.19 | 773.32 | +1.73% |
| 2026-09-23T14:40 | MSTRBUSDT | bottom | 162.61 | 160.97 | -1.01% |
| 2026-09-23T14:40 | BTCUSDT | bottom | 84041.7 | 84186 | +0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
