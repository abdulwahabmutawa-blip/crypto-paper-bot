#!/usr/bin/env bash
# One PLAYBOOK-book cycle on the VPS (second Binance account). Mirrors
# lottery_runner.sh but runs ONLY the playbook book: the Watcher/scout/heat
# pipeline is the lottery cycle's job and both books read its committed
# outputs (breadth.json). Keys live ONLY in /etc/playbook.env — a different
# file from /etc/lottery.env, so the two books can never see each other's
# secrets even on the same box.
set -uo pipefail

# REPO LOCK (review 08-21): lottery, playbook and git-pull all share
# one worktree — serialize whole cycles so two writers can never race
# a rebase. 120s wait >> a normal cycle; timing out skips the cycle.
exec 9>/opt/tradebot/repo.lock
flock -w 120 9 || { echo "[runner] repo lock timeout — skipping cycle"; exit 0; }

REPO="${PLAYBOOK_REPO:-/opt/tradebot/cloud-bot}"
cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }

# heal any wedge a previous kill left behind
git rebase --abort 2>/dev/null || true
git merge --abort 2>/dev/null || true
find .git -maxdepth 1 -name index.lock -mmin +10 -delete 2>/dev/null || true

# bounded pull; exits must still run on cached state if the network is down
timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
  || { git rebase --abort 2>/dev/null; echo "[playbook] pull failed — running on cached state"; }

# never trade on corrupted state
if ! python3 src/state_preflight.py; then
  echo "[playbook] STATE CORRUPT — trading skipped this cycle"
  exit 1
fi

python3 src/playbook_live.py
rc=$?

cp -f data/playbook_state.json docs/playbook.json 2>/dev/null || true
[ -f data/playbook_ledger.jsonl ] && tail -100 data/playbook_ledger.jsonl > docs/playbook_ledger.jsonl

for f in data/playbook_state.json data/playbook_ledger.jsonl \
         docs/playbook.json docs/playbook_ledger.jsonl; do
  git add "$f" 2>/dev/null || true
done
if ! git diff --cached --quiet; then
  git commit -q -m "playbook: $(date -u +'%Y-%m-%d %H:%M') UTC"
  pushed=0
  for attempt in 1 2 3; do
    timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
      && timeout -k 10 60 git push -q && { pushed=1; break; }
    git rebase --abort 2>/dev/null
    echo "[playbook] push attempt $attempt failed, retrying"
    sleep 5
  done
  [ "$pushed" = "1" ] || echo "[playbook] PUSH FAILED after 3 attempts — ledger NOT published this cycle"
fi
exit $rc
