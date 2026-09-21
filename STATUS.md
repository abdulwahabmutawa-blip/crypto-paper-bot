# Fleet status — 2026-09-21 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade (last: 09-08) | $1,161.98 (was $1,147.05) |
| meanrev | HD | No new trade (last: 09-03); history still marked to 09-18 close | $1,213.18 (unchanged) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10/10 seats | 40 round trips closed (457→497) | $923.92 (was $939.41) |
| smallwins (lab) | 591 open seats | 87 new runs; open 942→591 (net closed more than opened); resolved capped at 20,000 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC | n/a |
| social_radar | — (no capital) | Underlying scan also frozen since 09-11 15:29 UTC; report file re-renders but no new admitted rows (13, same as before) | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **scalper**: 40 new closed round trips (457→497). Equity $923.92, down from $939.41.
- **smallwins**: 87 new lab runs (1352→1439 total); open seats fell 942→591 (more resolved than opened this window).
- **crypto**: no trade; BTC-USD marked up to $1,161.98 from $1,147.05.
- **meanrev**: no trade; flat at $1,213.18.
- **sentiment**: no trade; unchanged in cash at $869.30.
- Paper-fleet cron: 87 cycle commits in this 24h window, steady ~13-18 min cadence, no gaps over 25 min.
- BTC execution watch: still collecting (ACCEPTED quotes, NO_TRADE, ~25bps est. cost) — no strategy qualified, nothing changed.

## Needs a look
- **Watcher (grok_sentinel)**: no new scan — verdict timestamp still 2026-09-11T15:12:52 UTC, now ~10 days stale. Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot.
- **social_radar**: same root staleness — `last_scan_utc` in state hasn't moved since 2026-09-11T15:29:50 UTC either, despite the dashboard file's timestamp updating each cycle. Likely same underlying cause as the Watcher (both consume Grok scans).
- **meanrev**: last equity mark is still Friday 09-18's close; today is Monday and no fresh close has landed yet this cycle — worth a re-check later today, not yet clearly broken.
- No error/exception text found in any cycle commit message across the 24h window; no cron gaps beyond normal cadence.
