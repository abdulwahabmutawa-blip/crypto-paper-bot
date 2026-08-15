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

python3 src/lottery_live.py
rc=$?

git add data/lottery_state.json data/lottery_ledger.jsonl 2>/dev/null
if ! git diff --cached --quiet; then
  git commit -q -m "lottery: $(date -u +'%Y-%m-%d %H:%M') UTC"
  for attempt in 1 2 3; do
    git pull --rebase --autostash -q && git push -q && break
    echo "[runner] push attempt $attempt failed, retrying"
    sleep 5
  done
fi
exit $rc
