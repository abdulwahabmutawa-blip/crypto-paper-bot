# Scalper — hyper-aggressive small-wins PAPER bot

**Execution caveat:** retrospective candle-close entries, observed later by a polling bot. This is a signal simulation, not an executable forward-fill record. Do not promote it on the trade count alone.

updated 2026-09-13T21:41:46+00:00 · runs 732 · equity **$887.74** (-11.23%) · cash $0.00 · open 10/10 · round trips 263

Rule: 10 seats, +3% target / -3% stop / 24h, cost 0.25%/RT, shapes surge + bottom on 15m candles. Judge on >= 100 round trips.

- hit 45% (break-even 54%) · mean -0.43%/trade · realized $-109.53 · worst day $-50.94 · trades/day 29.2

| shape | n | hit | mean | target% | stop% | time% |
|---|---|---|---|---|---|---|
| surge | 197 | 46% | -0.44% | 42% | 49% | 9% |
| bottom | 66 | 44% | -0.40% | 42% | 45% | 12% |

## Last 15 round trips
| exit (UTC) | coin | shape | how | hours | net | P&L |
|---|---|---|---|---|---|---|
| 2026-09-13T21:36 | XTZUSDT | surge | STOP | 0.8 | -3.25% | $-3.04 |
| 2026-09-13T20:30 | XTZUSDT | surge | TARGET | 3.2 | +2.75% | $+2.50 |
| 2026-09-13T19:41 | GMTUSDT | surge | STOP | 4.2 | -3.25% | $-2.88 |
| 2026-09-13T18:52 | SCRUSDT | surge | STOP | 1.0 | -3.25% | $-2.98 |
| 2026-09-13T17:46 | BATUSDT | surge | STOP | 1.2 | -3.25% | $-3.22 |
| 2026-09-13T17:30 | SCRUSDT | surge | TARGET | 0.0 | +2.75% | $+2.50 |
| 2026-09-13T17:30 | BABYUSDT | surge | STOP | 1.5 | -3.25% | $-3.01 |
| 2026-09-13T17:13 | ARUSDT | surge | TARGET | 0.5 | +2.75% | $+2.48 |
| 2026-09-13T17:13 | ZAMAUSDT | surge | TIME | 24.0 | -0.52% | $-0.46 |
| 2026-09-13T16:40 | PYTHUSDT | surge | TIME | 24.0 | +1.26% | $+1.13 |
| 2026-09-13T16:24 | XTZUSDT | surge | TARGET | 1.8 | +2.75% | $+2.65 |
| 2026-09-13T15:47 | KNCUSDT | surge | STOP | 2.0 | -3.25% | $-3.11 |
| 2026-09-13T15:14 | DODOUSDT | surge | TARGET | 5.2 | +2.75% | $+2.37 |
| 2026-09-13T14:25 | FILUSDT | surge | TARGET | 0.2 | +2.75% | $+2.58 |
| 2026-09-13T13:52 | GMTUSDT | surge | TARGET | 4.5 | +2.75% | $+2.51 |

## Open seats
| entry (UTC) | coin | shape | entry | mark | unrealized |
|---|---|---|---|---|---|
| 2026-09-12T17:16 | TVKUSDT | surge | 0.05405 | 0.05405 | +0.00% |
| 2026-09-12T22:22 | DOTUSDT | bottom | 1.025 | 1.02 | -0.49% |
| 2026-09-12T22:40 | DASHUSDT | bottom | 54.86 | 54.62 | -0.44% |
| 2026-09-13T03:40 | STXUSDT | surge | 0.2757 | 0.2706 | -1.85% |
| 2026-09-13T12:30 | CRVUSDT | surge | 0.3503 | 0.3535 | +0.91% |
| 2026-09-13T17:30 | MBLUSDT | surge | 0.00082 | 0.000805 | -1.83% |
| 2026-09-13T17:46 | ICPUSDT | surge | 2.784 | 2.828 | +1.58% |
| 2026-09-13T18:52 | ARUSDT | surge | 2.867 | 2.812 | -1.92% |
| 2026-09-13T19:41 | CAKEUSDT | surge | 2.269 | 2.283 | +0.62% |
| 2026-09-13T21:36 | ALGOUSDT | surge | 0.0988 | 0.099 | +0.20% |

_Paper only. $1,000 start, equal stakes = cash / free seats at entry. Entries at the close of the 15m candle that fired; exits on the first later candle touching target or stop (stop first if both), else the 24h close._
