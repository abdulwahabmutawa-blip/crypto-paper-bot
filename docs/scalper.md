# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-25T13:58:02+00:00 · runs 6748 · equity **$475.60** (-52.44%) · cash $302.98 · open 3/10 · round trips 2205

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.34%/trade · realized $-523.09 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1896 | 48% | -0.31% | 46% | 47% | 7% |
| bottom | 309 | 42% | -0.52% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-25T13:37 | ALICEUSDT | surge | STOP | 2.5 | -3.25% | $-1.42 |
| 2026-11-25T13:37 | ERAUSDT | surge | STOP | 4.8 | -3.25% | $-1.43 |
| 2026-11-25T13:37 | AAVEUSDT | bottom | TIME | 24.0 | -1.82% | $-0.79 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-25T03:47 | ICPUSDT | bottom | 1.976 | 1.947 | -1.47% |
| 2026-11-25T08:21 | SOLUSDT | bottom | 67.89 | 66.86 | -1.52% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
