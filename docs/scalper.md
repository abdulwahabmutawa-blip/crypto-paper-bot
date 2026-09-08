# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-08T13:59:10+00:00 · runs 268 · equity **$1,000.82** (+0.08%) · cash $0.00 · open 10/10 · round trips 96

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 53% (break-even 54%) · mean +0.01%/trade · realized $-0.25 · worst day $-18.97 · trades/day 24.0

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 44 | 59% | +0.25% | 55% | 39% | 7% |
| bottom | 52 | 48% | -0.20% | 46% | 44% | 10% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-08T13:57 | BICOUSDT | surge | STOP | 0.2 | -3.25% | $-3.32 |
| 2026-09-08T13:57 | SCRUSDT | surge | TARGET | 0.2 | +2.75% | $+2.81 |
| 2026-09-08T13:57 | LINKUSDT | bottom | STOP | 16.0 | -3.25% | $-3.38 |
| 2026-09-08T13:24 | MINAUSDT | surge | TIME | 24.0 | +0.85% | $+0.86 |
| 2026-09-08T13:24 | ZKPUSDT | surge | TIME | 24.0 | +0.78% | $+0.79 |
| 2026-09-08T13:08 | SAHARAUSDT | surge | TARGET | 2.2 | +2.75% | $+2.72 |
| 2026-09-08T12:35 | ATOMUSDT | surge | TARGET | 0.8 | +2.75% | $+2.55 |
| 2026-09-08T11:30 | MOVRUSDT | surge | STOP | 0.8 | -3.25% | $-3.12 |
| 2026-09-08T11:07 | VETUSDT | surge | TARGET | 0.8 | +2.75% | $+2.63 |
| 2026-09-08T10:34 | MEGAUSDT | surge | STOP | 2.5 | -3.25% | $-3.32 |
| 2026-09-08T10:17 | TSTUSDT | surge | STOP | 1.8 | -3.25% | $-3.22 |
| 2026-09-08T10:01 | MIRAUSDT | surge | STOP | 0.8 | -3.25% | $-3.21 |
| 2026-09-08T09:05 | KAITOUSDT | surge | STOP | 1.0 | -3.25% | $-3.32 |
| 2026-09-08T08:15 | 1000CATUSDT | surge | TARGET | 0.0 | +2.75% | $+2.81 |
| 2026-09-08T08:15 | HBARUSDT | surge | STOP | 12.0 | -3.25% | $-3.13 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-07T17:10 | KAVAUSDT | surge | 0.05979 | 0.0594 | -0.65% |
| 2026-09-08T00:58 | SKHYBUSDT | surge | 184.72 | 187.57 | +1.54% |
| 2026-09-08T07:58 | BNBUSDT | surge | 756.19 | 747.21 | -1.19% |
| 2026-09-08T08:15 | ETCUSDT | surge | 8.08 | 8.26 | +2.23% |
| 2026-09-08T11:07 | ZKCUSDT | surge | 0.0493 | 0.0495 | +0.41% |
| 2026-09-08T12:35 | VETUSDT | surge | 0.00783 | 0.00759 | -3.07% |
| 2026-09-08T13:08 | HEIUSDT | surge | 0.1439 | 0.1436 | -0.21% |
| 2026-09-08T13:57 | PROMUSDT | surge | 6.034 | 6.042 | +0.13% |
| 2026-09-08T13:57 | COTIUSDT | surge | 0.01804 | 0.01833 | +1.61% |
| 2026-09-08T13:57 | QQQBUSDT | bottom | 717.32 | 718.52 | +0.17% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
