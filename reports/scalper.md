# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-03T11:32:43+00:00 · runs 5093 · equity **$557.82** (-44.22%) · cash $0.00 · open 10/10 · round trips 1776

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 47% (break-even 54%) · mean -0.33%/trade · realized $-441.86 · worst day $-50.94 · trades/day 29.6

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1541 | 48% | -0.30% | 46% | 47% | 7% |
| bottom | 235 | 42% | -0.54% | 36% | 46% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-11-03T10:25 | MEGAUSDT | surge | STOP | 2.8 | -3.25% | $-1.64 |
| 2026-11-03T05:29 | 1000CATUSDT | bottom | STOP | 0.5 | -3.25% | $-1.64 |
| 2026-11-03T04:56 | MEGAUSDT | surge | STOP | 6.8 | -3.25% | $-1.74 |
| 2026-11-03T03:48 | HAEDALUSDT | surge | STOP | 3.5 | -3.25% | $-1.76 |
| 2026-11-03T03:14 | PROMUSDT | bottom | STOP | 19.8 | -3.25% | $-1.60 |
| 2026-11-03T01:50 | SOXSBUSDT | surge | STOP | 3.8 | -3.25% | $-1.74 |
| 2026-11-02T23:51 | KORUBUSDT | bottom | TARGET | 2.2 | +2.75% | $+1.47 |
| 2026-11-02T20:48 | TQQQBUSDT | bottom | STOP | 1.5 | -3.25% | $-1.76 |
| 2026-11-02T20:48 | SPCXBUSDT | surge | STOP | 3.8 | -3.25% | $-1.77 |
| 2026-11-02T19:59 | HOTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.49 |
| 2026-11-02T19:59 | MUBUSDT | bottom | STOP | 3.0 | -3.25% | $-1.77 |
| 2026-11-02T19:43 | HOTUSDT | surge | TARGET | 0.0 | +2.75% | $+1.47 |
| 2026-11-02T19:26 | MSTRBUSDT | surge | STOP | 2.2 | -3.25% | $-1.77 |
| 2026-11-02T19:10 | HOTUSDT | surge | TARGET | 0.2 | +2.75% | $+1.49 |
| 2026-11-02T19:10 | BEAMXUSDT | bottom | STOP | 0.8 | -3.25% | $-1.76 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-02T16:59 | TSLABUSDT | surge | 410.69 | 402.46 | -2.00% |
| 2026-11-02T16:59 | BABABUSDT | surge | 103.32 | 102.2 | -1.08% |
| 2026-11-02T16:59 | COWUSDT | surge | 0.1187 | 0.1184 | -0.25% |
| 2026-11-02T19:59 | FETUSDT | bottom | 0.1538 | 0.1548 | +0.65% |
| 2026-11-02T23:51 | XLMUSDT | bottom | 0.1628 | 0.1632 | +0.25% |
| 2026-11-03T04:39 | WLFIUSDT | surge | 0.0504 | 0.051 | +1.19% |
| 2026-11-03T06:36 | QQQBUSDT | bottom | 680.99 | 684.18 | +0.47% |
| 2026-11-03T07:25 | RUNEUSDT | surge | 0.578 | 0.58 | +0.35% |
| 2026-11-03T11:31 | STRKUSDT | surge | 0.0424 | 0.0424 | +0.00% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
