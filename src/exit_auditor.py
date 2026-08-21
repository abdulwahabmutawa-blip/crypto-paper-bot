"""Exit-timing auditor — the bot grading its own exits, every cycle.

WHY (owner-directed 2026-08-21): the manual 21-trade study found the book's
signature error is EARLY exits (9 early, 9 early-AND-late, 3 well-timed,
0 purely late), concentrated entirely in the stall clock — stalls gave back
only +1.5% of peak on average but the coins ran +6.5% within 24h of the
sell, while genuine lateness lived only in the dead hype-faded lane (+7.7%
giveback). That pattern was invisible for two weeks because nobody was
measuring it. This module makes the measurement continuous, so "are we
selling too early or too late" is a dashboard fact rather than a study
someone has to remember to run.

MEASUREMENT ONLY. Reads the realized ledger, fetches public klines, writes
an audit file and a report. It changes no trading behavior — any rule
change still goes through the owner and the freeze calendar.

Per exit, once its 24h post-exit window has fully elapsed:
  mfe       — best price seen while held, vs entry (what was available)
  giveback  — mfe minus realized pnl (what the exit let evaporate)
  post_max  — best price in the 24h AFTER the exit, vs exit price
  post_min  — worst price in that window, vs exit price
Verdict (3% of entry either way, same thresholds as the founding study):
  TOO LATE  — giveback >= 3%   (rode down off the in-hold peak)
  TOO EARLY — post_max >= 3%   (the coin kept going without us)
  BOTH / WELL-TIMED otherwise.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "data" / "lottery_state.json"
STATE2 = ROOT / "data" / "playbook_state.json"   # book #2 (08-21): same
                                                 # grading, dry-runs skipped
AUDIT = ROOT / "data" / "exit_audit.jsonl"
REPORT_JSON = ROOT / "reports" / "exit_timing.json"
REPORT_MD = ROOT / "reports" / "exit_timing.md"

# same host order as oracle/config.py: the mirror first (Actions runners
# are US-hosted and api.binance.com geo-blocks them with 451)
HOSTS = ("https://data-api.binance.vision", "https://api.binance.com")
DAY_MS = 86_400_000
THRESH = 0.03           # the founding study's early/late line
MAX_PER_CYCLE = 8       # audits are idempotent; don't hammer the API
MAX_AGE_DAYS = 14       # klines older than this aren't worth backfilling


def _klines(sym: str, start_ms: int, end_ms: int, interval: str) -> list:
    q = urllib.parse.quote(sym)
    for host in HOSTS:
        url = (f"{host}/api/v3/klines?symbol={q}&interval={interval}"
               f"&startTime={start_ms}&endTime={end_ms}&limit=1000")
        for _ in range(2):
            try:
                with urllib.request.urlopen(url, timeout=15) as r:
                    return json.load(r)
            except Exception:
                time.sleep(1.0)
    return []


def _ms(iso: str) -> int:
    return int(datetime.fromisoformat(iso).timestamp() * 1000)


def _verdict(giveback: float, post_max: float) -> str:
    late, early = giveback >= THRESH, post_max >= THRESH
    if late and early:
        return "BOTH"
    if late:
        return "TOO_LATE"
    if early:
        return "TOO_EARLY"
    return "WELL_TIMED"


def _audit_one(t: dict) -> dict | None:
    entry, exitp = t.get("entry_price"), t.get("exit_price")
    if not (entry and exitp and t.get("entry_time") and t.get("exit_time")):
        return None
    e, x = _ms(t["entry_time"]), _ms(t["exit_time"])
    hold = _klines(t["symbol"], e, x, "5m")
    post = _klines(t["symbol"], x, x + DAY_MS, "15m")
    if not hold or not post:
        return None
    mfe = max(float(k[2]) for k in hold) / entry - 1
    realized = exitp / entry - 1
    giveback = mfe - realized
    post_max = max(float(k[2]) for k in post) / exitp - 1
    post_min = min(float(k[3]) for k in post) / exitp - 1
    # exit family = first word(s) before the em-dash flourish; stable key
    fam = t.get("reason", "").split("(")[0].split("—")[0].strip()[:24] or "?"
    return {
        "symbol": t["symbol"], "date": t.get("date"),
        "source": t.get("source"), "family": fam,
        "exit_time": t["exit_time"], "pnl_pct": t.get("pnl_pct"),
        "mfe_pct": round(mfe * 100, 2),
        "giveback_pct": round(giveback * 100, 2),
        "post24h_max_pct": round(post_max * 100, 2),
        "post24h_min_pct": round(post_min * 100, 2),
        "verdict": _verdict(giveback, post_max),
        "audited_utc": datetime.now(timezone.utc).isoformat(
            timespec="seconds"),
    }


def _key(t: dict) -> str:
    return f"{t.get('symbol')}|{t.get('exit_time')}"


def run() -> None:
    if not STATE.exists():
        return
    st = json.loads(STATE.read_text(encoding="utf-8"))
    done: set[str] = set()
    rows: list[dict] = []
    if AUDIT.exists():
        for line in AUDIT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                rows.append(r)
                done.add(f"{r['symbol']}|{r['exit_time']}")

    # both books feed one audit stream; each row already carries `source`,
    # and dry-run rows (playbook unarmed) are simulations, never audited
    realized = list(st.get("realized", []))
    if STATE2.exists():
        try:
            st2 = json.loads(STATE2.read_text(encoding="utf-8"))
            realized += [t for t in st2.get("realized", [])
                         if not t.get("dry_run")]
        except Exception:
            pass

    now_ms = time.time() * 1000
    new = 0
    for t in realized:
        if _key(t) in done or not t.get("exit_time"):
            continue
        x = _ms(t["exit_time"])
        # audit only once the 24h post-window has fully elapsed, and skip
        # ancient exits (their manual audit already lives in the research
        # folder; klines beyond MAX_AGE_DAYS aren't worth re-pulling)
        if now_ms - x < DAY_MS or now_ms - x > MAX_AGE_DAYS * DAY_MS:
            continue
        rec = _audit_one(t)
        if rec:
            with AUDIT.open("a", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps(rec, sort_keys=True) + "\n")
            rows.append(rec)
            new += 1
            print(f"[exit_auditor] {rec['symbol']} {rec['verdict']} "
                  f"(giveback {rec['giveback_pct']:+.1f}%, "
                  f"post24h max {rec['post24h_max_pct']:+.1f}%)")
        if new >= MAX_PER_CYCLE:
            break
        time.sleep(0.3)

    # market capture (owner-directed 08-21): the 08-15..08-21 rally made
    # BTC +22% while this book made -7% — and nobody was measuring the gap.
    # Book return vs BTC/ETH over the last 24h and since inception, every
    # cycle, so "did we capture the market?" is a published number.
    capture = None
    try:
        book = float(st.get("last_value_usd") or 0)
        t0 = _ms("2026-08-15T00:00:00+00:00")     # book inception, $40
        now = int(time.time() * 1000)
        capture = {"book_since_inception_pct":
                   round((book / 40.0 - 1) * 100, 2)}
        for sym in ("BTCUSDT", "ETHUSDT"):
            ks = _klines(sym, t0, now, "1d")
            if ks:
                o, c = float(ks[0][1]), float(ks[-1][4])
                capture[f"{sym[:3].lower()}_since_inception_pct"] = round(
                    (c / o - 1) * 100, 2)
                if len(ks) >= 2:
                    capture[f"{sym[:3].lower()}_last24h_pct"] = round(
                        (c / float(ks[-2][4]) - 1) * 100, 2)
    except Exception:
        capture = None

    # ALPHA BY REGIME (owner-directed 08-21, second directive of the day):
    # "do not get fooled by a good market day." Raw book return conflates
    # skill with tide — on 08-21 the book made +4.1% while BTC made +5.9%,
    # which is UNDERPERFORMANCE dressed as a win. The honest score is the
    # daily PAIRED gap (book minus BTC), grouped by what kind of day the
    # market had. Skill = a non-negative gap on flat and red days; a green-
    # day gap proves nothing except beta. Same pairing discipline as the
    # Oracle's scorer, applied to the real book.
    alpha = None
    try:
        daily: dict[str, float] = {}
        for t in st.get("realized", []):
            d = t.get("date")
            if d and t.get("pnl_usd") is not None:
                daily[d] = daily.get(d, 0.0) + float(t["pnl_usd"])
        t0 = _ms("2026-08-15T00:00:00+00:00")
        btc = _klines("BTCUSDT", t0, int(time.time() * 1000), "1d")
        book_val, per_day = 40.0, []
        for k in btc:
            day = datetime.fromtimestamp(
                float(k[0]) / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
            btc_ret = float(k[4]) / float(k[1]) - 1
            book_ret = daily.get(day, 0.0) / book_val
            book_val += daily.get(day, 0.0)
            regime = ("green" if btc_ret >= 0.02 else
                      "red" if btc_ret <= -0.02 else "flat")
            per_day.append({"date": day, "regime": regime,
                            "book_pct": round(book_ret * 100, 2),
                            "btc_pct": round(btc_ret * 100, 2),
                            "gap_pp": round((book_ret - btc_ret) * 100, 2)})
        reg: dict[str, dict] = {}
        for d in per_day:
            a = reg.setdefault(d["regime"], {"n": 0, "gap": 0.0, "book": 0.0})
            a["n"] += 1
            a["gap"] += d["gap_pp"]
            a["book"] += d["book_pct"]
        alpha = {"per_day": per_day,
                 "by_regime": {k: {"n": v["n"],
                                   "avg_gap_pp": round(v["gap"] / v["n"], 2),
                                   "avg_book_pct": round(v["book"] / v["n"], 2)}
                               for k, v in sorted(reg.items())},
                 "note": ("gap = book minus BTC, daily, paired. Skill is a "
                          "non-negative gap on flat/red days; green-day "
                          "returns are tide, not skill. Realized-pnl based "
                          "(open-position marks excluded).")}
    except Exception:
        alpha = None

    if not rows:
        return

    # aggregate: the self-assessment the whole module exists for
    fams: dict[str, dict] = {}
    verdicts: dict[str, int] = {}
    for r in rows:
        verdicts[r["verdict"]] = verdicts.get(r["verdict"], 0) + 1
        f = fams.setdefault(r["family"], {"n": 0, "giveback": 0.0,
                                          "post_max": 0.0, "well": 0})
        f["n"] += 1
        f["giveback"] += r["giveback_pct"]
        f["post_max"] += r["post24h_max_pct"]
        f["well"] += (r["verdict"] == "WELL_TIMED")

    summary = {
        "generated_utc": datetime.now(timezone.utc).isoformat(
            timespec="seconds"),
        "n_audited": len(rows),
        "verdicts": verdicts,
        "families": {k: {"n": v["n"],
                         "avg_giveback_pct": round(v["giveback"] / v["n"], 2),
                         "avg_post24h_max_pct": round(v["post_max"] / v["n"], 2),
                         "well_timed": v["well"]}
                     for k, v in sorted(fams.items())},
        "thresholds_pct": THRESH * 100,
        "market_capture": capture,
        "alpha_by_regime": alpha,
    }
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(summary, indent=1, sort_keys=True),
                           encoding="utf-8", newline="\n")

    L = ["# Exit timing — the bot grading its own exits", "",
         f"updated {summary['generated_utc']} · {len(rows)} exits audited · "
         f"early/late line ±{THRESH:.0%} · MEASUREMENT ONLY", "",
         "| verdict | n |", "|---|---|"]
    for k in ("TOO_EARLY", "TOO_LATE", "BOTH", "WELL_TIMED"):
        if verdicts.get(k):
            L.append(f"| {k} | {verdicts[k]} |")
    L += ["", "| exit family | n | avg giveback | avg post-24h run | "
          "well-timed |", "|---|---|---|---|---|"]
    for k, v in summary["families"].items():
        L.append(f"| {k} | {v['n']} | {v['avg_giveback_pct']:+.1f}% | "
                 f"{v['avg_post24h_max_pct']:+.1f}% | {v['well_timed']} |")
    if capture:
        L += ["", "## Market capture", "",
              f"- book since inception (08-15, $40): "
              f"**{capture['book_since_inception_pct']:+.1f}%**"]
        for k in ("btc", "eth"):
            si = capture.get(f"{k}_since_inception_pct")
            d1 = capture.get(f"{k}_last24h_pct")
            if si is not None:
                gap = capture['book_since_inception_pct'] - si
                L.append(f"- {k.upper()} since inception: {si:+.1f}% "
                         f"(book gap **{gap:+.1f}pp**)"
                         + (f" · last 24h {d1:+.1f}%" if d1 is not None
                            else ""))
        L.append("")
    if alpha:
        L += ["## Alpha by regime (book minus BTC, daily, paired)", "",
              "**Skill is a non-negative gap on flat/red days. Green-day "
              "returns are tide, not skill.**", "",
              "| regime (BTC day) | days | avg book | avg gap vs BTC |",
              "|---|---|---|---|"]
        for k in ("red", "flat", "green"):
            v = alpha["by_regime"].get(k)
            if v:
                L.append(f"| {k} | {v['n']} | {v['avg_book_pct']:+.2f}% | "
                         f"**{v['avg_gap_pp']:+.2f}pp** |")
        L += ["", "| date | regime | book | BTC | gap |", "|---|---|---|---|---|"]
        for d in alpha["per_day"][-10:]:
            L.append(f"| {d['date']} | {d['regime']} | {d['book_pct']:+.2f}% "
                     f"| {d['btc_pct']:+.2f}% | {d['gap_pp']:+.2f}pp |")
        L.append("")
    L += ["", "_giveback = in-hold peak the exit surrendered; post-24h run "
          "= what the coin did after we sold. High post-run with low "
          "giveback = selling too early; high giveback = selling too "
          "late._", ""]
    REPORT_MD.write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(f"[exit_auditor] {new} new audits; totals {verdicts}")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:  # measurement must never take the fleet down
        print(f"[exit_auditor] non-fatal: {e}")
        sys.exit(0)
