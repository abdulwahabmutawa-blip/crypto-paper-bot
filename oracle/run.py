"""CLI: python -m oracle.run {predict|resolve|score|verify}

Kept as four small verbs on purpose. `predict` and `resolve` run as separate
processes so the resolver cannot see anything the forecaster held in memory.
"""
from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    cmd = argv[0] if argv else "help"

    if cmd == "predict":
        import oracle.predict as predict
        limit = None
        if "--limit" in argv:
            limit = int(argv[argv.index("--limit") + 1])
        predict.run(limit=limit)
        return 0

    if cmd == "resolve":
        import oracle.resolve as resolve
        resolve.run()
        return 0

    if cmd == "score":
        import oracle.score as score
        s = score.run()
        # a fired kill criterion must be loud and must fail the job
        return 2 if s.get("verdict", "").__contains__("KILL") else 0

    if cmd == "smoke":
        # Full pipeline against the REAL network into a scratch directory,
        # committing nothing. This exists because the first two scheduled
        # cycles failed for reasons no offline test could catch — a runner
        # geo-block, then a write-once violation — and each round trip cost
        # a manual re-run. CI now exercises the real path on every push.
        import tempfile
        from pathlib import Path
        import oracle.config as config
        tmp = Path(tempfile.mkdtemp())
        for name in ("DATA", "PREDICTIONS", "RESOLUTIONS", "SNAPSHOTS",
                     "LEDGER_DIR", "SCORES", "REPORTS", "ROOT"):
            setattr(config, name, tmp if name in ("DATA", "ROOT")
                    else tmp / name.lower())
        config.CHAIN = config.LEDGER_DIR / "chain.jsonl"
        for d in (config.PREDICTIONS, config.RESOLUTIONS, config.SNAPSHOTS,
                  config.LEDGER_DIR, config.SCORES, config.REPORTS):
            d.mkdir(parents=True, exist_ok=True)

        import oracle.predict as predict
        import oracle.resolve as resolve
        import oracle.score as score
        import oracle.ledger as ledger
        print(f"[oracle] smoke: scratch dir {tmp}")
        predict.run(limit=25)
        resolve.run()
        # twice on purpose: scoring the same day twice is what broke the
        # chain in cycle #2, so the smoke test must repeat it
        score.run()
        score.run()
        ok, problems = ledger.verify()
        if not ok:
            print("[oracle] SMOKE FAILED — chain did not verify")
            for p in problems:
                print(f"  - {p}")
            return 1
        print(f"[oracle] smoke OK — {len(ledger.read_chain())} chain entries")
        return 0

    if cmd == "verify":
        import oracle.ledger as ledger
        ok, problems = ledger.verify()
        if ok:
            n = len(ledger.read_chain())
            print(f"[oracle] chain OK — {n} entries, "
                  f"head {ledger.head()[:12]}")
            return 0
        print("[oracle] CHAIN VERIFICATION FAILED")
        for p in problems:
            print(f"  - {p}")
        print("\nA broken chain means a historical record changed. That is "
              "pre-committed kill criterion 5, not a bug to patch.")
        return 1

    print(__doc__)
    return 0 if cmd == "help" else 1


if __name__ == "__main__":
    raise SystemExit(main())
