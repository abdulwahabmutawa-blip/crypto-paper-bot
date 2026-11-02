# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-02T00:59:34+00:00 · runs 4990 · equity **$582.36** (-41.76%) · cash $0.00 · open 10/10 · round trips 1744

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-415.18 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1518 | 48% | -0.28% | 46% | 47% | 7% |
| bottom | 226 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-02T00:19 | MITOUSDT | surge | TARGET | 2.5 | +2.75% | $+1.45 |
| 2026-11-01T20:41 | BIOUSDT | surge | STOP | 0.2 | -3.25% | $-1.73 |
| 2026-11-01T20:07 | AEROUSDT | surge | STOP | 21.5 | -3.25% | $-1.84 |
| 2026-11-01T19:11 | LDOUSDT | surge | STOP | 3.2 | -3.25% | $-1.75 |
| 2026-11-01T18:54 | PHAUSDT | surge | STOP | 2.8 | -3.25% | $-1.78 |
| 2026-11-01T17:09 | BEAMXUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.50 |
| 2026-11-01T16:51 | INJUSDT | surge | STOP | 22.2 | -3.25% | $-1.85 |
| 2026-11-01T16:34 | HEMIUSDT | surge | STOP | 1.0 | -3.25% | $-1.71 |
| 2026-11-01T15:59 | BATUSDT | surge | STOP | 17.2 | -3.25% | $-1.84 |
| 2026-11-01T15:59 | NEARUSDT | surge | STOP | 23.5 | -3.25% | $-1.84 |
| 2026-11-01T15:41 | INITUSDT | surge | STOP | 0.2 | -3.25% | $-1.81 |
| 2026-11-01T15:23 | BIOUSDT | surge | STOP | 0.5 | -3.25% | $-1.76 |
| 2026-11-01T15:06 | TRUMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.49 |
| 2026-11-01T14:31 | TRUMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.45 |
| 2026-11-01T14:31 | BIOUSDT | surge | TARGET | 0.2 | +2.75% | $+1.45 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-01T04:58 | RADUSDT | bottom | 0.242 | 0.236 | -2.48% |
| 2026-11-01T06:06 | INTWBUSDT | surge | 7.52 | 7.51 | -0.13% |
| 2026-11-01T06:23 | INTCBUSDT | surge | 66.03 | 65.78 | -0.38% |
| 2026-11-01T16:34 | NIGHTUSDT | surge | 0.04234 | 0.04165 | -1.63% |
| 2026-11-01T16:51 | ONDOUSDT | bottom | 0.4048 | 0.3997 | -1.26% |
| 2026-11-01T17:09 | CELOUSDT | bottom | 0.07412 | 0.07434 | +0.30% |
| 2026-11-01T23:29 | TRUMPUSDT | surge | 1.729 | 1.73 | +0.06% |
| 2026-11-01T23:29 | SEIUSDT | surge | 0.04825 | 0.04834 | +0.19% |
| 2026-11-02T00:19 | KORUBUSDT | surge | 10.99 | 11.12 | +1.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
