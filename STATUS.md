# Fleet status — 2026-09-18 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade (last: 09-08) | $1,105.36 (was $1,089.06) |
| meanrev | HD | No new trade (last: 09-03); marked to 09-17 close | $1,223.49 (unchanged) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10/10 seats | 13 round trips closed (367→380) | $932.76 (was $911.83) |
| smallwins (lab) | 566 open seats | 48 new runs (518→566); resolved capped at 20,000 lifetime | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STUCK: 0 new scans since 09-11 15:12 UTC | n/a |
| social_radar | — (no capital) | STUCK: 0 new scans since 09-11 15:29 UTC | n/a |
| retired (8, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, analyst, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **scalper**: 13 new closed round trips (367→380). Equity $932.76, up from $911.83.
- **crypto**: no trade; BTC-USD marked up to $1,105.36 from $1,089.06.
- **meanrev**: no trade; flat at $1,223.49 (still marked to 09-17 close — 09-18 close not in yet).
- **sentiment**: no trade; unchanged in cash at $869.30.
- **smallwins**: 48 new lab runs (518→566), no capital involved.
- Paper-fleet cron: 89 cycle commits in this 24h window, steady ~13-18 min cadence, no gap over 18 min.

## Needs a look
- **Watcher (grok_sentinel)**: no new scan in ~158h (since 2026-09-11 15:12 UTC), same stuck state as yesterday, now 24h worse. Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot; this is 6+ days past that line.
- **social_radar**: same pipeline stuck since 2026-09-11 15:29 UTC (~158h), unchanged from yesterday — likely shares grok_sentinel's root cause.
- No red_flag.json, no state_preflight failures, and no error/exception text in any commit message across the 24h window.
- Local git clone was shallow at the start of this run (only 50 commits, back to ~01:56 UTC); fetched deeper history to cover the full 24h window before compiling this digest.
