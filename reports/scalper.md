# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-14T17:15:38+00:00 · runs 3384 · equity **$730.57** (-26.94%) · cash $220.62 · open 7/10 · round trips 1270

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.24%/trade · realized $-268.11 · worst day $-50.94 · trades/day 31.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1113 | 50% | -0.21% | 47% | 46% | 7% |
| bottom | 157 | 45% | -0.44% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-14T17:14 | AXLUSDT | surge | TARGET | 0.2 | +2.75% | $+1.99 |
| 2026-10-14T17:14 | BERAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.99 |
| 2026-10-14T16:26 | INTCBUSDT | surge | STOP | 22.2 | -3.25% | $-2.50 |
| 2026-10-14T16:09 | PYTHUSDT | surge | STOP | 2.5 | -3.25% | $-2.30 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-14T13:04 | BNBUSDT | bottom | 737.11 | 731.35 | -0.78% |
| 2026-10-14T13:20 | SOLUSDT | bottom | 104.93 | 104.95 | +0.02% |
| 2026-10-14T13:53 | BATUSDT | bottom | 0.1752 | 0.1739 | -0.74% |
| 2026-10-14T16:58 | AUSDT | surge | 0.1076 | 0.1091 | +1.39% |
| 2026-10-14T16:58 | SOXSBUSDT | surge | 41.6 | 41.75 | +0.36% |
| 2026-10-14T17:14 | BERAUSDT | surge | 0.2471 | 0.2418 | -2.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
