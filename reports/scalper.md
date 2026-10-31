# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-31T09:20:21+00:00 · runs 4845 · equity **$586.12** (-41.39%) · cash $222.18 · open 6/10 · round trips 1700

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.31%/trade · realized $-414.17 · worst day $-50.94 · trades/day 29.8

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1479 | 48% | -0.28% | 46% | 47% | 7% |
| bottom | 221 | 43% | -0.52% | 36% | 45% | 19% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-10-31T02:02 | HAEDALUSDT | surge | TARGET | 1.5 | +2.75% | $+1.53 |
| 2026-10-31T00:54 | TRXUSDT | bottom | STOP | 17.8 | -3.25% | $-1.81 |
| 2026-10-30T23:46 | OPUSDT | surge | TARGET | 0.2 | +2.75% | $+1.52 |
| 2026-10-30T15:50 | XPLUSDT | surge | TARGET | 8.8 | +2.75% | $+1.53 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-30T23:46 | PENDLEUSDT | surge | 1.848 | 1.848 | +0.00% |
| 2026-10-31T04:54 | ARBUSDT | bottom | 0.16 | 0.1622 | +1.38% |
| 2026-10-31T07:36 | TIAUSDT | surge | 0.4772 | 0.4757 | -0.31% |
| 2026-10-31T08:25 | TRXUSDT | bottom | 0.3206 | 0.3181 | -0.78% |
| 2026-10-31T08:58 | LTCUSDT | bottom | 54.62 | 54.76 | +0.26% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
