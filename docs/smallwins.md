# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T13:00:14+00:00 · runs 67 · open 416 · resolved 1092 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 8 | 2 | 4.0 | 88% | 41% | +3.75% | 88% | 12% | 0% | +1.5% | watch |
| range_bottom|t3|s4|h48 | 9 | 2 | 4.5 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t4|s2|h24 | 9 | 2 | 4.5 | 78% | 38% | +2.42% | 78% | 22% | 0% | +1.5% | watch |
| range_bottom|t3|s3|h24 | 11 | 2 | 5.5 | 91% | 54% | +2.20% | 91% | 9% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 7 | 2 | 3.5 | 86% | 61% | +1.75% | 86% | 14% | 0% | +5.5% | watch |
| momentum|t3|s4|h48 | 51 | 2 | 25.5 | 80% | 61% | +1.38% | 80% | 20% | 0% | -0.3% | watch |
| dip_mid|t1.5|s1.5|h8 | 1 | 1 | 1.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +1.2% | watch |
| dip_mid|t1.5|s1|h8 | 1 | 1 | 1.0 | 100% | 50% | +1.25% | 100% | 0% | 0% | +1.2% | watch |
| momentum|t5|s3|h48 | 37 | 2 | 18.5 | 54% | 41% | +1.07% | 54% | 46% | 0% | -14.8% | watch |
| momentum|t3|s3|h24 | 55 | 2 | 27.5 | 69% | 54% | +0.90% | 69% | 31% | 0% | -11.3% | watch |
| range_bottom|t3|s2|h12 | 22 | 2 | 11.0 | 55% | 45% | +0.81% | 32% | 9% | 59% | +0.5% | watch |
| dip_mid|t1|s1|h6 | 1 | 1 | 1.0 | 100% | 62% | +0.75% | 100% | 0% | 0% | +0.8% | watch |
| ignition|t3|s3|h24 | 8 | 2 | 4.0 | 62% | 54% | +0.50% | 62% | 38% | 0% | -3.8% | watch |
| range_bottom|t2|s2|h8 | 26 | 2 | 13.0 | 62% | 56% | +0.43% | 35% | 8% | 58% | +1.3% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 28 | 2 | 14.0 | 57% | 58% | +0.24% | 46% | 14% | 39% | +1.5% | fail |
| momentum|t4|s2|h24 | 59 | 2 | 29.5 | 41% | 38% | +0.19% | 41% | 59% | 0% | -17.2% | watch |
| momentum|t3|s2|h12 | 72 | 2 | 36.0 | 47% | 45% | +0.17% | 43% | 46% | 11% | -16.5% | watch |
| range_bottom|t1.5|s1|h8 | 29 | 2 | 14.5 | 52% | 50% | +0.16% | 41% | 24% | 34% | +0.0% | watch |
| momentum|t2|s2|h8 | 94 | 2 | 47.0 | 57% | 56% | +0.11% | 54% | 36% | 10% | -15.7% | watch |
| range_bottom|t1|s1|h6 | 34 | 2 | 17.0 | 53% | 62% | +0.05% | 47% | 21% | 32% | -0.4% | fail |
| momentum|t1.5|s1.5|h8 | 125 | 2 | 62.5 | 59% | 58% | +0.04% | 57% | 38% | 5% | -11.2% | watch |
| momentum|t1.5|s1|h8 | 141 | 2 | 70.5 | 50% | 50% | -0.02% | 48% | 49% | 4% | -6.2% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| ignition|t5|s3|h48 | 5 | 2 | 2.5 | 40% | 41% | -0.05% | 40% | 60% | 0% | -6.5% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t1|s1|h6 | 168 | 2 | 84.0 | 57% | 62% | -0.11% | 57% | 42% | 1% | -13.9% | fail |
| ignition|t1.5|s1.5|h8 | 12 | 2 | 6.0 | 50% | 58% | -0.13% | 50% | 42% | 8% | -2.5% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1|h8 | 14 | 2 | 7.0 | 36% | 50% | -0.29% | 36% | 57% | 7% | -5.3% | fail |
| dip_large|t2|s2|h8 | 3 | 1 | 3.0 | 33% | 56% | -0.92% | 33% | 67% | 0% | -2.7% | fail |
| dip_large|t1|s1|h6 | 3 | 1 | 3.0 | 0% | 62% | -1.25% | 0% | 100% | 0% | -3.8% | fail |
| dip_large|t1.5|s1|h8 | 3 | 1 | 3.0 | 0% | 50% | -1.25% | 0% | 100% | 0% | -3.8% | fail |
| dip_large|t1.5|s1.5|h8 | 3 | 1 | 3.0 | 0% | 58% | -1.75% | 0% | 100% | 0% | -5.3% | fail |
| dip_large|t3|s2|h12 | 2 | 1 | 2.0 | 0% | 45% | -2.25% | 0% | 100% | 0% | -4.5% | fail |
| dip_large|t4|s2|h24 | 2 | 1 | 2.0 | 0% | 38% | -2.25% | 0% | 100% | 0% | -4.5% | fail |
| dip_large|t3|s3|h24 | 2 | 1 | 2.0 | 0% | 54% | -3.25% | 0% | 100% | 0% | -6.5% | fail |
| dip_large|t5|s3|h48 | 2 | 1 | 2.0 | 0% | 41% | -3.25% | 0% | 100% | 0% | -6.5% | fail |
| dip_large|t3|s4|h48 | 1 | 1 | 1.0 | 0% | 61% | -4.25% | 0% | 100% | 0% | -4.2% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
