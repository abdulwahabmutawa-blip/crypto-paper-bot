# crypto-paper-bot

Notion project page: https://app.notion.com/p/3a6632591142819289cecca55dc39533
(Command Center → Trade Bot)

## What this is
Four active $1,000 paper books run on GitHub Actions: crypto (BTC tide gauge v4),
meanrev, sentiment (Watcher + sentinel_trader), and scalper (small-wins signal
simulation). Utilities include the Watcher, exit auditor, unlock/announcement
watch, social radar and smallwins lab. Retired dashboards are frozen archives;
see `reports/kill_criteria.md`. Dashboards are bilingual (English/Arabic).

The separate lottery/IBKR paths in this repository concern real-money trading
on the VPS; they are not part of the Actions paper fleet. Never infer their
live state from a paper-fleet update.

Scalper candle-close entries are retrospective, observed later by the polling
loop. Its results are signal research, not proof of executable fills. A method
replacement requires a separate prospective record with realistic timing/costs.

`btc_execution_watch.py` now collects public BTC bid/ask depth and receipt
latency each fleet cycle. It records NO_TRADE and hypothetical execution costs;
it does not run a qualified strategy or place orders. See
`reports/btc_execution_protocol.md`; immutable samples are in
`data/btc_execution/`, latest summary in `reports/btc_execution.md`.

## Where things are
- `src/` — the bots. One `bot_*.py` / `*_tracker.py` per strategy, plus:
  - `selection_engine.py` — shared engine used by several fleet strategies; crypto,
    sentiment and scalper also have their own position/accounting code.
  - `config.py`, `market_hours.py`, `sentinel_gate.py` — shared plumbing.
  - `*_dashboard_template.html` — the bilingual dashboard templates.
- `.github/workflows/bot.yml` — the schedule that runs the fleet. Cycles commit themselves.
- `docs/` — published dashboards + their `*_dashboard_data.json`.
- `reports/` — generated reports and `attribution_summary.json`.
- `STATUS.md` — **daily digest, auto-written each morning. Read this first for "how are the bots doing".**
- Local-only notes (not in this repo): `C:\Users\Hobii\claude\trading\` on the PC.

## Findings so far (don't re-derive these)
Copying Congress does **not** beat the index. With realistic assumptions — entry on disclosure date,
benchmarked vs SPY, real $1,000 constraint — every variant lost to SPY's +32%: top-6 traders +17.2%,
all-House-buys +11.3%, cluster-buys +9.7%, big-dollar conviction +3.8%. Pelosi-only +22.5% (~+2% alpha).
Only bright spot: cluster-buys had the lowest drawdown (−21%).
Limitations: ~2.8 years / one regime (2020 boom → 2022 bust); delisting gaps; 45-day reporting lag
makes real-time copying impossible.

## Conventions
- Paper only. Test before any real money. Report findings honestly even when the thesis dies.
- The trailing-stop + cooldown risk overlay and vol-target sizing now live in
  `selection_engine.py` as opt-in SPEC keys (`risk`, `vol_target`, `signal_frame`) — used by the
  Scholar ONLY; meanrev/commodity deliberately keep running without them (uncontaminated
  experiments). The old parked patch on the PC is superseded.

---

## All of Abdulwahab's projects (shared index — same block in every repo)

This repo is one of several. If the question is about another project, go to its repo or Notion page.

| Project | Repo | Notion |
|---|---|---|
| **Seerati** (سيرتي) — AI CV / LinkedIn / uni-application services, Kuwait | `seerati` | [page](https://app.notion.com/p/3a6632591142810f8fcbcb7de3420a7c) |
| **DateShield** — edible date-palm produce coating (SACGC startup) | `dateshield` | [page](https://app.notion.com/p/3a66325911428114af42d6f55c1f4408) |
| **Dawetkom** (دعوتكم) — digital invitation cards | `dawetkom` | [page](https://app.notion.com/p/3a66325911428136a708fe3bde4b13c3) |
| **Dawetkom RSVP** — WhatsApp invites + RSVP add-on tiers | `dawetkom-rsvp` | same as Dawetkom |
| **WhatsApp Bots** — Kuwaiti-dialect booking/FAQ bots for SMBs | `whatsapp-bots` | [page](https://app.notion.com/p/3a6632591142818eb791e67451c252f0) |
| **Content Studio** — monthly reels/content packages | `content-studio` | same as WhatsApp Bots |
| **Games** (Ta2leef) — Rawr Merge, Souq Sort, Sands of the Jinn | `ta2leef-games` | [page](https://app.notion.com/p/3a663259114281269ed3e5e366703fd0) |
| **Trade Bot** — 9-bot paper-trading fleet (paper money only) | `crypto-paper-bot` | [page](https://app.notion.com/p/3a6632591142819289cecca55dc39533) |
| **Kuwaiti Energy Video** — Kuwaiti-dialect heat/energy PSA | *(no repo)* | [page](https://app.notion.com/p/3a66325911428181b1fee30b11264074) |
| **KTECH — Advising** — the day job | **no repo, by design** | [page](https://app.notion.com/p/3a6632591142818db362f051c91b7b61) |

All repos are at `https://github.com/abdulwahabmutawa-blip/<name>` — private except `crypto-paper-bot`.
Hub: **Command Center** → https://app.notion.com/p/3a6632591142813ebef5e448bf63f0b7

## Rules that apply across every project
- **KTECH advising work never goes to GitHub** — it holds real student data (names, IDs, GPAs).
- **Never sell any service to students Abdulwahab advises at KTECH.** No side-business work during
  office hours, no KTECH resources.
- **Never promise admission results or job outcomes.** No "guaranteed acceptance" language anywhere.
- All prices in KD. Arabic marketing copy → Kuwaiti dialect; client deliverables → formal Arabic or English.
- AI-draft → human review. Never send raw AI output to a client.
- Work is hybrid phone/PC: **push before leaving the PC, pull before starting on it.**
