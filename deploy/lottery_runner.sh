#!/usr/bin/env bash
# One lottery cycle on the VPS: clean the repo, pull fresh Watcher scans,
# scout, trade, publish. Invoked by lottery.timer (oneshot — cycles can
# never stack on themselves).
#
# Git discipline (audit 08-15): two writers share this repo (GitHub Actions
# and this box). Every git network call is timeout-bound, every pull uses
# -X theirs under rebase (which keeps THIS box's replayed commits for
# conflicting hunks), and a half-done rebase is aborted rather than left to
# wedge every later cycle — the 08-12 poisoning class, VPS edition.
set -uo pipefail

REPO="${LOTTERY_REPO:-/opt/tradebot/cloud-bot}"
cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }

# 0) heal any wedge a previous kill left behind. --abort restores the tree
#    AND re-applies the autostash; a stale index.lock older than 10 minutes
#    can only be a corpse (cycles finish in seconds).
git rebase --abort 2>/dev/null || true
git merge --abort 2>/dev/null || true
find .git -maxdepth 1 -name index.lock -mmin +10 -delete 2>/dev/null || true

# 1) pull fresh scans — bounded, never wedging, never fatal (exits must
#    still run on cached state if the network is down)
timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
  || { git rebase --abort 2>/dev/null; echo "[runner] pull failed — running on cached state"; }

# 2) never trade on corrupted state (the fleet's own fail-loud rule; the
#    Actions loop has this, the VPS didn't until the audit called it)
if ! python3 src/state_preflight.py; then
  echo "[runner] STATE CORRUPT — trading skipped this cycle; fix data/*.json"
  exit 1
fi

# 3) heat map first (cross-source social agreement), then the Scout which
#    consumes it — both write files the book reads this same cycle
python3 src/social_heat.py || echo "[runner] heat map failed — scout runs without the heat surface"
python3 src/binance_scout.py || echo "[runner] scout failed — book falls back to Watcher-only"

python3 src/lottery_live.py
rc=$?

# 4) publish where GitHub Pages can serve it (data/ is not served):
#    state verbatim, ledger trimmed for the phone page
cp -f data/lottery_state.json docs/lottery.json 2>/dev/null || true
cp -f data/scout_signals.json docs/scout.json 2>/dev/null || true
[ -f data/lottery_ledger.jsonl ] && tail -100 data/lottery_ledger.jsonl > docs/lottery_ledger.jsonl

# stage per-file: one missing pathspec must not abort the whole add
for f in data/lottery_state.json data/lottery_ledger.jsonl \
         data/scout_signals.json data/scout_scorecard.json data/scout_log.jsonl \
         data/social_heat.json \
         docs/lottery.json docs/scout.json docs/lottery_ledger.jsonl; do
  git add "$f" 2>/dev/null || true
done
if ! git diff --cached --quiet; then
  git commit -q -m "lottery: $(date -u +'%Y-%m-%d %H:%M') UTC"
  pushed=0
  for attempt in 1 2 3; do
    timeout -k 10 60 git pull --rebase --autostash -X theirs -q \
      && timeout -k 10 60 git push -q && { pushed=1; break; }
    git rebase --abort 2>/dev/null
    echo "[runner] push attempt $attempt failed, retrying"
    sleep 5
  done
  # a silent publish failure hides real fills from the owner's phone —
  # say it loudly in the journal (the commit is safe locally; the next
  # cycle's push carries it)
  [ "$pushed" = "1" ] || echo "[runner] PUSH FAILED after 3 attempts — ledger NOT published this cycle"
fi
exit $rc
