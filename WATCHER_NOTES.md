# The Watcher (Grok Sentinel) — design notes

Reconstructed 2026-08-01 from git history and source. This is the *why* file
for the fleet's risk officer. Code: `src/grok_sentinel.py`,
`src/sentinel_gate.py`, `src/sentinel_trader.py`.

## What it is

Bot #7. Asks Grok (model `grok-4.5`, live X + web search) two questions per
scan:

1. **RISK** — did anything happen that should worry the fleet? (exchange
   collapse, war outbreak, emergency Fed action, market halts)
2. **HYPE** — which tickers/coins have unusual chatter, and what's the mood?

It observes and records; the risk verdict lands in
`data/sentinel_verdict.json` for the other bots to read.

## Why the budget guards

- **8h throttle** (`SCAN_INTERVAL_H = 8`, ~3 scans/day) + **hard cap 100
  scans/month** (`MONTHLY_CAP`) + prepaid xAI credits as the final wall.
  Three layers because the xAI API costs real money while everything else in
  the fleet is free — the workflow runs every ~20 min but this script only
  spends when a scan is due.
- Missing `XAI_API_KEY` = graceful skip, never a crash.

## Why the SEVERE gate works the way it does

- `sentinel_gate.severe()` is **read-only and free** — every bot checks the
  verdict file before taking risk; only the Watcher itself ever spends API
  credits.
- SEVERE is reserved for **crisis-level events**. Ordinary "caution" days
  change nothing — the gate is deliberately binary so bots don't half-react
  to noise.
- **All-Weather stays deaf to the gate on purpose**: it is the fleet's
  control group; wiring it to the Watcher would contaminate the baseline
  (commit 56d9d4d).

## Why the Hype Trader has the strictest guards

Sentiment-chasing is the weakest-evidence strategy in the fleet — that is
*why* it carries guards nothing else has (commit 1065899):

- **-10% hard stop** from entry (first stop-loss in the fleet), then the
  symbol is blacklisted until a fresh scan.
- Only trades symbols marked **euphoric in the LATEST scan**; hype faded →
  rotate or go to cash.
- SEVERE verdict → no buying, existing position sold.
- Trades the Watcher's existing scans from `data/sentinel_state.json` — zero
  extra API cost.

## Why the quantitative gauges

VIX + crypto Fear & Greed are logged with every scan (commit a07b072) so
Grok's **qualitative mood can be audited against hard numbers** later. Free
sources only (yfinance, alternative.me).

## Context sources (all free, all best-effort)

CNBC RSS headlines, Reddit r/wallstreetbets hot titles, CoinDesk RSS,
StockTwits trending (commits 0c7368b, a07b072). Any source failing returns
nothing and the scan proceeds — no external dependency can kill a scan.

## Naming

Born "Grok Sentinel", renamed **The Watcher** (dashboard-facing) in commit
01402b1; "Sentinel Hype Trader" became "Hype Trader". Code keeps the old
`sentinel_*` file names.

## Open items

- `sentinel_verdict.json` consumption marked "v2 agenda" in the original
  header — the severe-gate wiring (56d9d4d) delivered part of it; verdict
  fields beyond `risk_level` are still unread by the fleet.
- `grok.txt` / `set grok.txt` in the Trade Bot root were created empty on
  2026-07-17 and never filled; this file replaces whatever they were meant
  to hold.

PAPER PROJECT. Not investment advice.
