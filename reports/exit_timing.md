# Exit timing — the bot grading its own exits

updated 2026-08-28T03:25:37+00:00 · 25 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 11 |
| TOO_LATE | 1 |
| BOTH | 9 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| FUEL GONE | 1 | +2.1% | +1.3% | 1 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| RATCHET | 2 | +8.9% | +6.6% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 1 | +15.5% | +16.3% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-25.5%** — trading P&L only (-$10.20 over 26 closed trades), deposits excluded
- account balance: $51.75 (of which **+$21.95 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +26.9% (book gap **-52.5pp**) · last 24h -0.3%
- ETH since inception: +32.6% (book gap **-58.1pp**) · last 24h -0.6%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| flat | 10 | -2.02% | **-2.25pp** |
| green | 4 | -1.76% | **-7.34pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-08-19 | green | -8.44% | +7.12% | -15.56pp |
| 2026-08-20 | green | -1.25% | +5.32% | -6.58pp |
| 2026-08-21 | green | +5.00% | +7.27% | -2.27pp |
| 2026-08-22 | flat | -4.66% | -1.61% | -3.05pp |
| 2026-08-23 | flat | -0.66% | +0.86% | -1.52pp |
| 2026-08-24 | flat | +0.00% | +1.62% | -1.62pp |
| 2026-08-25 | flat | +0.00% | -0.57% | +0.57pp |
| 2026-08-26 | flat | +0.00% | +0.62% | -0.62pp |
| 2026-08-27 | flat | -2.05% | +1.55% | -3.60pp |
| 2026-08-28 | flat | +0.00% | -0.27% | +0.27pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
