# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-11-03T03:33:32+00:00 · runs 5067 · equity **$560.06** (-43.99%) · cash $99.22 · open 8/10 · round trips 1772

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 48% (break-even 54%) · mean -0.32%/trade · realized $-435.08 · worst day $-50.94 · trades/day 29.5

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 1538 | 48% | -0.29% | 46% | 47% | 7% |
| bottom | 234 | 42% | -0.53% | 36% | 45% | 18% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
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
| 2026-11-02T18:05 | SOXSBUSDT | surge | TARGET | 0.5 | +2.75% | $+1.54 |
| 2026-11-02T18:05 | SEIUSDT | surge | STOP | 18.5 | -3.25% | $-1.71 |
| 2026-11-02T17:16 | DRAMBUSDT | surge | STOP | 15.5 | -3.25% | $-1.88 |
| 2026-11-02T16:59 | MEGAUSDT | surge | STOP | 0.8 | -3.25% | $-1.60 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-11-02T16:59 | TSLABUSDT | surge | 410.69 | 405.03 | -1.38% |
| 2026-11-02T16:59 | BABABUSDT | surge | 103.32 | 102.46 | -0.83% |
| 2026-11-02T16:59 | COWUSDT | surge | 0.1187 | 0.1166 | -1.77% |
| 2026-11-02T19:59 | FETUSDT | bottom | 0.1538 | 0.1533 | -0.33% |
| 2026-11-02T21:53 | MEGAUSDT | surge | 0.04512 | 0.04438 | -1.64% |
| 2026-11-02T23:51 | XLMUSDT | bottom | 0.1628 | 0.1618 | -0.61% |
| 2026-11-03T00:09 | HAEDALUSDT | surge | 0.02876 | 0.02807 | -2.40% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
