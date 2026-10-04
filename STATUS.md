# Fleet status — 2026-10-04 (UTC)

| Bot | Holds | 24h change | Value |
|---|---|---|---|
| crypto | BTC-USD | No trade; small BTC drift | $1,210.52 (was $1,206.91 on 10-02) |
| meanrev | JNJ | No trade; no new daily mark (weekend) | $1,115.82 (last mark 10-02, Fri) |
| sentiment | CASH | No activity — Watcher feed stale (see below) | $869.30 (flat) |
| scalper | 10/10 seats (full) | 21 round trips, 6 targets / 9 stops / 6 time-exits, net -$13.13 | $853.24 (was $868.34) |
| Watcher (sentinel) | — | No new scan | last scan 2026-09-11 (day 23) |

## Changed
- scalper: 21 round trips closed (6 TARGET / 9 STOP / 6 TIME), net -$13.13 realized; seats filled 9 → 10 (full book).
- crypto, sentiment: no position changes, no new trades.
- meanrev: no position change; no new daily mark posted 10-03 or 10-04 — stock market closed (Sat/Sun), last mark is Friday 10-02. Expected, not an error.

## Needs a look
- Watcher (sentinel) has not produced a scan since 2026-09-11 (23 days now, up from 22 yesterday). sentiment stays idle while it's down — pre-existing, known issue, not new today.
- scalper's TVKUSDT seat (stake $86.17) has been open since 2026-09-12 (day 21) carrying the corrupted entry timestamp (resolves to Nov 2023). Flagged before and still unresolved.
- Git history visible to this session only goes back to 2026-10-04 01:37 UTC (~3.5h), not a true 24h window — the shallow clone's 50-commit cap is eaten by frequent `lottery:` commits (unrelated VPS real-money path, out of scope here per CLAUDE.md). Round-trip/P&L stats above come from the full trade log embedded in `data/scalper_state.json` (reliable), but cron-cadence claims for hours before 01:37 UTC can't be verified from commits.
- This fleet is 4 active paper books (crypto, meanrev, sentiment, scalper) plus the non-capital Watcher, per CLAUDE.md/kill_criteria.md — unchanged from yesterday.
