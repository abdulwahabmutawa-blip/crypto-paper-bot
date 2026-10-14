# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-14T18:20:49+00:00 · runs 3388 · equity **$725.00** (-27.50%) · cash $211.00 · open 7/10 · round trips 1272

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.25%/trade · realized $-272.62 · worst day $-50.94 · trades/day 31.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1114 | 50% | -0.22% | 47% | 46% | 7% |
| bottom | 158 | 44% | -0.45% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-14T18:03 | BERAUSDT | surge | STOP | 0.8 | -3.25% | $-2.39 |
| 2026-10-14T18:03 | BATUSDT | bottom | STOP | 4.0 | -3.25% | $-2.12 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-14T13:04 | BNBUSDT | bottom | 737.11 | 728.74 | -1.14% |
| 2026-10-14T13:20 | SOLUSDT | bottom | 104.93 | 104 | -0.89% |
| 2026-10-14T16:58 | AUSDT | surge | 0.1076 | 0.1068 | -0.74% |
| 2026-10-14T16:58 | SOXSBUSDT | surge | 41.6 | 42.19 | +1.42% |
| 2026-10-14T17:30 | AXLUSDT | surge | 0.0625 | 0.0612 | -2.08% |
| 2026-10-14T18:03 | QQQBUSDT | bottom | 728.76 | 729.63 | +0.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
