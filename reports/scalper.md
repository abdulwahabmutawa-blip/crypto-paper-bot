# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-20T04:08:31+00:00 · runs 1278 · equity **$939.21** (-6.08%) · cash $0.00 · open 10/10 · round trips 455

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.12%/trade · realized $-58.01 · worst day $-50.94 · trades/day 28.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 372 | 53% | -0.04% | 49% | 42% | 9% |
| bottom | 83 | 42% | -0.49% | 41% | 46% | 13% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-20T03:50 | ACEUSDT | surge | TARGET | 18.8 | +2.75% | $+3.04 |
| 2026-09-20T03:34 | ZKUSDT | surge | TARGET | 0.0 | +2.75% | $+2.52 |
| 2026-09-20T03:01 | CTSIUSDT | surge | STOP | 0.5 | -3.25% | $-2.93 |
| 2026-09-20T03:01 | KAITOUSDT | surge | STOP | 1.0 | -3.25% | $-3.14 |
| 2026-09-20T03:01 | SEIUSDT | surge | STOP | 3.5 | -3.25% | $-2.99 |
| 2026-09-20T03:01 | VETUSDT | surge | STOP | 18.5 | -3.25% | $-3.25 |
| 2026-09-20T02:44 | ALGOUSDT | surge | STOP | 1.8 | -3.25% | $-3.24 |
| 2026-09-20T02:44 | TAOUSDT | surge | STOP | 14.2 | -3.25% | $-2.90 |
| 2026-09-20T02:28 | UNIUSDT | bottom | TARGET | 4.8 | +2.75% | $+2.42 |
| 2026-09-20T01:55 | HOMEUSDT | surge | STOP | 0.8 | -3.25% | $-3.24 |
| 2026-09-20T00:50 | ALGOUSDT | surge | TARGET | 0.2 | +2.75% | $+2.67 |
| 2026-09-20T00:50 | ZILUSDT | surge | TARGET | 0.2 | +2.75% | $+2.67 |
| 2026-09-20T00:17 | HOMEUSDT | surge | TARGET | 3.8 | +2.75% | $+2.70 |
| 2026-09-20T00:17 | 0GUSDT | surge | TARGET | 6.5 | +2.75% | $+2.50 |
| 2026-09-19T22:13 | FLOKIUSDT | surge | STOP | 2.0 | -3.25% | $-3.09 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-19T21:56 | SOLUSDT | bottom | 110.33 | 108.8 | -1.39% |
| 2026-09-19T21:56 | DASHUSDT | bottom | 57.97 | 56.98 | -1.71% |
| 2026-09-20T02:44 | XRPUSDT | bottom | 1.3972 | 1.382 | -1.09% |
| 2026-09-20T03:34 | LDOUSDT | surge | 0.4205 | 0.4142 | -1.50% |
| 2026-09-20T03:50 | ZKUSDT | surge | 0.01186 | 0.01192 | +0.51% |
| 2026-09-20T03:50 | ACEUSDT | surge | 0.1629 | 0.1639 | +0.61% |
| 2026-09-20T03:50 | ARBUSDT | surge | 0.2148 | 0.217 | +1.02% |
| 2026-09-20T03:50 | STXUSDT | surge | 0.3194 | 0.3218 | +0.75% |
| 2026-09-20T04:07 | ARKUSDT | surge | 0.1587 | 0.1583 | -0.25% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
