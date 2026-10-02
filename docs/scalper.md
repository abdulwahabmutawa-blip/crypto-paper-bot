# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-02T08:58:59+00:00 · runs 2337 · equity **$881.37** (-11.86%) · cash $0.00 · open 10/10 · round trips 887

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-122.70 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 767 | 52% | -0.10% | 49% | 44% | 7% |
| bottom | 120 | 46% | -0.38% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-02T08:24 | ZKUSDT | surge | TARGET | 2.0 | +2.75% | $+2.66 |
| 2026-10-02T06:45 | RESOLVUSDT | surge | STOP | 1.0 | -3.25% | $-2.80 |
| 2026-10-02T06:28 | KORUBUSDT | surge | TARGET | 3.8 | +2.75% | $+2.45 |
| 2026-10-02T06:12 | DEXEUSDT | surge | TARGET | 2.0 | +2.75% | $+2.59 |
| 2026-10-02T05:39 | SUPERUSDT | surge | STOP | 0.8 | -3.25% | $-2.89 |
| 2026-10-02T04:33 | PEPEUSDT | surge | TARGET | 12.8 | +2.75% | $+2.38 |
| 2026-10-02T03:54 | RESOLVUSDT | surge | TARGET | 0.0 | +2.75% | $+2.52 |
| 2026-10-02T03:37 | SUPERUSDT | surge | TARGET | 1.0 | +2.75% | $+2.45 |
| 2026-10-02T02:28 | LSKUSDT | surge | STOP | 0.8 | -3.25% | $-3.01 |
| 2026-10-02T02:28 | MSTRBUSDT | surge | TARGET | 11.5 | +2.75% | $+2.38 |
| 2026-10-02T01:36 | RESOLVUSDT | surge | TARGET | 0.5 | +2.75% | $+2.48 |
| 2026-10-02T00:45 | LSKUSDT | surge | TARGET | 1.0 | +2.75% | $+2.39 |
| 2026-10-02T00:45 | SKYUSDT | surge | TARGET | 4.5 | +2.75% | $+2.43 |
| 2026-10-02T00:28 | ACEUSDT | surge | STOP | 8.5 | -3.25% | $-2.82 |
| 2026-10-01T23:36 | DYDXUSDT | surge | TARGET | 6.0 | +2.75% | $+2.43 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-01T12:13 | UNIUSDT | surge | 9.062 | 9.064 | +0.02% |
| 2026-10-01T13:23 | BNCBUSDT | surge | 6.03 | 6.07 | +0.66% |
| 2026-10-01T17:36 | SKHYBUSDT | surge | 188.77 | 193.84 | +2.69% |
| 2026-10-01T23:36 | DYDXUSDT | surge | 0.15245 | 0.15196 | -0.32% |
| 2026-10-02T00:28 | MORPHOUSDT | surge | 2.571 | 2.616 | +1.75% |
| 2026-10-02T00:45 | PLUMEUSDT | bottom | 0.01859 | 0.01868 | +0.48% |
| 2026-10-02T06:28 | CVXUSDT | surge | 2.34 | 2.331 | -0.38% |
| 2026-10-02T06:45 | WIFUSDT | surge | 0.2634 | 0.2577 | -2.16% |
| 2026-10-02T08:24 | ENJUSDT | surge | 0.0319 | 0.03243 | +1.66% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
