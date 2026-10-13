# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T10:53:40+00:00 · runs 3280 · equity **$748.02** (-25.20%) · cash $0.00 · open 10/10 · round trips 1224

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-247.29 · worst day $-50.94 · trades/day 31.4

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1074 | 50% | -0.19% | 47% | 45% | 7% |
| bottom | 150 | 44% | -0.49% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-13T09:41 | BATUSDT | surge | STOP | 0.8 | -3.25% | $-2.40 |
| 2026-10-13T09:24 | DUSKUSDT | surge | STOP | 0.2 | -3.25% | $-2.40 |
| 2026-10-13T08:30 | ZAMAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.01 |
| 2026-10-13T07:09 | DODOUSDT | surge | TARGET | 0.5 | +2.75% | $+2.01 |
| 2026-10-13T05:23 | XAIUSDT | surge | STOP | 0.5 | -3.25% | $-2.39 |
| 2026-10-13T02:14 | ZROUSDT | bottom | TARGET | 0.2 | +2.75% | $+2.00 |
| 2026-10-13T01:57 | SKLUSDT | surge | TARGET | 0.0 | +2.75% | $+2.00 |
| 2026-10-13T00:14 | POLUSDT | bottom | STOP | 1.2 | -3.25% | $-2.35 |
| 2026-10-13T00:14 | AVAXUSDT | bottom | STOP | 2.0 | -3.25% | $-2.34 |
| 2026-10-13T00:14 | RENDERUSDT | surge | STOP | 3.2 | -3.25% | $-2.41 |
| 2026-10-12T23:38 | SOXSBUSDT | surge | TARGET | 7.0 | +2.75% | $+2.16 |
| 2026-10-12T22:45 | HYPEUSDT | bottom | STOP | 8.8 | -3.25% | $-2.45 |
| 2026-10-12T22:10 | FETUSDT | bottom | STOP | 7.0 | -3.25% | $-2.29 |
| 2026-10-12T21:52 | AAVEUSDT | bottom | STOP | 7.8 | -3.25% | $-2.45 |
| 2026-10-12T20:40 | BEAMXUSDT | surge | STOP | 0.5 | -3.25% | $-2.44 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 163.32 | -1.73% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.13976 | -0.16% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3293 | -0.18% |
| 2026-10-13T01:39 | SOXSBUSDT | surge | 39.02 | 39.16 | +0.36% |
| 2026-10-13T07:09 | PROMUSDT | surge | 5.304 | 5.217 | -1.64% |
| 2026-10-13T08:30 | ZAMAUSDT | surge | 0.08124 | 0.08116 | -0.10% |
| 2026-10-13T08:49 | TIAUSDT | surge | 0.609 | 0.6063 | -0.44% |
| 2026-10-13T10:16 | RSRUSDT | bottom | 0.002017 | 0.002023 | +0.30% |
| 2026-10-13T10:51 | KAIAUSDT | surge | 0.0494 | 0.048 | -2.83% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
