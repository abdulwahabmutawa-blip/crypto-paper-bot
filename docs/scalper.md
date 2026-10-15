# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-15T00:51:21+00:00 · runs 3412 · equity **$721.58** (-27.84%) · cash $353.44 · open 5/10 · round trips 1278

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.25%/trade · realized $-278.02 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1120 | 50% | -0.22% | 47% | 46% | 7% |
| bottom | 158 | 44% | -0.45% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-15T00:49 | WCTUSDT | surge | STOP | 1.2 | -3.25% | $-2.31 |
| 2026-10-14T22:30 | SOXSBUSDT | surge | TARGET | 2.8 | +2.75% | $+1.94 |
| 2026-10-14T20:44 | AXLUSDT | surge | STOP | 3.0 | -3.25% | $-2.39 |
| 2026-10-14T19:23 | DODOUSDT | surge | STOP | 0.5 | -3.25% | $-2.29 |
| 2026-10-14T19:23 | SOXSBUSDT | surge | TARGET | 2.2 | +2.75% | $+1.99 |
| 2026-10-14T19:23 | AUSDT | surge | STOP | 2.2 | -3.25% | $-2.36 |
| 2026-10-14T18:03 | BERAUSDT | surge | STOP | 0.8 | -3.25% | $-2.39 |
| 2026-10-14T18:03 | BATUSDT | bottom | STOP | 4.0 | -3.25% | $-2.12 |
| 2026-10-14T17:14 | AXLUSDT | surge | TARGET | 0.2 | +2.75% | $+1.99 |
| 2026-10-14T17:14 | BERAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.99 |
| 2026-10-14T16:26 | INTCBUSDT | surge | STOP | 22.2 | -3.25% | $-2.50 |
| 2026-10-14T16:09 | PYTHUSDT | surge | STOP | 2.5 | -3.25% | $-2.30 |
| 2026-10-14T15:53 | SOXSBUSDT | surge | TARGET | 1.2 | +2.75% | $+2.01 |
| 2026-10-14T15:53 | BERAUSDT | surge | TARGET | 6.0 | +2.75% | $+2.00 |
| 2026-10-14T15:37 | LUMIAUSDT | surge | STOP | 0.0 | -3.25% | $-2.35 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-14T13:04 | BNBUSDT | bottom | 737.11 | 728.84 | -1.12% |
| 2026-10-14T13:20 | SOLUSDT | bottom | 104.93 | 104.18 | -0.71% |
| 2026-10-14T18:03 | QQQBUSDT | bottom | 728.76 | 724.48 | -0.59% |
| 2026-10-14T21:00 | MEGAUSDT | surge | 0.04515 | 0.04599 | +1.86% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
