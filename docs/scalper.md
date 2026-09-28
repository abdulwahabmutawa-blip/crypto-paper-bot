# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-28T03:02:56+00:00 · runs 1980 · equity **$934.75** (-6.52%) · cash $0.00 · open 10/10 · round trips 723

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 52% (break-even 54%) · mean -0.08%/trade · realized $-59.71 · worst day $-50.94 · trades/day 30.1

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 617 | 53% | -0.02% | 50% | 43% | 7% |
| bottom | 106 | 44% | -0.42% | 41% | 44% | 15% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-28T03:01 | JASMYUSDT | surge | STOP | 2.0 | -3.25% | $-2.84 |
| 2026-09-28T02:12 | NMRUSDT | surge | STOP | 0.8 | -3.25% | $-3.40 |
| 2026-09-28T02:12 | SOLUSDT | surge | STOP | 15.8 | -3.25% | $-3.10 |
| 2026-09-28T01:38 | SKYUSDT | surge | STOP | 0.8 | -3.25% | $-3.40 |
| 2026-09-28T01:06 | NMRUSDT | surge | TARGET | 0.8 | +2.75% | $+2.80 |
| 2026-09-28T01:06 | PUMPUSDT | surge | TARGET | 3.0 | +2.75% | $+2.79 |
| 2026-09-28T00:49 | VTHOUSDT | bottom | STOP | 3.5 | -3.25% | $-2.94 |
| 2026-09-28T00:33 | SKYUSDT | surge | TARGET | 0.2 | +2.75% | $+2.80 |
| 2026-09-28T00:12 | METUSDT | surge | TARGET | 1.5 | +2.75% | $+2.72 |
| 2026-09-28T00:12 | SKYUSDT | surge | TARGET | 1.5 | +2.75% | $+2.72 |
| 2026-09-27T22:15 | NOMUSDT | surge | TARGET | 0.0 | +2.75% | $+2.79 |
| 2026-09-27T22:15 | PENDLEUSDT | surge | STOP | 3.5 | -3.25% | $-3.15 |
| 2026-09-27T21:58 | JASMYUSDT | surge | TARGET | 1.8 | +2.75% | $+2.75 |
| 2026-09-27T21:58 | PUMPUSDT | surge | TARGET | 3.0 | +2.75% | $+2.69 |
| 2026-09-27T21:08 | TRXUSDT | bottom | TIME | 24.0 | -0.64% | $-0.58 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-27T05:36 | JSTUSDT | surge | 0.12466 | 0.12769 | +2.43% |
| 2026-09-27T12:58 | MMTUSDT | surge | 0.1833 | 0.1799 | -1.85% |
| 2026-09-27T14:43 | CAKEUSDT | surge | 2.844 | 2.767 | -2.71% |
| 2026-09-27T15:49 | HYPEUSDT | bottom | 91.19 | 90.22 | -1.06% |
| 2026-09-28T01:06 | PUMPUSDT | surge | 0.005169 | 0.005181 | +0.23% |
| 2026-09-28T01:38 | IMXUSDT | surge | 0.1895 | 0.187 | -1.32% |
| 2026-09-28T02:12 | IOTAUSDT | surge | 0.0526 | 0.0525 | -0.19% |
| 2026-09-28T02:12 | HBARUSDT | surge | 0.09647 | 0.09491 | -1.62% |
| 2026-09-28T03:01 | BABYUSDT | bottom | 0.01357 | 0.0136 | +0.22% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
