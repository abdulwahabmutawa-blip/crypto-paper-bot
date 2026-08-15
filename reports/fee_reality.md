# Fee reality at pilot size (100 KWD ≈ $325, IBKR Fixed tier)

_Generated 2026-08-15T00:10:25+00:00 by src/fee_reality.py from the fleet's actual ledgers. IBKR Fixed: $0.005/share, min $1/order, max 1% of value, + half-spread. Verdict rule of thumb: annualized fee drag above ~10% of the book means the cadence cannot beat a savings account after costs._

| bot | lane | fills | days | paper fees ($1k book) | pilot fees ($325 book) | annualized drag |
|---|---|---|---|---|---|---|
| scholar | equity | 1 | 12 | $0.00 | $1.02 | 9.5%/yr |
| analyst | equity | 1 | 11 | $0.00 | $1.02 | 10.4%/yr |
| stock | equity | 1 | 11 | $0.00 | $1.05 | 10.7%/yr |
| commodity | equity | 3 | 22 | $2.33 | $3.17 | 16.2%/yr |
| congress | equity | 10 | 22 | $0.70 | $3.31 | 16.9%/yr |
| meanrev | equity | 7 | 22 | $0.00 | $7.21 | 36.8%/yr |
| hunter | mixed (4/21 crypto) | 21 | 21 | $4.50 | $19.56 | 104.6%/yr |
| sentiment | mixed (4/28 crypto) | 28 | 25 | $7.68 | $27.38 | 123.0%/yr |
| crypto | crypto @ Binance 10bps | 103 | 30 | $71.06 | $48.44 | 181.3%/yr |

Fee-fit candidates are the equity-lane bots at the top of the table; anything above ~10%/yr drag is disqualified at this account size (research 08-13 §5).