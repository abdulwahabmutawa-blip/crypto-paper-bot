# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-05T10:37:29+00:00 · runs 2607 · equity **$848.10** (-15.19%) · cash $0.00 · open 10/10 · round trips 970

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.16%/trade · realized $-150.41 · worst day $-50.94 · trades/day 31.3

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 843 | 51% | -0.13% | 48% | 44% | 7% |
| bottom | 127 | 46% | -0.38% | 40% | 44% | 16% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-05T07:55 | GRTUSDT | surge | TARGET | 3.2 | +2.75% | $+2.15 |
| 2026-10-05T05:29 | SCRUSDT | surge | STOP | 0.2 | -3.25% | $-2.73 |
| 2026-10-05T04:55 | BROCCOLI714USDT | surge | STOP | 11.2 | -3.25% | $-2.64 |
| 2026-10-05T04:55 | ACEUSDT | surge | TARGET | 20.5 | +2.75% | $+2.39 |
| 2026-10-05T04:21 | ATOMUSDT | surge | STOP | 12.8 | -3.25% | $-2.63 |
| 2026-10-05T03:31 | VIRTUALUSDT | surge | TARGET | 8.8 | +2.75% | $+2.69 |
| 2026-10-05T03:31 | RUNEUSDT | surge | STOP | 9.8 | -3.25% | $-2.77 |
| 2026-10-05T00:04 | ROBOUSDT | surge | STOP | 7.8 | -3.25% | $-2.69 |
| 2026-10-04T23:15 | CHIPUSDT | surge | TARGET | 5.2 | +2.75% | $+2.34 |
| 2026-10-04T22:58 | ADAUSDT | surge | TARGET | 0.5 | +2.75% | $+2.25 |
| 2026-10-04T22:09 | GUNUSDT | surge | STOP | 10.5 | -3.25% | $-2.75 |
| 2026-10-04T21:53 | DODOUSDT | surge | TIME | 24.0 | -2.04% | $-1.74 |
| 2026-10-04T18:37 | SENTUSDT | surge | STOP | 2.8 | -3.25% | $-3.28 |
| 2026-10-04T17:59 | CHIPUSDT | surge | TARGET | 1.5 | +2.75% | $+2.28 |
| 2026-10-04T17:43 | BNBUSDT | surge | TIME | 24.0 | -0.35% | $-0.30 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-04T21:53 | SHIBUSDT | surge | 5.94e-06 | 5.95e-06 | +0.17% |
| 2026-10-04T22:58 | MSTRBUSDT | surge | 165.16 | 164.21 | -0.58% |
| 2026-10-04T23:15 | FLOKIUSDT | surge | 2.915e-05 | 2.948e-05 | +1.13% |
| 2026-10-05T00:04 | MEMEUSDT | surge | 0.000625 | 0.000618 | -1.12% |
| 2026-10-05T03:31 | ADAUSDT | surge | 0.2696 | 0.2736 | +1.48% |
| 2026-10-05T03:31 | LDOUSDT | surge | 0.4723 | 0.4693 | -0.64% |
| 2026-10-05T04:55 | PENGUUSDT | surge | 0.009789 | 0.00972 | -0.70% |
| 2026-10-05T05:29 | VIRTUALUSDT | surge | 0.8669 | 0.866 | -0.10% |
| 2026-10-05T07:55 | PENDLEUSDT | surge | 2.521 | 2.479 | -1.67% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
