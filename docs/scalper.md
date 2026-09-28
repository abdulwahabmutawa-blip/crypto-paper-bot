# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-28T06:40:46+00:00 · runs 1994 · equity **$910.49** (-8.95%) · cash $275.69 · open 7/10 · round trips 731

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.10%/trade · realized $-78.85 · worst day $-50.94 · trades/day 30.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 625 | 53% | -0.05% | 50% | 43% | 7% |
| bottom | 106 | 44% | -0.42% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28T05:45 | ONDOUSDT | surge | STOP | 1.0 | -3.25% | $-2.97 |
| 2026-09-28T05:45 | SEIUSDT | surge | STOP | 1.8 | -3.25% | $-3.07 |
| 2026-09-28T05:45 | MMTUSDT | surge | STOP | 16.8 | -3.25% | $-3.00 |
| 2026-09-28T05:45 | JSTUSDT | surge | TIME | 24.0 | +2.60% | $+2.49 |
| 2026-09-28T04:40 | SKYUSDT | surge | STOP | 0.5 | -3.25% | $-3.07 |
| 2026-09-28T03:34 | IOTAUSDT | surge | STOP | 1.2 | -3.25% | $-3.14 |
| 2026-09-28T03:34 | IMXUSDT | surge | STOP | 1.8 | -3.25% | $-3.29 |
| 2026-09-28T03:34 | CAKEUSDT | surge | STOP | 12.8 | -3.25% | $-3.08 |
| 2026-09-28T03:01 | JASMYUSDT | surge | STOP | 2.0 | -3.25% | $-2.84 |
| 2026-09-28T02:12 | NMRUSDT | surge | STOP | 0.8 | -3.25% | $-3.40 |
| 2026-09-28T02:12 | SOLUSDT | surge | STOP | 15.8 | -3.25% | $-3.10 |
| 2026-09-28T01:38 | SKYUSDT | surge | STOP | 0.8 | -3.25% | $-3.40 |
| 2026-09-28T01:06 | NMRUSDT | surge | TARGET | 0.8 | +2.75% | $+2.80 |
| 2026-09-28T01:06 | PUMPUSDT | surge | TARGET | 3.0 | +2.75% | $+2.79 |
| 2026-09-28T00:49 | VTHOUSDT | bottom | STOP | 3.5 | -3.25% | $-2.94 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-27T15:49 | HYPEUSDT | bottom | 91.19 | 88.97 | -2.43% |
| 2026-09-28T01:06 | PUMPUSDT | surge | 0.005169 | 0.004911 | -4.99% |
| 2026-09-28T02:12 | HBARUSDT | surge | 0.09647 | 0.09692 | +0.47% |
| 2026-09-28T03:01 | BABYUSDT | bottom | 0.01357 | 0.01339 | -1.33% |
| 2026-09-28T03:34 | MSTRBUSDT | bottom | 156.65 | 155.49 | -0.74% |
| 2026-09-28T06:23 | PROMUSDT | surge | 6.433 | 6.296 | -2.13% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
