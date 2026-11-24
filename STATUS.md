# Fleet Status — 2026-11-24 UTC

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto (BTC tide gauge v4) | CASH | Unchanged since 11-12, no trade | $1,027.21 |
| meanrev | JPM | Unchanged position; price drifted up | $868.81 (vs $851.86 11-20) |
| sentiment (Watcher + sentinel_trader) | CASH | Unchanged, still R1-frozen since 10-12 | $726.83 |
| scalper | 10/10 seats | 34 round trips closed (22W/12L, net +$6.36) | $486.31 (vs $480.79 yday) |
| Watcher (sentinel, no capital) | — | Grok risk scan still NOT refreshed (~35d stale) | n/a |

## Changed
- **scalper**: 34 round trips closed in the 24h window (22 wins, 12 losses, net +$6.36); equity $480.79 → $486.31. Seats held at 10/10, same rotation pattern.
- **crypto, sentiment**: no trades, no position changes.
- **meanrev**: no new trade; still holding JPM from the 11-20 trailing-stop re-entry. Value moved from $851.86 to $868.81 on price action alone.
- Routine data refreshes (`social_radar.md`, `smallwins.md`, `announcements.json`, btc execution samples): nothing abnormal.
- Full 24h of commit history was available this run (prior shallow-clone limitation did not recur).

## Needs a look
- **Cycle gap, 2026-11-23**: ~6h12m between the 12:19 and 17:59 UTC cycles (vs. the usual ~17-25 min cadence) — larger than the previously-documented ~2h GH Actions throttling gap. No error text in commit messages explaining it; worth checking Actions run history if it recurs. One smaller 130min gap (08:02→10:08) also present.
- **Watcher's Grok risk scan**: unchanged since 2026-10-20T16:09 UTC — now ~35 days stale.
- **scalper seat TVKUSDT**: still open since 2026-09-12 (~73 days), past the bot's 24h hold cap — known unresolved bug, unchanged.
- **scalper equity** ($486.31) remains below the R1 hard-stop floor ($750); no retirement action taken (known open item, human call).
- **sentiment** remains R1-frozen in CASH at $726.83 since 10-12; un-freeze or formal retirement still undecided.
- `exit_auditor`'s `data/exit_audit.jsonl` has no new entries since 2026-09-10 — ~75 days stale.
- **Scheduled-task roster mismatch (recurring)**: this digest's stored instructions describe a 9-bot fleet (trend, regime, congress, meanrev, commodity, allweather, hype, Hunter, Watcher) that doesn't match the actual roster. Per CLAUDE.md, the active paper fleet is 4 books — crypto, meanrev, sentiment, scalper — plus the non-capital Watcher; the others are retired/frozen archives.
