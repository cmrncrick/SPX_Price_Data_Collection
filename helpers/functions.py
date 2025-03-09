import requests
import pandas as pd
import yfinance as yf

from helpers.config import DISCORD_AUTH, DISCORD_URL


def send_discord_msg(url: str, content: str, auth: dict):
    """
    Send messages to discord channel.

    Args:
        url (str): channel url
        content (str): message to deliver
        auth (dict): username authorization
    """

    payload = {"content": content}

    headers = auth

    res = requests.post(url, payload, headers=headers)


def max_date_existing(table_name: str, engine):
    # Get the max date for each table
    if '1d' in table_name or '1wk' in table_name:
        max_date_query = (f"SELECT MAX(Date) FROM {table_name}")
    else:
        max_date_query = (f"SELECT MAX(Datetime) FROM {table_name}")

    max_date = pd.read_sql(max_date_query, engine).values[0][0]

    return max_date
