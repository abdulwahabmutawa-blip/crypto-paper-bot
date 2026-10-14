# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-14T07:19:15+00:00 · runs 3347 · equity **$750.43** (-24.96%) · cash $0.00 · open 10/10 · round trips 1251

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.22%/trade · realized $-247.63 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1097 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 154 | 45% | -0.43% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-13T17:18 | LINEAUSDT | surge | STOP | 0.8 | -3.25% | $-2.41 |
| 2026-10-13T17:02 | ACEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.04 |
| 2026-10-13T16:28 | ZKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.99 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-13T11:26 | MUBUSDT | bottom | 951.97 | 946.6 | -0.56% |
| 2026-10-13T14:11 | GOOGLBUSDT | surge | 357.8 | 356.94 | -0.24% |
| 2026-10-13T16:28 | PEPEUSDT | surge | 4.2e-06 | 4.18e-06 | -0.48% |
| 2026-10-13T16:45 | AMDBUSDT | surge | 600.13 | 604.25 | +0.69% |
| 2026-10-13T17:51 | INTCBUSDT | surge | 102.33 | 102.37 | +0.04% |
| 2026-10-13T18:07 | CRCLBUSDT | surge | 84.28 | 84.18 | -0.12% |
| 2026-10-13T20:18 | INJUSDT | surge | 8.194 | 8.164 | -0.37% |
| 2026-10-14T03:13 | ARUSDT | surge | 4.009 | 3.947 | -1.55% |
| 2026-10-14T05:32 | ZECUSDT | surge | 1254.15 | 1253.5 | -0.05% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
