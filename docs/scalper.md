# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-31T15:26:04+00:00 · runs 4868 · equity **$601.58** (-39.84%) · cash $0.00 · open 10/10 · round trips 1707

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.30%/trade · realized $-403.10 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1486 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 221 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-31T08:25 | SOPHUSDT | bottom | TARGET | 0.8 | +2.75% | $+1.53 |
| 2026-10-31T08:25 | GTCUSDT | surge | STOP | 2.5 | -3.25% | $-1.80 |
| 2026-10-31T08:09 | RADUSDT | surge | TARGET | 2.8 | +2.75% | $+1.53 |
| 2026-10-31T07:20 | PEPEUSDT | bottom | TARGET | 3.0 | +2.75% | $+1.53 |
| 2026-10-31T06:31 | SPKUSDT | surge | STOP | 0.0 | -3.25% | $-1.82 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T23:46 | PENDLEUSDT | surge | 1.848 | 1.877 | +1.57% |
| 2026-10-31T04:54 | ARBUSDT | bottom | 0.16 | 0.165 | +3.12% |
| 2026-10-31T07:36 | TIAUSDT | surge | 0.4772 | 0.4852 | +1.68% |
| 2026-10-31T08:25 | TRXUSDT | bottom | 0.3206 | 0.3137 | -2.15% |
| 2026-10-31T08:58 | LTCUSDT | bottom | 54.62 | 55.45 | +1.52% |
| 2026-10-31T09:35 | ZROUSDT | surge | 1.746 | 1.784 | +2.18% |
| 2026-10-31T10:40 | QNTUSDT | surge | 198.38 | 199.74 | +0.69% |
| 2026-10-31T14:30 | ZBTUSDT | surge | 0.0753 | 0.0753 | +0.00% |
| 2026-10-31T15:24 | AAVEUSDT | surge | 135.29 | 135.1 | -0.14% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
