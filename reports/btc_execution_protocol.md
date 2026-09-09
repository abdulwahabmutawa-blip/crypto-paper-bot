# BTC execution measurement protocol v1

Purpose: collect prospective, observable execution inputs before approving another strategy trial. No strategy has qualified. Every observation records NO_TRADE. This recorder has only public GET market-data access and no account credentials or order methods.

Each existing fleet cycle requests 20 levels of BTCUSDT depth after recording local request time, then records local receipt time and request latency. Preserve both book sides and the exchange update ID. The endpoint provides no exchange quote timestamp: receipt time must never be described as exchange event time or proof of quote freshness.

Reject malformed/crossed/locked books, nonpositive or nonfinite levels, requests taking more than five seconds, spreads over ten basis points, and depth insufficient for the cost probe. Rejections are saved as observations and return a nonzero process status so the fleet logs a warning.

A hypothetical $200 buy consumes displayed asks, including a 0.10% assumed fee and an extra 0.025% adverse slippage buffer. The same quantity is valued against displayed bids with the same sell-side assumptions. The result measures estimated immediate round-trip friction, not realized profit, order acceptance, guaranteed liquidity, or actual fills. Fee tier is unverified. There is no invented historical fill and no paper-trade balance.

Persist immutable UUID-named samples under data/btc_execution/YYYY-MM-DD/. The latest human-readable report is reports/btc_execution.md, copied to docs/btc_execution.md by the fleet. The existing approximately 13-minute schedule has gaps and is not suitable for subsecond or continuous scalping analysis. No new service or separate automation is created.

Next trial gate: define one defensible candidate, immutable rule version and start date; simulate entry at subsequently received asks and exits at subsequently received bids; count missed observations, gaps and all costs. Compare a separate $1,000 paper account to cash and BTC holding with matched allocation from the same start. Historical scalper results remain a separate retrospective simulation. Do not automatically promote a strategy after a trade-count threshold or mix old and new records.
