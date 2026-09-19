# Fleet status — 2026-09-19 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade (last: 09-08) | $1,155.37 (was $1,105.36) |
| meanrev | HD | No new trade (last: 09-03); marked to 09-18 close | $1,213.18 (was $1,223.49) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10/10 seats | 29 round trips closed (380→409) | $945.12 (was $931.33) |
| smallwins (lab) | 503 open seats | 83 new runs; open 646→503 (net resolved); lifetime capped at 20,000 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STUCK: still 0 new scans since 09-11 15:12 UTC | n/a |
| social_radar | — (no capital) | RECOVERED: fresh scans resuming ~09-18 05:09 UTC, current as of 05:00 UTC today | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **scalper**: 29 new closed round trips (380→409). Equity $945.12, up from $931.33.
- **crypto**: no trade; BTC-USD marked up to $1,155.37 from $1,105.36.
- **meanrev**: no trade; marked down to $1,213.18 from $1,223.49 (price drift on HD, now marked to 09-18 close).
- **sentiment**: no trade; unchanged in cash at $869.30.
- **smallwins**: 83 new lab runs (1182→1265 total); open seats fell 646→503 as runs resolved, no capital involved.
- **social_radar**: recovered — first fresh scan landed ~2026-09-18 05:09 UTC after being stuck since 09-11; scans have continued through today (latest 05:00 UTC).
- Paper-fleet cron: 84 cycle commits in this 24h window, one gap of 58 min (23:12→00:10 UTC), otherwise steady ~13-18 min cadence.

## Needs a look
- **Watcher (grok_sentinel)**: still no new scan — verdict timestamp unchanged at 2026-09-11T15:12:52 UTC, now ~7.6 days stale. Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot. No commits touched its state files at all in this 24h window.
- One cron gap of 58 minutes (23:12→00:10 UTC) — outside normal ~13-18 min cadence; no error text found in commit messages for that stretch.
- No red_flag.json changes, no error/exception text found in any cycle commit message across the 24h window.
