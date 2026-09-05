# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T07:56:24+00:00 · runs 58 · open 313 · resolved 659 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 5 | 2 | 2.5 | 80% | 41% | +3.15% | 80% | 20% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 6 | 2 | 3.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s3|h24 | 8 | 2 | 4.0 | 88% | 54% | +2.00% | 88% | 12% | 0% | -0.5% | watch |
| range_bottom|t4|s2|h24 | 6 | 2 | 3.0 | 67% | 38% | +1.75% | 67% | 33% | 0% | +1.5% | watch |
| momentum|t3|s4|h48 | 26 | 2 | 13.0 | 85% | 61% | +1.67% | 85% | 15% | 0% | -0.3% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| momentum|t5|s3|h48 | 21 | 2 | 10.5 | 57% | 41% | +1.32% | 57% | 43% | 0% | -14.8% | watch |
| range_bottom|t3|s2|h12 | 14 | 2 | 7.0 | 50% | 45% | +0.84% | 43% | 14% | 43% | +0.5% | watch |
| momentum|t3|s3|h24 | 28 | 2 | 14.0 | 68% | 54% | +0.82% | 68% | 32% | 0% | -11.3% | watch |
| ignition|t3|s3|h24 | 6 | 2 | 3.0 | 67% | 54% | +0.75% | 67% | 33% | 0% | -3.2% | watch |
| ignition|t5|s3|h48 | 4 | 2 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | -3.2% | watch |
| range_bottom|t2|s2|h8 | 24 | 2 | 12.0 | 62% | 56% | +0.45% | 38% | 8% | 54% | +1.3% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| momentum|t4|s2|h24 | 30 | 2 | 15.0 | 43% | 38% | +0.35% | 43% | 57% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 27 | 2 | 13.5 | 59% | 58% | +0.26% | 48% | 15% | 37% | +1.5% | watch |
| momentum|t3|s2|h12 | 41 | 2 | 20.5 | 49% | 45% | +0.25% | 41% | 41% | 17% | -16.5% | watch |
| range_bottom|t1.5|s1|h8 | 28 | 2 | 14.0 | 54% | 50% | +0.17% | 43% | 25% | 32% | +0.0% | watch |
| momentum|t1.5|s1|h8 | 71 | 2 | 35.5 | 54% | 50% | +0.07% | 49% | 44% | 7% | -6.2% | watch |
| range_bottom|t1|s1|h6 | 31 | 2 | 15.5 | 55% | 62% | +0.04% | 48% | 23% | 29% | -0.4% | fail |
| momentum|t1.5|s1.5|h8 | 65 | 2 | 32.5 | 60% | 58% | +0.04% | 55% | 37% | 8% | -11.2% | watch |
| momentum|t2|s2|h8 | 55 | 2 | 27.5 | 55% | 56% | -0.01% | 49% | 36% | 15% | -15.7% | fail |
| momentum|t1|s1|h6 | 89 | 2 | 44.5 | 61% | 62% | -0.03% | 60% | 38% | 2% | -4.0% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
