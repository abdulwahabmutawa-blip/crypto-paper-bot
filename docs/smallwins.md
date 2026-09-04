# Small-wins lab — paper study (owner request 2026-09-04)

updated 2026-09-04T17:38:27+00:00 · runs 10 · open 121 · resolved 8 · cost 0.25%/RT

PASS needs: >=5 UTC days, >=60 trades, hit >= break-even + 5pts, mean > 0, worst day > -3 units.

| tactic | n | days | trades/day | hit | break-even | mean net | target% | stop% | time% | worst day | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| momentum|t2|s2|h8 | 1 | 1 | 1.0 | 100% | 56% | +1.75% | 100% | 0% | 0% | +1.8% | watch |
| momentum|t1.5|s1.5|h8 | 1 | 1 | 1.0 | 100% | 58% | +1.25% | 100% | 0% | 0% | +1.2% | watch |
| momentum|t1.5|s1|h8 | 3 | 1 | 3.0 | 33% | 50% | -0.42% | 33% | 67% | 0% | -1.2% | fail |
| momentum|t1|s1|h6 | 3 | 1 | 3.0 | 33% | 62% | -0.58% | 33% | 67% | 0% | -1.8% | fail |

_hit = share of trades with positive net return; break-even = (stop+cost)/(target+stop); worst day = sum of unit returns on the worst UTC day. Paper only, one unit per trade, no keys, no orders._
