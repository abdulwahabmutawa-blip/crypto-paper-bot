# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T03:04:31+00:00 · runs 2315 · equity **$874.82** (-12.52%) · cash $0.00 · open 10/10 · round trips 879

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-132.07 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 759 | 52% | -0.11% | 49% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T02:28 | LSKUSDT | surge | STOP | 0.8 | -3.25% | $-3.01 |
| 2026-10-02T02:28 | MSTRBUSDT | surge | TARGET | 11.5 | +2.75% | $+2.38 |
| 2026-10-02T01:36 | RESOLVUSDT | surge | TARGET | 0.5 | +2.75% | $+2.48 |
| 2026-10-02T00:45 | LSKUSDT | surge | TARGET | 1.0 | +2.75% | $+2.39 |
| 2026-10-02T00:45 | SKYUSDT | surge | TARGET | 4.5 | +2.75% | $+2.43 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T12:13 | UNIUSDT | surge | 9.062 | 9.071 | +0.10% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 6.06 | +0.50% |
| 2026-10-01T15:43 | PEPEUSDT | surge | 4.39e-06 | 4.46e-06 | +1.59% |
| 2026-10-01T17:36 | SKHYBUSDT | surge | 188.77 | 192.33 | +1.89% |
| 2026-10-01T23:36 | DYDXUSDT | surge | 0.15245 | 0.1513 | -0.75% |
| 2026-10-02T00:28 | MORPHOUSDT | surge | 2.571 | 2.576 | +0.19% |
| 2026-10-02T00:45 | PLUMEUSDT | bottom | 0.01859 | 0.01881 | +1.18% |
| 2026-10-02T02:28 | KORUBUSDT | surge | 21.21 | 21.38 | +0.80% |
| 2026-10-02T02:28 | SUPERUSDT | surge | 0.2299 | 0.2352 | +2.31% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
