# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T02:46:22+00:00 · runs 1273 · equity **$939.69** (-6.03%) · cash $91.34 · open 9/10 · round trips 449

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.11%/trade · realized $-51.25 · worst day $-50.94 · trades/day 28.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 366 | 54% | -0.02% | 49% | 42% | 9% |
| bottom | 83 | 42% | -0.49% | 41% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T02:44 | ALGOUSDT | surge | STOP | 1.8 | -3.25% | $-3.24 |
| 2026-09-20T02:44 | TAOUSDT | surge | STOP | 14.2 | -3.25% | $-2.90 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T08:27 | VETUSDT | surge | 0.008627 | 0.008497 | -1.51% |
| 2026-09-19T08:45 | ACEUSDT | surge | 0.1575 | 0.1598 | +1.46% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 108.18 | -1.95% |
| 2026-09-19T21:56 | DASHUSDT | bottom | 57.97 | 57.42 | -0.95% |
| 2026-09-19T23:28 | SEIUSDT | surge | 0.04964 | 0.0484 | -2.50% |
| 2026-09-20T01:55 | KAITOUSDT | surge | 0.3482 | 0.3419 | -1.81% |
| 2026-09-20T02:28 | CTSIUSDT | surge | 0.02948 | 0.02901 | -1.59% |
| 2026-09-20T02:44 | XRPUSDT | bottom | 1.3972 | 1.3831 | -1.01% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
