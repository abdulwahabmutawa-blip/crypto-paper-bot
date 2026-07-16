"""Central config: paths and constants for the congressional trade bot."""
from pathlib import Path

# Project root = parent of this src/ folder
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
DATA.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)

# --- Data source -------------------------------------------------------------
# House Stock Watcher snapshot (June 2012 -> Oct 2022), committed to a public
# GitHub repo. No API key or login required. Columns include BOTH
# transaction_date and disclosure_date, which we need to model the reporting lag.
HOUSE_CSV_URL = (
    "https://raw.githubusercontent.com/noodleslove/"
    "House-of-Representative-Analysis-I/main/data/all_transactions.csv"
)

RAW_HOUSE_CSV = DATA / "house_transactions_raw.csv"
CLEAN_CSV = DATA / "transactions_clean.csv"
PRICE_CACHE = DATA / "prices.csv"

# --- Simulation defaults -----------------------------------------------------
STARTING_CASH = 1000.0
BENCHMARK = "SPY"          # what we measure ourselves against
HOLD_DAYS = 90             # default holding horizon for a mimicked position

# Map disclosed amount ranges to a representative dollar value (midpoint).
# These are the standard STOCK Act brackets.
AMOUNT_MIDPOINTS = {
    "$1,001 - $15,000": 8000,
    "$15,001 - $50,000": 32500,
    "$50,001 - $100,000": 75000,
    "$100,001 - $250,000": 175000,
    "$250,001 - $500,000": 375000,
    "$500,001 - $1,000,000": 750000,
    "$1,000,001 - $5,000,000": 3000000,
    "$1,000,000 +": 5000000,
    "$5,000,001 - $25,000,000": 15000000,
    "$25,000,001 - $50,000,000": 37500000,
    "$50,000,000 +": 50000000,
}
