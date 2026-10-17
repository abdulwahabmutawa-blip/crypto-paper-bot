# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-17T11:44:51+00:00 · runs 3628 · equity **$697.92** (-30.21%) · cash $0.00 · open 10/10 · round trips 1331

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 49% (break-even 54%) · mean -0.26%/trade · realized $-298.22 · worst day $-50.94 · trades/day 31.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1162 | 49% | -0.24% | 47% | 46% | 7% |
| bottom | 169 | 45% | -0.41% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-17T10:37 | MINAUSDT | surge | TARGET | 7.2 | +2.75% | $+1.94 |
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

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-16T15:42 | SENTUSDT | surge | 0.02139 | 0.02084 | -2.57% |
| 2026-10-16T20:22 | SOXSBUSDT | surge | 49.26 | 48.94 | -0.65% |
| 2026-10-16T20:22 | MUBUSDT | bottom | 878.21 | 882.08 | +0.44% |
| 2026-10-17T06:52 | EIGENUSDT | surge | 0.2708 | 0.2684 | -0.89% |
| 2026-10-17T07:24 | NMRUSDT | surge | 12.34 | 12.48 | +1.13% |
| 2026-10-17T09:17 | KMNOUSDT | surge | 0.04254 | 0.04215 | -0.92% |
| 2026-10-17T09:33 | ARBUSDT | bottom | 0.1886 | 0.1878 | -0.42% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1797 | +0.34% |
| 2026-10-17T10:37 | AXLUSDT | surge | 0.0577 | 0.0565 | -2.08% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
