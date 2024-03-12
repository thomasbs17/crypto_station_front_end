from pathlib import Path

import ccxt
import django
import environ
from ccxt import async_support as async_ccxt
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH, verbose=True)
env = environ.Env()
environ.Env.read_env()
HOST = "localhost"
BASE_WS = f"ws://{HOST}:"
BASE_API = "http://127.0.0.1:8000"


def get_api_keys(exchange: str, websocket: bool = False) -> dict:
    try:
        key = env(f"{exchange}_api_key")
        secret = env(f"{exchange}_api_secret")
    except django.core.exceptions.ImproperlyConfigured:
        key = secret = None
    if key and secret:
        if websocket:
            return dict(key_id=key, key_secret=secret)
        else:
            return dict(apiKey=key, secret=secret)


def get_exchange_object(
    exchange: str, async_mode: bool
) -> ccxt.Exchange or async_ccxt.Exchange:
    module = async_ccxt if async_mode else ccxt
    exchange_class = getattr(module, exchange)
    keys = get_api_keys(exchange)
    return exchange_class(keys) if keys else exchange_class()
