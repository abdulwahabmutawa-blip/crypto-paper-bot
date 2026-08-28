# Exit timing — the bot grading its own exits

updated 2026-08-28T23:04:25+00:00 · 26 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 12 |
| TOO_LATE | 1 |
| BOTH | 9 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| FUEL GONE | 1 | +2.1% | +1.3% | 1 |
| Grok scans stale | 1 | +1.6% | +3.1% | 0 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| RATCHET | 2 | +8.9% | +6.6% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 1 | +15.5% | +16.3% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-40.5%** — trading P&L only (-$16.19 over 28 closed trades), deposits excluded
- account balance: $45.77 (of which **+$21.96 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +23.2% (book gap **-63.7pp**) · last 24h -3.2%
- ETH since inception: +29.6% (book gap **-70.0pp**) · last 24h -2.9%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 1 | -20.08% | **-16.88pp** |
| flat | 9 | -2.25% | **-2.53pp** |
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
| 2026-08-28 | red | -20.08% | -3.19% | -16.88pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
