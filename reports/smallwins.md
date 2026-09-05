# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T08:44:47+00:00 · runs 50 · open 310 · resolved 636 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 6 | 2 | 3.0 | 83% | 41% | +3.42% | 83% | 17% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 6 | 2 | 3.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t4|s2|h24 | 7 | 2 | 3.5 | 71% | 38% | +2.04% | 71% | 29% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 8 | 2 | 4.0 | 88% | 54% | +2.00% | 88% | 12% | 0% | -0.5% | watch |
| momentum|t3|s4|h48 | 24 | 2 | 12.0 | 88% | 61% | +1.88% | 88% | 12% | 0% | -0.3% | watch |
| ignition|t3|s4|h48 | 7 | 2 | 3.5 | 86% | 61% | +1.75% | 86% | 14% | 0% | +5.5% | watch |
| momentum|t5|s3|h48 | 20 | 2 | 10.0 | 60% | 41% | +1.55% | 60% | 40% | 0% | -14.8% | watch |
| ignition|t3|s3|h24 | 7 | 2 | 3.5 | 71% | 54% | +1.04% | 71% | 29% | 0% | -0.5% | watch |
| momentum|t3|s3|h24 | 26 | 2 | 13.0 | 69% | 54% | +0.90% | 69% | 31% | 0% | -11.3% | watch |
| range_bottom|t3|s2|h12 | 16 | 2 | 8.0 | 56% | 45% | +0.77% | 38% | 12% | 50% | +0.5% | watch |
| ignition|t5|s3|h48 | 4 | 2 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | -3.2% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t2|s2|h8 | 23 | 2 | 11.5 | 61% | 56% | +0.39% | 35% | 9% | 57% | +1.3% | watch |
| range_bottom|t1.5|s1.5|h8 | 26 | 2 | 13.0 | 58% | 58% | +0.23% | 46% | 15% | 38% | +1.5% | fail |
| momentum|t4|s2|h24 | 32 | 2 | 16.0 | 41% | 38% | +0.19% | 41% | 59% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1|h8 | 27 | 2 | 13.5 | 52% | 50% | +0.13% | 41% | 26% | 33% | +0.0% | watch |
| momentum|t3|s2|h12 | 41 | 2 | 20.5 | 46% | 45% | +0.13% | 39% | 44% | 17% | -16.5% | watch |
| range_bottom|t1|s1|h6 | 30 | 2 | 15.0 | 53% | 62% | +0.02% | 47% | 23% | 30% | -0.4% | fail |
| momentum|t2|s2|h8 | 54 | 2 | 27.0 | 54% | 56% | -0.04% | 48% | 37% | 15% | -15.7% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1.5|s1|h8 | 65 | 2 | 32.5 | 48% | 50% | -0.07% | 43% | 49% | 8% | -6.2% | fail |
| momentum|t1|s1|h6 | 80 | 2 | 40.0 | 57% | 62% | -0.10% | 56% | 41% | 2% | -4.0% | fail |
| momentum|t1.5|s1.5|h8 | 58 | 2 | 29.0 | 55% | 58% | -0.10% | 50% | 41% | 9% | -11.2% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
