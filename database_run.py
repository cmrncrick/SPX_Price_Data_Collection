from sqlalchemy import create_engine
from datetime import timedelta
import pandas as pd
import yfinance as yf

from helpers.constants import TICKER, TABLE_TICKER, PERIOD, INTERVALS
from helpers.functions import max_date_existing
from helpers.log_setup import logger

engine = create_engine("sqlite:///SPX_Price_DB.db")

# Creating list of table names
table_names = [f"{TABLE_TICKER}_{interval}" for interval in INTERVALS]

# Merging table names with intervals
table_to_interval = {table_names[i]: INTERVALS[i]
                     for i in range(len(table_names))}

for table_name in table_names:

    max_date = max_date_existing(table_name=table_name, engine=engine)

    i = table_to_interval.get(table_name, None)

    # Download yfinance data with correct interval
    if '1d' in table_name or '1wk' in table_name:
        df = yf.download(tickers=TICKER, period=PERIOD, interval=i)

        df = df.xs(TICKER, axis=1, level="Ticker")
    else:
        df = yf.download(tickers=TICKER, start=pd.to_datetime(
            'today') - timedelta(7), interval=i)
        df = df.xs(TICKER, axis=1, level='Ticker')
        df.index = df.index.tz_convert("America/Chicago")

    # Extracting only new data
    try:
        # Specify that new rows have a date greater than max date
        new_rows = df[df.index > max_date]

        # Send new rows to sql table
        new_rows.to_sql(table_name, engine, if_exists="append")

    except Exception as e:
        logger.error("\n\n***** ERROR *****")
        logger.error(f"Error with {table_name} and interval {i}")
        logger.error(f"{e}\n\n")

    logger.info(
        f"{str(len(new_rows))} have been imported to {table_name}.")
