# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-14T19:25:15+00:00 · runs 3392 · equity **$722.58** (-27.74%) · cash $282.75 · open 6/10 · round trips 1275

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.25%/trade · realized $-275.27 · worst day $-50.94 · trades/day 31.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1117 | 50% | -0.22% | 47% | 46% | 7% |
| bottom | 158 | 44% | -0.45% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-14T15:16 | AMDBUSDT | surge | STOP | 22.2 | -3.25% | $-2.41 |
| 2026-10-14T14:26 | GOOGLBUSDT | surge | TIME | 24.0 | -1.12% | $-0.81 |
| 2026-10-14T14:09 | CRCLBUSDT | surge | STOP | 19.8 | -3.25% | $-2.50 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-14T13:04 | BNBUSDT | bottom | 737.11 | 730.5 | -0.90% |
| 2026-10-14T13:20 | SOLUSDT | bottom | 104.93 | 104.77 | -0.15% |
| 2026-10-14T17:30 | AXLUSDT | surge | 0.0625 | 0.0618 | -1.12% |
| 2026-10-14T18:03 | QQQBUSDT | bottom | 728.76 | 729.87 | +0.15% |
| 2026-10-14T19:23 | SOXSBUSDT | surge | 42.6 | 42.18 | -0.99% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
