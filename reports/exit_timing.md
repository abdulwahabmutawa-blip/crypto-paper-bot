# Exit timing — the bot grading its own exits

updated 2026-10-31T14:47:54+00:00 · 47 exits audited · early/late line ±3% · MEASUREMENT ONLY

| verdict | n |
|---|---|
| TOO_EARLY | 17 |
| TOO_LATE | 9 |
| BOTH | 17 |
| WELL_TIMED | 4 |

| exit family | n | avg giveback | avg post-24h run | well-timed |
|---|---|---|---|---|
| CLIMAX | 2 | +3.0% | +13.9% | 0 |
| FUEL GONE | 6 | +3.9% | +5.0% | 1 |
| Grok scans stale | 1 | +1.6% | +3.1% | 0 |
| Hype faded | 7 | +6.1% | +10.7% | 0 |
| MOMENTUM GONE | 2 | +0.6% | +12.3% | 0 |
| PROTECTIVE STOP | 9 | +6.3% | +7.0% | 0 |
| RATCHET | 4 | +9.2% | +3.7% | 0 |
| STALLED | 12 | +1.5% | +9.7% | 3 |
| STOP-LOSS | 2 | +11.5% | +8.8% | 0 |
| TARGET | 1 | +1.9% | +13.9% | 0 |
| TURBO HOP | 1 | +0.8% | +9.8% | 0 |

## Market capture

- book since inception (08-15, $40 stake): **-66.4%** — trading P&L only (-$26.55 over 47 closed trades), deposits excluded
- account balance: $33.15 (of which **+$19.70 is deposited capital, not profit** — inferred as balance minus stake minus P&L; deposits are not tracked anywhere yet)
- BTC since inception: +23.1% (book gap **-89.4pp**) · last 24h +0.3%
- ETH since inception: +19.7% (book gap **-86.1pp**) · last 24h +0.3%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 8 | -3.42% | **-0.58pp** |
| flat | 62 | -0.83% | **-0.88pp** |
| green | 8 | -2.24% | **-7.49pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-10-22 | red | +0.00% | -3.18% | +3.18pp |
| 2026-10-23 | flat | +0.00% | -0.28% | +0.28pp |
| 2026-10-24 | flat | +0.00% | -0.37% | +0.37pp |
| 2026-10-25 | flat | +0.00% | -0.91% | +0.91pp |
| 2026-10-26 | flat | +0.00% | -0.00% | +0.00pp |
| 2026-10-27 | flat | +0.00% | +0.95% | -0.95pp |
| 2026-10-28 | flat | +0.00% | +0.54% | -0.54pp |
| 2026-10-29 | red | +0.00% | -4.12% | +4.12pp |
| 2026-10-30 | flat | +0.00% | -0.80% | +0.80pp |
| 2026-10-31 | flat | +0.00% | +0.27% | -0.27pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
