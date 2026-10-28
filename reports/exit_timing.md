# Exit timing — the bot grading its own exits

updated 2026-10-28T22:44:29+00:00 · 47 exits audited · early/late line ±3% · MEASUREMENT ONLY

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
- BTC since inception: +29.0% (book gap **-95.4pp**) · last 24h +0.5%
- ETH since inception: +25.5% (book gap **-91.8pp**) · last 24h +0.5%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 7 | -3.91% | **-1.25pp** |
| flat | 60 | -0.85% | **-0.92pp** |
| green | 8 | -2.24% | **-7.49pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-10-19 | flat | +0.00% | -0.22% | +0.22pp |
| 2026-10-20 | flat | +0.00% | +1.33% | -1.33pp |
| 2026-10-21 | flat | +0.00% | +1.28% | -1.28pp |
| 2026-10-22 | red | +0.00% | -3.18% | +3.18pp |
| 2026-10-23 | flat | +0.00% | -0.28% | +0.28pp |
| 2026-10-24 | flat | +0.00% | -0.37% | +0.37pp |
| 2026-10-25 | flat | +0.00% | -0.91% | +0.91pp |
| 2026-10-26 | flat | +0.00% | -0.00% | +0.00pp |
| 2026-10-27 | flat | +0.00% | +0.95% | -0.95pp |
| 2026-10-28 | flat | +0.00% | +0.51% | -0.51pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
