# Fleet Status — 2026-11-25 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged since 11-12, no trade | $1,027.21 |
| meanrev | JPM | Unchanged position; price drifted | $870.35 (vs $868.81 11-24) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 6/10 seats | 9 round trips closed, 5 opened, net -4 seats | $482.40 (vs $486.31 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed (~36d stale) | n/a |

## Changed
- **scalper**: 9 round trips closed and 5 new entries opened in the 24h window; seats 10/10 → 6/10; equity $486.31 → $482.40 (net -$3.91).
- **crypto, sentiment**: no trades, no position changes.
- **meanrev**: no new trade; still holding JPM. Value moved $868.81 → $870.35 on price action alone.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, `announcements.json`, btc execution samples): nothing abnormal.

## Needs a look
- **Cycle gaps**: ~4h24m (05:51→10:15 UTC 11-24) and ~4h55m (15:52→20:47 UTC 11-24) between cycles, plus a smaller 85min gap (02:26→03:51 UTC 11-25) — all above the usual ~15-25min cadence. No error text in commit messages explaining them.
- **Watcher's Grok risk scan**: unchanged since 2026-10-20T16:09 UTC — now ~36 days stale.
- **scalper seat TVKUSDT**: still open since 2026-09-12 (~74 days), past the bot's 24h hold cap — known unresolved bug, unchanged.
- **scalper equity** ($482.40) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~76 days stale.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen archives.
