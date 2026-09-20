# Fleet status — 2026-09-20 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade (last: 09-08) | $1,147.05 (was $1,155.37) |
| meanrev | HD | No new trade (last: 09-03); weekend, marked to 09-18 close still | $1,213.18 (unchanged) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10/10 seats | 47 round trips closed (409→456) | $936.94 (was $945.12) |
| smallwins (lab) | 943 open seats | 86 new runs; open 503→943 (net opened); lifetime resolved capped at 20,000 | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STILL STUCK: 0 new scans since 09-11 15:12 UTC | n/a |
| social_radar | — (no capital) | Active — latest scan 09-20 04:56 UTC, 13 rows (unchanged row count) | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **scalper**: 47 new closed round trips (409→456). Equity $936.94, down from $945.12.
- **smallwins**: 86 new lab runs (1265→1351 total); open seats rose 503→943 as more entries opened than resolved.
- **crypto**: no trade; BTC-USD marked down to $1,147.05 from $1,155.37.
- **meanrev**: no trade; flat at $1,213.18 — weekend (Sat/Sun), no new stock close to mark to.
- **sentiment**: no trade; unchanged in cash at $869.30.
- **social_radar**: still producing fresh scans (latest 2026-09-20T04:56 UTC), same 13 admitted rows as yesterday.
- Paper-fleet cron: 86 cycle commits in this 24h window, steady ~13-18 min cadence, no gaps over 25 min.

## Needs a look
- **Watcher (grok_sentinel)**: still no new scan — verdict timestamp unchanged at 2026-09-11T15:12:52 UTC, now ~8.6 days stale. Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot. No commits touched its state files at all in this 24h window.
- No error/exception text found in any of the 346 commit messages across the 24h window; no cron gaps beyond normal cadence.
