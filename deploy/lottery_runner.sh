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

# REPO LOCK (review 08-21): lottery, playbook and git-pull all share
# one worktree — serialize whole cycles so two writers can never race
# a rebase. 120s wait >> a normal cycle; timing out skips the cycle.
exec 9>/opt/tradebot/repo.lock
flock -w 120 9 || { echo "[runner] repo lock timeout — skipping cycle"; exit 0; }

REPO="${LOTTERY_REPO:-/opt/tradebot/cloud-bot}"
cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }

# 0) heal any wedge a previous kill left behind. --abort restores the tree
#    AND re-applies the autostash; a stale index.lock older than 10 minutes
#    can only be a corpse (cycles finish in seconds).
git rebase --abort 2>/dev/null || true
git merge --abort 2>/dev/null || true
find .git -maxdepth 1 -name index.lock -mmin +10 -delete 2>/dev/null || true

# 0b) UNMERGED INDEX ENTRIES (incident 2026-08-25, and the likely 09-01
#     silence): a host event killed a cycle mid `pull --rebase --autostash`,
#     the stash-pop left stage-2/stage-3 entries with no MERGE_HEAD, and
#     --abort cannot see them — so every later cycle RAN but could not
#     pull, commit or push until a human SSHed in. Heal mechanically and
#     direction-agnostically (stage numbering flips between rebase and
#     stash-pop, so never trust "ours"/"theirs"): append-only logs keep the
#     side with MORE lines, the state file keeps the side with the NEWER
#     last_updated_utc, everything else (caches, generated files) takes the
#     committed HEAD and regenerates next cycle.
if [ -n "$(git ls-files -u 2>/dev/null)" ]; then
  echo "[runner] HEAL: unmerged index entries — resolving mechanically"
  git ls-files -u | awk '{print $4}' | sort -u | while read -r f; do
    python3 - "$f" <<'PY'
import json, subprocess, sys
f = sys.argv[1]
def stage(n):
    r = subprocess.run(["git", "show", f":{n}:{f}"], capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None
a, b = stage(2), stage(3)
pick = None
if a is not None and b is not None:
    if f.endswith(".jsonl"):
        pick = a if a.count("\n") >= b.count("\n") else b
    elif f == "data/lottery_state.json":
        def ts(s):
            try:
                return json.loads(s).get("last_updated_utc") or ""
            except Exception:
                return ""
        pick = a if ts(a) >= ts(b) else b
if pick is None:
    subprocess.run(["git", "checkout", "HEAD", "--", f], capture_output=True)
else:
    open(f, "w", encoding="utf-8", newline="").write(pick)
subprocess.run(["git", "add", "--", f], capture_output=True)
print(f"[runner]   healed {f} ({'content rule' if pick is not None else 'HEAD'})")
PY
  done
  git stash drop -q 2>/dev/null || true
  git commit -q -m "lottery: heal unmerged index $(date -u +'%Y-%m-%d %H:%M') UTC" 2>/dev/null \
    || git reset -q 2>/dev/null || true
fi

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

# 3) the Watcher first (needs XAI_API_KEY in /etc/lottery.env; without it
#    this is a graceful one-line skip). Self-throttled to its 2h cadence,
#    so most cycles it costs a second. Running it HERE frees scans from
#    GitHub Actions' ~6% scheduler-acceptance — the reason the Watcher
#    went silent for hours at a time. Actions still runs it too as a
#    backup; the shared last_scan_utc throttle dedupes the two hosts, and
#    a rare same-window race costs one overwritten scan, nothing worse.
python3 src/grok_sentinel.py || echo "[runner] watcher scan failed — riding the last committed scan"
# social radar (08-23): learn which X chatter precedes rises; observation only
python3 src/social_radar.py || echo "[runner] social radar failed — labels ride next cycle"
# then the heat map (cross-source social agreement), then the Scout which
# consumes both — all write files the book reads this same cycle
python3 src/social_heat.py || echo "[runner] heat map failed — scout runs without the heat surface"
python3 src/binance_scout.py || echo "[runner] scout failed — book falls back to Watcher-only"
# exchange announcements (08-23): delisting instant-exit + entry veto
python3 src/announcement_watch.py || echo "[runner] announcements fetch failed — riding the last file"
# publish the sentinel dashboard the same way the Actions loop does
cp -f reports/sentinel_dashboard.html docs/sentinel.html 2>/dev/null || true

python3 src/lottery_live.py 2>&1 | tee /tmp/lottery_cycle.log
rc=${PIPESTATUS[0]}

# 3b) A CRASHED CYCLE MUST BE VISIBLE ON THE PHONE (incident 2026-09-01: the
#     book died every cycle for 30 hours with a real position open and the
#     only symptom was a dashboard that quietly stopped updating). A non-zero
#     exit writes docs/lottery_red_flag.json with the traceback tail; the
#     phone page shows it in red; a clean cycle removes it.
python3 - "$rc" <<'PY'
import json, pathlib, sys
from datetime import datetime, timezone
rc = int(sys.argv[1])
flag = pathlib.Path("docs/lottery_red_flag.json")
log = pathlib.Path("/tmp/lottery_cycle.log")
if rc != 0:
    tail = log.read_text(encoding="utf-8", errors="replace").splitlines()[-30:] \
        if log.exists() else []
    flag.write_text(json.dumps({
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "what": f"lottery_live.py exited {rc} — exits/entries did NOT complete this cycle",
        "tail": tail,
    }, indent=1), encoding="utf-8")
    print(f"[runner] RED FLAG written — lottery_live.py exited {rc}")
elif flag.exists():
    flag.unlink()
    print("[runner] red flag cleared — cycle completed")
PY

# 4) publish where GitHub Pages can serve it (data/ is not served):
#    state verbatim, ledger trimmed for the phone page
cp -f data/lottery_state.json docs/lottery.json 2>/dev/null || true
cp -f data/scout_signals.json docs/scout.json 2>/dev/null || true
[ -f data/lottery_ledger.jsonl ] && tail -100 data/lottery_ledger.jsonl > docs/lottery_ledger.jsonl

# stage per-file: one missing pathspec must not abort the whole add
for f in data/lottery_state.json data/lottery_ledger.jsonl \
         data/scout_signals.json data/scout_scorecard.json data/scout_log.jsonl \
         data/social_heat.json data/breadth.json \
         data/sentinel_state.json data/sentinel_verdict.json \
         data/announcements.json data/surge_signals.json data/surge_log.jsonl \
         data/social_radar_log.jsonl data/social_radar_card.json data/social_radar_state.json reports/social_radar.md \
         docs/sentinel.html \
         docs/lottery.json docs/scout.json docs/lottery_ledger.jsonl; do
  git add "$f" 2>/dev/null || true
done
# the red flag is added OR removed: stage its deletion too
git add -A docs/lottery_red_flag.json 2>/dev/null || true
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
