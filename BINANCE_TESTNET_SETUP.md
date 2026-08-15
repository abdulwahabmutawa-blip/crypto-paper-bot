# Binance Spot TESTNET shadow — setup (5 minutes, zero money)

The crypto bot mirrors every sim trade to Binance's spot **testnet** matching
engine (fake funds) and records the real fill beside the sim fill, exactly
like the Alpaca paper shadow does for meanrev. This validates the whole
order pipeline — symbol mapping, lot-size filters, market-order mechanics —
before any real key ever exists. `src/binance_broker.py` hardcodes the
testnet URL: a mainnet key pasted here still cannot touch real markets.

## Steps (owner)

1. Go to **https://testnet.binance.vision** and log in (GitHub account works).
2. **Generate HMAC-SHA256 API Key** — copy the API Key and Secret shown.
3. In the repo: Settings → Secrets and variables → Actions → New repository
   secret, twice:
   - `BINANCE_TESTNET_API_KEY` = the key
   - `BINANCE_TESTNET_API_SECRET` = the secret
4. Done. No code change needed — the next trade the crypto bot makes will
   carry `testnet_fill` and `fill_gap_bps` fields in its trade record.

## Notes

- Testnet balances are fake and periodically reset by Binance (roughly
  monthly). A reset just means the shadow sells skip until the next buy.
- Without the secrets, every shadow call is a silent no-op — the sim is
  never affected by this module, in any failure mode.
- Testnet order books are thin: `fill_gap_bps` here proves the plumbing
  works, not what real slippage will be. Real-liquidity realism for crypto
  would need a mainnet read-only feed — separate decision, Track C first.
- Promotion to real crypto money is NOT this module and is gated by
  GO_LIVE_PLAN Track C + an explicit reviewed mainnet adapter that does not
  exist yet.
