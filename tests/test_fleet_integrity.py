"""Regression cases for v4 migration, quote dates and all-bot failure handling."""
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import crypto_tracker as crypto
import sentinel_trader as sentiment


def test_btc_v4_migrates_hot_legacy_alt_without_churn_block():
    board = {"BTC-USD": {"mom_pct": 1.7, "z": 0.16},
             "ADA-USD": {"mom_pct": 12.24, "z": 0.72}}
    assert crypto.v4_pick("BTC-USD", "ADA-USD", board, "TREND") == "BTC-USD"
    assert crypto.v4_pick("CASH", "ADA-USD", board, "TREND") == "CASH"
    assert crypto.v4_pick("CASH", "BTC-USD", board, "TREND") == "BTC-USD"
    assert crypto.v4_pick("BTC-USD", "ADA-USD", board, "TREND", severe=True) == "CASH"
    assert crypto.v4_pick("CASH", "BTC-USD", board, "TREND", severe=True) == "CASH"


def test_exchange_quote_does_not_depend_on_yahoo_coverage(monkeypatch):
    import binance_data
    monkeypatch.setattr(binance_data, "price", lambda s: {"SOPHUSDT": 0.01124}.get(s))
    px, received = sentiment.exchange_quotes({"SPY": 500, "BAD-USD": 100},
                                            ["SOPH-USD", "BAD-USD"])
    assert px == {"SPY": 500, "SOPH-USD": 0.01124}
    assert received == {"SOPH-USD"}


def test_crypto_mark_uses_exchange_date_stock_mark_keeps_session_date():
    raw = pd.DataFrame({"SPY": [500, float("nan")],
                        "SOPH-USD": [0.009, 0.010]},
                       index=pd.to_datetime(["2026-09-04", "2026-09-06"]))
    now = datetime(2026, 9, 8, 10, tzinfo=timezone.utc)
    assert sentiment.mark_date("SOPH-USD", raw, {"SOPH-USD"}, now) == "2026-09-08"
    assert sentiment.mark_date("CASH", raw, set(), now) == "2026-09-08"
    assert sentiment.mark_date("SPY", raw, set(), now) == "2026-09-04"


def test_sentiment_cycle_appends_today_without_redating_old_history(tmp_path, monkeypatch):
    import binance_data
    now = datetime(2026, 9, 8, 10, tzinfo=timezone.utc)
    class Clock(datetime):
        @classmethod
        def now(cls, tz=None):
            return now
    monkeypatch.setattr(sentiment, "datetime", Clock)
    monkeypatch.setattr(sentiment, "scan_is_stale", lambda _: False)
    monkeypatch.setattr(sentiment, "scan_age_hours", lambda _: 1)
    monkeypatch.setattr(sentiment.market_hours, "can_fill", lambda _: True)
    monkeypatch.setattr(sentiment.risk_common, "r1_breached", lambda _: False)
    monkeypatch.setattr(sentiment, "STATE", tmp_path / "state.json")
    monkeypatch.setattr(sentiment, "SENTINEL", tmp_path / "scan.json")
    monkeypatch.setattr(sentiment.config, "REPORTS", tmp_path)
    monkeypatch.setattr(sentiment.config, "ROOT", ROOT)
    raw = pd.DataFrame({"SPY": [500, float("nan")], "SOPH-USD": [0.009, 0.010]},
                       index=pd.to_datetime(["2026-09-04", "2026-09-06"]))
    monkeypatch.setattr(sentiment, "quotes", lambda _: ({"SPY": 500, "SOPH-USD": .010}, raw))
    monkeypatch.setattr(binance_data, "price", lambda _: .012)
    historical = {"date": "2026-09-06", "holding": "SOPH-USD", "value": 1000, "bench": 1000}
    st = {"created": "2026-09-04", "cash": 0, "holding": "SOPH-USD", "units": 100000,
          "entry_price": .010, "bench_units": 2, "stopped": {}, "trades": [],
          "history": [historical], "intraday": []}
    sentiment.STATE.write_text(json.dumps(st))
    h = {"symbol": "SOPH", "mood": "euphoric"}
    sentiment.SENTINEL.write_text(json.dumps({"scans": [{"ts": now.isoformat(), "hype": [h],
                                                        "crypto_hype": [h], "risk_level": "caution"}]}))
    sentiment.main()
    result = json.loads(sentiment.STATE.read_text())
    assert result["history"][0] == historical
    assert result["history"][-1]["date"] == "2026-09-08"
    assert result["history"][-1]["value"] == 1200
    assert result["history"][-1]["bench_asof"] == "2026-09-04"
    payload = json.loads((tmp_path / "sentiment_dashboard_data.json").read_text())
    assert payload["board"][0]["tag"] == "HELD"
    assert payload["current"] == result["history"][-1]


@pytest.mark.parametrize("all_fail", [True, False])
def test_actual_workflow_aborts_only_when_every_script_fails(all_fail):
    bash = shutil.which("bash")
    if not bash and Path("C:/Program Files/Git/bin/bash.exe").exists():
        bash = "C:/Program Files/Git/bin/bash.exe"
    if not bash:
        pytest.skip("bash unavailable")
    workflow = (ROOT / ".github/workflows/bot.yml").read_text(encoding="utf-8")
    block = workflow[workflow.index("            bots=("):workflow.index("            # publish dashboards")]
    # Execute the actual workflow roster and failure branch with fake processes.
    # One successful script must keep running; all failures must exit nonzero.
    stub = 'timeout() { return 1; }' if all_fail else 'timeout() { [[ "$*" == *crypto_tracker.py* ]]; }'
    result = subprocess.run([bash, "-c", "fails=0\n" + stub + "\n" + block],
                            capture_output=True, text=True, timeout=10)
    assert result.returncode == (1 if all_fail else 0), result.stdout + result.stderr
    assert ("systemic fault" in result.stdout) == all_fail


def test_fill_audit_void_carries_previous_equity(tmp_path, monkeypatch):
    import sentiment_fill_audit as audit
    monkeypatch.setattr(audit, "OUT", tmp_path / "audit.md")
    monkeypatch.setattr(audit.risk_common, "fee", lambda *args: 0.)
    bars = pd.DataFrame({"Low": [99.], "High": [101.], "Close": [100.]},
                        index=pd.to_datetime(["2026-09-08T10:00:00Z"]))
    monkeypatch.setattr(audit, "stock_bars", lambda *args: bars)
    fills = [{"ticker": t, "price": p, "units": 10, "value": p*10,
              "date": "2026-09-08", "action": "BUY", "commit_ts": f"2026-09-08T10:0{i}:00Z"}
             for i,(t,p) in enumerate([("BAD",1.),("AAA",100.),("BAD",1.)])]
    file = tmp_path / "fills.json"
    file.write_text(json.dumps(fills))
    assert audit.main(str(file)) == 0
    result = json.loads((tmp_path / "audit.json").read_text())
    assert result["restated_equity"] == 1000.
    assert audit.OUT.read_text().count("BUY void") == 2
