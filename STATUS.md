# Fleet status — 2026-09-04 (UTC)

10 paper bots ($1,000 each, no real money) + Watcher (Grok risk gate).

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (trend/regime) | ADA-USD | CASH → ADA-USD (signal flip, 09-03) | $1,158.84 |
| congress | 10 positions | No new trade — marks only | $1,003.21 |
| meanrev | HD | WMT → HD (signal flip, 09-03) | $1,286.23 |
| commodity | DBC | No new trade — marks only (prior whipsaw already settled) | $1,033.03 |
| allweather | 5-asset basket | No new trade — marks only | $1,025.74 |
| sentiment | SNOW | DELL → SNOW (Grok hype rotation) — see below | $2,488.60 |
| hypecrypto | CASH | No change — still frozen (kill floor, 08-31) | $739.48 |
| Hunter | BTC-USD | No new trade — marks only | $1,013.66 |
| Scholar | ETH-USD | SPY → ETH-USD (signal flip, 09-03) | $1,030.22 |
| Analyst | SPY | No new trade — marks only | $1,029.25 |
| Watcher | — (no capital) | No new scan since 09-03 11:11 UTC — see below | n/a |

## Changed
- crypto: went to CASH then bought ADA-USD in the same window (signal flip, 09-03).
- meanrev: WMT → HD, oversold-dip rotation.
- scholar: SPY → ETH-USD, vol-targeted 36% position, rest cash.
- sentiment: DELL → SNOW on a Grok hype signal — book value still anomalous, see below.
- No stop-outs. No failed or skipped cycles — 110 cycle commits over the last 24h, no gap over 20 min.

## Needs a look
- **sentiment bot's value is still anomalous.** $2,488.60 vs every other bot's $739–$1,286 range. Yesterday's flagged cause (a frozen ARB-USD quote, 0.00062903 repeated across 3 trades on 09-01/09-02, plus a same-day GPRO round-trip showing +67%) is still sitting in its trade history and hasn't been corrected. Today's DELL/SNOW fills look like real distinct prices, but the inflated cash base carried forward from the earlier bug is unverified.
- **Watcher hasn't scanned in ~18h.** Last verdict is 2026-09-03T11:11 UTC ("caution"); normal cadence is ~8h. September scan count is 7, far under the 100/month cap, so it isn't budget throttling — cause unclear. Not yet past the 24h "treat as UNKNOWN" line, but worth checking the scan scheduler.
