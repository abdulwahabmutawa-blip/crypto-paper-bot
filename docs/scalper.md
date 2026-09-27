# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-27T16:40:11+00:00 · runs 1941 · equity **$930.72** (-6.93%) · cash $0.00 · open 10/10 · round trips 700

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.09%/trade · realized $-66.11 · worst day $-50.94 · trades/day 30.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 598 | 53% | -0.02% | 50% | 43% | 7% |
| bottom | 102 | 44% | -0.46% | 40% | 45% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-27T16:22 | WUSDT | surge | TARGET | 0.5 | +2.75% | $+2.68 |
| 2026-09-27T16:05 | PUMPUSDT | surge | TARGET | 1.2 | +2.75% | $+2.61 |
| 2026-09-27T15:49 | REUSDT | surge | STOP | 10.8 | -3.25% | $-2.93 |
| 2026-09-27T15:33 | AMPUSDT | bottom | TARGET | 0.0 | +2.75% | $+2.61 |
| 2026-09-27T15:16 | ZECUSDT | surge | STOP | 15.0 | -3.25% | $-3.19 |
| 2026-09-27T14:43 | JASMYUSDT | surge | STOP | 0.0 | -3.25% | $-3.10 |
| 2026-09-27T14:43 | BCHUSDT | surge | STOP | 6.8 | -3.25% | $-3.27 |
| 2026-09-27T14:27 | JASMYUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-27T13:54 | XPLUSDT | bottom | STOP | 12.8 | -3.25% | $-3.13 |
| 2026-09-27T13:21 | ZROUSDT | surge | STOP | 4.8 | -3.25% | $-3.12 |
| 2026-09-27T12:58 | JASMYUSDT | surge | TARGET | 1.5 | +2.75% | $+2.47 |
| 2026-09-27T11:12 | DASHUSDT | surge | STOP | 18.5 | -3.25% | $-3.02 |
| 2026-09-27T10:01 | MOVRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.55 |
| 2026-09-27T09:26 | STXUSDT | surge | STOP | 3.5 | -3.25% | $-3.12 |
| 2026-09-27T08:15 | PYTHUSDT | surge | TARGET | 2.2 | +2.75% | $+2.57 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-26T20:51 | TRXUSDT | bottom | 0.335 | 0.3338 | -0.36% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.125 | +0.27% |
| 2026-09-27T10:01 | SOLUSDT | surge | 124.47 | 121.91 | -2.06% |
| 2026-09-27T12:58 | MMTUSDT | surge | 0.1833 | 0.1814 | -1.04% |
| 2026-09-27T13:54 | OPNUSDT | surge | 0.0574 | 0.0561 | -2.26% |
| 2026-09-27T14:43 | CAKEUSDT | surge | 2.844 | 2.793 | -1.79% |
| 2026-09-27T15:49 | HYPEUSDT | bottom | 91.19 | 91.26 | +0.08% |
| 2026-09-27T16:05 | AMPUSDT | bottom | 0.000632 | 0.00065 | +2.85% |
| 2026-09-27T16:22 | XVGUSDT | surge | 0.003598 | 0.003626 | +0.78% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
