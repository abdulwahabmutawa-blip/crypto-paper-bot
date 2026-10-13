# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T17:19:58+00:00 · runs 3295 · equity **$743.96** (-25.60%) · cash $74.92 · open 9/10 · round trips 1240

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-253.87 · worst day $-50.94 · trades/day 31.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1089 | 50% | -0.20% | 47% | 45% | 7% |
| bottom | 151 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-13T17:18 | AMPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.09 |
| 2026-10-13T17:18 | LINEAUSDT | surge | STOP | 0.8 | -3.25% | $-2.41 |
| 2026-10-13T17:02 | ACEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.04 |
| 2026-10-13T16:28 | ZKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.99 |
| 2026-10-13T16:28 | DUSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.35 |
| 2026-10-13T16:28 | JSTUSDT | surge | TIME | 24.0 | -1.96% | $-1.62 |
| 2026-10-13T14:11 | AMPUSDT | surge | STOP | 0.0 | -3.25% | $-2.36 |
| 2026-10-13T14:11 | DUSKUSDT | surge | TARGET | 1.0 | +2.75% | $+2.00 |
| 2026-10-13T13:46 | SOXSBUSDT | surge | TARGET | 12.0 | +2.75% | $+2.00 |
| 2026-10-13T13:46 | SPCXBUSDT | surge | STOP | 23.5 | -3.25% | $-2.37 |
| 2026-10-13T13:28 | PROMUSDT | surge | STOP | 6.2 | -3.25% | $-2.39 |
| 2026-10-13T13:11 | RSRUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.97 |
| 2026-10-13T12:36 | SUSDT | surge | TARGET | 0.0 | +2.75% | $+1.97 |
| 2026-10-13T12:01 | TIAUSDT | surge | STOP | 3.0 | -3.25% | $-2.40 |
| 2026-10-13T11:44 | ZAMAUSDT | surge | STOP | 2.8 | -3.25% | $-2.40 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3278 | -0.64% |
| 2026-10-13T11:26 | MUBUSDT | bottom | 951.97 | 939.86 | -1.27% |
| 2026-10-13T14:11 | GOOGLBUSDT | surge | 357.8 | 355.15 | -0.74% |
| 2026-10-13T14:11 | RENDERUSDT | bottom | 2.029 | 2.038 | +0.44% |
| 2026-10-13T16:28 | PEPEUSDT | surge | 4.2e-06 | 4.19e-06 | -0.24% |
| 2026-10-13T16:45 | AMDBUSDT | surge | 600.13 | 598.13 | -0.33% |
| 2026-10-13T16:45 | OPUSDT | surge | 0.1451 | 0.1442 | -0.62% |
| 2026-10-13T17:18 | ACEUSDT | surge | 0.1926 | 0.1933 | +0.36% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
