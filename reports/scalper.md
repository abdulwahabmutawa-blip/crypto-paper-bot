# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-18T04:42:39+00:00 · runs 1110 · equity **$928.39** (-7.16%) · cash $0.00 · open 10/10 · round trips 380

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.20%/trade · realized $-77.04 · worst day $-50.94 · trades/day 27.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 298 | 52% | -0.11% | 48% | 44% | 9% |
| bottom | 82 | 41% | -0.53% | 40% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-18T04:41 | AUSDT | surge | TARGET | 3.0 | +2.75% | $+2.65 |
| 2026-09-18T04:24 | SEIUSDT | surge | TARGET | 1.5 | +2.75% | $+2.73 |
| 2026-09-18T03:31 | COINBUSDT | surge | TARGET | 13.0 | +2.75% | $+2.40 |
| 2026-09-18T03:31 | CAKEUSDT | surge | TARGET | 14.8 | +2.75% | $+2.47 |
| 2026-09-18T02:42 | APTUSDT | surge | TARGET | 0.8 | +2.75% | $+2.66 |
| 2026-09-18T01:37 | APTUSDT | surge | TARGET | 0.8 | +2.75% | $+2.58 |
| 2026-09-18T01:20 | AXSUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-18T01:20 | PHAUSDT | surge | STOP | 0.8 | -3.25% | $-3.13 |
| 2026-09-18T01:20 | AUSDT | surge | TARGET | 7.8 | +2.75% | $+2.65 |
| 2026-09-18T00:32 | KORUBUSDT | surge | STOP | 7.8 | -3.25% | $-3.05 |
| 2026-09-18T00:32 | TRUMPUSDT | surge | TIME | 24.0 | +0.37% | $+0.36 |
| 2026-09-18T00:15 | ROSEUSDT | surge | STOP | 0.2 | -3.25% | $-3.23 |
| 2026-09-17T23:59 | WLDUSDT | surge | TARGET | 23.5 | +2.75% | $+2.66 |
| 2026-09-17T17:29 | PROVEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.58 |
| 2026-09-17T16:30 | PROVEUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-17T10:23 | DODOUSDT | surge | 0.01812 | 0.0184 | +1.55% |
| 2026-09-17T15:38 | INTCBUSDT | surge | 109.9 | 110.5 | +0.55% |
| 2026-09-17T16:13 | BMNRBUSDT | surge | 23.97 | 24.31 | +1.42% |
| 2026-09-18T01:20 | AXSUSDT | surge | 0.995 | 1.011 | +1.61% |
| 2026-09-18T01:20 | RENDERUSDT | surge | 1.477 | 1.503 | +1.76% |
| 2026-09-18T03:31 | 币安人生USDT | surge | 0.5087 | 0.5096 | +0.18% |
| 2026-09-18T03:31 | BCHUSDT | surge | 246.2 | 245 | -0.49% |
| 2026-09-18T04:24 | TRBUSDT | surge | 17.56 | 17.51 | -0.28% |
| 2026-09-18T04:41 | SEIUSDT | surge | 0.04638 | 0.04626 | -0.26% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
