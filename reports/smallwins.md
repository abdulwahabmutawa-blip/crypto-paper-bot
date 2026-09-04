# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T20:07:42+00:00 · runs 20 · open 237 · resolved 123 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| momentum|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| range_bottom|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| ignition|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| range_bottom|t4|s2|h24 | 1 | 1 | 1.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +3.8% | watch |
| momentum|t3|s3|h24 | 2 | 1 | 2.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| momentum|t3|s4|h48 | 2 | 1 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| ignition|t3|s3|h24 | 2 | 1 | 2.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| ignition|t3|s4|h48 | 2 | 1 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| range_bottom|t3|s2|h12 | 1 | 1 | 1.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t2|s2|h8 | 2 | 1 | 2.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +3.5% | watch |
| ignition|t2|s2|h8 | 2 | 1 | 2.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +3.5% | watch |
| ignition|t4|s2|h24 | 3 | 1 | 3.0 | 67% | 38% | +1.75% | 67% | 33% | 0% | +5.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 4 | 1 | 4.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +5.0% | watch |
| range_bottom|t1.5|s1|h8 | 4 | 1 | 4.0 | 100% | 50% | +1.25% | 100% | 0% | 0% | +5.0% | watch |
| ignition|t3|s2|h12 | 3 | 1 | 3.0 | 67% | 45% | +1.08% | 67% | 33% | 0% | +3.2% | watch |
| range_bottom|t1|s1|h6 | 5 | 1 | 5.0 | 100% | 62% | +0.75% | 100% | 0% | 0% | +3.8% | watch |
| ignition|t1.5|s1.5|h8 | 4 | 1 | 4.0 | 75% | 58% | +0.50% | 75% | 25% | 0% | +2.0% | watch |
| momentum|t2|s2|h8 | 9 | 1 | 9.0 | 67% | 56% | +0.42% | 67% | 33% | 0% | +3.8% | watch |
| ignition|t1.5|s1|h8 | 5 | 1 | 5.0 | 60% | 50% | +0.25% | 60% | 40% | 0% | +1.2% | watch |
| momentum|t1|s1|h6 | 26 | 1 | 26.0 | 73% | 62% | +0.21% | 73% | 27% | 0% | +5.5% | watch |
| momentum|t1.5|s1|h8 | 14 | 1 | 14.0 | 57% | 50% | +0.18% | 57% | 43% | 0% | +2.5% | watch |
| momentum|t4|s2|h24 | 5 | 1 | 5.0 | 40% | 38% | +0.15% | 40% | 60% | 0% | +0.8% | watch |
| momentum|t1.5|s1.5|h8 | 12 | 1 | 12.0 | 58% | 58% | -0.00% | 58% | 42% | 0% | -0.0% | fail |
| ignition|t1|s1|h6 | 5 | 1 | 5.0 | 60% | 62% | -0.05% | 60% | 40% | 0% | -0.3% | fail |
| momentum|t3|s2|h12 | 5 | 1 | 5.0 | 40% | 45% | -0.25% | 40% | 60% | 0% | -1.2% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
