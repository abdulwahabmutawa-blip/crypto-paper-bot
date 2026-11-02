# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-02T07:45:59+00:00 · runs 5014 · equity **$578.94** (-42.11%) · cash $0.00 · open 10/10 · round trips 1750

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-415.64 · worst day $-50.94 · trades/day 29.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1523 | 49% | -0.28% | 46% | 47% | 7% |
| bottom | 227 | 43% | -0.47% | 37% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-02T07:11 | NIGHTUSDT | surge | STOP | 14.2 | -3.25% | $-1.65 |
| 2026-11-02T06:35 | INTCBUSDT | surge | TIME | 24.0 | +0.51% | $+0.29 |
| 2026-11-02T05:10 | RADUSDT | bottom | TIME | 24.0 | -0.66% | $-0.42 |
| 2026-11-02T04:53 | TRUMPUSDT | surge | STOP | 5.2 | -3.25% | $-1.71 |
| 2026-11-02T01:32 | INTWBUSDT | surge | TARGET | 19.2 | +2.75% | $+1.55 |
| 2026-11-02T01:15 | KORUBUSDT | surge | TARGET | 0.8 | +2.75% | $+1.49 |
| 2026-11-02T00:19 | MITOUSDT | surge | TARGET | 2.5 | +2.75% | $+1.45 |
| 2026-11-01T20:41 | BIOUSDT | surge | STOP | 0.2 | -3.25% | $-1.73 |
| 2026-11-01T20:07 | AEROUSDT | surge | STOP | 21.5 | -3.25% | $-1.84 |
| 2026-11-01T19:11 | LDOUSDT | surge | STOP | 3.2 | -3.25% | $-1.75 |
| 2026-11-01T18:54 | PHAUSDT | surge | STOP | 2.8 | -3.25% | $-1.78 |
| 2026-11-01T17:09 | BEAMXUSDT | bottom | TARGET | 1.0 | +2.75% | $+1.50 |
| 2026-11-01T16:51 | INJUSDT | surge | STOP | 22.2 | -3.25% | $-1.85 |
| 2026-11-01T16:34 | HEMIUSDT | surge | STOP | 1.0 | -3.25% | $-1.71 |
| 2026-11-01T15:59 | BATUSDT | surge | STOP | 17.2 | -3.25% | $-1.84 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-01T16:51 | ONDOUSDT | bottom | 0.4048 | 0.3953 | -2.35% |
| 2026-11-01T17:09 | CELOUSDT | bottom | 0.07412 | 0.07282 | -1.75% |
| 2026-11-01T23:29 | SEIUSDT | surge | 0.04825 | 0.04754 | -1.47% |
| 2026-11-02T01:15 | SKHYBUSDT | surge | 156.37 | 155.8 | -0.36% |
| 2026-11-02T01:32 | DRAMBUSDT | surge | 49.57 | 49.68 | +0.22% |
| 2026-11-02T04:53 | SOXLBUSDT | surge | 82.34 | 80.67 | -2.03% |
| 2026-11-02T05:10 | CRCLBUSDT | surge | 74.21 | 73.5 | -0.96% |
| 2026-11-02T06:35 | KORUBUSDT | surge | 11.79 | 11.68 | -0.93% |
| 2026-11-02T07:11 | PROMUSDT | bottom | 5.468 | 5.455 | -0.24% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
