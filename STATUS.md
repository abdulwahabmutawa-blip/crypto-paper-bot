# Fleet Status — 2026-11-17 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged, no new trade since 11-12 sell | $1,027.21 |
| meanrev | **NVDA** | Re-entered NVDA 11-16 (bought dip, 6.2978 units @ $158.73) after 7 days in cash | $983.46 (vs $1,000.74 yday) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats (full) | 23 round trips closed (14 win/9 loss, net +$5.89) | $500.88 (vs $493.13 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed | n/a |

## Changed
- **meanrev**: flipped from CASH to **NVDA** on 2026-11-16 — bought the dip at $158.73 (6.2978 units, $999.64) on a oversold-mega-cap signal. First trade since the 11-09 trailing-stop sell. Value $1,000.74 → $983.46 (down with NVDA's own move since entry, stock data as-of 11-16 close — no newer print yet).
- **scalper**: 23 round trips closed in the last 24h — 14 wins, 9 losses, net +$5.89. Equity $493.13 → $500.88. Seats remain 10/10 (full); TVKUSDT (the stuck seat) still open.
- **crypto, sentiment**: no trades, no position changes. Values flat vs yesterday.
- GitHub Actions `paper-trade-cycle`: 50 cycle commits in the window, running 2026-11-16 10:54 UTC → 2026-11-17 04:54 UTC. Two multi-hour gaps (13:36→16:15, 21:54→00:24) are the documented GitHub schedule-throttling behavior (see `.github/workflows/bot.yml` comments), not failures. No failed or error commits found.

## Needs a look
- **Watcher's Grok risk scan still stale**: `data/sentinel_verdict.json`-equivalent (`sentinel_state.json.last_scan_utc`) unchanged since 2026-10-20T16:09 UTC — now ~661h (~27.5 days) old. `sentinel_gate.severe()` treats verdicts older than 24h as UNKNOWN — risk gate still running blind. Unresolved, growing.
- **scalper** seat **TVKUSDT still open since 2026-09-12** (~66 days) — past the bot's 24h hold cap; known unresolved bug, not new this run.
- **scalper** equity $500.88 remains below the R1 hard-stop floor ($750, -25%); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 2026-10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-11 — still unmoved for over two months.
- **Scheduled-task roster mismatch (recurring)**: today's digest instructions again describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md / `reports/kill_criteria.md`, congress/commodity/allweather/hype/hunter/stock/scholar/analyst are retired, frozen archives. The active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher.
- Lottery/IBKR activity (real-money VPS path) is out of scope for this digest per CLAUDE.md.
