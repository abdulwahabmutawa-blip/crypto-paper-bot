# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T11:42:41+00:00 · runs 694 · equity **$866.33** (-13.37%) · cash $0.00 · open 10/10 · round trips 242

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 43% (break-even 54%) · mean -0.54%/trade · realized $-124.05 · worst day $-50.94 · trades/day 26.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 176 | 43% | -0.59% | 40% | 51% | 9% |
| bottom | 66 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-13T11:08 | NEWTUSDT | surge | STOP | 2.8 | -3.25% | $-2.80 |
| 2026-09-13T09:53 | API3USDT | surge | TARGET | 1.2 | +2.75% | $+2.37 |
| 2026-09-13T09:53 | WLDUSDT | bottom | STOP | 8.5 | -3.25% | $-2.83 |
| 2026-09-13T09:00 | ORDIUSDT | surge | STOP | 6.2 | -3.25% | $-3.07 |
| 2026-09-13T08:24 | CVCUSDT | surge | STOP | 0.2 | -3.25% | $-2.89 |
| 2026-09-13T08:06 | PENDLEUSDT | surge | STOP | 15.5 | -3.25% | $-2.89 |
| 2026-09-13T07:48 | NEWTUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
| 2026-09-13T07:13 | PUMPUSDT | surge | STOP | 10.5 | -3.25% | $-2.91 |
| 2026-09-13T03:40 | SAGAUSDT | surge | STOP | 0.0 | -3.25% | $-2.81 |
| 2026-09-13T03:24 | INJUSDT | surge | STOP | 6.2 | -3.25% | $-2.91 |
| 2026-09-13T02:19 | KAVAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.52 |
| 2026-09-13T01:30 | KAVAUSDT | surge | TARGET | 3.2 | +2.75% | $+2.46 |
| 2026-09-13T01:14 | NEIROUSDT | surge | STOP | 10.5 | -3.25% | $-2.92 |
| 2026-09-12T22:40 | PARTIUSDT | surge | STOP | 3.5 | -3.25% | $-2.83 |
| 2026-09-12T22:22 | JTOUSDT | surge | STOP | 3.8 | -3.25% | $-3.21 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T16:18 | PYTHUSDT | surge | 0.05484 | 0.05367 | -2.13% |
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.0483 | -1.65% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.01 | -1.46% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 54.17 | -1.26% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.2713 | -1.60% |
| 2026-09-13T09:00 | GMTUSDT | surge | 0.00781 | 0.00768 | -1.66% |
| 2026-09-13T09:53 | DODOUSDT | surge | 0.01812 | 0.01814 | +0.11% |
| 2026-09-13T09:53 | GLMUSDT | surge | 0.1216 | 0.1196 | -1.64% |
| 2026-09-13T11:08 | POLYXUSDT | surge | 0.0413 | 0.0415 | +0.48% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
