# Fleet status — 2026-09-17 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No new trade | $1,090.78 (was $1,087.69) |
| meanrev | HD | No new trade — marked to 09-16 close (today's not in yet) | $1,223.90 (was $1,235.51) |
| sentiment | CASH | No new trade — still in cash since 09-11 | $869.30 (unchanged) |
| scalper | 10/10 seats | 28 round trips closed (326→354) | $889.49 (was $876.15) |
| smallwins (lab) | 569 open seats | 86 new runs (1006→1092); resolved capped at 20,000 lifetime | n/a — research only |
| Watcher (grok_sentinel) | — (no capital) | STUCK: 0 new scans since 09-11 15:12 UTC | n/a |
| social_radar | — (no capital) | STUCK: 0 new scans since 09-11 15:29 UTC | n/a |
| retired (7, frozen) | congress, commodity, allweather, hunter, hypecrypto, scholar, stock | No state file changed in 24h | — |

Lottery/carry/hype-ibkr (VPS, real-money paths) are out of scope for this digest per CLAUDE.md — not shown.

## Changed
- **scalper**: 28 new closed round trips (326→354). Equity $889.49, up from $876.15.
- **crypto**: no trade; BTC-USD drifted up to $1,090.78 (+0.3%) from $1,087.69.
- **meanrev**: no trade; still marked to Tuesday's close, $1,223.90 (down $11.61) from $1,235.51.
- **sentiment**: no trade; unchanged in cash at $869.30.
- **smallwins**: 86 new lab runs (1006→1092), no capital involved.
- Paper-fleet cron: 87 cycle commits in this 24h window, steady ~13-17 min cadence, no gap over ~18 min.

## Needs a look
- **Watcher (grok_sentinel)**: no new scan in ~134h (since 2026-09-11 15:12 UTC) despite running every cycle without a logged failure — same stuck state as yesterday's digest, now 24h worse. Verdicts older than 24h are treated as UNKNOWN by every risk-gated bot; this is 5+ days past that line.
- **social_radar**: same pipeline stuck since 2026-09-11 15:29 UTC (~134h), unchanged from yesterday — likely shares grok_sentinel's root cause.
- Bot roster note: this digest's active fleet is crypto, meanrev, sentiment, scalper (+ smallwins/social_radar/btc_execution utilities), per `.github/workflows/bot.yml` and `CLAUDE.md`. The other 7 (congress, hunter, analyst, hypecrypto, commodity, allweather, scholar; stock retired earlier) are frozen archives — 0 state changes in 24h, as expected.
- Local git clone was shallow at the start of this run (only ~50 commits, back to 01:31 UTC); had to fetch depth 1000 to cover the full 24h window before compiling this digest.
- Everything else: no red_flag.json, no exceptions or corrupted-state markers found in the data touched this window.
