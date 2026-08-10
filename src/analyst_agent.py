"""The Analyst (المحلل) — bot #11: an LLM trading agent on trial.

Pre-registered spec: trading/specs/analyst-agent-spec.md (2026-07-22).
Hypothesis: a frontier LLM reasoning fresh over daily context can beat simple
rules and its benchmark, with honest fills and costs. External evidence says
expect ~zero alpha (LiveTradeBench: reasoning models do NOT outperform) —
the live run is the test, and the glass-box reasoning log is the payload.

Design: agent PROPOSES, code DISPOSES. One decision per US trading day.
Every guardrail is plain Python the agent cannot waive. Its API bill is
charged against its own paper account (edge must beat its own token cost).

Model is a config constant, recorded in every decision for attribution.
(Spec said claude-sonnet-5 "to start"; launched 2026-07-31 on claude-opus-5,
the current default tier — amendment recorded in the journal BEFORE the
first decision. Est. cost at 1 call/day: ~$3-5/month.)
"""
from __future__ import annotations

import json
import re
import urllib.request
from datetime import datetime, timezone, timedelta

import pandas as pd

import config
import market_hours
import selection_engine

MODEL = "claude-opus-5"
IN_PRICE, OUT_PRICE = 5.0, 25.0          # USD per 1M tokens (claude-opus-5)
UNIVERSE = ["SPY", "QQQ", "GLD", "USO", "TLT", "BTC-USD", "ETH-USD"]
BENCH = "SPY"
MAX_TOOL_CALLS = 6
MAX_HEADLINE_CALLS = 3
MONTHLY_DECISION_CAP = 25                 # ~22 trading days + slack
R1_FLOOR = 750.0
STATE = config.DATA / "analyst_state.json"
BRIEFING = """You are The Analyst: one daily trading decision for a $1,000 paper
portfolio benchmarked against SPY buy & hold. Universe: SPY, QQQ, GLD, USO,
TLT, BTC-USD, ETH-USD, CASH. Long only, ONE position, one trade per day max.

Hard-won lessons from this project (do not relearn them with losses):
1. CHURN IS A TAX. Costs are real; a strategy trading daily must clear a much
   higher bar than one trading monthly. Trading less is usually the alpha.
2. BETA IS NOT SKILL. Holding QQQ while QQQ rises proves nothing. If your
   reasoning is "market will go up," holding SPY is the honest version.
3. A GOOD STORY IS NOT EVIDENCE. This project killed congress-copying, tuned
   MA parameters, and MA-timing-as-return-edge — all sounded excellent. Cite
   prices and dates, not narratives. HOLD is a position, often the best one.
4. STREAKS MEAN NOTHING AT SMALL SAMPLE. 5 wins can be coin flips. Do not
   increase conviction because recent calls worked.
5. REGIME CONTEXT BEATS PREDICTION. Trend gates cut drawdowns (protection,
   not alpha); crowded positioning is risk. You cannot predict prices; you
   CAN notice mispriced risk or an imminent event.

Decision discipline:
- Every decision needs a FALSIFIER: what observable event proves it wrong,
  by when. "It might go up" is not a decision.
- "high" conviction requires two independent cited pieces of evidence
  (a price fact + a dated catalyst, not two vibes).
- If today's reasoning would be identical yesterday and tomorrow, it is a
  holding thesis, not a daily decision — say HOLD and restate its falsifier.
- You are graded on: excess return vs SPY, whether falsifiers fired, hold
  discipline, and whether profits came for your STATED reason.
- Your API cost is charged against your own account. Wasted tool calls and
  churn come straight out of your P/L.

Use your tools to check prices, headlines, and the Watcher before deciding.
You MUST finish by calling submit_decision. Guardrails you cannot waive:
long only, one position, one trade/day, Watcher SEVERE forces cash, equity
below $750 retires you."""

TOOLS = [
    {"name": "get_price_history",
     "description": "Daily closing prices for one universe ticker. Call for "
                    "any ticker whose recent action matters to your decision.",
     "input_schema": {"type": "object", "properties": {
         "ticker": {"type": "string", "enum": UNIVERSE},
         # no minimum/maximum — strict mode rejects numeric constraints
         # (found by the 2026-07-31 rehearsal run); range clamped in code
         "days": {"type": "integer"}},
         "required": ["ticker", "days"], "additionalProperties": False},
     "strict": True},
    {"name": "get_headlines",
     "description": "Latest top financial headlines (CNBC). Call when a "
                    "catalyst or news check matters. Max 3 calls.",
     "input_schema": {"type": "object", "properties": {},
                      "additionalProperties": False},
     "strict": True},
    {"name": "read_watcher",
     "description": "The fleet's risk officer (Grok Watcher): latest risk "
                    "level, alerts, and market mood from its X/news scan.",
     "input_schema": {"type": "object", "properties": {},
                      "additionalProperties": False},
     "strict": True},
    {"name": "submit_decision",
     "description": "Submit your final decision for today. REQUIRED once per day.",
     "input_schema": {"type": "object", "properties": {
         "action": {"type": "string", "enum": ["buy", "sell", "hold"]},
         "ticker": {"type": "string", "enum": UNIVERSE + ["NONE"]},
         "conviction": {"type": "string", "enum": ["low", "medium", "high"]},
         "reasoning": {"type": "string"},
         "falsifier": {"type": "string"}},
         "required": ["action", "ticker", "conviction", "reasoning", "falsifier"],
         "additionalProperties": False},
     "strict": True},
]


def _et_today():
    return str(market_hours._et_now().date())


def _headlines():
    try:
        req = urllib.request.Request(
            "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            headers={"User-Agent": "paper-bot-analyst"})
        xml = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
        titles = re.findall(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", xml)
        return [t for t in titles if t and "CNBC" not in t][:15]
    except Exception as e:
        return [f"(headlines unavailable: {e})"]


def _watcher():
    p = config.DATA / "sentinel_verdict.json"
    if not p.exists():
        return {"risk_level": "unknown", "note": "no Watcher scan on file"}
    v = json.loads(p.read_text())
    return {k: v.get(k) for k in ("risk_level", "alerts", "overall_mood",
                                  "scanned_at") if k in v}


def _recent_record(st, close):
    """The Analyst's own recent decisions WITH realized outcomes — this is the
    in-context learning loop: it sees what happened after each of its calls."""
    out = []
    for d in st["decisions"][-10:]:
        row = {"date": d["date"], "action": d["decision"].get("action"),
               "ticker": d["decision"].get("ticker"),
               "conviction": d["decision"].get("conviction"),
               "falsifier": d["decision"].get("falsifier"),
               "outcome": d.get("outcome", "n/a")}
        t = d.get("fill_ticker")
        if t and t in close.columns and d.get("fill_price"):
            now = float(close[t].dropna().iloc[-1])
            row["price_change_since"] = f"{(now / d['fill_price'] - 1) * 100:+.1f}%"
        out.append(row)
    return out


def decide(client, context, close_raw):
    """Run the tool loop. Returns (decision_dict_or_None, tools_called, usage)."""
    messages = [{"role": "user", "content": context}]
    tools_called, headline_calls = [], 0
    usage = {"in": 0, "out": 0}

    for _ in range(MAX_TOOL_CALLS + 2):
        resp = client.messages.create(
            model=MODEL, max_tokens=8000, system=BRIEFING,
            tools=TOOLS, messages=messages)
        usage["in"] += resp.usage.input_tokens
        usage["out"] += resp.usage.output_tokens
        if resp.stop_reason == "refusal":
            return None, tools_called, usage
        calls = [b for b in resp.content if b.type == "tool_use"]
        if not calls:
            # no decision submitted and no tool asked — force the decision
            messages.append({"role": "assistant", "content": resp.content})
            messages.append({"role": "user", "content":
                            "Submit your decision now via submit_decision."})
            continue
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for c in calls:
            if c.name == "submit_decision":
                return dict(c.input), tools_called, usage
            tools_called.append(c.name)
            if c.name == "get_price_history":
                days = max(5, min(200, int(c.input["days"])))
                s = close_raw[c.input["ticker"]].dropna().tail(days)
                body = "\n".join(f"{d.date()} {v:.2f}" for d, v in s.items())
            elif c.name == "get_headlines":
                headline_calls += 1
                body = ("(headline call limit reached)" if headline_calls > MAX_HEADLINE_CALLS
                        else "\n".join(_headlines()))
            elif c.name == "read_watcher":
                body = json.dumps(_watcher())
            else:
                body = "unknown tool"
            results.append({"type": "tool_result", "tool_use_id": c.id,
                            "content": body})
        messages.append({"role": "user", "content": results})
        if len(tools_called) >= MAX_TOOL_CALLS:
            # out of budget: one final forced decision
            resp = client.messages.create(
                model=MODEL, max_tokens=8000, system=BRIEFING, tools=TOOLS,
                tool_choice={"type": "tool", "name": "submit_decision"},
                messages=messages + [{"role": "user", "content":
                                     "Tool budget exhausted — submit your decision now."}])
            usage["in"] += resp.usage.input_tokens
            usage["out"] += resp.usage.output_tokens
            for b in resp.content:
                if b.type == "tool_use" and b.name == "submit_decision":
                    return dict(b.input), tools_called, usage
            return None, tools_called, usage
    return None, tools_called, usage


def apply_guardrails(decision, holding, equity, severe):
    """Agent proposes, code disposes. Returns (action, ticker, reason_tag).
    action in {'buy','cash','hold'}; every rule here is unwaivable."""
    if equity < R1_FLOOR:
        return "cash", None, "R1 FLOOR — forced liquidation, agent benched"
    if severe:
        return "cash", None, "WATCHER SEVERE — forced flat, agent's opinion ignored"
    if not decision:
        return "hold", None, "agent_error — malformed/no decision, defaulting to HOLD"
    act, tkr = decision.get("action"), decision.get("ticker")
    if act == "buy":
        if tkr not in UNIVERSE:
            return "hold", None, "agent_error — invalid ticker, HOLD"
        if tkr == holding:
            return "hold", None, "already holding — treated as HOLD"
        return "buy", tkr, "agent decision"
    if act == "sell":
        if holding == "CASH":
            return "hold", None, "nothing to sell — treated as HOLD"
        return "cash", None, "agent decision"
    return "hold", None, "agent decision"


def main():
    close, close_raw = selection_engine._fetch_daily(UNIVERSE, BENCH)
    close_cal = close_raw.copy()          # calendar oracle, pre-splice
    live, live_ts, live_raw = selection_engine._fetch_live(UNIVERSE, BENCH)
    for t, p in live.items():
        if t in close.columns:
            close.iloc[-1, close.columns.get_loc(t)] = p
    last = close.iloc[-1]

    st = json.loads(STATE.read_text()) if STATE.exists() else None

    # Date the mark by the asset that determines its value — holding a
    # weekday-only asset (or sitting in cash against an equity benchmark)
    # means no weekend marks, even though BTC/ETH give the frame weekend
    # rows. See the long note in selection_engine.run(); the phantom weekend
    # marks this prevents once froze this agent through an entire weekend.
    value_asset = st["holding"] if st and st["holding"] != "CASH" else BENCH
    asof = (market_hours.newest_real_date(close_cal, live_raw, value_asset)
            or str(close.index[-1].date()))
    bench_asof = market_hours.newest_real_date(close_cal, live_raw, BENCH)

    if st is None:
        if pd.isna(last[BENCH]):
            print("[analyst] no benchmark price — cannot initialize"); return
        st = {"created": asof, "starting_cash": 1000.0, "holding": "CASH",
              "units": 0.0, "cash": 1000.0, "benched": False,
              "bench_units": 1000.0 / float(last[BENCH]),
              "api_cost_usd": 0.0, "model": MODEL,
              "decisions": [], "trades": [], "history": [], "intraday": []}
        print(f"[analyst] NEW sim {asof}")

    # Guards (same discipline as the engine): a regressed feed blocks trading
    # and the history write, but never takes the agent offline.
    newest = st["history"][-1]["date"] if st["history"] else ""
    feed_delayed = bool(asof < newest)
    if feed_delayed:
        print(f"[analyst] FEED DELAYED — freshest genuine price is {asof} but "
              f"newest mark is {newest}; no decision, holding steady")
    if st["holding"] != "CASH" and pd.isna(last.get(st["holding"])):
        print(f"[analyst] held ticker has no price — cycle skipped"); return

    equity = st["cash"] + (0.0 if st["holding"] == "CASH"
                           else st["units"] * float(last[st["holding"]]))

    # ---- once-per-trading-day decision gate ----
    today = _et_today()
    import os
    # .strip(): a secret pasted with a trailing newline breaks the HTTP
    # header (found by the key-check run 2026-07-31)
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip() or None
    month = today[:7]
    n_month = sum(1 for d in st["decisions"] if d["date"].startswith(month))
    should_decide = (market_hours.us_equities_open()
                     and not feed_delayed
                     and st.get("last_decision_date") != today
                     and not st.get("benched", False)
                     and n_month < MONTHLY_DECISION_CAP)
    # ANALYST_REHEARSAL=1: run the full decision loop for real (API and all)
    # but record NOTHING — proves the pipeline works without waiting for the
    # next market open. Used by the key-check workflow's rehearsal option.
    rehearsal = os.environ.get("ANALYST_REHEARSAL") == "1"
    if rehearsal:
        should_decide = bool(api_key)

    if should_decide and not api_key:
        print("[analyst] ANTHROPIC_API_KEY not set — skipping decision "
              "(add it as a repo secret to activate)")
        should_decide = False

    if should_decide:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)  # api_key pre-stripped
        mom = {c: f"{float(close_raw[c].dropna().pct_change(30).iloc[-1]) * 100:+.1f}%"
               for c in UNIVERSE if close_raw[c].dropna().shape[0] > 31}
        context = (
            f"Date: {today}. Portfolio: holding {st['holding']}, equity "
            f"${equity:,.2f} (start $1,000). Benchmark SPY: "
            f"${st['bench_units'] * float(last[BENCH]):,.2f}. Cumulative API "
            f"cost charged to you so far: ${st['api_cost_usd']:.2f}.\n"
            f"30-day momentum snapshot: {json.dumps(mom)}\n"
            f"Watcher latest: {json.dumps(_watcher())}\n"
            f"Your recent decisions and what happened after them:\n"
            f"{json.dumps(_recent_record(st, close), indent=1)}\n\n"
            f"Make today's decision. Investigate with tools first if useful.")
        decision, tools_called, usage = None, [], {"in": 0, "out": 0}
        try:
            decision, tools_called, usage = decide(client, context, close_raw)
        except Exception as e:
            # Fleet review 2026-08-10: one retry. A transient API error on a
            # falsifier-fire day (2026-08-05, 0 tokens used) silently became a
            # forced HOLD — the one edge this bot claims is exit discipline,
            # so a single blip must not be able to cancel an exit.
            print(f"[analyst] API failure: {e} — retrying once in 30s")
            import time
            time.sleep(30)
            try:
                decision, tools_called, usage = decide(client, context, close_raw)
            except Exception as e2:
                print(f"[analyst] API failure on retry: {e2} -> HOLD")
        cost = usage["in"] * IN_PRICE / 1e6 + usage["out"] * OUT_PRICE / 1e6
        if rehearsal:
            import sentinel_gate
            severe, _why = sentinel_gate.severe()
            action, tkr, tag = apply_guardrails(decision, st["holding"], equity, severe)
            print("[analyst] === REHEARSAL — nothing recorded, account untouched ===")
            print("decision:", json.dumps(decision, indent=1, ensure_ascii=False))
            print(f"tools called: {tools_called} · tokens {usage} · "
                  f"API cost this run ${cost:.3f} (billed to the key, not the sim)")
            print(f"guardrail verdict: {action} {tkr or ''} ({tag})")
            return
        st["cash"] -= cost                       # the agent pays its own bill
        st["api_cost_usd"] = round(st["api_cost_usd"] + cost, 4)

        import sentinel_gate
        severe, _why = sentinel_gate.severe()
        equity = st["cash"] + (0.0 if st["holding"] == "CASH"
                               else st["units"] * float(last[st["holding"]]))
        action, tkr, tag = apply_guardrails(decision, st["holding"], equity, severe)
        if equity < R1_FLOOR:
            st["benched"] = True

        fill_ticker, fill_price = None, None
        if action == "buy" and pd.notna(last.get(tkr)):
            value = st["cash"] + (0.0 if st["holding"] == "CASH"
                                  else st["units"] * float(last[st["holding"]]))
            if st["holding"] != "CASH":
                st["trades"].append({"date": asof, "action": "SELL",
                                     "ticker": st["holding"],
                                     "price": round(float(last[st["holding"]]), 2),
                                     "units": round(st["units"], 4),
                                     "value": round(st["units"] * float(last[st["holding"]]), 2),
                                     "reason": "Switching on today's decision"})
            p = float(last[tkr])
            st["holding"], st["units"], st["cash"] = tkr, value / p, 0.0
            fill_ticker, fill_price = tkr, p
            reason = (decision or {}).get("reasoning", "")[:400]
            st["trades"].append({"date": asof, "action": "BUY", "ticker": tkr,
                                 "price": round(p, 2), "units": round(st["units"], 4),
                                 "value": round(value, 2),
                                 "reason": f"[{(decision or {}).get('conviction', '?')}] {reason}"})
        elif action == "cash" and st["holding"] != "CASH":
            value = st["cash"] + st["units"] * float(last[st["holding"]])
            st["trades"].append({"date": asof, "action": "SELL",
                                 "ticker": st["holding"],
                                 "price": round(float(last[st["holding"]]), 2),
                                 "units": round(st["units"], 4),
                                 "value": round(st["units"] * float(last[st["holding"]]), 2),
                                 "reason": tag})
            st["holding"], st["units"], st["cash"] = "CASH", 0.0, value
            st["trades"].append({"date": asof, "action": "TO CASH", "ticker": "—",
                                 "price": 0, "units": 0, "value": round(value, 2),
                                 "reason": tag if "agent decision" != tag
                                 else (decision or {}).get("reasoning", "")[:400]})

        st["last_decision_date"] = today
        st["decisions"].append({
            "date": today, "model": MODEL,
            "decision": decision or {"action": "hold", "error": tag},
            "guardrail_action": action, "guardrail_tag": tag,
            "tools_called": tools_called,
            "fill_ticker": fill_ticker, "fill_price": fill_price,
            "tokens": usage, "api_cost_usd": round(cost, 4),
        })
        print(f"[analyst] decision: {(decision or {}).get('action', 'ERROR')} "
              f"{(decision or {}).get('ticker', '')} -> {action} ({tag}) "
              f"cost ${cost:.3f}")

    # ---- mark to market + dashboard (every cycle) ----
    val = st["cash"] + (0.0 if st["holding"] == "CASH"
                        else st["units"] * float(last[st["holding"]]))
    bench = st["bench_units"] * float(last[BENCH])
    if not feed_delayed:
        row = {"date": asof, "value": round(val, 2), "bench": round(bench, 2),
               "holding": st["holding"]}
        if bench_asof and bench_asof != asof:
            row["bench_asof"] = bench_asof
        st["history"] = sorted(
            [h for h in st["history"] if h["date"] != asof] + [row],
            key=lambda h: h["date"])
    st["feed_delayed"] = feed_delayed
    st["data_asof"] = asof
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    st["last_updated_utc"] = now
    st["intraday"] = [p for p in st.get("intraday", [])
                      if p["ts"] != now][-1499:] + [
        {"ts": now, "value": round(val, 2), "bench": round(bench, 2),
         "holding": st["holding"]}]
    STATE.write_text(json.dumps(st, indent=2))

    board = []
    mom30 = {c: close_raw[c].dropna().pct_change(30).iloc[-1] for c in UNIVERSE}
    for c in sorted(UNIVERSE, key=lambda c: -(mom30[c] if pd.notna(mom30[c]) else -9)):
        m = float(mom30[c]) * 100 if pd.notna(mom30[c]) else 0
        board.append({"sym": c, "price": round(float(last[c]), 2)
                      if pd.notna(last.get(c)) else 0,
                      "line": f"mom30 {m:+.1f}%",
                      "tag": "HELD" if c == st["holding"] else "watching",
                      "on": c == st["holding"], "pick": c == st["holding"],
                      "fill": max(-50, min(50, m))})
    last_d = st["decisions"][-1] if st["decisions"] else None
    payload = {
        "generated_utc": now, "created": st["created"],
        "starting_cash": st["starting_cash"], "live_ts": live_ts,
        "current": st["history"][-1], "board": board,
        "board_title": "7-instrument macro universe · one reasoned decision per day",
        "meta": {"title": "The Analyst — $1,000 Challenge",
                 "badge": "PAPER SIM · LLM AGENT ON TRIAL",
                 "bench_label": "SPY benchmark ($1,000 same day)",
                 "board_note": "Once per trading day, a Claude model reads "
                               "prices, headlines, and the Watcher's risk scan, "
                               "then commits one decision — with its full "
                               "reasoning and a tripwire shown above."},
        "thoughts": (f"My decision on {last_d['date']}: "
                     f"{last_d['decision'].get('action', 'hold').upper()}"
                     f"{' ' + last_d['decision'].get('ticker', '') if last_d['decision'].get('ticker') not in (None, 'NONE') else ''}"
                     f" (conviction: {last_d['decision'].get('conviction', '?')}).\n\n"
                     f"{last_d['decision'].get('reasoning', 'n/a')}\n\n"
                     f"What would prove me wrong: "
                     f"{last_d['decision'].get('falsifier', 'n/a')}"
                     if last_d else
                     "I haven't made my first decision yet — it comes shortly "
                     "after the next US market open. Each day I'll explain "
                     "exactly why I did what I did, and name the thing that "
                     "would prove me wrong."),
        "intraday": st["intraday"], "trades": st["trades"][-20:],
        "history": st["history"],
        "strategy": {
            "name": "The Analyst — LLM daily reasoner",
            "rule": "One decision per US trading day by " + MODEL + " over "
                    "prices, headlines, and the Watcher; guardrails in code: "
                    "long only, 1 position, 1 trade/day, SEVERE=cash, $750 floor; "
                    "its own API bill is charged to the account",
            "backtest_cagr": "NO BACKTEST POSSIBLE — sentiment/reasoning has no "
                             "historical replay; the live run IS the test",
            "backtest_maxdd": f"External evidence: LLM agents show no credible "
                              f"net-of-cost alpha (LiveTradeBench). Expectation: ~zero. "
                              f"API cost so far ${st['api_cost_usd']:.2f}",
            "note": "Glass-box experiment: every decision logs verbatim reasoning "
                    "plus a falsifier the attribution log scores later. Judged by "
                    "kill_criteria.md like every other bot.",
        },
    }
    (config.REPORTS / "analyst_dashboard_data.json").write_text(
        json.dumps(payload, indent=2))
    template = (config.ROOT / "src" / "fleet_dashboard_template.html").read_text(
        encoding="utf-8")
    html = template.replace("/*__DATA__*/", json.dumps(payload)).replace(
        "__DATAFILE__", "analyst_dashboard_data.json")
    (config.REPORTS / "analyst_dashboard.html").write_text(html, encoding="utf-8")
    print(f"[analyst] {asof} holding {st['holding']} value ${val:,.2f} "
          f"vs SPY ${bench:,.2f} · lifetime API cost ${st['api_cost_usd']:.2f}")


if __name__ == "__main__":
    main()
