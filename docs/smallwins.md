# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T09:14:48+00:00 · runs 52 · open 320 · resolved 662 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 6 | 2 | 3.0 | 83% | 41% | +3.42% | 83% | 17% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 6 | 2 | 3.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t4|s2|h24 | 7 | 2 | 3.5 | 71% | 38% | +2.04% | 71% | 29% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 8 | 2 | 4.0 | 88% | 54% | +2.00% | 88% | 12% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 7 | 2 | 3.5 | 86% | 61% | +1.75% | 86% | 14% | 0% | +5.5% | watch |
| momentum|t3|s4|h48 | 26 | 2 | 13.0 | 85% | 61% | +1.67% | 85% | 15% | 0% | -0.3% | watch |
| momentum|t5|s3|h48 | 21 | 2 | 10.5 | 57% | 41% | +1.32% | 57% | 43% | 0% | -14.8% | watch |
| range_bottom|t3|s2|h12 | 17 | 2 | 8.5 | 59% | 45% | +0.87% | 35% | 12% | 53% | +0.5% | watch |
| momentum|t3|s3|h24 | 28 | 2 | 14.0 | 68% | 54% | +0.82% | 68% | 32% | 0% | -11.3% | watch |
| ignition|t3|s3|h24 | 8 | 2 | 4.0 | 62% | 54% | +0.50% | 62% | 38% | 0% | -3.8% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t2|s2|h8 | 23 | 2 | 11.5 | 61% | 56% | +0.39% | 35% | 9% | 57% | +1.3% | watch |
| range_bottom|t1.5|s1.5|h8 | 26 | 2 | 13.0 | 58% | 58% | +0.23% | 46% | 15% | 38% | +1.5% | fail |
| momentum|t4|s2|h24 | 32 | 2 | 16.0 | 41% | 38% | +0.19% | 41% | 59% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1|h8 | 27 | 2 | 13.5 | 52% | 50% | +0.13% | 41% | 26% | 33% | +0.0% | watch |
| momentum|t3|s2|h12 | 41 | 2 | 20.5 | 46% | 45% | +0.13% | 39% | 44% | 17% | -16.5% | watch |
| range_bottom|t1|s1|h6 | 31 | 2 | 15.5 | 52% | 62% | +0.02% | 45% | 23% | 32% | -0.4% | fail |
| momentum|t2|s2|h8 | 55 | 2 | 27.5 | 55% | 56% | -0.01% | 49% | 36% | 15% | -15.7% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t5|s3|h48 | 5 | 2 | 2.5 | 40% | 41% | -0.05% | 40% | 60% | 0% | -6.5% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1.5|s1.5|h8 | 61 | 2 | 30.5 | 56% | 58% | -0.09% | 51% | 41% | 8% | -11.2% | fail |
| momentum|t1.5|s1|h8 | 70 | 2 | 35.0 | 47% | 50% | -0.09% | 43% | 50% | 7% | -6.2% | fail |
| momentum|t1|s1|h6 | 88 | 2 | 44.0 | 58% | 62% | -0.09% | 57% | 41% | 2% | -4.0% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
