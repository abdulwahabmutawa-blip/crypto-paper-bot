# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-13T14:13:22+00:00 · runs 3291 · equity **$748.19** (-25.18%) · cash $144.90 · open 8/10 · round trips 1234

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.23%/trade · realized $-253.61 · worst day $-50.94 · trades/day 31.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1083 | 50% | -0.20% | 47% | 45% | 7% |
| bottom | 151 | 44% | -0.47% | 38% | 45% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-13T14:11 | AMPUSDT | surge | STOP | 0.0 | -3.25% | $-2.36 |
| 2026-10-13T14:11 | DUSKUSDT | surge | TARGET | 1.0 | +2.75% | $+2.00 |
| 2026-10-13T13:46 | SOXSBUSDT | surge | TARGET | 12.0 | +2.75% | $+2.00 |
| 2026-10-13T13:46 | SPCXBUSDT | surge | STOP | 23.5 | -3.25% | $-2.37 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-12T15:49 | JSTUSDT | surge | 0.13999 | 0.13765 | -1.67% |
| 2026-10-12T21:52 | TRXUSDT | bottom | 0.3299 | 0.3279 | -0.61% |
| 2026-10-13T11:26 | MUBUSDT | bottom | 951.97 | 950.78 | -0.13% |
| 2026-10-13T14:11 | GOOGLBUSDT | surge | 357.8 | 354.28 | -0.98% |
| 2026-10-13T14:11 | DUSKUSDT | surge | 0.0996 | 0.101 | +1.41% |
| 2026-10-13T14:11 | ZKUSDT | surge | 0.016 | 0.01665 | +4.06% |
| 2026-10-13T14:11 | RENDERUSDT | bottom | 2.029 | 2.042 | +0.64% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
