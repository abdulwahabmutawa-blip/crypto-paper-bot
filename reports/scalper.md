# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-23T14:09:15+00:00 · runs 1579 · equity **$950.72** (-4.93%) · cash $0.00 · open 10/10 · round trips 569

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean -0.06%/trade · realized $-40.77 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 476 | 54% | +0.02% | 50% | 42% | 8% |
| bottom | 93 | 43% | -0.48% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-23T14:07 | LUNAUSDT | surge | STOP | 14.2 | -3.25% | $-3.38 |
| 2026-09-23T14:07 | SOXLBUSDT | surge | STOP | 19.5 | -3.25% | $-3.19 |
| 2026-09-23T13:51 | SNXXBUSDT | surge | STOP | 0.0 | -3.25% | $-3.39 |
| 2026-09-23T13:35 | RAYUSDT | surge | TARGET | 0.0 | +2.75% | $+2.80 |
| 2026-09-23T13:18 | COTIUSDT | surge | TARGET | 0.0 | +2.75% | $+2.72 |
| 2026-09-23T13:02 | ICPUSDT | surge | STOP | 0.5 | -3.25% | $-3.22 |
| 2026-09-23T13:02 | SPCXBUSDT | bottom | TIME | 24.0 | +0.77% | $+0.78 |
| 2026-09-23T12:29 | 0GUSDT | surge | STOP | 0.8 | -3.25% | $-3.33 |
| 2026-09-23T11:48 | PEOPLEUSDT | surge | STOP | 13.8 | -3.25% | $-3.12 |
| 2026-09-23T11:31 | BBUSDT | surge | STOP | 2.2 | -3.25% | $-3.44 |
| 2026-09-23T09:09 | CAKEUSDT | surge | STOP | 4.8 | -3.25% | $-3.56 |
| 2026-09-23T04:10 | TIAUSDT | surge | TARGET | 2.2 | +2.75% | $+2.93 |
| 2026-09-23T01:40 | ENSUSDT | surge | TARGET | 0.2 | +2.75% | $+2.85 |
| 2026-09-23T01:07 | PLUMEUSDT | surge | TARGET | 3.2 | +2.75% | $+2.77 |
| 2026-09-22T23:36 | ONDOUSDT | bottom | TARGET | 10.5 | +2.75% | $+2.78 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-22T14:44 | SKHYBUSDT | surge | 194.89 | 189.78 | -2.62% |
| 2026-09-22T15:02 | SNDKBUSDT | surge | 1858.77 | 1858.16 | -0.03% |
| 2026-09-22T15:56 | MUBUSDT | surge | 1074.98 | 1088.87 | +1.29% |
| 2026-09-22T23:19 | LUNCUSDT | surge | 5.67e-05 | 5.536e-05 | -2.36% |
| 2026-09-23T11:48 | PROVEUSDT | surge | 0.2371 | 0.2363 | -0.34% |
| 2026-09-23T13:02 | SKYUSDT | surge | 0.07419 | 0.07556 | +1.85% |
| 2026-09-23T13:51 | COTIUSDT | surge | 0.01758 | 0.01686 | -4.10% |
| 2026-09-23T14:07 | ZROUSDT | surge | 1.482 | 1.462 | -1.35% |
| 2026-09-23T14:07 | HBARUSDT | bottom | 0.09406 | 0.09322 | -0.89% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
