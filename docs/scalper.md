# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-27T04:17:29+00:00 · runs 6844 · equity **$498.63** (-50.14%) · cash $0.00 · open 10/10 · round trips 2250

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-503.09 · worst day $-50.94 · trades/day 26.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1932 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 318 | 43% | -0.46% | 38% | 44% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-27T04:15 | KORUBUSDT | surge | TARGET | 1.5 | +2.75% | $+1.24 |
| 2026-11-27T03:58 | SENTUSDT | surge | TARGET | 9.0 | +2.75% | $+1.28 |
| 2026-11-27T03:42 | SNDKBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.19 |
| 2026-11-27T02:34 | TRUMPUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.21 |
| 2026-11-27T02:34 | TIAUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.21 |
| 2026-11-27T02:34 | SKYUSDT | surge | TARGET | 11.0 | +2.75% | $+1.20 |
| 2026-11-27T01:44 | SOPHUSDT | surge | STOP | 0.5 | -3.25% | $-1.46 |
| 2026-11-27T00:54 | EWYBUSDT | surge | TIME | 24.0 | -1.35% | $-0.61 |
| 2026-11-26T23:46 | SAGAUSDT | surge | STOP | 4.5 | -3.25% | $-1.47 |
| 2026-11-26T23:46 | SUPERUSDT | surge | TIME | 24.0 | -1.10% | $-0.49 |
| 2026-11-26T19:32 | FETUSDT | surge | TARGET | 1.0 | +2.75% | $+1.26 |
| 2026-11-26T18:58 | SENTUSDT | surge | TARGET | 3.0 | +2.75% | $+1.25 |
| 2026-11-26T18:42 | SAGAUSDT | surge | TARGET | 3.2 | +2.75% | $+1.21 |
| 2026-11-26T18:25 | SEIUSDT | surge | TARGET | 0.0 | +2.75% | $+1.21 |
| 2026-11-26T18:25 | WIFUSDT | surge | TARGET | 2.0 | +2.75% | $+1.24 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-26T15:19 | TRXUSDT | bottom | 0.3026 | 0.3051 | +0.83% |
| 2026-11-26T17:51 | THETAUSDT | surge | 0.1357 | 0.1354 | -0.22% |
| 2026-11-26T18:25 | WIFUSDT | surge | 0.1387 | 0.1375 | -0.87% |
| 2026-11-26T19:32 | DOTUSDT | surge | 0.676 | 0.688 | +1.78% |
| 2026-11-27T02:34 | QQQBUSDT | surge | 647.34 | 650.22 | +0.44% |
| 2026-11-27T02:34 | TQQQBUSDT | surge | 48.01 | 48.63 | +1.29% |
| 2026-11-27T03:42 | SKHYBUSDT | surge | 117.38 | 117.69 | +0.26% |
| 2026-11-27T03:58 | GOOGLBUSDT | surge | 279.91 | 280.63 | +0.26% |
| 2026-11-27T04:15 | SPCXBUSDT | surge | 133.15 | 133.15 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
