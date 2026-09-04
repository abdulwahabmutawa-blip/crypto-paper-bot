# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T21:50:22+00:00 · runs 26 · open 294 · resolved 191 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| range_bottom|t4|s2|h24 | 1 | 1 | 1.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +3.8% | watch |
| momentum|t3|s4|h48 | 2 | 1 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| ignition|t3|s4|h48 | 3 | 1 | 3.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +8.2% | watch |
| range_bottom|t3|s2|h12 | 1 | 1 | 1.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t2|s2|h8 | 2 | 1 | 2.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +3.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 4 | 1 | 4.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +5.0% | watch |
| range_bottom|t1.5|s1|h8 | 4 | 1 | 4.0 | 100% | 50% | +1.25% | 100% | 0% | 0% | +5.0% | watch |
| ignition|t3|s3|h24 | 4 | 1 | 4.0 | 75% | 54% | +1.25% | 75% | 25% | 0% | +5.0% | watch |
| ignition|t2|s2|h8 | 4 | 1 | 4.0 | 75% | 56% | +0.75% | 75% | 25% | 0% | +3.0% | watch |
| ignition|t3|s2|h12 | 5 | 1 | 5.0 | 60% | 45% | +0.75% | 60% | 40% | 0% | +3.8% | watch |
| range_bottom|t1|s1|h6 | 6 | 1 | 6.0 | 100% | 62% | +0.75% | 100% | 0% | 0% | +4.5% | watch |
| ignition|t4|s2|h24 | 4 | 1 | 4.0 | 50% | 38% | +0.75% | 50% | 50% | 0% | +3.0% | watch |
| ignition|t5|s3|h48 | 2 | 1 | 2.0 | 50% | 41% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| ignition|t1.5|s1.5|h8 | 6 | 1 | 6.0 | 67% | 58% | +0.25% | 67% | 33% | 0% | +1.5% | watch |
| momentum|t1|s1|h6 | 36 | 1 | 36.0 | 64% | 62% | +0.03% | 64% | 36% | 0% | +1.0% | watch |
| ignition|t1.5|s1|h8 | 8 | 1 | 8.0 | 50% | 50% | +0.00% | 50% | 50% | 0% | +0.0% | fail |
| momentum|t1.5|s1|h8 | 25 | 1 | 25.0 | 48% | 50% | -0.05% | 48% | 52% | 0% | -1.2% | fail |
| ignition|t1|s1|h6 | 9 | 1 | 9.0 | 56% | 62% | -0.14% | 56% | 44% | 0% | -1.3% | fail |
| momentum|t1.5|s1.5|h8 | 21 | 1 | 21.0 | 52% | 58% | -0.18% | 52% | 48% | 0% | -3.8% | fail |
| momentum|t2|s2|h8 | 16 | 1 | 16.0 | 50% | 56% | -0.25% | 50% | 50% | 0% | -4.0% | fail |
| momentum|t3|s3|h24 | 4 | 1 | 4.0 | 50% | 54% | -0.25% | 50% | 50% | 0% | -1.0% | fail |
| momentum|t5|s3|h48 | 3 | 1 | 3.0 | 33% | 41% | -0.58% | 33% | 67% | 0% | -1.8% | fail |
| momentum|t4|s2|h24 | 9 | 1 | 9.0 | 22% | 38% | -0.92% | 22% | 78% | 0% | -8.2% | fail |
| momentum|t3|s2|h12 | 9 | 1 | 9.0 | 22% | 45% | -1.14% | 22% | 78% | 0% | -10.2% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
