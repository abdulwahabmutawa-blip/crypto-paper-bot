# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-20T14:30:51+00:00 · runs 3902 · equity **$681.99** (-31.80%) · cash $0.00 · open 10/10 · round trips 1427

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.27%/trade · realized $-323.53 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1245 | 49% | -0.26% | 46% | 46% | 7% |
| bottom | 182 | 46% | -0.32% | 40% | 42% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-20T14:29 | SNDKBUSDT | bottom | TARGET | 3.2 | +2.75% | $+1.81 |
| 2026-10-20T14:29 | SKYUSDT | surge | TARGET | 11.0 | +2.75% | $+1.74 |
| 2026-10-20T14:29 | TRUMPUSDT | bottom | TARGET | 13.5 | +2.75% | $+1.77 |
| 2026-10-20T14:29 | HBARUSDT | bottom | TARGET | 17.8 | +2.75% | $+1.83 |
| 2026-10-20T13:36 | REZUSDT | surge | TARGET | 2.2 | +2.75% | $+1.82 |
| 2026-10-20T13:03 | WLDUSDT | surge | TARGET | 7.5 | +2.75% | $+1.70 |
| 2026-10-20T12:47 | BNCBUSDT | surge | TARGET | 23.0 | +2.75% | $+1.84 |
| 2026-10-20T11:09 | ATOMUSDT | surge | TIME | 24.0 | -1.40% | $-0.94 |
| 2026-10-20T10:53 | BEAMXUSDT | surge | TARGET | 14.8 | +2.75% | $+1.76 |
| 2026-10-20T10:21 | NEARUSDT | bottom | STOP | 9.5 | -3.25% | $-2.09 |
| 2026-10-20T05:18 | SUSDT | surge | STOP | 9.2 | -3.25% | $-2.08 |
| 2026-10-20T03:25 | BMTUSDT | surge | STOP | 0.5 | -3.25% | $-2.12 |
| 2026-10-20T02:36 | TQQQBUSDT | surge | TIME | 24.0 | -0.05% | $-0.03 |
| 2026-10-20T00:32 | WUSDT | surge | STOP | 1.8 | -3.25% | $-2.08 |
| 2026-10-20T00:32 | TSLABUSDT | surge | TIME | 24.0 | +1.84% | $+1.20 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-19T15:16 | GOOGLBUSDT | surge | 346.27 | 344.75 | -0.44% |
| 2026-10-20T10:21 | IOUSDT | surge | 0.1632 | 0.1653 | +1.29% |
| 2026-10-20T12:47 | TIAUSDT | surge | 0.6427 | 0.6527 | +1.56% |
| 2026-10-20T13:03 | BEAMXUSDT | surge | 0.003193 | 0.003208 | +0.47% |
| 2026-10-20T13:36 | BNCBUSDT | surge | 4.95 | 5.06 | +2.22% |
| 2026-10-20T14:29 | VELODROMEUSDT | surge | 0.03622 | 0.03739 | +3.23% |
| 2026-10-20T14:29 | RSRUSDT | surge | 0.00192 | 0.001927 | +0.36% |
| 2026-10-20T14:29 | ZROUSDT | surge | 1.986 | 1.975 | -0.55% |
| 2026-10-20T14:29 | CRCLBUSDT | surge | 85.2 | 85.3 | +0.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
