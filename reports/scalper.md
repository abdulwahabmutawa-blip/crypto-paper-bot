# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-14T12:16:35+00:00 · runs 3365 · equity **$744.70** (-25.53%) · cash $0.00 · open 10/10 · round trips 1256

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-258.14 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1101 | 50% | -0.20% | 47% | 45% | 7% |
| bottom | 155 | 45% | -0.44% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-14T11:42 | MUBUSDT | bottom | TIME | 24.0 | -1.50% | $-1.04 |
| 2026-10-14T11:26 | AXLUSDT | surge | STOP | 0.2 | -3.25% | $-2.26 |
| 2026-10-14T10:53 | CAKEUSDT | surge | STOP | 0.5 | -3.25% | $-2.34 |
| 2026-10-14T10:04 | INJUSDT | surge | STOP | 13.2 | -3.25% | $-2.42 |
| 2026-10-14T09:34 | ARUSDT | surge | STOP | 6.2 | -3.25% | $-2.44 |
| 2026-10-14T05:32 | WALUSDT | surge | TARGET | 0.0 | +2.75% | $+1.95 |
| 2026-10-14T05:15 | SOXLBUSDT | surge | STOP | 2.8 | -3.25% | $-2.38 |
| 2026-10-14T03:13 | PYTHUSDT | bottom | TARGET | 5.0 | +2.75% | $+2.01 |
| 2026-10-14T02:25 | BEAMXUSDT | surge | TARGET | 3.5 | +2.75% | $+1.96 |
| 2026-10-13T22:40 | ATOMUSDT | surge | STOP | 0.8 | -3.25% | $-2.39 |
| 2026-10-13T22:02 | TRXUSDT | bottom | TIME | 24.0 | -0.80% | $-0.59 |
| 2026-10-13T21:40 | ACEUSDT | surge | STOP | 3.0 | -3.25% | $-2.47 |
| 2026-10-13T20:18 | RENDERUSDT | bottom | TARGET | 6.0 | +2.75% | $+1.99 |
| 2026-10-13T18:23 | OPUSDT | surge | TARGET | 1.2 | +2.75% | $+2.04 |
| 2026-10-13T18:07 | ACEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.06 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-13T14:11 | GOOGLBUSDT | surge | 357.8 | 358.75 | +0.27% |
| 2026-10-13T16:28 | PEPEUSDT | surge | 4.2e-06 | 4.24e-06 | +0.95% |
| 2026-10-13T16:45 | AMDBUSDT | surge | 600.13 | 602.04 | +0.32% |
| 2026-10-13T17:51 | INTCBUSDT | surge | 102.33 | 101.72 | -0.60% |
| 2026-10-13T18:07 | CRCLBUSDT | surge | 84.28 | 84.22 | -0.07% |
| 2026-10-14T05:32 | ZECUSDT | surge | 1254.15 | 1249 | -0.41% |
| 2026-10-14T09:34 | BERAUSDT | surge | 0.2359 | 0.2402 | +1.82% |
| 2026-10-14T11:26 | SPCXBUSDT | bottom | 157.19 | 157.42 | +0.15% |
| 2026-10-14T11:42 | AMPUSDT | bottom | 0.000683 | 0.000694 | +1.61% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
