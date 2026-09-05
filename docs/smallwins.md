# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T05:53:45+00:00 · runs 50 · open 302 · resolved 535 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 4 | 2 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t5|s3|h48 | 3 | 2 | 1.5 | 67% | 41% | +2.08% | 67% | 33% | 0% | +1.5% | watch |
| momentum|t3|s4|h48 | 20 | 2 | 10.0 | 85% | 61% | +1.70% | 85% | 15% | 0% | -0.3% | watch |
| range_bottom|t3|s3|h24 | 5 | 2 | 2.5 | 80% | 54% | +1.55% | 80% | 20% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t4|s2|h24 | 5 | 2 | 2.5 | 60% | 38% | +1.35% | 60% | 40% | 0% | +1.5% | watch |
| ignition|t3|s3|h24 | 6 | 2 | 3.0 | 67% | 54% | +0.75% | 67% | 33% | 0% | -3.2% | watch |
| ignition|t5|s3|h48 | 4 | 2 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | -3.2% | watch |
| range_bottom|t3|s2|h12 | 11 | 2 | 5.5 | 45% | 45% | +0.61% | 36% | 18% | 45% | +0.5% | watch |
| momentum|t3|s3|h24 | 22 | 2 | 11.0 | 64% | 54% | +0.57% | 64% | 36% | 0% | -11.3% | watch |
| momentum|t5|s3|h48 | 15 | 2 | 7.5 | 47% | 41% | +0.48% | 47% | 53% | 0% | -14.8% | watch |
| ignition|t4|s2|h24 | 9 | 2 | 4.5 | 44% | 38% | +0.42% | 44% | 56% | 0% | -4.5% | watch |
| range_bottom|t2|s2|h8 | 19 | 2 | 9.5 | 58% | 56% | +0.31% | 37% | 11% | 53% | +1.3% | watch |
| momentum|t3|s2|h12 | 30 | 2 | 15.0 | 50% | 45% | +0.26% | 47% | 47% | 7% | -16.5% | watch |
| momentum|t4|s2|h24 | 24 | 2 | 12.0 | 42% | 38% | +0.25% | 42% | 58% | 0% | -17.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 21 | 2 | 10.5 | 52% | 58% | +0.05% | 38% | 19% | 43% | -0.4% | fail |
| momentum|t1.5|s1|h8 | 56 | 2 | 28.0 | 50% | 50% | -0.02% | 45% | 46% | 9% | -6.2% | fail |
| ignition|t3|s2|h12 | 10 | 2 | 5.0 | 40% | 45% | -0.05% | 40% | 50% | 10% | -4.8% | fail |
| momentum|t1|s1|h6 | 72 | 2 | 36.0 | 60% | 62% | -0.05% | 58% | 39% | 3% | -4.0% | fail |
| range_bottom|t1|s1|h6 | 26 | 2 | 13.0 | 50% | 62% | -0.05% | 42% | 27% | 31% | -1.0% | fail |
| range_bottom|t1.5|s1|h8 | 22 | 2 | 11.0 | 45% | 50% | -0.06% | 32% | 32% | 36% | -1.3% | fail |
| ignition|t1|s1|h6 | 16 | 2 | 8.0 | 56% | 62% | -0.06% | 56% | 38% | 6% | -0.8% | fail |
| momentum|t2|s2|h8 | 46 | 2 | 23.0 | 52% | 56% | -0.09% | 46% | 37% | 17% | -15.7% | fail |
| momentum|t1.5|s1.5|h8 | 51 | 2 | 25.5 | 55% | 58% | -0.11% | 49% | 41% | 10% | -11.2% | fail |
| ignition|t1.5|s1|h8 | 13 | 2 | 6.5 | 38% | 50% | -0.21% | 38% | 54% | 8% | -4.0% | fail |
| ignition|t2|s2|h8 | 9 | 2 | 4.5 | 44% | 56% | -0.25% | 44% | 44% | 11% | -4.8% | fail |
| ignition|t1.5|s1.5|h8 | 11 | 2 | 5.5 | 45% | 58% | -0.25% | 45% | 45% | 9% | -3.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
