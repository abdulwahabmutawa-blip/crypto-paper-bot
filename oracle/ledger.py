"""Append-only hash chain over every artifact the experiment produces.

Why a chain and not just git: git history can be rewritten with a
force-push, and pre-registrations that rely on human discipline drift by
default — not from dishonesty, but because a well-meaning "fix" months in
looks harmless at the time. Each entry commits to the sha256 of the file it
describes AND to the previous entry, so any later edit of any historical
record breaks every entry after it. CI rebuilds the chain on every push.

The chain proves ORDER and CONTENT. It does not prove wall-clock time; that
would need an external anchor, deliberately deferred (see README).
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import oracle.config as config

GENESIS = "0" * 64


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _canonical(entry: dict) -> str:
    """Deterministic serialisation for hashing: sorted keys, no spaces, and
    chain_self excluded (it is the hash OF this)."""
    body = {k: v for k, v in entry.items() if k != "chain_self"}
    return json.dumps(body, sort_keys=True, separators=(",", ":"))


def read_chain() -> list[dict]:
    if not config.CHAIN.exists():
        return []
    out = []
    for line in config.CHAIN.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def head() -> str:
    chain = read_chain()
    return chain[-1]["chain_self"] if chain else GENESIS


def append(kind: str, path: Path, n_records: int, extra: dict | None = None
           ) -> dict:
    """Commit a produced file to the chain. Returns the new entry."""
    chain = read_chain()
    entry = {
        "seq": len(chain) + 1,
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "kind": kind,
        "path": str(path.relative_to(config.ROOT)).replace("\\", "/"),
        "file_sha256": sha256_file(path),
        "n_records": n_records,
        "generation_id": config.GENERATION_ID,
        "chain_prev": chain[-1]["chain_self"] if chain else GENESIS,
        **(extra or {}),
    }
    entry["chain_self"] = sha256_text(_canonical(entry))
    # newline="\n" on EVERY artifact write, without exception: Python
    # translates "\n" to "\r\n" on Windows, git normalises it back to "\n"
    # on commit, and the chain then hashes different bytes than CI checks
    # out — which broke verification on day one. The record must be
    # byte-identical on every platform or it proves nothing.
    with config.CHAIN.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(entry, sort_keys=True) + "\n")
    return entry


def verify() -> tuple[bool, list[str]]:
    """Rebuild the chain and re-hash every file it references.

    Returns (ok, problems). Any break means a historical record changed —
    which is a pre-committed kill criterion, not something to patch over.
    """
    problems: list[str] = []
    prev = GENESIS
    for e in read_chain():
        if e.get("chain_prev") != prev:
            problems.append(f"seq {e.get('seq')}: chain_prev mismatch "
                            f"(expected {prev[:12]}, "
                            f"got {str(e.get('chain_prev'))[:12]})")
        recomputed = sha256_text(_canonical(e))
        if recomputed != e.get("chain_self"):
            problems.append(f"seq {e.get('seq')}: entry hash mismatch — "
                            f"the ledger line itself was edited")
        p = config.ROOT / e["path"]
        if not p.exists():
            problems.append(f"seq {e.get('seq')}: missing file {e['path']}")
        elif sha256_file(p) != e.get("file_sha256"):
            problems.append(f"seq {e.get('seq')}: CONTENT CHANGED "
                            f"for {e['path']}")
        prev = e.get("chain_self", prev)
    return (not problems), problems
