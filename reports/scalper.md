# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T20:20:03+00:00 · runs 3306 · equity **$754.62** (-24.54%) · cash $0.00 · open 10/10 · round trips 1244

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.22%/trade · realized $-245.72 · worst day $-50.94 · trades/day 31.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1092 | 50% | -0.19% | 48% | 45% | 7% |
| bottom | 152 | 45% | -0.45% | 39% | 45% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-13T20:18 | RENDERUSDT | bottom | TARGET | 6.0 | +2.75% | $+1.99 |
| 2026-10-13T18:23 | OPUSDT | surge | TARGET | 1.2 | +2.75% | $+2.04 |
| 2026-10-13T18:07 | ACEUSDT | surge | TARGET | 0.5 | +2.75% | $+2.06 |
| 2026-10-13T17:51 | AMPUSDT | surge | TARGET | 0.0 | +2.75% | $+2.06 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3289 | -0.30% |
| 2026-10-13T11:26 | MUBUSDT | bottom | 951.97 | 955.84 | +0.41% |
| 2026-10-13T14:11 | GOOGLBUSDT | surge | 357.8 | 354.51 | -0.92% |
| 2026-10-13T16:28 | PEPEUSDT | surge | 4.2e-06 | 4.19e-06 | -0.24% |
| 2026-10-13T16:45 | AMDBUSDT | surge | 600.13 | 608.6 | +1.41% |
| 2026-10-13T17:51 | INTCBUSDT | surge | 102.33 | 103.24 | +0.89% |
| 2026-10-13T18:07 | CRCLBUSDT | surge | 84.28 | 84.72 | +0.52% |
| 2026-10-13T18:23 | ACEUSDT | surge | 0.2015 | 0.1992 | -1.14% |
| 2026-10-13T20:18 | INJUSDT | surge | 8.194 | 8.178 | -0.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
