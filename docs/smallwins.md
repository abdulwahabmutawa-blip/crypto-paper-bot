# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T21:34:50+00:00 · runs 25 · open 300 · resolved 172 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| ignition|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| range_bottom|t4|s2|h24 | 1 | 1 | 1.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +3.8% | watch |
| momentum|t3|s4|h48 | 2 | 1 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| ignition|t3|s4|h48 | 2 | 1 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| range_bottom|t3|s2|h12 | 1 | 1 | 1.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t2|s2|h8 | 2 | 1 | 2.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +3.5% | watch |
| ignition|t4|s2|h24 | 3 | 1 | 3.0 | 67% | 38% | +1.75% | 67% | 33% | 0% | +5.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 4 | 1 | 4.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +5.0% | watch |
| range_bottom|t1.5|s1|h8 | 4 | 1 | 4.0 | 100% | 50% | +1.25% | 100% | 0% | 0% | +5.0% | watch |
| ignition|t3|s2|h12 | 3 | 1 | 3.0 | 67% | 45% | +1.08% | 67% | 33% | 0% | +3.2% | watch |
| range_bottom|t1|s1|h6 | 6 | 1 | 6.0 | 100% | 62% | +0.75% | 100% | 0% | 0% | +4.5% | watch |
| ignition|t3|s3|h24 | 3 | 1 | 3.0 | 67% | 54% | +0.75% | 67% | 33% | 0% | +2.2% | watch |
| ignition|t1.5|s1.5|h8 | 4 | 1 | 4.0 | 75% | 58% | +0.50% | 75% | 25% | 0% | +2.0% | watch |
| ignition|t2|s2|h8 | 3 | 1 | 3.0 | 67% | 56% | +0.42% | 67% | 33% | 0% | +1.3% | watch |
| momentum|t1|s1|h6 | 35 | 1 | 35.0 | 66% | 62% | +0.06% | 66% | 34% | 0% | +2.2% | watch |
| momentum|t1.5|s1|h8 | 24 | 1 | 24.0 | 50% | 50% | +0.00% | 50% | 50% | 0% | +0.0% | fail |
| ignition|t1.5|s1|h8 | 6 | 1 | 6.0 | 50% | 50% | +0.00% | 50% | 50% | 0% | +0.0% | fail |
| momentum|t1.5|s1.5|h8 | 20 | 1 | 20.0 | 55% | 58% | -0.10% | 55% | 45% | 0% | -2.0% | fail |
| ignition|t1|s1|h6 | 7 | 1 | 7.0 | 57% | 62% | -0.11% | 57% | 43% | 0% | -0.8% | fail |
| momentum|t2|s2|h8 | 15 | 1 | 15.0 | 53% | 56% | -0.12% | 53% | 47% | 0% | -1.7% | fail |
| momentum|t3|s3|h24 | 4 | 1 | 4.0 | 50% | 54% | -0.25% | 50% | 50% | 0% | -1.0% | fail |
| momentum|t5|s3|h48 | 3 | 1 | 3.0 | 33% | 41% | -0.58% | 33% | 67% | 0% | -1.8% | fail |
| momentum|t4|s2|h24 | 8 | 1 | 8.0 | 25% | 38% | -0.75% | 25% | 75% | 0% | -6.0% | fail |
| momentum|t3|s2|h12 | 8 | 1 | 8.0 | 25% | 45% | -1.00% | 25% | 75% | 0% | -8.0% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
