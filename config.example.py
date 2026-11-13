"""
Project configuration for the Stock Market Impact Prediction pipeline.

Keep this file in the SAME FOLDER as the notebook (finalProject_fixed.ipynb).
The notebook loads it with:  import config as cfg
"""

import torch

# ----------------------------------------------------------------------
# Alpaca API credentials -> https://app.alpaca.markets/paper/dashboard/overview
# Free (paper) keys are enough: News API history goes back to 2015 and the
# free IEX data feed gives 1-minute bars for several years back.
# ----------------------------------------------------------------------
ALPACA_API_KEY = "YOUR_ALPACA_API_KEY_HERE"
ALPACA_SECRET_KEY = "YOUR_ALPACA_SECRET_KEY_HERE"

# Selected Companies Mapping
COMPANIES = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Tesla": "TSLA",
    "Amazon": "AMZN",
    "Alphabet": "GOOGL",
    "Meta": "META",
    "Netflix": "NFLX",
    "AMD": "AMD",
    "JPMorgan": "JPM",
}

# Synonyms for Entity Resolution (used as a fallback when the Symbols
# field returned by Alpaca is missing/ambiguous)
ENTITY_RESOLVER = {
    "apple": "AAPL", "apple inc": "AAPL", "apple inc.": "AAPL", "aapl": "AAPL",
    "microsoft": "MSFT", "microsoft corp": "MSFT", "microsoft corporation": "MSFT", "msft": "MSFT",
    "nvidia": "NVDA", "nvidia corp": "NVDA", "nvidia corporation": "NVDA", "nvda": "NVDA",
    "tesla": "TSLA", "tesla inc": "TSLA", "tesla motors": "TSLA", "tsla": "TSLA",
    "amazon": "AMZN", "amazon.com": "AMZN", "amazon inc": "AMZN", "amzn": "AMZN",
    "alphabet": "GOOGL", "google": "GOOGL", "alphabet inc": "GOOGL", "googl": "GOOGL", "goog": "GOOGL",
    "meta": "META", "meta platforms": "META", "facebook": "META", "meta inc": "META",
    "netflix": "NFLX", "netflix inc": "NFLX", "nflx": "NFLX",
    "amd": "AMD", "advanced micro devices": "AMD",
    "jpmorgan": "JPM", "jp morgan": "JPM", "jpmorgan chase": "JPM", "jpm": "JPM",
}

# ----------------------------------------------------------------------
# Data collection window
# ----------------------------------------------------------------------
NEWS_LOOKBACK_DAYS = 730        # ~2 years of history

# ----------------------------------------------------------------------
# Labeling settings
# ----------------------------------------------------------------------
RETURN_WINDOW_MIN = 5           # forward window (in 1-min candles) used for the label
UPPER_THRESHOLD = 0.15          # >= +0.15% forward return  -> SPIKE
LOWER_THRESHOLD = -0.15         # <= -0.15% forward return  -> CRASH

# ----------------------------------------------------------------------
# Model / training settings
# ----------------------------------------------------------------------
MODEL_NAME = "ProsusAI/finbert"
MAX_LEN = 64
BATCH_SIZE = 16
EPOCHS = 4
LEARNING_RATE = 2e-5
NUMERIC_FEATURE_DIM = 5          # headline_len, hour_sin, hour_cos, dow_sin, dow_cos

# ----------------------------------------------------------------------
# Hardware & reproducibility
# ----------------------------------------------------------------------
SEED = 42
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----------------------------------------------------------------------
# Logging
# ----------------------------------------------------------------------
LOG_DIR = "logs"
LOG_FILE_PATH = "logs/training_pipeline.log"
