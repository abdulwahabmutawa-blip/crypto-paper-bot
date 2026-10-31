# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-31T14:15:05+00:00 · runs 4863 · equity **$594.64** (-40.54%) · cash $0.00 · open 10/10 · round trips 1704

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-407.98 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1483 | 49% | -0.27% | 46% | 47% | 7% |
| bottom | 221 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-31T05:59 | SPKUSDT | surge | TARGET | 1.2 | +2.75% | $+1.53 |
| 2026-10-31T04:05 | SPKUSDT | surge | TARGET | 0.0 | +2.75% | $+1.52 |
| 2026-10-31T03:49 | OPUSDT | surge | STOP | 3.5 | -3.25% | $-1.81 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T23:46 | PENDLEUSDT | surge | 1.848 | 1.887 | +2.11% |
| 2026-10-31T04:54 | ARBUSDT | bottom | 0.16 | 0.1622 | +1.38% |
| 2026-10-31T07:36 | TIAUSDT | surge | 0.4772 | 0.4788 | +0.34% |
| 2026-10-31T08:25 | TRXUSDT | bottom | 0.3206 | 0.317 | -1.12% |
| 2026-10-31T08:58 | LTCUSDT | bottom | 54.62 | 55.12 | +0.92% |
| 2026-10-31T09:35 | ZROUSDT | surge | 1.746 | 1.72 | -1.49% |
| 2026-10-31T10:40 | QNTUSDT | surge | 198.38 | 200.32 | +0.98% |
| 2026-10-31T12:51 | MORPHOUSDT | surge | 2.196 | 2.209 | +0.59% |
| 2026-10-31T13:57 | ZBTUSDT | surge | 0.0733 | 0.074 | +0.95% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
