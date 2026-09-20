# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T02:29:59+00:00 · runs 1272 · equity **$953.87** (-4.61%) · cash $0.00 · open 10/10 · round trips 447

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-45.12 · worst day $-50.94 · trades/day 27.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 364 | 54% | -0.00% | 49% | 41% | 9% |
| bottom | 83 | 42% | -0.49% | 41% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T02:28 | UNIUSDT | bottom | TARGET | 4.8 | +2.75% | $+2.42 |
| 2026-09-20T01:55 | HOMEUSDT | surge | STOP | 0.8 | -3.25% | $-3.24 |
| 2026-09-20T00:50 | ALGOUSDT | surge | TARGET | 0.2 | +2.75% | $+2.67 |
| 2026-09-20T00:50 | ZILUSDT | surge | TARGET | 0.2 | +2.75% | $+2.67 |
| 2026-09-20T00:17 | HOMEUSDT | surge | TARGET | 3.8 | +2.75% | $+2.70 |
| 2026-09-20T00:17 | 0GUSDT | surge | TARGET | 6.5 | +2.75% | $+2.50 |
| 2026-09-19T22:13 | FLOKIUSDT | surge | STOP | 2.0 | -3.25% | $-3.09 |
| 2026-09-19T21:56 | PEPEUSDT | surge | STOP | 0.8 | -3.25% | $-3.20 |
| 2026-09-19T21:56 | BERAUSDT | surge | STOP | 0.8 | -3.25% | $-3.20 |
| 2026-09-19T21:20 | NEIROUSDT | surge | STOP | 3.5 | -3.25% | $-2.95 |
| 2026-09-19T20:45 | PHAUSDT | surge | TARGET | 2.5 | +2.75% | $+2.70 |
| 2026-09-19T20:45 | SENTUSDT | surge | TIME | 24.0 | +0.82% | $+0.78 |
| 2026-09-19T20:27 | SNDKBUSDT | surge | TIME | 24.0 | -0.61% | $-0.60 |
| 2026-09-19T20:09 | ONDOUSDT | surge | STOP | 2.8 | -3.25% | $-3.19 |
| 2026-09-19T17:48 | PROVEUSDT | surge | TARGET | 12.8 | +2.75% | $+2.62 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.008703 | +0.88% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.1608 | +2.10% |
| 2026-09-19T12:23 | TAOUSDT | surge | 267.9 | 261.6 | -2.35% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 109.77 | -0.51% |
| 2026-09-19T21:56 | DASHUSDT | bottom | 57.97 | 57.98 | +0.02% |
| 2026-09-19T23:28 | SEIUSDT | surge | 0.04964 | 0.04908 | -1.13% |
| 2026-09-20T00:50 | ALGOUSDT | surge | 0.1078 | 0.1066 | -1.11% |
| 2026-09-20T01:55 | KAITOUSDT | surge | 0.3482 | 0.3498 | +0.46% |
| 2026-09-20T02:28 | CTSIUSDT | surge | 0.02948 | 0.0295 | +0.07% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
