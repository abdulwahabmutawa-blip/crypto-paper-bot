# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-28T00:51:09+00:00 · runs 1972 · equity **$951.28** (-4.87%) · cash $0.00 · open 10/10 · round trips 717

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.07%/trade · realized $-52.57 · worst day $-50.94 · trades/day 29.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 611 | 54% | -0.00% | 50% | 42% | 7% |
| bottom | 106 | 44% | -0.42% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28T00:49 | VTHOUSDT | bottom | STOP | 3.5 | -3.25% | $-2.94 |
| 2026-09-28T00:33 | SKYUSDT | surge | TARGET | 0.2 | +2.75% | $+2.80 |
| 2026-09-28T00:12 | METUSDT | surge | TARGET | 1.5 | +2.75% | $+2.72 |
| 2026-09-28T00:12 | SKYUSDT | surge | TARGET | 1.5 | +2.75% | $+2.72 |
| 2026-09-27T22:15 | NOMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.79 |
| 2026-09-27T22:15 | PENDLEUSDT | surge | STOP | 3.5 | -3.25% | $-3.15 |
| 2026-09-27T21:58 | JASMYUSDT | surge | TARGET | 1.8 | +2.75% | $+2.75 |
| 2026-09-27T21:58 | PUMPUSDT | surge | TARGET | 3.0 | +2.75% | $+2.69 |
| 2026-09-27T21:08 | TRXUSDT | bottom | TIME | 24.0 | -0.64% | $-0.58 |
| 2026-09-27T19:45 | ARUSDT | surge | STOP | 1.5 | -3.25% | $-3.36 |
| 2026-09-27T18:55 | ARBUSDT | bottom | TARGET | 1.8 | +2.75% | $+2.62 |
| 2026-09-27T18:33 | XVGUSDT | surge | STOP | 2.0 | -3.25% | $-3.26 |
| 2026-09-27T18:00 | NOMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.76 |
| 2026-09-27T17:44 | NOMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.69 |
| 2026-09-27T17:27 | NOMUSDT | surge | TARGET | 0.2 | +2.75% | $+2.62 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12653 | +1.50% |
| 2026-09-27T10:01 | SOLUSDT | surge | 124.47 | 122.57 | -1.53% |
| 2026-09-27T12:58 | MMTUSDT | surge | 0.1833 | 0.1849 | +0.87% |
| 2026-09-27T14:43 | CAKEUSDT | surge | 2.844 | 2.834 | -0.35% |
| 2026-09-27T15:49 | HYPEUSDT | bottom | 91.19 | 90.99 | -0.22% |
| 2026-09-27T21:58 | PUMPUSDT | surge | 0.005082 | 0.00519 | +2.13% |
| 2026-09-28T00:12 | NMRUSDT | surge | 10.36 | 10.6 | +2.32% |
| 2026-09-28T00:33 | SKYUSDT | surge | 0.08487 | 0.08332 | -1.83% |
| 2026-09-28T00:49 | JASMYUSDT | surge | 0.00534 | 0.0054 | +1.12% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
