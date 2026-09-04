# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T19:52:48+00:00 · runs 19 · open 238 · resolved 95 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| momentum|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| range_bottom|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| ignition|t5|s3|h48 | 1 | 1 | 1.0 | 100% | 41% | +4.75% | 100% | 0% | 0% | +4.8% | watch |
| ignition|t4|s2|h24 | 2 | 1 | 2.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +7.5% | watch |
| range_bottom|t4|s2|h24 | 1 | 1 | 1.0 | 100% | 38% | +3.75% | 100% | 0% | 0% | +3.8% | watch |
| momentum|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| momentum|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| ignition|t3|s2|h12 | 2 | 1 | 2.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| ignition|t3|s3|h24 | 2 | 1 | 2.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| ignition|t3|s4|h48 | 2 | 1 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +5.5% | watch |
| range_bottom|t3|s2|h12 | 1 | 1 | 1.0 | 100% | 45% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s3|h24 | 1 | 1 | 1.0 | 100% | 54% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t3|s4|h48 | 1 | 1 | 1.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t2|s2|h8 | 2 | 1 | 2.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +3.5% | watch |
| ignition|t2|s2|h8 | 2 | 1 | 2.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +3.5% | watch |
| range_bottom|t1.5|s1.5|h8 | 3 | 1 | 3.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +3.8% | watch |
| range_bottom|t1.5|s1|h8 | 3 | 1 | 3.0 | 100% | 50% | +1.25% | 100% | 0% | 0% | +3.8% | watch |
| ignition|t1.5|s1.5|h8 | 3 | 1 | 3.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +3.8% | watch |
| momentum|t2|s2|h8 | 5 | 1 | 5.0 | 80% | 56% | +0.95% | 80% | 20% | 0% | +4.8% | watch |
| momentum|t4|s2|h24 | 2 | 1 | 2.0 | 50% | 38% | +0.75% | 50% | 50% | 0% | +1.5% | watch |
| range_bottom|t1|s1|h6 | 5 | 1 | 5.0 | 100% | 62% | +0.75% | 100% | 0% | 0% | +3.8% | watch |
| ignition|t1.5|s1|h8 | 4 | 1 | 4.0 | 75% | 50% | +0.62% | 75% | 25% | 0% | +2.5% | watch |
| momentum|t3|s2|h12 | 2 | 1 | 2.0 | 50% | 45% | +0.25% | 50% | 50% | 0% | +0.5% | watch |
| ignition|t1|s1|h6 | 4 | 1 | 4.0 | 75% | 62% | +0.25% | 75% | 25% | 0% | +1.0% | watch |
| momentum|t1.5|s1|h8 | 13 | 1 | 13.0 | 54% | 50% | +0.10% | 54% | 46% | 0% | +1.2% | watch |
| momentum|t1.5|s1.5|h8 | 10 | 1 | 10.0 | 60% | 58% | +0.05% | 60% | 40% | 0% | +0.5% | watch |
| momentum|t1|s1|h6 | 20 | 1 | 20.0 | 65% | 62% | +0.05% | 65% | 35% | 0% | +1.0% | watch |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
