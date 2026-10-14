# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-14T15:55:06+00:00 · runs 3379 · equity **$727.75** (-27.22%) · cash $292.21 · open 6/10 · round trips 1266

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.24%/trade · realized $-267.29 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1109 | 50% | -0.21% | 47% | 46% | 7% |
| bottom | 157 | 45% | -0.44% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-14T15:53 | SOXSBUSDT | surge | TARGET | 1.2 | +2.75% | $+2.01 |
| 2026-10-14T15:53 | BERAUSDT | surge | TARGET | 6.0 | +2.75% | $+2.00 |
| 2026-10-14T15:37 | LUMIAUSDT | surge | STOP | 0.0 | -3.25% | $-2.35 |
| 2026-10-14T15:16 | AMDBUSDT | surge | STOP | 22.2 | -3.25% | $-2.41 |
| 2026-10-14T14:26 | GOOGLBUSDT | surge | TIME | 24.0 | -1.12% | $-0.81 |
| 2026-10-14T14:09 | CRCLBUSDT | surge | STOP | 19.8 | -3.25% | $-2.50 |
| 2026-10-14T13:53 | SPCXBUSDT | bottom | STOP | 2.2 | -3.25% | $-2.19 |
| 2026-10-14T13:20 | AMPUSDT | bottom | TARGET | 1.5 | +2.75% | $+1.88 |
| 2026-10-14T13:20 | PEPEUSDT | surge | STOP | 20.8 | -3.25% | $-2.41 |
| 2026-10-14T13:04 | ZECUSDT | surge | STOP | 7.2 | -3.25% | $-2.36 |
| 2026-10-14T11:42 | MUBUSDT | bottom | TIME | 24.0 | -1.50% | $-1.04 |
| 2026-10-14T11:26 | AXLUSDT | surge | STOP | 0.2 | -3.25% | $-2.26 |
| 2026-10-14T10:53 | CAKEUSDT | surge | STOP | 0.5 | -3.25% | $-2.34 |
| 2026-10-14T10:04 | INJUSDT | surge | STOP | 13.2 | -3.25% | $-2.42 |
| 2026-10-14T09:34 | ARUSDT | surge | STOP | 6.2 | -3.25% | $-2.44 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-13T17:51 | INTCBUSDT | surge | 102.33 | 99.81 | -2.46% |
| 2026-10-14T13:04 | BNBUSDT | bottom | 737.11 | 730.44 | -0.90% |
| 2026-10-14T13:20 | PYTHUSDT | surge | 0.08348 | 0.08136 | -2.54% |
| 2026-10-14T13:20 | SOLUSDT | bottom | 104.93 | 104.17 | -0.72% |
| 2026-10-14T13:53 | BATUSDT | bottom | 0.1752 | 0.1749 | -0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
