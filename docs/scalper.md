# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-14T10:54:49+00:00 · runs 3360 · equity **$740.93** (-25.91%) · cash $0.00 · open 10/10 · round trips 1254

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-254.83 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1100 | 50% | -0.20% | 47% | 45% | 7% |
| bottom | 154 | 45% | -0.43% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-13T17:51 | AMPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.06 |
| 2026-10-13T17:18 | AMPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.09 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-13T11:26 | MUBUSDT | bottom | 951.97 | 940.7 | -1.18% |
| 2026-10-13T14:11 | GOOGLBUSDT | surge | 357.8 | 357.38 | -0.12% |
| 2026-10-13T16:28 | PEPEUSDT | surge | 4.2e-06 | 4.19e-06 | -0.24% |
| 2026-10-13T16:45 | AMDBUSDT | surge | 600.13 | 600.2 | +0.01% |
| 2026-10-13T17:51 | INTCBUSDT | surge | 102.33 | 101.49 | -0.82% |
| 2026-10-13T18:07 | CRCLBUSDT | surge | 84.28 | 83.74 | -0.64% |
| 2026-10-14T05:32 | ZECUSDT | surge | 1254.15 | 1244.54 | -0.77% |
| 2026-10-14T09:34 | BERAUSDT | surge | 0.2359 | 0.2336 | -0.97% |
| 2026-10-14T10:53 | AXLUSDT | surge | 0.063 | 0.0623 | -1.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
