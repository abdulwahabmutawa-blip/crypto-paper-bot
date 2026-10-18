# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-18T15:04:23+00:00 · runs 3730 · equity **$657.21** (-34.28%) · cash $247.77 · open 6/10 · round trips 1378

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-341.44 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1205 | 48% | -0.28% | 46% | 47% | 7% |
| bottom | 173 | 45% | -0.41% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-18T14:14 | OGNUSDT | surge | STOP | 0.8 | -3.25% | $-2.05 |
| 2026-10-18T14:14 | MORPHOUSDT | surge | STOP | 10.8 | -3.25% | $-2.02 |
| 2026-10-18T13:57 | SUSDT | surge | STOP | 1.2 | -3.25% | $-2.12 |
| 2026-10-18T13:24 | MEGAUSDT | surge | STOP | 3.5 | -3.25% | $-2.13 |
| 2026-10-18T12:50 | ERAUSDT | surge | STOP | 0.8 | -3.25% | $-2.12 |
| 2026-10-18T11:45 | ERAUSDT | surge | TARGET | 0.2 | +2.75% | $+1.77 |
| 2026-10-18T11:28 | AMPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.75 |
| 2026-10-18T10:34 | SENTUSDT | surge | STOP | 0.2 | -3.25% | $-2.10 |
| 2026-10-18T10:00 | OSMOUSDT | surge | STOP | 0.5 | -3.25% | $-2.10 |
| 2026-10-18T09:43 | XLMUSDT | bottom | TIME | 24.0 | -0.70% | $-0.47 |
| 2026-10-18T09:26 | GLMRUSDT | surge | TARGET | 0.2 | +2.75% | $+1.75 |
| 2026-10-18T09:09 | AXLUSDT | surge | TARGET | 0.8 | +2.75% | $+1.75 |
| 2026-10-18T07:44 | GTCUSDT | surge | STOP | 0.8 | -3.25% | $-2.02 |
| 2026-10-18T06:53 | HBARUSDT | surge | TARGET | 10.2 | +2.75% | $+1.91 |
| 2026-10-18T02:48 | APEUSDT | surge | STOP | 1.0 | -3.25% | $-2.06 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-17T20:29 | RWUSDUSDT | bottom | 1 | 1.0001 | +0.01% |
| 2026-10-18T01:44 | TRXUSDT | bottom | 0.3338 | 0.332 | -0.54% |
| 2026-10-18T03:05 | MSTRBUSDT | surge | 137.28 | 135.6 | -1.22% |
| 2026-10-18T06:53 | HBARUSDT | surge | 0.08749 | 0.08817 | +0.78% |
| 2026-10-18T10:17 | ALTUSDT | bottom | 0.00843 | 0.00833 | -1.19% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
