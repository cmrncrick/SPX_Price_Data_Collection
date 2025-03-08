from sqlalchemy import create_engine
import pandas as pd

from helpers.constants import TICKER, TABLE_TICKER, INTERVALS
from helpers.log_setup import logger

engine = create_engine("sqlite:///SPX_Price_DB.db")

table_names = [f"{TABLE_TICKER}_{interval}" for interval in INTERVALS]

logger.info(table_names)
logger.info(
    "Run without deleting log to see if it will populate existing log from another machine.")
