#!/usr/bin/env bash
# One Oracle cycle on the VPS. Predict-only: this script never touches
# /etc/lottery.env and the oracle package cannot import a broker (enforced
# by tests/test_oracle.py in CI).
#
# Git discipline mirrors lottery_runner.sh — two writers share this repo, so
# every network call is timeout-bound and a half-done rebase is aborted
# rather than left to wedge the next cycle.
set -uo pipefail

REPO="${ORACLE_REPO:-/opt/tradebot/cloud-bot}"
cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }

git rebase --abort 2>/dev/null || true
find .git -maxdepth 1 -name index.lock -mmin +10 -delete 2>/dev/null || true
timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
  || { git rebase --abort 2>/dev/null; echo "[oracle] pull failed — running on cached state"; }

# Separate processes: the resolver must not inherit the forecaster's memory.
python3 -m oracle.run predict || echo "[oracle] predict failed this cycle"
python3 -m oracle.run resolve || echo "[oracle] resolve failed this cycle"
python3 -m oracle.run score   || echo "[oracle] score failed this cycle"

# Refuse to publish a record that does not verify. A broken chain is
# pre-committed kill criterion 5, not something to commit over.
if ! python3 -m oracle.run verify; then
  echo "[oracle] CHAIN VERIFICATION FAILED — not committing this cycle"
  exit 1
fi

git add oracle/data 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -q -m "oracle: $(date -u +'%Y-%m-%d %H:%M') UTC"
  for attempt in 1 2 3; do
    timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
      && timeout -k 10 60 git push -q && exit 0
    git rebase --abort 2>/dev/null
    echo "[oracle] push attempt $attempt failed, retrying"
    sleep 5
  done
  echo "[oracle] PUSH FAILED after 3 attempts — record is safe locally"
fi
