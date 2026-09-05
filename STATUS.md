# Fleet status — 2026-09-05 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | ADA-USD | No new trade — marks only | $1,089.97 |
| meanrev | HD | No new trade — marks only | $1,298.52 |
| commodity | DBC | No new trade — marks only | $1,031.42 |
| allweather | 5-asset basket | No new trade — marks only | $1,023.80 |
| scholar | ETH-USD | No new trade — marks only | $1,019.62 |
| sentiment | CASH | SNOW → CASH (stale Grok feed, 09-04) | $2,453.00 |
| hypecrypto | CASH | Frozen (R1 kill, 08-31) — no change | $739.48 |
| congress *(retired)* | 10 positions | Retired 09-04 by owner decision — frozen | $990.64 |
| hunter *(retired)* | BTC-USD | Retired 09-04 by owner decision — frozen | $994.61 |
| analyst *(retired)* | SPY | Retired 09-04 by owner decision — frozen | $1,025.35 |
| lottery — REAL MONEY | CASH | Stopped out of ORDIUSDT, circuit breaker tripped | $39.03 |
| Watcher | — (no capital) | Last scan 09-04 21:10 UTC | n/a |

## Changed
- **sentiment**: sold SNOW → CASH on 09-04 ("Grok scans stale 26h — flying blind is not a strategy"). Its $2,453 value still carries the unresolved stale-quote inflation flagged in a prior digest — unverified.
- **congress, hunter, analyst, hypecrypto retired** from the active roster by owner decision 2026-09-04 (recorded in `reports/kill_criteria.md`). Dashboards remain as frozen archives; they no longer run in the Actions workflow. Not yet reflected in CLAUDE.md's bot list.
- **lottery (real money, no cap)**: ORDIUSDT stopped out at -6.1% (-$2.56) on 09-04 10:18 UTC. Day P&L hit -11.9%, tripping the circuit breaker (no new entries same UTC day); a separate "tape dead" signal gate has kept it flat since 09-04 14:41 UTC. No fills since. Book value $39.03 vs $44.27 high-water mark.
- No skipped or failed cycles: paper-fleet cycles ran every ~13-16 min, lottery every ~5-8 min throughout the window — no gaps.

## Needs a look
- **lottery book is real money, currently $39.03**, halted by its own circuit breaker/tape gate — not actively bleeding, but worth the owner's eyes given it has no cap.
- **sentiment's $2,453 value is still unverified** — the stale-quote inflation from 09-01/09-02 flagged previously has not been corrected.
- Watcher's last scan (09-04 21:10 UTC, ~8h old) is within normal cadence — not stale, noted only because it was flagged yesterday.
