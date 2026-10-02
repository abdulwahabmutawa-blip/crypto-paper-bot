# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T00:29:53+00:00 · runs 2306 · equity **$869.89** (-13.01%) · cash $0.00 · open 10/10 · round trips 874

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-138.74 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 754 | 52% | -0.12% | 49% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T00:28 | ACEUSDT | surge | STOP | 8.5 | -3.25% | $-2.82 |
| 2026-10-01T23:36 | DYDXUSDT | surge | TARGET | 6.0 | +2.75% | $+2.43 |
| 2026-10-01T23:36 | AAVEUSDT | surge | TARGET | 7.2 | +2.75% | $+2.22 |
| 2026-10-01T19:58 | PORTALUSDT | surge | STOP | 0.8 | -3.25% | $-2.97 |
| 2026-10-01T18:47 | SKYUSDT | surge | TARGET | 2.2 | +2.75% | $+2.45 |
| 2026-10-01T17:36 | KITEUSDT | surge | TARGET | 5.8 | +2.75% | $+2.36 |
| 2026-10-01T17:18 | OPNUSDT | surge | TARGET | 0.0 | +2.75% | $+2.36 |
| 2026-10-01T17:00 | POLUSDT | bottom | STOP | 6.0 | -3.25% | $-2.89 |
| 2026-10-01T16:18 | MEGAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.38 |
| 2026-10-01T16:01 | HYPEUSDT | surge | STOP | 15.5 | -3.25% | $-2.71 |
| 2026-10-01T15:43 | MOVEUSDT | surge | TARGET | 1.0 | +2.75% | $+2.38 |
| 2026-10-01T15:43 | MEGAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.38 |
| 2026-10-01T15:43 | HEIUSDT | surge | STOP | 1.5 | -3.25% | $-2.76 |
| 2026-10-01T14:33 | OPNUSDT | surge | TARGET | 0.0 | +2.75% | $+2.38 |
| 2026-10-01T14:33 | TRBUSDT | surge | STOP | 0.5 | -3.25% | $-2.76 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T12:13 | UNIUSDT | surge | 9.062 | 8.986 | -0.84% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 6.01 | -0.33% |
| 2026-10-01T14:33 | MSTRBUSDT | surge | 157.17 | 161.08 | +2.49% |
| 2026-10-01T15:43 | PEPEUSDT | surge | 4.39e-06 | 4.44e-06 | +1.14% |
| 2026-10-01T17:36 | SKHYBUSDT | surge | 188.77 | 191.37 | +1.38% |
| 2026-10-01T19:58 | SKYUSDT | surge | 0.08311 | 0.08586 | +3.31% |
| 2026-10-01T23:36 | DYDXUSDT | surge | 0.15245 | 0.15311 | +0.43% |
| 2026-10-01T23:36 | LSKUSDT | surge | 0.2995 | 0.306 | +2.17% |
| 2026-10-02T00:28 | MORPHOUSDT | surge | 2.571 | 2.573 | +0.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
