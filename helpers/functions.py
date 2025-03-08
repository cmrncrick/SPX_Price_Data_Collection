import requests

from log_setup import logger
from config import DISCORD_AUTH, DISCORD_URL


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

