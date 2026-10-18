# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-10-18T01:45:30+00:00 · runs 3681 · equity **$673.06** (-32.69%) · cash $126.81 · open 8/10 · round trips 1361

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.29%/trade · realized $-327.03 · worst day $-50.94 · trades/day 30.9

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1189 | 49% | -0.27% | 46% | 46% | 7% |
| bottom | 172 | 45% | -0.41% | 39% | 44% | 17% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-10-18T01:44 | UNIUSDT | bottom | TARGET | 8.8 | +2.75% | $+1.80 |
| 2026-10-17T23:50 | SOXSBUSDT | surge | STOP | 1.8 | -3.25% | $-2.06 |
| 2026-10-17T23:17 | ALTUSDT | surge | STOP | 1.0 | -3.25% | $-2.06 |
| 2026-10-17T21:51 | CRVUSDT | surge | STOP | 1.5 | -3.25% | $-2.09 |
| 2026-10-17T21:51 | AXLUSDT | surge | STOP | 2.5 | -3.25% | $-2.13 |
| 2026-10-17T21:51 | CAKEUSDT | surge | STOP | 7.2 | -3.25% | $-2.14 |
| 2026-10-17T21:34 | AUSDT | surge | STOP | 1.2 | -3.25% | $-2.09 |
| 2026-10-17T21:34 | NMRUSDT | surge | STOP | 6.0 | -3.25% | $-2.21 |
| 2026-10-17T20:29 | MUBUSDT | bottom | TIME | 24.0 | -0.29% | $-0.20 |
| 2026-10-17T20:29 | SOXSBUSDT | surge | TIME | 24.0 | -0.29% | $-0.20 |
| 2026-10-17T20:06 | OGNUSDT | surge | STOP | 0.5 | -3.25% | $-2.16 |
| 2026-10-17T20:06 | LSKUSDT | surge | STOP | 0.5 | -3.25% | $-2.16 |
| 2026-10-17T19:17 | ALTUSDT | surge | TARGET | 0.8 | +2.75% | $+1.80 |
| 2026-10-17T18:28 | ALTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.79 |
| 2026-10-17T17:55 | AUSDT | surge | STOP | 0.5 | -3.25% | $-2.07 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-10-17T09:33 | XLMUSDT | bottom | 0.1791 | 0.1782 | -0.50% |
| 2026-10-17T20:29 | HBARUSDT | surge | 0.0849 | 0.08686 | +2.31% |
| 2026-10-17T20:29 | RWUSDUSDT | bottom | 1 | 1 | +0.00% |
| 2026-10-17T22:56 | LSKUSDT | surge | 0.2166 | 0.2124 | -1.94% |
| 2026-10-18T01:44 | APEUSDT | surge | 0.1519 | 0.154 | +1.38% |
| 2026-10-18T01:44 | RSRUSDT | surge | 0.002108 | 0.002078 | -1.42% |
| 2026-10-18T01:44 | TRXUSDT | bottom | 0.3338 | 0.3343 | +0.15% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
