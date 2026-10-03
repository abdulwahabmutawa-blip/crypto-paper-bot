# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-03T16:09:53+00:00 · runs 2451 · equity **$864.02** (-13.60%) · cash $0.00 · open 10/10 · round trips 928

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 51% (break-even 54%) · mean -0.15%/trade · realized $-138.84 · worst day $-50.94 · trades/day 32.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 804 | 52% | -0.11% | 49% | 44% | 7% |
| bottom | 124 | 45% | -0.42% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-03T16:08 | SPCXBUSDT | surge | TIME | 24.0 | +0.92% | $+0.90 |
| 2026-10-03T15:50 | ARUSDT | surge | STOP | 3.0 | -3.25% | $-2.64 |
| 2026-10-03T15:33 | TSLABUSDT | surge | TIME | 24.0 | -0.32% | $-0.30 |
| 2026-10-03T14:59 | SUPERUSDT | surge | TARGET | 0.8 | +2.75% | $+2.30 |
| 2026-10-03T13:27 | SYNUSDT | surge | STOP | 5.2 | -3.25% | $-2.65 |
| 2026-10-03T13:27 | DODOUSDT | surge | TIME | 24.0 | -1.64% | $-1.47 |
| 2026-10-03T12:00 | RAYUSDT | surge | TARGET | 3.0 | +2.75% | $+2.17 |
| 2026-10-03T08:31 | LPTUSDT | surge | STOP | 2.8 | -3.25% | $-2.65 |
| 2026-10-03T07:54 | AXSUSDT | surge | STOP | 4.0 | -3.25% | $-2.74 |
| 2026-10-03T04:21 | PYTHUSDT | surge | STOP | 2.8 | -3.25% | $-2.74 |
| 2026-10-03T01:28 | XPLUSDT | bottom | TARGET | 6.2 | +2.75% | $+2.29 |
| 2026-10-02T20:33 | NMRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.29 |
| 2026-10-02T18:54 | PEPEUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | FETUSDT | bottom | STOP | 0.8 | -3.25% | $-2.75 |
| 2026-10-02T18:54 | VTHOUSDT | surge | STOP | 0.8 | -3.25% | $-2.75 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-02T17:48 | CRCLBUSDT | bottom | 80.95 | 82.14 | +1.47% |
| 2026-10-02T18:54 | BNBUSDT | bottom | 761.25 | 777.48 | +2.13% |
| 2026-10-03T01:28 | SNDKBUSDT | bottom | 1718.8 | 1716.69 | -0.12% |
| 2026-10-03T03:31 | INJUSDT | surge | 7.685 | 7.709 | +0.31% |
| 2026-10-03T14:01 | STXUSDT | surge | 0.3736 | 0.3785 | +1.31% |
| 2026-10-03T14:59 | IOUSDT | surge | 0.1665 | 0.1679 | +0.84% |
| 2026-10-03T15:33 | AVAUSDT | surge | 0.2744 | 0.2682 | -2.26% |
| 2026-10-03T15:50 | MORPHOUSDT | surge | 2.724 | 2.715 | -0.33% |
| 2026-10-03T16:08 | SUPERUSDT | surge | 0.2655 | 0.266 | +0.19% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
