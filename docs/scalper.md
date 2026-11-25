# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-25T07:48:48+00:00 · runs 6740 · equity **$479.36** (-52.06%) · cash $262.84 · open 4/10 · round trips 2202

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-519.44 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1894 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 308 | 43% | -0.51% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-25T07:47 | TAOUSDT | bottom | STOP | 9.5 | -3.25% | $-1.43 |
| 2026-11-25T07:29 | USUALUSDT | surge | STOP | 0.2 | -3.25% | $-1.44 |
| 2026-11-25T06:21 | USUALUSDT | surge | TARGET | 1.2 | +2.75% | $+1.21 |
| 2026-11-25T04:39 | ERAUSDT | surge | TARGET | 0.5 | +2.75% | $+1.21 |
| 2026-11-25T04:22 | INITUSDT | surge | TARGET | 0.0 | +2.75% | $+1.21 |
| 2026-11-25T04:22 | BLURUSDT | surge | STOP | 0.2 | -3.25% | $-1.43 |
| 2026-11-25T03:47 | USUALUSDT | surge | TARGET | 4.8 | +2.75% | $+1.21 |
| 2026-11-25T00:14 | ETHUSDT | bottom | TIME | 24.0 | -2.58% | $-1.14 |
| 2026-11-24T20:44 | HBARUSDT | bottom | STOP | 8.8 | -3.25% | $-1.42 |
| 2026-11-24T20:44 | SPYBUSDT | surge | TIME | 24.0 | -0.54% | $-0.24 |
| 2026-11-24T20:44 | METABUSDT | surge | TIME | 24.0 | +0.03% | $+0.01 |
| 2026-11-24T14:37 | TRXUSDT | surge | TIME | 24.0 | -0.96% | $-0.44 |
| 2026-11-24T13:26 | INJUSDT | bottom | STOP | 9.5 | -3.25% | $-1.39 |
| 2026-11-24T12:33 | GOOGLBUSDT | surge | TIME | 24.0 | -0.33% | $-0.15 |
| 2026-11-24T10:11 | BABYUSDT | surge | TARGET | 3.5 | +2.75% | $+1.25 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-24T13:26 | AAVEUSDT | bottom | 93.51 | 92.57 | -1.01% |
| 2026-11-25T03:47 | ICPUSDT | bottom | 1.976 | 1.97 | -0.30% |
| 2026-11-25T04:56 | ERAUSDT | surge | 0.0768 | 0.0757 | -1.43% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
