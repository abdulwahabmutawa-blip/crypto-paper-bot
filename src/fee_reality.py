"""Fee reality at pilot size — GO_LIVE_PLAN A2.

Re-prices every bot's ACTUAL ledger as if it had traded a 325-dollar book
(100 KWD) through IBKR Fixed tier instead of a $1,000 paper book at the
10/25bps model. Answers one question with the fleet's own trades: which
cadence survives real small-account fees?

Reads data/*_state.json (read-only), writes reports/fee_reality.md.
Run manually: python src/fee_reality.py
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import config
import risk_common

PILOT = 325.0
SCALE = PILOT / 1000.0


def main():
    rows = []
    for p in sorted(config.DATA.glob("*_state.json")):
        key = p.name.replace("_state.json", "")
        try:
            st = json.loads(p.read_text())
        except Exception:
            continue
        trades = [t for t in st.get("trades", [])
                  if t.get("action") in ("BUY", "SELL") and t.get("value")]
        if not trades or "history" not in st:
            continue
        days = max(1, len({h["date"] for h in st.get("history", [])}))
        paper_fees = sum(t.get("fee", 0.0) for t in trades)
        pilot_fees = 0.0
        n_crypto = 0
        for t in trades:
            v = float(t["value"]) * SCALE
            u = float(t.get("units", 0.0)) * SCALE
            # per-TRADE venue: crypto legs at Binance spot 10bps (best-case
            # tier, lane still Track-C-gated), equity legs at IBKR Fixed
            if str(t.get("ticker", "")).endswith("-USD"):
                pilot_fees += risk_common.binance_fee(v)
                n_crypto += 1
            else:
                pilot_fees += risk_common.ibkr_fee(t["ticker"], v, u)
        ann = pilot_fees / PILOT * (365.0 / days) * 100.0
        lane = ("crypto @ Binance 10bps" if n_crypto == len(trades) else
                ("equity" if n_crypto == 0 else
                 f"mixed ({n_crypto}/{len(trades)} crypto)"))
        rows.append({"bot": key, "trades": len(trades), "days": days,
                     "paper_fees_1000": paper_fees,
                     "pilot_fees_325": pilot_fees, "annualized_pct": ann,
                     "lane": lane})

    rows.sort(key=lambda r: r["annualized_pct"])
    lines = [
        "# Fee reality at pilot size (100 KWD ≈ $325, IBKR Fixed tier)",
        "",
        f"_Generated {datetime.now(timezone.utc).isoformat(timespec='seconds')} "
        f"by src/fee_reality.py from the fleet's actual ledgers. IBKR Fixed: "
        f"$0.005/share, min $1/order, max 1% of value, + half-spread. "
        f"Verdict rule of thumb: annualized fee drag above ~10% of the book "
        f"means the cadence cannot beat a savings account after costs._",
        "",
        "| bot | lane | fills | days | paper fees ($1k book) | "
        "pilot fees ($325 book) | annualized drag |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['bot']} | {r['lane']} | {r['trades']} | {r['days']} | "
            f"${r['paper_fees_1000']:.2f} | ${r['pilot_fees_325']:.2f} | "
            f"{r['annualized_pct']:.1f}%/yr |")
    lines += ["", "Fee-fit candidates are the equity-lane bots at the top of "
                  "the table; anything above ~10%/yr drag is disqualified at "
                  "this account size (research 08-13 §5)."]
    out = config.REPORTS / "fee_reality.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")
    for r in rows:
        print(f"  {r['bot']:<12} {r['lane']:<22} {r['trades']:>3} fills "
              f"-> {r['annualized_pct']:6.1f}%/yr drag at pilot size")


if __name__ == "__main__":
    main()
