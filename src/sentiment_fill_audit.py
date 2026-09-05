"""Hype Trader fill audit — price every recorded fill against the market at
the minute it was booked, and restate the book.

Owner 2026-09-05: "there is an issue with the output, find it." There was:
Yahoo's daily frame often lacks TODAY's bar for a ticker that just started
moving; sentinel_trader ffilled it and booked the order at YESTERDAY's close.
GPRO 09-01 filled at 0.876 when the day's low was 1.16; SOUN 08-06 at 6.43
against a 7.00 low. The bug is fixed in sentinel_trader (fresh-bar gate);
this script measures the damage and writes the restated equity.

Inputs: a JSON list of fills with `commit_ts` (the Actions commit that first
carried the trade = fill time within ~1 min), recovered from git history.
Prices: Yahoo 1h bars for stocks, Binance 1h klines for coins; a fill is
ACCEPTED if it lies inside that hour's low..high (0.5% tolerance), else it
is RESTATED to the bar's close. The book is then replayed leg by leg.

Usage: python src/sentiment_fill_audit.py <fills.json>  -> reports/sentiment_fill_audit.md
"""
from __future__ import annotations

import json
import sys

import pandas as pd
import yfinance as yf

import config
import binance_data
import risk_common

OUT = config.REPORTS / "sentiment_fill_audit.md"
TOL = 0.005


def stock_bars(t: str, start, end) -> pd.DataFrame | None:
    df = yf.download(t, start=start, end=end, interval="1h", auto_adjust=True,
                     progress=False, threads=False)
    if df is None or df.empty:
        return None
    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)
    df.index = df.index.tz_convert("UTC") if df.index.tz else df.index.tz_localize("UTC")
    return df[["Low", "High", "Close"]]


def coin_bars(sym: str, start, end) -> pd.DataFrame | None:
    rows, cur = [], int(pd.Timestamp(start).timestamp() * 1000)
    end_ms = int(pd.Timestamp(end).timestamp() * 1000)
    while cur < end_ms:
        d = binance_data._get("/api/v3/klines", {"symbol": sym + "USDT", "interval": "1h",
                                                 "startTime": cur, "limit": 1000}, weight=2)
        if not isinstance(d, list) or not d:
            break
        rows += d
        cur = d[-1][6] + 1
    if not rows:
        return None
    df = pd.DataFrame({"Low": [float(r[3]) for r in rows], "High": [float(r[2]) for r in rows],
                       "Close": [float(r[4]) for r in rows]},
                      index=pd.to_datetime([r[0] for r in rows], unit="ms", utc=True))
    return df


def main(path: str) -> int:
    fills = json.load(open(path, encoding="utf-8"))
    # legs booked before the git window carry the window's first commit time,
    # not their fill time; they were already restated on 2026-07-22 — keep as is
    legs = [f for f in fills if f["ticker"] != "—"]
    first_ts = min(pd.Timestamp(f["commit_ts"]) for f in legs)
    for f in legs:
        f["audit_price"] = (f["value"] / f["units"]) if f.get("units") and f["price"] == 0 else f["price"]
        f["pre_window"] = pd.Timestamp(f["commit_ts"]) == first_ts and f["date"] < str(first_ts.date())
    by_t: dict[str, list] = {}
    for f in legs:
        by_t.setdefault(f["ticker"], []).append(pd.Timestamp(f["commit_ts"]).tz_convert("UTC"))
    bars = {}
    for t, tss in by_t.items():
        a, b = (min(tss) - pd.Timedelta(days=3)).date(), (max(tss) + pd.Timedelta(days=2)).date()
        bars[t] = coin_bars(t[:-4], a, b) if t.endswith("-USD") else stock_bars(t, a, b)
    audited = []
    for f in legs:
        ts = pd.Timestamp(f["commit_ts"]).tz_convert("UTC")
        df = bars.get(f["ticker"])
        row = {**f, "status": "no data", "true": None}
        if f["pre_window"]:
            row["status"] = "ok (restated 2026-07-22, fill time unknown)"
        elif df is not None:
            prior = df[df.index <= ts]
            if len(prior):
                bar = prior.iloc[-1]
                age_h = (ts - prior.index[-1]).total_seconds() / 3600
                lo, hi, cl = float(bar["Low"]), float(bar["High"]), float(bar["Close"])
                inside = lo * (1 - TOL) <= f["audit_price"] <= hi * (1 + TOL)
                row.update({"true": cl, "lo": lo, "hi": hi, "bar_age_h": round(age_h, 1),
                            "status": "ok" if inside else ("stale bar (market closed)" if age_h > 2 and inside
                                                             else "RESTATED"),
                            "gap_pct": round((f["audit_price"] / cl - 1) * 100, 2)})
                if abs(f["audit_price"] / cl - 1) > 0.5:
                    # not a stale print — a different asset (ARB-USD on Yahoo
                    # was a $0.0006 token, Arbitrum is ~$0.11): no trade happened
                    row["status"] = "VOID (wrong asset)"
                if age_h > 2 and not inside:
                    # fill booked while the market was shut: the honest price is
                    # the last real bar's close, which is what we restate to
                    row["status"] = "RESTATED (booked off-hours)"
        audited.append(row)
    # replay the book with restated prices
    cash, units, held, fee_paid = 1000.0, 0.0, None, 0.0
    equity_path = []
    for r in audited:
        if r["status"].startswith("VOID"):
            equity_path.append((r["commit_ts"][:16], r["action"] + " void", r["ticker"], 0,
                                round(cash if held is None else units * px, 2)))
            continue
        px = r["true"] if r["status"].startswith("RESTATED") and r["true"] else r["audit_price"]
        if r["action"] == "BUY":
            f = risk_common.fee(r["ticker"], cash)
            fee_paid += f
            units, held, cash = (cash - f) / px, r["ticker"], 0.0
        elif r["action"] == "SELL" and held == r["ticker"]:
            gross = units * px
            f = risk_common.fee(r["ticker"], gross)
            fee_paid += f
            cash, units, held = gross - f, 0.0, None
        equity_path.append((r["commit_ts"][:16], r["action"], r["ticker"], round(px, 6), round(cash if held is None else units * px, 2)))
    restated = cash if held is None else units * px
    n_bad = sum(1 for r in audited if r["status"].startswith("RESTATED"))
    lines = [f"# Hype Trader fill audit", "",
             f"{len(audited)} legs audited ({len(fills)} records), {n_bad} restated. "
             f"Recorded final equity: see data/sentiment_state.json. "
             f"**Restated equity after replaying every leg at market prices: ${restated:,.2f}** "
             f"(fees ${fee_paid:,.2f}).", "",
             "| booked (UTC) | leg | ticker | recorded | market bar low-high | bar close | gap | status |",
             "|---|---|---|---|---|---|---|---|"]
    for r in audited:
        if r["status"].startswith("ok"):
            continue
        lines.append(f"| {r['commit_ts'][:16]} | {r['action']} | {r['ticker']} | {r['price']} | "
                     f"{r.get('lo', '')}-{r.get('hi', '')} | {r.get('true', '')} | {r.get('gap_pct', '')}% | {r['status']} |")
    lines += ["", "## Replayed equity path (restated prices)", "", "| booked | leg | ticker | price used | equity |", "|---|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | {d} | ${e:,.2f} |" for a, b, c, d, e in equity_path]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    json.dump({"restated_equity": round(restated, 2), "restated_legs": n_bad, "audited": audited},
              open(str(OUT).replace(".md", ".json"), "w"), indent=1, default=str)
    print(f"restated equity ${restated:,.2f}; {n_bad} legs restated; wrote {OUT}")
    for r in audited:
        if not r["status"].startswith("ok"):
            print(f"  {r['commit_ts'][:16]} {r['action']:4} {r['ticker']:8} rec {r['price']} true {r.get('true')} {r['status']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
