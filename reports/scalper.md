# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T14:32:20+00:00 · runs 1147 · equity **$935.52** (-6.45%) · cash $0.00 · open 10/10 · round trips 391

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.17%/trade · realized $-67.88 · worst day $-50.94 · trades/day 27.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 309 | 53% | -0.07% | 48% | 43% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-18T14:30 | SKYUSDT | surge | TARGET | 0.2 | +2.75% | $+2.49 |
| 2026-09-18T14:14 | AUSDT | surge | TARGET | 5.8 | +2.75% | $+2.35 |
| 2026-09-18T14:14 | BCHUSDT | surge | TARGET | 10.2 | +2.75% | $+2.50 |
| 2026-09-18T13:10 | ZAMAUSDT | surge | STOP | 0.2 | -3.25% | $-3.40 |
| 2026-09-18T12:37 | TRBUSDT | surge | TARGET | 8.0 | +2.75% | $+2.80 |
| 2026-09-18T11:16 | 币安人生USDT | surge | STOP | 3.8 | -3.25% | $-2.94 |
| 2026-09-18T10:44 | DODOUSDT | surge | TIME | 24.0 | +1.13% | $+0.97 |
| 2026-09-18T10:12 | RENDERUSDT | surge | TARGET | 8.5 | +2.75% | $+2.65 |
| 2026-09-18T08:29 | BMNRBUSDT | surge | TARGET | 16.0 | +2.75% | $+2.28 |
| 2026-09-18T07:24 | REZUSDT | surge | STOP | 1.2 | -3.25% | $-3.04 |
| 2026-09-18T05:46 | 币安人生USDT | surge | TARGET | 2.0 | +2.75% | $+2.50 |
| 2026-09-18T04:41 | AUSDT | surge | TARGET | 3.0 | +2.75% | $+2.65 |
| 2026-09-18T04:24 | SEIUSDT | surge | TARGET | 1.5 | +2.75% | $+2.73 |
| 2026-09-18T03:31 | COINBUSDT | surge | TARGET | 13.0 | +2.75% | $+2.40 |
| 2026-09-18T03:31 | CAKEUSDT | surge | TARGET | 14.8 | +2.75% | $+2.47 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-17T15:38 | INTCBUSDT | surge | 109.9 | 108.12 | -1.62% |
| 2026-09-18T01:20 | AXSUSDT | surge | 0.995 | 1.003 | +0.80% |
| 2026-09-18T04:41 | SEIUSDT | surge | 0.04638 | 0.04728 | +1.94% |
| 2026-09-18T10:12 | ZKUSDT | surge | 0.01024 | 0.01034 | +0.98% |
| 2026-09-18T10:44 | BANKUSDT | surge | 0.0298 | 0.0304 | +2.01% |
| 2026-09-18T11:16 | DODOUSDT | surge | 0.01835 | 0.01831 | -0.22% |
| 2026-09-18T13:10 | THETAUSDT | surge | 0.2055 | 0.2064 | +0.44% |
| 2026-09-18T14:14 | SUSDT | surge | 0.03166 | 0.03147 | -0.60% |
| 2026-09-18T14:30 | PROVEUSDT | surge | 0.2039 | 0.2034 | -0.25% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
