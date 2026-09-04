# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T19:08:00+00:00 · runs 16 · open 240 · resolved 37 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| momentum|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| momentum|t4|s2|h24 | 1 | 1 | 1.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +3.8% | watch |
| ignition|t4|s2|h24 | 1 | 1 | 1.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +3.8% | watch |
| momentum|t3|s2|h12 | 1 | 1 | 1.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| momentum|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| momentum|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t3|s2|h12 | 1 | 1 | 1.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| momentum|t2|s2|h8 | 1 | 1 | 1.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +1.8% | watch |
| range_bottom|t2|s2|h8 | 1 | 1 | 1.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +1.8% | watch |
| ignition|t2|s2|h8 | 1 | 1 | 1.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +1.8% | watch |
| range_bottom|t1.5|s1.5|h8 | 1 | 1 | 1.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +1.2% | watch |
| range_bottom|t1.5|s1|h8 | 1 | 1 | 1.0 | 100% | 50% | +1.25% | 100% | 0% | 0% | +1.2% | watch |
| ignition|t1.5|s1.5|h8 | 1 | 1 | 1.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +1.2% | watch |
| range_bottom|t1|s1|h6 | 1 | 1 | 1.0 | 100% | 62% | +0.75% | 100% | 0% | 0% | +0.8% | watch |
| momentum|t1.5|s1|h8 | 5 | 1 | 5.0 | 60% | 50% | +0.25% | 60% | 40% | 0% | +1.2% | watch |
| momentum|t1|s1|h6 | 7 | 1 | 7.0 | 71% | 62% | +0.18% | 71% | 29% | 0% | +1.2% | watch |
| momentum|t1.5|s1.5|h8 | 5 | 1 | 5.0 | 60% | 58% | +0.05% | 60% | 40% | 0% | +0.2% | watch |
| ignition|t1.5|s1|h8 | 2 | 1 | 2.0 | 50% | 50% | +0.00% | 50% | 50% | 0% | +0.0% | fail |
| ignition|t1|s1|h6 | 2 | 1 | 2.0 | 50% | 62% | -0.25% | 50% | 50% | 0% | -0.5% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
