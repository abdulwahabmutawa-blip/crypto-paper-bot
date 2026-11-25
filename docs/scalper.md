# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-25T01:04:13+00:00 · runs 6720 · equity **$480.68** (-51.93%) · cash $262.60 · open 4/10 · round trips 2195

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-519.98 · worst day $-50.94 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1888 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 307 | 43% | -0.50% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-25T00:14 | ETHUSDT | bottom | TIME | 24.0 | -2.58% | $-1.14 |
| 2026-11-24T20:44 | HBARUSDT | bottom | STOP | 8.8 | -3.25% | $-1.42 |
| 2026-11-24T20:44 | SPYBUSDT | surge | TIME | 24.0 | -0.54% | $-0.24 |
| 2026-11-24T20:44 | METABUSDT | surge | TIME | 24.0 | +0.03% | $+0.01 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-24T13:26 | AAVEUSDT | bottom | 93.51 | 93.83 | +0.34% |
| 2026-11-24T22:05 | USUALUSDT | surge | 0.01159 | 0.01175 | +1.38% |
| 2026-11-24T22:05 | TAOUSDT | bottom | 180.2 | 179.8 | -0.22% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
