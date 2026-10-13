# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T23:29:59+00:00 · runs 3318 · equity **$748.32** (-25.17%) · cash $0.00 · open 10/10 · round trips 1247

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-251.17 · worst day $-50.94 · trades/day 32.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1094 | 50% | -0.20% | 47% | 45% | 7% |
| bottom | 153 | 44% | -0.45% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-13T16:28 | DUSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.35 |
| 2026-10-13T16:28 | JSTUSDT | surge | TIME | 24.0 | -1.96% | $-1.62 |
| 2026-10-13T14:11 | AMPUSDT | surge | STOP | 0.0 | -3.25% | $-2.36 |
| 2026-10-13T14:11 | DUSKUSDT | surge | TARGET | 1.0 | +2.75% | $+2.00 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-13T11:26 | MUBUSDT | bottom | 951.97 | 955.17 | +0.34% |
| 2026-10-13T14:11 | GOOGLBUSDT | surge | 357.8 | 354.8 | -0.84% |
| 2026-10-13T16:28 | PEPEUSDT | surge | 4.2e-06 | 4.2e-06 | +0.00% |
| 2026-10-13T16:45 | AMDBUSDT | surge | 600.13 | 608.52 | +1.40% |
| 2026-10-13T17:51 | INTCBUSDT | surge | 102.33 | 103.35 | +1.00% |
| 2026-10-13T18:07 | CRCLBUSDT | surge | 84.28 | 84.24 | -0.05% |
| 2026-10-13T20:18 | INJUSDT | surge | 8.194 | 8.132 | -0.76% |
| 2026-10-13T22:02 | PYTHUSDT | bottom | 0.07851 | 0.07787 | -0.82% |
| 2026-10-13T22:40 | BEAMXUSDT | surge | 0.002995 | 0.002964 | -1.04% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
