# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T04:30:57+00:00 · runs 1810 · equity **$944.98** (-5.50%) · cash $0.00 · open 10/10 · round trips 640

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.07%/trade · realized $-53.21 · worst day $-50.94 · trades/day 29.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 542 | 54% | -0.00% | 50% | 42% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T04:29 | AVNTUSDT | surge | TARGET | 0.0 | +2.75% | $+2.64 |
| 2026-09-26T04:29 | PROMUSDT | surge | TARGET | 1.0 | +2.75% | $+2.61 |
| 2026-09-26T04:13 | SENTUSDT | surge | STOP | 1.0 | -3.25% | $-2.88 |
| 2026-09-26T04:13 | AVNTUSDT | surge | TARGET | 3.8 | +2.75% | $+2.84 |
| 2026-09-26T03:24 | RUNEUSDT | surge | TARGET | 5.2 | +2.75% | $+2.54 |
| 2026-09-26T02:47 | WLDUSDT | surge | STOP | 1.8 | -3.25% | $-2.97 |
| 2026-09-26T01:42 | VTHOUSDT | surge | TARGET | 11.8 | +2.75% | $+2.67 |
| 2026-09-26T00:53 | DODOUSDT | surge | STOP | 7.5 | -3.25% | $-3.07 |
| 2026-09-26T00:04 | MUBARAKUSDT | surge | TARGET | 4.0 | +2.75% | $+2.77 |
| 2026-09-25T21:55 | AEROUSDT | surge | TARGET | 1.2 | +2.75% | $+2.60 |
| 2026-09-25T21:55 | BANKUSDT | surge | STOP | 15.0 | -3.25% | $-2.93 |
| 2026-09-25T20:25 | AMDBUSDT | surge | TIME | 24.0 | -0.02% | $-0.02 |
| 2026-09-25T19:49 | SUIUSDT | surge | TARGET | 4.8 | +2.75% | $+2.69 |
| 2026-09-25T18:38 | KMNOUSDT | surge | STOP | 2.5 | -3.25% | $-3.02 |
| 2026-09-25T18:02 | REZUSDT | surge | TARGET | 0.2 | +2.75% | $+2.59 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-25T16:15 | KORUBUSDT | surge | 21.59 | 21.41 | -0.83% |
| 2026-09-25T16:51 | SKHYBUSDT | surge | 191.35 | 190.81 | -0.28% |
| 2026-09-25T18:02 | REZUSDT | surge | 0.004321 | 0.004277 | -1.02% |
| 2026-09-25T18:38 | ZKUSDT | surge | 0.01278 | 0.01281 | +0.23% |
| 2026-09-25T21:55 | ZROUSDT | surge | 1.606 | 1.564 | -2.62% |
| 2026-09-26T01:42 | DOTUSDT | surge | 1.236 | 1.221 | -1.21% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07848 | +1.04% |
| 2026-09-26T04:29 | AVNTUSDT | surge | 0.1323 | 0.1334 | +0.83% |
| 2026-09-26T04:29 | PROMUSDT | surge | 6.254 | 6.372 | +1.89% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
