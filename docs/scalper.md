# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T23:36:11+00:00 · runs 2218 · equity **$870.80** (-12.92%) · cash $0.00 · open 10/10 · round trips 836

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-121.65 · worst day $-50.94 · trades/day 32.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 718 | 52% | -0.11% | 49% | 44% | 7% |
| bottom | 118 | 46% | -0.36% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-30T13:37 | ENAUSDT | surge | TARGET | 0.2 | +2.75% | $+2.31 |
| 2026-09-30T13:19 | ASTERUSDT | surge | TARGET | 11.5 | +2.75% | $+2.45 |
| 2026-09-30T13:02 | PROMUSDT | surge | STOP | 0.5 | -3.25% | $-2.77 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.384 | -0.07% |
| 2026-09-30T08:24 | AXSUSDT | surge | 1.166 | 1.152 | -1.20% |
| 2026-09-30T13:02 | ZENUSDT | surge | 7.433 | 7.354 | -1.06% |
| 2026-09-30T14:11 | GOOGLBUSDT | surge | 350.03 | 349.27 | -0.22% |
| 2026-09-30T14:29 | SPCXBUSDT | surge | 151.73 | 150.84 | -0.59% |
| 2026-09-30T15:20 | PROMUSDT | surge | 6.599 | 6.457 | -2.15% |
| 2026-09-30T15:38 | SNXXBUSDT | surge | 16.85 | 16.68 | -1.01% |
| 2026-09-30T20:24 | HUMAUSDT | surge | 0.03244 | 0.03232 | -0.37% |
| 2026-09-30T22:42 | STXUSDT | surge | 0.3791 | 0.3721 | -1.85% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
