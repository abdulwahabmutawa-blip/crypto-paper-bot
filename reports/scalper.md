# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-30T19:51:29+00:00 · runs 2205 · equity **$871.03** (-12.90%) · cash $0.00 · open 10/10 · round trips 832

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.14%/trade · realized $-121.99 · worst day $-50.94 · trades/day 32.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 714 | 52% | -0.11% | 49% | 44% | 7% |
| bottom | 118 | 46% | -0.36% | 42% | 44% | 14% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-09-30T13:02 | CRCLBUSDT | bottom | TARGET | 18.8 | +2.75% | $+2.28 |
| 2026-09-30T12:45 | REZUSDT | surge | TARGET | 1.2 | +2.75% | $+2.34 |
| 2026-09-30T12:27 | RAREUSDT | surge | STOP | 2.0 | -3.25% | $-2.87 |
| 2026-09-30T11:22 | BERAUSDT | surge | STOP | 3.0 | -3.25% | $-2.86 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-29T19:59 | ENSUSDT | surge | 7.04 | 6.94 | -1.42% |
| 2026-09-30T05:38 | LINKUSDT | bottom | 14.394 | 14.245 | -1.04% |
| 2026-09-30T08:24 | AXSUSDT | surge | 1.166 | 1.138 | -2.40% |
| 2026-09-30T13:02 | ZENUSDT | surge | 7.433 | 7.242 | -2.57% |
| 2026-09-30T14:11 | GOOGLBUSDT | surge | 350.03 | 348.5 | -0.44% |
| 2026-09-30T14:29 | SPCXBUSDT | surge | 151.73 | 151.91 | +0.12% |
| 2026-09-30T15:20 | PROMUSDT | surge | 6.599 | 6.495 | -1.58% |
| 2026-09-30T15:38 | SNXXBUSDT | surge | 16.85 | 16.89 | +0.24% |
| 2026-09-30T19:32 | STXUSDT | surge | 0.3546 | 0.3588 | +1.18% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
