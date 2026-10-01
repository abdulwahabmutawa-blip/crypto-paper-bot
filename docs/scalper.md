# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-01T03:51:45+00:00 · runs 2233 · equity **$873.41** (-12.66%) · cash $0.00 · open 10/10 · round trips 839

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-130.25 · worst day $-50.94 · trades/day 31.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 721 | 52% | -0.12% | 49% | 45% | 7% |
| bottom | 118 | 46% | -0.36% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-01T03:13 | PROMUSDT | surge | STOP | 11.8 | -3.25% | $-2.99 |
| 2026-10-01T00:15 | STXUSDT | surge | STOP | 1.5 | -3.25% | $-2.86 |
| 2026-10-01T00:15 | HUMAUSDT | surge | STOP | 3.8 | -3.25% | $-2.74 |
| 2026-09-30T22:42 | STXUSDT | surge | TARGET | 1.8 | +2.75% | $+2.36 |
| 2026-09-30T20:41 | STXUSDT | surge | TARGET | 0.8 | +2.75% | $+2.30 |
| 2026-09-30T20:24 | BLURUSDT | surge | STOP | 0.0 | -3.25% | $-2.83 |
| 2026-09-30T20:06 | ENSUSDT | surge | TIME | 24.0 | -1.67% | $-1.48 |
| 2026-09-30T19:32 | RUNEUSDT | surge | STOP | 1.0 | -3.25% | $-2.80 |
| 2026-09-30T18:23 | HYPEUSDT | surge | STOP | 0.8 | -3.25% | $-2.90 |
| 2026-09-30T17:21 | RUNEUSDT | surge | TARGET | 1.2 | +2.75% | $+2.39 |
| 2026-09-30T15:55 | CHZUSDT | surge | TIME | 24.0 | -0.50% | $-0.43 |
| 2026-09-30T15:38 | REZUSDT | surge | TARGET | 2.5 | +2.75% | $+2.41 |
| 2026-09-30T15:20 | SKHYBUSDT | surge | TIME | 24.0 | -1.19% | $-1.11 |
| 2026-09-30T14:29 | ARKMUSDT | surge | STOP | 1.0 | -3.25% | $-2.98 |
| 2026-09-30T14:11 | ENAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.37 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.518 | +0.86% |
| 2026-09-30T08:24 | AXSUSDT | surge | 1.166 | 1.164 | -0.17% |
| 2026-09-30T13:02 | ZENUSDT | surge | 7.433 | 7.463 | +0.40% |
| 2026-09-30T14:11 | GOOGLBUSDT | surge | 350.03 | 352.61 | +0.74% |
| 2026-09-30T14:29 | SPCXBUSDT | surge | 151.73 | 151.5 | -0.15% |
| 2026-09-30T15:38 | SNXXBUSDT | surge | 16.85 | 17.22 | +2.20% |
| 2026-10-01T00:15 | HYPEUSDT | surge | 90.39 | 89.14 | -1.38% |
| 2026-10-01T00:15 | SUSDT | surge | 0.04092 | 0.04101 | +0.22% |
| 2026-10-01T03:13 | SOXLBUSDT | surge | 150.96 | 152.97 | +1.33% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
