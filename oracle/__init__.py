"""The Oracle — a predict-only forecasting experiment.

CANNOT TRADE, BY CONSTRUCTION: this package holds no API keys, imports no
broker or execution module, and tests/test_oracle.py fails the build if it
ever does. It reads public Binance market data, writes falsifiable
predictions, resolves them mechanically and scores itself.

See oracle/README.md — the pre-registration, written before any prediction
existed. Phase 0 contains no LLM on purpose.
"""
