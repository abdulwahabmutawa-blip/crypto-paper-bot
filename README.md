# Crypto Paper Bot ☁️

A $1,000 **paper-trading** simulation that runs itself on GitHub Actions —
no server, no computer left on.

- **Strategy:** regime switcher. BTC above its 200-day MA → momentum brain
  (hold the hottest rising coin of 8 majors). Below → mean-reversion brain
  (buy deeply oversold dips, harvest the bounce), else cash.
- **Cadence:** a GitHub Action runs every ~20 minutes, fetches live prices,
  trades if the signal flipped, and commits the new state back to this repo.
- **Dashboard:** published via GitHub Pages from `docs/` — portfolio value,
  BTC benchmark, signal board, and the full trade log.
- **State:** `data/crypto_state.json` is the bot's memory. The trade log in it
  is append-only history.

**Paper money only.** This project never touches an exchange or a real
dollar, and nothing in it is investment advice.

Run a cycle locally: `pip install -r requirements.txt && python src/crypto_tracker.py`
