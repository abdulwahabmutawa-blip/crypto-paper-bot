# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-18T13:26:21+00:00 · runs 3724 · equity **$662.75** (-33.72%) · cash $63.40 · open 9/10 · round trips 1375

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-335.25 · worst day $-50.94 · trades/day 31.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1202 | 49% | -0.28% | 46% | 47% | 7% |
| bottom | 173 | 45% | -0.41% | 39% | 43% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-18T02:16 | RSRUSDT | surge | STOP | 0.5 | -3.25% | $-2.06 |
| 2026-10-18T02:00 | LSKUSDT | surge | STOP | 3.0 | -3.25% | $-2.06 |
| 2026-10-18T01:44 | UNIUSDT | bottom | TARGET | 8.8 | +2.75% | $+1.80 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-17T20:29 | RWUSDUSDT | bottom | 1 | 1 | +0.00% |
| 2026-10-18T01:44 | TRXUSDT | bottom | 0.3338 | 0.3327 | -0.33% |
| 2026-10-18T03:05 | MSTRBUSDT | surge | 137.28 | 137.17 | -0.08% |
| 2026-10-18T03:21 | MORPHOUSDT | surge | 2.409 | 2.371 | -1.58% |
| 2026-10-18T06:53 | HBARUSDT | surge | 0.08749 | 0.08827 | +0.89% |
| 2026-10-18T10:17 | ALTUSDT | bottom | 0.00843 | 0.00836 | -0.83% |
| 2026-10-18T12:17 | SUSDT | surge | 0.05592 | 0.05511 | -1.45% |
| 2026-10-18T13:06 | OGNUSDT | surge | 0.03191 | 0.03198 | +0.22% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
