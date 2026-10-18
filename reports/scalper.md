# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-18T08:54:04+00:00 · runs 3707 · equity **$667.61** (-33.24%) · cash $63.51 · open 9/10 · round trips 1366

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-333.33 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1194 | 48% | -0.28% | 46% | 47% | 7% |
| bottom | 172 | 45% | -0.41% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-17T21:51 | CAKEUSDT | surge | STOP | 7.2 | -3.25% | $-2.14 |
| 2026-10-17T21:34 | AUSDT | surge | STOP | 1.2 | -3.25% | $-2.09 |
| 2026-10-17T21:34 | NMRUSDT | surge | STOP | 6.0 | -3.25% | $-2.21 |
| 2026-10-17T20:29 | MUBUSDT | bottom | TIME | 24.0 | -0.29% | $-0.20 |
| 2026-10-17T20:29 | SOXSBUSDT | surge | TIME | 24.0 | -0.29% | $-0.20 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1773 | -1.01% |
| 2026-10-17T20:29 | RWUSDUSDT | bottom | 1 | 1 | +0.00% |
| 2026-10-18T01:44 | TRXUSDT | bottom | 0.3338 | 0.3331 | -0.21% |
| 2026-10-18T03:05 | MSTRBUSDT | surge | 137.28 | 136.63 | -0.47% |
| 2026-10-18T03:21 | MORPHOUSDT | surge | 2.409 | 2.385 | -1.00% |
| 2026-10-18T06:53 | HBARUSDT | surge | 0.08749 | 0.08818 | +0.79% |
| 2026-10-18T08:01 | AXLUSDT | surge | 0.0586 | 0.0597 | +1.88% |
| 2026-10-18T08:52 | GLMRUSDT | surge | 0.010304 | 0.01046 | +1.51% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
