# Exit timing — the bot grading its own exits

updated 2026-11-25T04:58:12+00:00 · 47 exits audited · early/late line ±3% · MEASUREMENT ONLY

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
- BTC since inception: -6.1% (book gap **-60.3pp**) · last 24h -1.0%
- ETH since inception: -11.8% (book gap **-54.6pp**) · last 24h -1.2%

## Alpha by regime (book minus BTC, daily, paired)

**Skill is a non-negative gap on flat/red days. Green-day returns are tide, not skill.**

| regime (BTC day) | days | avg book | avg gap vs BTC |
|---|---|---|---|
| red | 16 | -1.71% | **+1.69pp** |
| flat | 77 | -0.67% | **-0.70pp** |
| green | 10 | -1.79% | **-6.60pp** |

| date | regime | book | BTC | gap |
|---|---|---|---|---|
| 2026-11-16 | flat | +0.00% | -0.72% | +0.72pp |
| 2026-11-17 | flat | +0.00% | +0.10% | -0.10pp |
| 2026-11-18 | red | +0.00% | -2.89% | +2.89pp |
| 2026-11-19 | flat | +0.00% | -1.71% | +1.71pp |
| 2026-11-20 | red | +0.00% | -4.90% | +4.90pp |
| 2026-11-21 | green | +0.00% | +2.14% | -2.14pp |
| 2026-11-22 | flat | +0.00% | +1.75% | -1.75pp |
| 2026-11-23 | flat | +0.00% | -0.00% | +0.00pp |
| 2026-11-24 | red | +0.00% | -2.35% | +2.35pp |
| 2026-11-25 | flat | +0.00% | -1.02% | +1.02pp |


_giveback = in-hold peak the exit surrendered; post-24h run = what the coin did after we sold. High post-run with low giveback = selling too early; high giveback = selling too late._
