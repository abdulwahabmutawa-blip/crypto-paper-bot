# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T06:57:30+00:00 · runs 677 · equity **$879.53** (-12.05%) · cash $0.00 · open 10/10 · round trips 234

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.50%/trade · realized $-111.42 · worst day $-50.94 · trades/day 26.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 169 | 44% | -0.55% | 40% | 50% | 9% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-13T03:40 | SAGAUSDT | surge | STOP | 0.0 | -3.25% | $-2.81 |
| 2026-09-13T03:24 | INJUSDT | surge | STOP | 6.2 | -3.25% | $-2.91 |
| 2026-09-13T02:19 | KAVAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.52 |
| 2026-09-13T01:30 | KAVAUSDT | surge | TARGET | 3.2 | +2.75% | $+2.46 |
| 2026-09-13T01:14 | NEIROUSDT | surge | STOP | 10.5 | -3.25% | $-2.92 |
| 2026-09-12T22:40 | PARTIUSDT | surge | STOP | 3.5 | -3.25% | $-2.83 |
| 2026-09-12T22:22 | JTOUSDT | surge | STOP | 3.8 | -3.25% | $-3.21 |
| 2026-09-12T22:04 | HEMIUSDT | surge | STOP | 0.5 | -3.25% | $-3.00 |
| 2026-09-12T21:28 | KAVAUSDT | surge | TARGET | 6.8 | +2.75% | $+2.47 |
| 2026-09-12T20:51 | SPCXBUSDT | surge | TIME | 24.0 | -0.57% | $-0.51 |
| 2026-09-12T20:15 | HEMIUSDT | surge | TARGET | 2.0 | +2.75% | $+2.39 |
| 2026-09-12T18:46 | ORDIUSDT | surge | STOP | 2.5 | -3.25% | $-2.93 |
| 2026-09-12T18:28 | PROMUSDT | surge | TARGET | 7.2 | +2.75% | $+2.65 |
| 2026-09-12T17:52 | WLFIUSDT | surge | STOP | 0.8 | -3.25% | $-2.92 |
| 2026-09-12T17:16 | CHIPUSDT | surge | STOP | 0.8 | -3.25% | $-2.89 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T16:18 | PYTHUSDT | surge | 0.05484 | 0.05466 | -0.33% |
| 2026-09-12T16:18 | PENDLEUSDT | surge | 2.187 | 2.142 | -2.06% |
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.04843 | -1.38% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T20:15 | PUMPUSDT | surge | 0.003852 | 0.00374 | -2.91% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.017 | -0.78% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 55.46 | +1.09% |
| 2026-09-13T01:14 | WLDUSDT | bottom | 0.3994 | 0.3927 | -1.68% |
| 2026-09-13T02:19 | ORDIUSDT | surge | 4.248 | 4.163 | -2.00% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.276 | +0.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
