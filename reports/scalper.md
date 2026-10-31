# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-31T16:16:20+00:00 · runs 4871 · equity **$602.05** (-39.79%) · cash $0.00 · open 10/10 · round trips 1712

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-402.28 · worst day $-50.94 · trades/day 30.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1489 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 223 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-31T16:14 | ZBTUSDT | surge | STOP | 1.5 | -3.25% | $-1.96 |
| 2026-10-31T16:14 | TRXUSDT | bottom | STOP | 7.8 | -3.25% | $-1.81 |
| 2026-10-31T16:14 | TIAUSDT | surge | TARGET | 8.5 | +2.75% | $+1.53 |
| 2026-10-31T15:57 | ZROUSDT | surge | TARGET | 6.0 | +2.75% | $+1.53 |
| 2026-10-31T15:41 | ARBUSDT | bottom | TARGET | 10.5 | +2.75% | $+1.53 |
| 2026-10-31T15:24 | MORPHOUSDT | surge | TARGET | 0.0 | +2.75% | $+1.66 |
| 2026-10-31T15:07 | MORPHOUSDT | surge | TARGET | 2.0 | +2.75% | $+1.61 |
| 2026-10-31T14:30 | ZBTUSDT | surge | TARGET | 0.5 | +2.75% | $+1.61 |
| 2026-10-31T13:57 | EDENUSDT | surge | TARGET | 1.5 | +2.75% | $+1.57 |
| 2026-10-31T12:51 | STXUSDT | surge | TARGET | 0.0 | +2.75% | $+1.57 |
| 2026-10-31T12:35 | STXUSDT | surge | TARGET | 2.8 | +2.75% | $+1.53 |
| 2026-10-31T12:02 | EDENUSDT | surge | TARGET | 0.8 | +2.75% | $+1.53 |
| 2026-10-31T09:18 | RADUSDT | surge | TARGET | 1.0 | +2.75% | $+1.55 |
| 2026-10-31T08:58 | EDENUSDT | surge | STOP | 0.0 | -3.25% | $-1.81 |
| 2026-10-31T08:58 | HYPEUSDT | bottom | STOP | 9.2 | -3.25% | $-1.80 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T23:46 | PENDLEUSDT | surge | 1.848 | 1.887 | +2.11% |
| 2026-10-31T08:58 | LTCUSDT | bottom | 54.62 | 55.53 | +1.67% |
| 2026-10-31T10:40 | QNTUSDT | surge | 198.38 | 202.25 | +1.95% |
| 2026-10-31T15:24 | AAVEUSDT | surge | 135.29 | 136.24 | +0.70% |
| 2026-10-31T15:41 | STRKUSDT | surge | 0.04582 | 0.04584 | +0.04% |
| 2026-10-31T15:57 | NMRUSDT | surge | 10.19 | 10.26 | +0.69% |
| 2026-10-31T16:14 | MARSCOINUSDT | surge | 0.054 | 0.0541 | +0.19% |
| 2026-10-31T16:14 | ETHFIUSDT | surge | 0.6381 | 0.6389 | +0.13% |
| 2026-10-31T16:14 | NEARUSDT | surge | 4.479 | 4.49 | +0.25% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
