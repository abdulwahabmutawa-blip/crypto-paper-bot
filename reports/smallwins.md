# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T09:44:48+00:00 · runs 54 · open 404 · resolved 819 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 7 | 2 | 3.5 | 86% | 41% | +3.61% | 86% | 14% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 7 | 2 | 3.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t4|s2|h24 | 8 | 2 | 4.0 | 75% | 38% | +2.25% | 75% | 25% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 9 | 2 | 4.5 | 89% | 54% | +2.08% | 89% | 11% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 7 | 2 | 3.5 | 86% | 61% | +1.75% | 86% | 14% | 0% | +5.5% | watch |
| momentum|t3|s4|h48 | 37 | 2 | 18.5 | 84% | 61% | +1.61% | 84% | 16% | 0% | -0.3% | watch |
| momentum|t5|s3|h48 | 28 | 2 | 14.0 | 61% | 41% | +1.61% | 61% | 39% | 0% | -14.8% | watch |
| momentum|t3|s3|h24 | 39 | 2 | 19.5 | 72% | 54% | +1.06% | 72% | 28% | 0% | -11.3% | watch |
| range_bottom|t3|s2|h12 | 18 | 2 | 9.0 | 56% | 45% | +0.81% | 33% | 11% | 56% | +0.5% | watch |
| ignition|t3|s3|h24 | 8 | 2 | 4.0 | 62% | 54% | +0.50% | 62% | 38% | 0% | -3.8% | watch |
| range_bottom|t2|s2|h8 | 24 | 2 | 12.0 | 62% | 56% | +0.45% | 38% | 8% | 54% | +1.3% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| momentum|t3|s2|h12 | 52 | 2 | 26.0 | 50% | 45% | +0.33% | 44% | 40% | 15% | -16.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 27 | 2 | 13.5 | 59% | 58% | +0.26% | 48% | 15% | 37% | +1.5% | watch |
| momentum|t4|s2|h24 | 39 | 2 | 19.5 | 41% | 38% | +0.21% | 41% | 59% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1|h8 | 28 | 2 | 14.0 | 54% | 50% | +0.17% | 43% | 25% | 32% | +0.0% | watch |
| momentum|t2|s2|h8 | 68 | 2 | 34.0 | 57% | 56% | +0.09% | 53% | 35% | 12% | -15.7% | watch |
| momentum|t1.5|s1.5|h8 | 85 | 2 | 42.5 | 60% | 58% | +0.04% | 56% | 38% | 6% | -11.2% | watch |
| range_bottom|t1|s1|h6 | 32 | 2 | 16.0 | 53% | 62% | +0.04% | 47% | 22% | 31% | -0.4% | fail |
| momentum|t1.5|s1|h8 | 100 | 2 | 50.0 | 49% | 50% | -0.04% | 46% | 49% | 5% | -6.2% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t5|s3|h48 | 5 | 2 | 2.5 | 40% | 41% | -0.05% | 40% | 60% | 0% | -6.5% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1|s1|h6 | 122 | 2 | 61.0 | 57% | 62% | -0.10% | 57% | 42% | 2% | -8.4% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
