import json
import logging
import os
from logging import config, handlers

# Getting current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(
    current_dir, "log_config.json")
log_dir = os.path.join(current_dir, "Log")

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Setting up logger
logger = logging.getLogger("__name__")


def setup_logger():
    if not os.path.exists(config_file):
        raise FileNotFoundError(
            f"Logging configuration file not found: {config_file}")

    with open(config_file, "r") as f_in:
        config = json.load(f_in)

    # Set log file dynamically
    config["handlers"]["standard"]["filename"] = os.path.join(
        log_dir, "SPX_Database_Log.log")

    logging.config.dictConfig(config)

    logger.info("\n\n--------------------------------------------------\
--------------------------------------------------")

    return logger


# Setup logger
logger = setup_logger()

logger.info("Logger initialized successfully.")
