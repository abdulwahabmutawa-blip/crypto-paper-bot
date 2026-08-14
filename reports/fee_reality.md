# Fee reality at pilot size (100 KWD ≈ $325, IBKR Fixed tier)

_Generated 2026-08-14T01:44:30+00:00 by src/fee_reality.py from the fleet's actual ledgers. IBKR Fixed: $0.005/share, min $1/order, max 1% of value, + half-spread. Verdict rule of thumb: annualized fee drag above ~10% of the book means the cadence cannot beat a savings account after costs._

| bot | lane | fills | days | paper fees ($1k book) | pilot fees ($325 book) | annualized drag |
|---|---|---|---|---|---|---|
| scholar | equity | 1 | 11 | $0.00 | $1.02 | 10.4%/yr |
| stock | equity | 1 | 11 | $0.00 | $1.05 | 10.7%/yr |
| analyst | equity | 1 | 10 | $0.00 | $1.02 | 11.4%/yr |
| commodity | equity | 3 | 21 | $2.33 | $3.17 | 17.0%/yr |
| congress | equity | 10 | 21 | $0.70 | $3.31 | 17.7%/yr |
| meanrev | equity | 7 | 21 | $0.00 | $7.21 | 38.6%/yr |
| hunter | CRYPTO (no pilot lane) | 21 | 20 | $4.50 | $9.58 | 53.8%/yr |
| sentiment | CRYPTO (no pilot lane) | 27 | 24 | $6.02 | $12.83 | 60.0%/yr |
| crypto | CRYPTO (no pilot lane) | 103 | 30 | $71.06 | $100.34 | 375.6%/yr |

Fee-fit candidates are the equity-lane bots at the top of the table; anything above ~10%/yr drag is disqualified at this account size (research 08-13 §5).