# Fleet status — 2026-08-23 (UTC)

9 paper bots ($1,000 each, no real money) + Watcher (Grok risk gate) + Lottery (REAL money, VPS) + 1 unverified book (playbook).

| Bot | Holds | 24h change | Value (asof) |
|---|---|---|---|
| crypto (trend) | XRP-USD | No trade | $1,177.33 (08-23) |
| congress | 10 positions | No trade | $990.44 (08-21) |
| meanrev | UNH | No trade | $1,196.26 (08-21) |
| commodity | USO | No trade | $1,049.33 (08-21) |
| allweather | 5-asset basket | No trade | $1,026.58 (08-21) |
| hype (sentiment) | MRNA | No trade | $1,518.86 (08-21) |
| hypecrypto | CASH | Round-tripped ENA-USD (Grok hype signal), hype faded → cash | $942.14 (08-23) |
| Hunter | SOL-USD | SOLD BTC-USD ("outgunned" on reward/risk) → BUY SOL-USD, all-in | $895.79 (08-23) |
| Scholar | SPY | No trade | $1,014.39 (08-21) |
| Analyst | SPY | No trade | $1,019.97 (08-21) |
| Watcher (sentinel) | — (risk gate, no position) | Scanning normally, verdict = CAUTION (yields/oil, crypto liquidations) | n/a |
| **Lottery (REAL $)** | CASH | 2 losing round trips: ESPUSDT −$0.44, XRPUSDT ×2 (−$1.49, −$0.20) → cash | $52.38 (08-23) |

## Changed
- hypecrypto: bought/sold ENA-USD same day chasing a Grok euphoria signal; hype faded, cost ~$53 (5.3% of book), ended in cash.
- Hunter: sold BTC-USD (Solana scored >1.25x better reward/risk), went all-in SOL-USD.
- Lottery (real $): two more losing round trips (ESPUSDT, XRPUSDT ×2, all "hype faded" / "fuel gone" exits), book $54.07 → $52.38.
- crypto, congress, meanrev, commodity, allweather, hype, Scholar, Analyst: no position changes — stock/weekend bots last marked 08-21 (Fri close), normal for a Sunday.
- 111 paper-bot cycles + 259 lottery cycles in the last 24h, largest gap 14.5 min — cadence healthy, no missed crons.

## Needs a look
- Analyst cash is −$0.85, same as yesterday — looks like the same fee/rounding artifact, not worsening.
- hypecrypto and Hunter both churned into same-day losing trades today (ENA round trip, BTC→SOL flip) — same fast-turnover pattern flagged in prior digests; still worth confirming transaction costs aren't quietly eating gains.
- Fleet is bigger than CLAUDE.md's documented "9 bots + Watcher" list: Analyst, hypecrypto (separate from hype/sentiment), Lottery (real money), an oracle-bot pipeline, and an undocumented `playbook_state.json` bot (created 08-21, still flat/no trades) all exist in `data/` — carried over from prior digests, still unreconciled with the docs.
- Nothing else broken today: no exceptions/error fields found in any bot's state file, no stalled or skipped cycles, Watcher/sentinel scanning on schedule (last scan 04:31 UTC).
