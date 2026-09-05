#!/usr/bin/env bash
# One hype-trader cycle against IBKR (paper or live by port). Invoked by
# hype_ibkr.timer on weekdays during US regular hours. Shares the repo lock
# with the lottery runner so the two never race a git operation.
set -uo pipefail
exec 9>/opt/tradebot/repo.lock
flock -w 120 9 || { echo "[hype-ibkr] repo lock timeout — skipping cycle"; exit 0; }
REPO="${LOTTERY_REPO:-/opt/tradebot/cloud-bot}"
cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }
timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
  || { git rebase --abort 2>/dev/null; echo "[hype-ibkr] pull failed — running on cached state"; }
python3 src/hype_ibkr.py 2>&1 | tee /tmp/hype_ibkr_cycle.log
rc=${PIPESTATUS[0]}
for f in data/hype_ibkr_state.json data/hype_ibkr_ledger.jsonl; do git add "$f" 2>/dev/null || true; done
if ! git diff --cached --quiet; then
  git commit -q -m "hype-ibkr: $(date -u +'%Y-%m-%d %H:%M') UTC"
  for attempt in 1 2 3; do
    timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
      && timeout -k 10 60 git push -q && break
    git rebase --abort 2>/dev/null; sleep 5
  done
fi
exit $rc
