# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-14T03:24:40+00:00 · runs 753 · equity **$886.73** (-11.33%) · cash $0.00 · open 10/10 · round trips 274

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.43%/trade · realized $-113.76 · worst day $-50.94 · trades/day 27.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 203 | 46% | -0.43% | 42% | 49% | 9% |
| bottom | 71 | 44% | -0.42% | 42% | 45% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-14T03:23 | CAKEUSDT | surge | TARGET | 7.5 | +2.75% | $+2.36 |
| 2026-09-14T02:50 | SAGAUSDT | bottom | TARGET | 4.5 | +2.75% | $+2.35 |
| 2026-09-14T02:34 | PEPEUSDT | bottom | TARGET | 4.0 | +2.75% | $+2.42 |
| 2026-09-14T02:18 | LAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.39 |
| 2026-09-14T00:07 | PUMPUSDT | bottom | STOP | 1.8 | -3.25% | $-2.78 |
| 2026-09-13T22:29 | ALGOUSDT | surge | STOP | 0.8 | -3.25% | $-2.94 |
| 2026-09-13T22:29 | DOTUSDT | bottom | TIME | 24.0 | -2.30% | $-2.20 |
| 2026-09-13T22:13 | ARUSDT | surge | STOP | 3.2 | -3.25% | $-2.88 |
| 2026-09-13T22:13 | MBLUSDT | surge | TARGET | 4.5 | +2.75% | $+2.52 |
| 2026-09-13T22:13 | STXUSDT | surge | STOP | 18.5 | -3.25% | $-2.72 |
| 2026-09-13T22:13 | DASHUSDT | bottom | STOP | 23.5 | -3.25% | $-2.74 |
| 2026-09-13T21:36 | XTZUSDT | surge | STOP | 0.8 | -3.25% | $-3.04 |
| 2026-09-13T20:30 | XTZUSDT | surge | TARGET | 3.2 | +2.75% | $+2.50 |
| 2026-09-13T19:41 | GMTUSDT | surge | STOP | 4.2 | -3.25% | $-2.88 |
| 2026-09-13T18:52 | SCRUSDT | surge | STOP | 1.0 | -3.25% | $-2.98 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.3528 | +0.71% |
| 2026-09-13T17:46 | ICPUSDT | surge | 2.784 | 2.838 | +1.94% |
| 2026-09-14T00:07 | TRXUSDT | bottom | 0.3384 | 0.339 | +0.18% |
| 2026-09-14T02:01 | BABYUSDT | surge | 0.01249 | 0.01264 | +1.20% |
| 2026-09-14T02:18 | LAUSDT | surge | 0.0676 | 0.066 | -2.37% |
| 2026-09-14T02:18 | AEROUSDT | surge | 0.5712 | 0.5757 | +0.79% |
| 2026-09-14T02:34 | ARUSDT | surge | 2.897 | 2.859 | -1.31% |
| 2026-09-14T02:50 | BANKUSDT | surge | 0.0282 | 0.028 | -0.71% |
| 2026-09-14T03:23 | TRUMPUSDT | surge | 2.003 | 2.003 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
