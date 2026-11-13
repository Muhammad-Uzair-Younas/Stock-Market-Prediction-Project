"""
Logging setup for the Stock Market Impact Prediction pipeline.

Keep this file in the SAME FOLDER as the notebook and config.py.
The notebook loads it with:  from logger_setup import setup_logger
"""

import os
import logging

import config as cfg


def setup_logger(log_file: str = None):
    """Creates a logger that writes to BOTH the console and a persistent
    log file (logs/training_pipeline.log by default), so every run's
    history is kept on disk, not just printed in the notebook output."""
    log_file = log_file or cfg.LOG_FILE_PATH
    os.makedirs(os.path.dirname(log_file) or ".", exist_ok=True)

    logger = logging.getLogger("StockImpactLogger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if this cell/script is re-run
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Append mode: every run's logs accumulate in the same file
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
