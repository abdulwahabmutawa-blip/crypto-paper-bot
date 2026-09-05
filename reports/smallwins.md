# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T11:29:53+00:00 · runs 61 · open 422 · resolved 950 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 8 | 2 | 4.0 | 88% | 41% | +3.75% | 88% | 12% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 7 | 2 | 3.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t4|s2|h24 | 9 | 2 | 4.5 | 78% | 38% | +2.42% | 78% | 22% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 9 | 2 | 4.5 | 89% | 54% | +2.08% | 89% | 11% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 7 | 2 | 3.5 | 86% | 61% | +1.75% | 86% | 14% | 0% | +5.5% | watch |
| momentum|t3|s4|h48 | 43 | 2 | 21.5 | 84% | 61% | +1.61% | 84% | 16% | 0% | -0.3% | watch |
| momentum|t5|s3|h48 | 32 | 2 | 16.0 | 56% | 41% | +1.25% | 56% | 44% | 0% | -14.8% | watch |
| momentum|t3|s3|h24 | 46 | 2 | 23.0 | 72% | 54% | +1.05% | 72% | 28% | 0% | -11.3% | watch |
| range_bottom|t3|s2|h12 | 21 | 2 | 10.5 | 52% | 45% | +0.72% | 29% | 10% | 62% | +0.5% | watch |
| ignition|t3|s3|h24 | 8 | 2 | 4.0 | 62% | 54% | +0.50% | 62% | 38% | 0% | -3.8% | watch |
| range_bottom|t2|s2|h8 | 25 | 2 | 12.5 | 64% | 56% | +0.46% | 36% | 8% | 56% | +1.3% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 27 | 2 | 13.5 | 59% | 58% | +0.26% | 48% | 15% | 37% | +1.5% | watch |
| momentum|t3|s2|h12 | 60 | 2 | 30.0 | 48% | 45% | +0.23% | 43% | 43% | 13% | -16.5% | watch |
| range_bottom|t1.5|s1|h8 | 28 | 2 | 14.0 | 54% | 50% | +0.17% | 43% | 25% | 32% | +0.0% | watch |
| momentum|t2|s2|h8 | 81 | 2 | 40.5 | 58% | 56% | +0.11% | 54% | 36% | 10% | -15.7% | watch |
| momentum|t4|s2|h24 | 46 | 2 | 23.0 | 39% | 38% | +0.10% | 39% | 61% | 0% | -17.2% | watch |
| range_bottom|t1|s1|h6 | 34 | 2 | 17.0 | 53% | 62% | +0.05% | 47% | 21% | 32% | -0.4% | fail |
| momentum|t1.5|s1.5|h8 | 108 | 2 | 54.0 | 59% | 58% | +0.02% | 56% | 39% | 5% | -11.2% | watch |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t5|s3|h48 | 5 | 2 | 2.5 | 40% | 41% | -0.05% | 40% | 60% | 0% | -6.5% | fail |
| momentum|t1.5|s1|h8 | 125 | 2 | 62.5 | 48% | 50% | -0.06% | 46% | 50% | 4% | -6.2% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1|s1|h6 | 151 | 2 | 75.5 | 57% | 62% | -0.11% | 56% | 42% | 1% | -12.6% | fail |
| ignition|t1.5|s1.5|h8 | 12 | 2 | 6.0 | 50% | 58% | -0.13% | 50% | 42% | 8% | -2.5% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
