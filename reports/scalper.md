# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T13:31:03+00:00 · runs 3289 · equity **$743.83** (-25.62%) · cash $217.29 · open 7/10 · round trips 1230

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-252.88 · worst day $-50.94 · trades/day 31.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1079 | 50% | -0.20% | 47% | 45% | 7% |
| bottom | 151 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-13T13:28 | PROMUSDT | surge | STOP | 6.2 | -3.25% | $-2.39 |
| 2026-10-13T13:11 | RSRUSDT | bottom | TARGET | 2.5 | +2.75% | $+1.97 |
| 2026-10-13T12:36 | SUSDT | surge | TARGET | 0.0 | +2.75% | $+1.97 |
| 2026-10-13T12:01 | TIAUSDT | surge | STOP | 3.0 | -3.25% | $-2.40 |
| 2026-10-13T11:44 | ZAMAUSDT | surge | STOP | 2.8 | -3.25% | $-2.40 |
| 2026-10-13T11:09 | KAIAUSDT | surge | STOP | 0.0 | -3.25% | $-2.33 |
| 2026-10-13T09:41 | BATUSDT | surge | STOP | 0.8 | -3.25% | $-2.40 |
| 2026-10-13T09:24 | DUSKUSDT | surge | STOP | 0.2 | -3.25% | $-2.40 |
| 2026-10-13T08:30 | ZAMAUSDT | surge | TARGET | 0.8 | +2.75% | $+2.01 |
| 2026-10-13T07:09 | DODOUSDT | surge | TARGET | 0.5 | +2.75% | $+2.01 |
| 2026-10-13T05:23 | XAIUSDT | surge | STOP | 0.5 | -3.25% | $-2.39 |
| 2026-10-13T02:14 | ZROUSDT | bottom | TARGET | 0.2 | +2.75% | $+2.00 |
| 2026-10-13T01:57 | SKLUSDT | surge | TARGET | 0.0 | +2.75% | $+2.00 |
| 2026-10-13T00:14 | POLUSDT | bottom | STOP | 1.2 | -3.25% | $-2.35 |
| 2026-10-13T00:14 | AVAXUSDT | bottom | STOP | 2.0 | -3.25% | $-2.34 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T14:09 | SPCXBUSDT | surge | 166.2 | 160.09 | -3.68% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.13834 | -1.18% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3282 | -0.52% |
| 2026-10-13T01:39 | SOXSBUSDT | surge | 39.02 | 40.03 | +2.59% |
| 2026-10-13T11:26 | MUBUSDT | bottom | 951.97 | 935.18 | -1.76% |
| 2026-10-13T12:54 | DUSKUSDT | surge | 0.0992 | 0.0993 | +0.10% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
