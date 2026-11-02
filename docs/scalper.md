# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-02T20:00:49+00:00 · runs 5043 · equity **$566.23** (-43.38%) · cash $108.43 · open 8/10 · round trips 1767

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-429.69 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1536 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 231 | 42% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-02T19:59 | HOTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.49 |
| 2026-11-02T19:59 | MUBUSDT | bottom | STOP | 3.0 | -3.25% | $-1.77 |
| 2026-11-02T19:43 | HOTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.47 |
| 2026-11-02T19:26 | MSTRBUSDT | surge | STOP | 2.2 | -3.25% | $-1.77 |
| 2026-11-02T19:10 | HOTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.49 |
| 2026-11-02T19:10 | BEAMXUSDT | bottom | STOP | 0.8 | -3.25% | $-1.76 |
| 2026-11-02T18:05 | SOXSBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.54 |
| 2026-11-02T18:05 | SEIUSDT | surge | STOP | 18.5 | -3.25% | $-1.71 |
| 2026-11-02T17:16 | DRAMBUSDT | surge | STOP | 15.5 | -3.25% | $-1.88 |
| 2026-11-02T16:59 | MEGAUSDT | surge | STOP | 0.8 | -3.25% | $-1.60 |
| 2026-11-02T16:59 | MITOUSDT | surge | TARGET | 2.2 | +2.75% | $+1.47 |
| 2026-11-02T16:59 | KORUBUSDT | surge | STOP | 8.0 | -3.25% | $-1.86 |
| 2026-11-02T16:59 | CRCLBUSDT | surge | STOP | 9.5 | -3.25% | $-2.05 |
| 2026-11-02T16:59 | SKHYBUSDT | surge | STOP | 15.2 | -3.25% | $-1.81 |
| 2026-11-02T16:59 | CELOUSDT | bottom | STOP | 22.8 | -3.25% | $-1.83 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-02T07:11 | PROMUSDT | bottom | 5.468 | 5.412 | -1.02% |
| 2026-11-02T16:59 | TSLABUSDT | surge | 410.69 | 405.51 | -1.26% |
| 2026-11-02T16:59 | BABABUSDT | surge | 103.32 | 102.44 | -0.85% |
| 2026-11-02T16:59 | SPCXBUSDT | surge | 140.88 | 137.98 | -2.06% |
| 2026-11-02T16:59 | COWUSDT | surge | 0.1187 | 0.1162 | -2.11% |
| 2026-11-02T19:10 | TQQQBUSDT | bottom | 61.48 | 60.66 | -1.33% |
| 2026-11-02T19:59 | FETUSDT | bottom | 0.1538 | 0.1554 | +1.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
