"""Fail-loud state preflight — a cycle must not run on corrupted state.

2026-08-12 incident: a mid-loop rebase left conflict markers inside
data/*.json; 225 JSONDecodeError crashes across 25 cycles were swallowed by
the per-bot `|| warning` and every run reported green. This script is the
inversion: it runs BEFORE the bots each cycle, and any unparseable state
file aborts the whole loop with a red workflow run and a committed red-flag
file the fleet dashboard shows.

Exit 0: all data/*.json parse (also clears a stale docs/red_flag.json).
Exit 1: at least one is corrupt; docs/red_flag.json written with details.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone

import config

RED_FLAG = config.ROOT / "docs" / "red_flag.json"


def main() -> int:
    failures = []
    for p in sorted(config.DATA.glob("*.json")):
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            failures.append({"file": p.name, "error": f"{type(e).__name__}: {e}"[:200]})
    if not failures:
        if RED_FLAG.exists():
            RED_FLAG.unlink()
            print("[preflight] previous red flag cleared — state healthy again")
        else:
            print(f"[preflight] state OK")
        return 0
    RED_FLAG.write_text(json.dumps({
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "what": "STATE CORRUPTION — trading loop aborted before any bot ran",
        "failures": failures,
        "action": "fix data/*.json by hand (usually leftover rebase conflict "
                  "markers), commit, and the next loop resumes",
    }, indent=2))
    for f in failures:
        print(f"[preflight] CORRUPT {f['file']}: {f['error']}", file=sys.stderr)
    print(f"[preflight] {len(failures)} corrupt state file(s) — RED FLAG "
          f"written, aborting loop", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
