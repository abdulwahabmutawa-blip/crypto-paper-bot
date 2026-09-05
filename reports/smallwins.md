# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-05T04:04:30+00:00 · runs 43 · open 293 · resolved 443 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| range_bottom|t3|s4|h48 | 4 | 2 | 2.0 | 100% | 61% | +2.75% | 100% | 0% | 0% | +2.8% | watch |
| range_bottom|t5|s3|h48 | 3 | 2 | 1.5 | 67% | 41% | +2.08% | 67% | 33% | 0% | +1.5% | watch |
| ignition|t5|s3|h48 | 3 | 1 | 3.0 | 67% | 41% | +2.08% | 67% | 33% | 0% | +6.2% | watch |
| ignition|t3|s3|h24 | 5 | 1 | 5.0 | 80% | 54% | +1.55% | 80% | 20% | 0% | +7.8% | watch |
| range_bottom|t3|s3|h24 | 5 | 2 | 2.5 | 80% | 54% | +1.55% | 80% | 20% | 0% | -0.5% | watch |
| ignition|t3|s4|h48 | 5 | 1 | 5.0 | 80% | 61% | +1.35% | 80% | 20% | 0% | +6.8% | watch |
| range_bottom|t4|s2|h24 | 5 | 2 | 2.5 | 60% | 38% | +1.35% | 60% | 40% | 0% | +1.5% | watch |
| momentum|t3|s4|h48 | 14 | 2 | 7.0 | 79% | 61% | +1.25% | 79% | 21% | 0% | -0.3% | watch |
| ignition|t4|s2|h24 | 7 | 1 | 7.0 | 57% | 38% | +1.18% | 57% | 43% | 0% | +8.3% | watch |
| range_bottom|t3|s2|h12 | 6 | 2 | 3.0 | 67% | 45% | +1.08% | 67% | 33% | 0% | +0.5% | watch |
| ignition|t3|s2|h12 | 7 | 1 | 7.0 | 57% | 45% | +0.61% | 57% | 43% | 0% | +4.2% | watch |
| range_bottom|t2|s2|h8 | 15 | 2 | 7.5 | 60% | 56% | +0.43% | 47% | 13% | 40% | +1.3% | watch |
| ignition|t2|s2|h8 | 7 | 2 | 3.5 | 57% | 56% | +0.32% | 57% | 29% | 14% | -0.2% | watch |
| ignition|t1.5|s1|h8 | 10 | 2 | 5.0 | 50% | 50% | +0.10% | 50% | 40% | 10% | -0.2% | watch |
| range_bottom|t1.5|s1.5|h8 | 18 | 2 | 9.0 | 56% | 58% | +0.10% | 44% | 22% | 33% | +0.2% | fail |
| ignition|t1.5|s1.5|h8 | 9 | 2 | 4.5 | 56% | 58% | +0.08% | 56% | 33% | 11% | -0.2% | fail |
| ignition|t1|s1|h6 | 12 | 2 | 6.0 | 58% | 62% | -0.00% | 58% | 33% | 8% | -0.8% | fail |
| range_bottom|t1.5|s1|h8 | 19 | 2 | 9.5 | 47% | 50% | -0.00% | 37% | 32% | 32% | -0.0% | fail |
| momentum|t1|s1|h6 | 61 | 2 | 30.5 | 61% | 62% | -0.03% | 59% | 38% | 3% | -4.0% | fail |
| momentum|t1.5|s1|h8 | 47 | 2 | 23.5 | 49% | 50% | -0.03% | 45% | 47% | 9% | -6.2% | fail |
| range_bottom|t1|s1|h6 | 26 | 2 | 13.0 | 50% | 62% | -0.05% | 42% | 27% | 31% | -1.0% | fail |
| momentum|t2|s2|h8 | 40 | 2 | 20.0 | 52% | 56% | -0.14% | 45% | 40% | 15% | -15.7% | fail |
| momentum|t1.5|s1.5|h8 | 44 | 2 | 22.0 | 52% | 58% | -0.18% | 48% | 43% | 9% | -11.2% | fail |
| momentum|t4|s2|h24 | 21 | 2 | 10.5 | 33% | 38% | -0.25% | 33% | 67% | 0% | -17.2% | fail |
| momentum|t3|s3|h24 | 16 | 2 | 8.0 | 50% | 54% | -0.25% | 50% | 50% | 0% | -11.3% | fail |
| momentum|t3|s2|h12 | 22 | 2 | 11.0 | 36% | 45% | -0.43% | 36% | 64% | 0% | -16.5% | fail |
| momentum|t5|s3|h48 | 12 | 2 | 6.0 | 33% | 41% | -0.58% | 33% | 67% | 0% | -14.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
