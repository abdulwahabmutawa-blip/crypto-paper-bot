# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T09:02:11+00:00 · runs 684 · equity **$869.00** (-13.10%) · cash $0.00 · open 10/10 · round trips 239

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 44% (break-even 54%) · mean -0.53%/trade · realized $-120.79 · worst day $-50.94 · trades/day 26.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 174 | 43% | -0.59% | 40% | 51% | 9% |
| bottom | 65 | 45% | -0.35% | 43% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-12T22:04 | HEMIUSDT | surge | STOP | 0.5 | -3.25% | $-3.00 |
| 2026-09-12T21:28 | KAVAUSDT | surge | TARGET | 6.8 | +2.75% | $+2.47 |
| 2026-09-12T20:51 | SPCXBUSDT | surge | TIME | 24.0 | -0.57% | $-0.51 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T16:18 | PYTHUSDT | surge | 0.05484 | 0.05364 | -2.19% |
| 2026-09-12T16:53 | ZAMAUSDT | surge | 0.04911 | 0.04845 | -1.34% |
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.003 | -2.15% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 54.04 | -1.49% |
| 2026-09-13T01:14 | WLDUSDT | bottom | 0.3994 | 0.3894 | -2.50% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.2719 | -1.38% |
| 2026-09-13T08:06 | NEWTUSDT | surge | 0.04608 | 0.04605 | -0.07% |
| 2026-09-13T08:24 | API3USDT | surge | 0.2565 | 0.2558 | -0.27% |
| 2026-09-13T09:00 | GMTUSDT | surge | 0.00781 | 0.0078 | -0.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
