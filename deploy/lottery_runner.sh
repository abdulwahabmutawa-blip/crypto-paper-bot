#!/usr/bin/env bash
# One lottery cycle on the VPS: refresh Watcher scans, run the bot, publish
# its ledger. Invoked by lottery.timer — never run as a background loop, so
# a hung cycle can never stack on itself.
#
# Order matters: the bot reads data/sentinel_state.json for hype candidates,
# and that file is written by the GitHub Actions fleet — so PULL FIRST or the
# bot trades on yesterday's euphoria.
set -uo pipefail

REPO="${LOTTERY_REPO:-/opt/tradebot/cloud-bot}"
cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }

# stale scans are handled inside the bot (it grounds itself), so a failed
# pull is a warning, never a reason to skip the cycle: exits must still run
git pull --rebase --autostash -q || echo "[runner] pull failed — running on cached state"

# the Scout first: it writes data/scout_signals.json, which the book reads
# this same cycle — fresh signals, not last cycle's leftovers
python3 src/binance_scout.py || echo "[runner] scout failed — book falls back to Watcher-only"

python3 src/lottery_live.py
rc=$?

# publish the book where GitHub Pages can serve it (data/ is not served):
# state verbatim, ledger trimmed to the last 100 lines for the phone page
cp -f data/lottery_state.json docs/lottery.json 2>/dev/null || true
cp -f data/scout_signals.json docs/scout.json 2>/dev/null || true
[ -f data/lottery_ledger.jsonl ] && tail -100 data/lottery_ledger.jsonl > docs/lottery_ledger.jsonl

git add data/lottery_state.json data/lottery_ledger.jsonl \
        data/scout_signals.json data/scout_scorecard.json data/scout_log.jsonl \
        docs/lottery.json docs/scout.json docs/lottery_ledger.jsonl 2>/dev/null
if ! git diff --cached --quiet; then
  git commit -q -m "lottery: $(date -u +'%Y-%m-%d %H:%M') UTC"
  for attempt in 1 2 3; do
    git pull --rebase --autostash -q && git push -q && break
    echo "[runner] push attempt $attempt failed, retrying"
    sleep 5
  done
fi
exit $rc
