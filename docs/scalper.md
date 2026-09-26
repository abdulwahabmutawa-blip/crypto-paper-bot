# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-26T17:26:53+00:00 · runs 1857 · equity **$945.88** (-5.41%) · cash $0.00 · open 10/10 · round trips 661

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-55.74 · worst day $-50.94 · trades/day 30.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 563 | 54% | -0.01% | 50% | 42% | 8% |
| bottom | 98 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-26T17:08 | SKHYBUSDT | surge | TIME | 24.0 | +0.05% | $+0.05 |
| 2026-09-26T16:36 | ZKUSDT | surge | TARGET | 21.8 | +2.75% | $+2.47 |
| 2026-09-26T16:36 | KORUBUSDT | surge | TIME | 24.0 | -0.39% | $-0.38 |
| 2026-09-26T16:19 | SPELLUSDT | surge | STOP | 0.2 | -3.25% | $-3.12 |
| 2026-09-26T15:46 | TNSRUSDT | surge | STOP | 4.0 | -3.25% | $-3.23 |
| 2026-09-26T15:13 | TLMUSDT | surge | STOP | 0.8 | -3.25% | $-3.02 |
| 2026-09-26T14:19 | TLMUSDT | surge | TARGET | 0.5 | +2.75% | $+2.49 |
| 2026-09-26T13:30 | RESOLVUSDT | surge | STOP | 1.5 | -3.25% | $-3.04 |
| 2026-09-26T11:52 | VELODROMEUSDT | surge | STOP | 1.5 | -3.25% | $-3.14 |
| 2026-09-26T11:35 | SPELLUSDT | surge | TARGET | 0.0 | +2.75% | $+2.66 |
| 2026-09-26T11:19 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.59 |
| 2026-09-26T10:13 | QNTUSDT | surge | TARGET | 0.2 | +2.75% | $+2.59 |
| 2026-09-26T09:57 | ACEUSDT | surge | TARGET | 0.2 | +2.75% | $+2.46 |
| 2026-09-26T09:57 | DOTUSDT | surge | STOP | 8.0 | -3.25% | $-3.24 |
| 2026-09-26T09:40 | PROMUSDT | surge | STOP | 2.0 | -3.25% | $-3.26 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T04:13 | SKYUSDT | surge | 0.07767 | 0.07789 | +0.28% |
| 2026-09-26T04:45 | INJUSDT | bottom | 7.814 | 7.741 | -0.93% |
| 2026-09-26T06:39 | BABYUSDT | surge | 0.01403 | 0.01409 | +0.43% |
| 2026-09-26T09:40 | STXUSDT | surge | 0.3439 | 0.3467 | +0.81% |
| 2026-09-26T15:13 | OPGUSDT | surge | 0.1428 | 0.1395 | -2.31% |
| 2026-09-26T16:19 | DASHUSDT | surge | 71.61 | 72.65 | +1.45% |
| 2026-09-26T16:36 | ESPUSDT | surge | 0.1039 | 0.1062 | +2.21% |
| 2026-09-26T16:36 | ZENUSDT | surge | 7.968 | 7.896 | -0.90% |
| 2026-09-26T17:08 | KMNOUSDT | surge | 0.04944 | 0.04972 | +0.57% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
