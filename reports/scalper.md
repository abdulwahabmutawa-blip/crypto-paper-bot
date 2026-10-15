# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-15T09:17:29+00:00 · runs 3444 · equity **$718.36** (-28.16%) · cash $562.46 · open 2/10 · round trips 1283

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.25%/trade · realized $-281.04 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1123 | 50% | -0.22% | 47% | 46% | 7% |
| bottom | 160 | 44% | -0.49% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-15T07:14 | SOXSBUSDT | surge | TARGET | 6.0 | +2.75% | $+1.94 |
| 2026-10-15T02:32 | DUSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.31 |
| 2026-10-15T02:32 | SOLUSDT | bottom | STOP | 13.0 | -3.25% | $-2.30 |
| 2026-10-15T02:32 | BNBUSDT | bottom | STOP | 13.2 | -3.25% | $-2.29 |
| 2026-10-15T01:23 | MEGAUSDT | surge | TARGET | 4.0 | +2.75% | $+1.95 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-14T18:03 | QQQBUSDT | bottom | 728.76 | 722.5 | -0.86% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
