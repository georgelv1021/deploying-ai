import os
import sys
import requests
from dotenv import load_dotenv

sys.path.append("../../05_src/")
load_dotenv("../../05_src/.secrets")

BASE_URL = "https://api.marketstack.com/v1/eod"


def get_api_key():
    api_key = os.getenv("MARKETSTACK_API_KEY")

    return api_key.strip()


def get_stock_summary(symbol: str = "AAPL") -> str:
    symbol = symbol.upper().strip()

    params = {
        "access_key": get_api_key(),
        "symbols": symbol,
        "sort": "DESC",
        "limit": 1,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return f"Marketstack HTTP {response.status_code}: {data}"

        if "error" in data:
            return f"Marketstack error: {data['error']}"

        results = data.get("data", [])

        if not results:
            return f"No market data found for {symbol}."

        stock = results[0]

        open_price = stock.get("open")
        close_price = stock.get("close")
        high_price = stock.get("high")
        low_price = stock.get("low")
        volume = stock.get("volume")
        date = stock.get("date", "")[:10]

        open_text = f"${open_price:.2f}" if open_price is not None else "N/A"
        close_text = f"${close_price:.2f}" if close_price is not None else "N/A"
        high_text = f"${high_price:.2f}" if high_price is not None else "N/A"
        low_text = f"${low_price:.2f}" if low_price is not None else "N/A"
        volume_text = f"{volume:,}" if volume is not None else "N/A"

        return (
            f"Latest market summary for {symbol}: "
            f"on {date}, it opened at {open_text}, "
            f"reached a high of {high_text}, "
            f"dropped to a low of {low_text}, "
            f"and closed at {close_text}. "
            f"Trading volume was {volume_text} shares."
        )

    except requests.exceptions.SSLError:
        return (
            "SSL certificate error. Your Mac Python certificates are broken. "
            "Try running: /Applications/Python\\ 3*/Install\\ Certificates.command"
        )

    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"
