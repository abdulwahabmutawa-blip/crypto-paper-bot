# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-18T10:36:07+00:00 · runs 3713 · equity **$665.74** (-33.43%) · cash $126.99 · open 8/10 · round trips 1371

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-334.51 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1198 | 48% | -0.28% | 46% | 47% | 7% |
| bottom | 173 | 45% | -0.41% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-18T10:34 | SENTUSDT | surge | STOP | 0.2 | -3.25% | $-2.10 |
| 2026-10-18T10:00 | OSMOUSDT | surge | STOP | 0.5 | -3.25% | $-2.10 |
| 2026-10-18T09:43 | XLMUSDT | bottom | TIME | 24.0 | -0.70% | $-0.47 |
| 2026-10-18T09:26 | GLMRUSDT | surge | TARGET | 0.2 | +2.75% | $+1.75 |
| 2026-10-18T09:09 | AXLUSDT | surge | TARGET | 0.8 | +2.75% | $+1.75 |
| 2026-10-18T07:44 | GTCUSDT | surge | STOP | 0.8 | -3.25% | $-2.02 |
| 2026-10-18T06:53 | HBARUSDT | surge | TARGET | 10.2 | +2.75% | $+1.91 |
| 2026-10-18T02:48 | APEUSDT | surge | STOP | 1.0 | -3.25% | $-2.06 |
| 2026-10-18T02:16 | RSRUSDT | surge | STOP | 0.5 | -3.25% | $-2.06 |
| 2026-10-18T02:00 | LSKUSDT | surge | STOP | 3.0 | -3.25% | $-2.06 |
| 2026-10-18T01:44 | UNIUSDT | bottom | TARGET | 8.8 | +2.75% | $+1.80 |
| 2026-10-17T23:50 | SOXSBUSDT | surge | STOP | 1.8 | -3.25% | $-2.06 |
| 2026-10-17T23:17 | ALTUSDT | surge | STOP | 1.0 | -3.25% | $-2.06 |
| 2026-10-17T21:51 | CRVUSDT | surge | STOP | 1.5 | -3.25% | $-2.09 |
| 2026-10-17T21:51 | AXLUSDT | surge | STOP | 2.5 | -3.25% | $-2.13 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-17T20:29 | RWUSDUSDT | bottom | 1 | 1.0001 | +0.01% |
| 2026-10-18T01:44 | TRXUSDT | bottom | 0.3338 | 0.3334 | -0.12% |
| 2026-10-18T03:05 | MSTRBUSDT | surge | 137.28 | 138.15 | +0.63% |
| 2026-10-18T03:21 | MORPHOUSDT | surge | 2.409 | 2.427 | +0.75% |
| 2026-10-18T06:53 | HBARUSDT | surge | 0.08749 | 0.08862 | +1.29% |
| 2026-10-18T09:43 | MEGAUSDT | surge | 0.04547 | 0.04451 | -2.11% |
| 2026-10-18T10:17 | ALTUSDT | bottom | 0.00843 | 0.00843 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
