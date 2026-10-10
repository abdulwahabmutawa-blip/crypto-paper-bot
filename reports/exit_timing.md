# Exit timing — the bot grading its own exits

updated 2026-10-10T03:32:31+00:00 · 47 exits audited · early/late line ±3% · MEASUREMENT ONLY

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
- BTC since inception: +31.0% (book gap **-97.4pp**) · last 24h -0.1%
- ETH since inception: +32.4% (book gap **-98.7pp**) · last 24h +0.1%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 5 | -5.48% | **-2.84pp** |
| flat | 44 | -1.17% | **-1.16pp** |
| green | 8 | -2.24% | **-7.49pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-10-01 | flat | +0.00% | +1.50% | -1.50pp |
| 2026-10-02 | flat | +0.00% | -0.43% | +0.43pp |
| 2026-10-03 | flat | +0.00% | +0.28% | -0.28pp |
| 2026-10-04 | green | +0.00% | +2.10% | -2.10pp |
| 2026-10-05 | flat | +0.00% | -0.88% | +0.88pp |
| 2026-10-06 | flat | +0.00% | -0.25% | +0.25pp |
| 2026-10-07 | red | +0.00% | -2.60% | +2.60pp |
| 2026-10-08 | flat | +0.00% | -1.88% | +1.88pp |
| 2026-10-09 | flat | +0.00% | +1.08% | -1.08pp |
| 2026-10-10 | flat | +0.00% | -0.06% | +0.06pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
