# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-09T15:12:34+00:00 · runs 2956 · equity **$765.85** (-23.42%) · cash $0.00 · open 10/10 · round trips 1109

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 50% (break-even 54%) · mean -0.23%/trade · realized $-229.53 · worst day $-50.94 · trades/day 31.7

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 971 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 138 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-09T14:35 | CRCLBUSDT | surge | TARGET | 0.0 | +2.75% | $+2.09 |
| 2026-10-09T14:35 | API3USDT | surge | TARGET | 0.0 | +2.75% | $+2.09 |
| 2026-10-09T14:17 | SUSDT | surge | STOP | 3.8 | -3.25% | $-2.50 |
| 2026-10-09T14:17 | API3USDT | surge | TARGET | 4.0 | +2.75% | $+2.07 |
| 2026-10-09T14:00 | PROMUSDT | surge | STOP | 3.8 | -3.25% | $-2.45 |
| 2026-10-09T14:00 | APTUSDT | surge | STOP | 5.0 | -3.25% | $-2.42 |
| 2026-10-09T12:49 | GRAMUSDT | surge | TARGET | 2.2 | +2.75% | $+2.11 |
| 2026-10-09T10:29 | ZKUSDT | surge | TARGET | 0.2 | +2.75% | $+2.07 |
| 2026-10-09T10:29 | ONTUSDT | surge | TARGET | 8.0 | +2.75% | $+2.04 |
| 2026-10-09T10:06 | SUSDT | surge | TARGET | 1.0 | +2.75% | $+2.04 |
| 2026-10-09T10:06 | BEAMXUSDT | surge | TARGET | 1.5 | +2.75% | $+2.01 |
| 2026-10-09T10:06 | API3USDT | surge | TARGET | 1.8 | +2.75% | $+2.01 |
| 2026-10-09T08:58 | MUBARAKUSDT | surge | STOP | 11.8 | -3.25% | $-2.49 |
| 2026-10-09T08:41 | NMRUSDT | surge | STOP | 0.5 | -3.25% | $-2.51 |
| 2026-10-09T08:24 | ONEUSDT | surge | STOP | 5.8 | -3.25% | $-2.46 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-08T20:37 | FILUSDT | surge | 1.0745 | 1.07 | -0.42% |
| 2026-10-08T20:37 | TRXUSDT | bottom | 0.333 | 0.3329 | -0.03% |
| 2026-10-09T00:52 | ALGOUSDT | bottom | 0.1177 | 0.1159 | -1.53% |
| 2026-10-09T07:50 | ATOMUSDT | surge | 1.954 | 1.951 | -0.15% |
| 2026-10-09T12:49 | GRAMUSDT | surge | 1.493 | 1.475 | -1.21% |
| 2026-10-09T14:00 | TSLABUSDT | surge | 385.25 | 385.75 | +0.13% |
| 2026-10-09T14:00 | ZKUSDT | surge | 0.01318 | 0.01334 | +1.21% |
| 2026-10-09T14:35 | API3USDT | surge | 0.3326 | 0.3257 | -2.07% |
| 2026-10-09T14:35 | CRCLBUSDT | surge | 86.8 | 85.2 | -1.84% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
