# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T09:51:02+00:00 · runs 3621 · equity **$700.61** (-29.94%) · cash $0.00 · open 10/10 · round trips 1330

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-300.16 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1161 | 49% | -0.24% | 47% | 46% | 7% |
| bottom | 169 | 45% | -0.41% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-17T09:33 | RSRUSDT | surge | TARGET | 0.5 | +2.75% | $+1.89 |
| 2026-10-17T09:33 | NILUSDT | surge | STOP | 1.2 | -3.25% | $-2.18 |
| 2026-10-17T09:17 | AUSDT | surge | TARGET | 0.0 | +2.75% | $+1.78 |
| 2026-10-17T09:01 | SANDUSDT | surge | STOP | 0.8 | -3.25% | $-2.18 |
| 2026-10-17T08:45 | ERAUSDT | surge | TARGET | 6.8 | +2.75% | $+1.84 |
| 2026-10-17T08:12 | BEAMXUSDT | surge | STOP | 9.8 | -3.25% | $-2.17 |
| 2026-10-17T08:12 | OPENUSDT | surge | STOP | 17.5 | -3.25% | $-2.32 |
| 2026-10-17T07:24 | RSRUSDT | surge | TARGET | 1.0 | +2.75% | $+1.87 |
| 2026-10-17T06:52 | PHAUSDT | surge | STOP | 3.2 | -3.25% | $-2.15 |
| 2026-10-17T06:13 | AEROUSDT | bottom | TARGET | 13.0 | +2.75% | $+1.82 |
| 2026-10-17T03:22 | APEUSDT | surge | STOP | 12.0 | -3.25% | $-2.22 |
| 2026-10-17T03:05 | BCHUSDT | bottom | TARGET | 9.2 | +2.75% | $+1.89 |
| 2026-10-17T01:37 | SEIUSDT | surge | STOP | 5.2 | -3.25% | $-2.25 |
| 2026-10-16T22:00 | AUDIOUSDT | surge | STOP | 2.5 | -3.25% | $-2.25 |
| 2026-10-16T20:22 | SOXSBUSDT | surge | TARGET | 1.8 | +2.75% | $+1.90 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02123 | -0.75% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 48.85 | -0.83% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 883.04 | +0.55% |
| 2026-10-17T03:05 | MINAUSDT | surge | 0.0777 | 0.0793 | +2.06% |
| 2026-10-17T06:52 | EIGENUSDT | surge | 0.2708 | 0.2706 | -0.07% |
| 2026-10-17T07:24 | NMRUSDT | surge | 12.34 | 12.4 | +0.49% |
| 2026-10-17T09:17 | KMNOUSDT | surge | 0.04254 | 0.04248 | -0.14% |
| 2026-10-17T09:33 | ARBUSDT | bottom | 0.1886 | 0.1879 | -0.37% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1793 | +0.11% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
