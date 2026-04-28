import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.market_api import get_stock_summary


def main():
    print("Testing Marketstack API service...\n")

    symbols = ["AAPL", "TSLA", "MSFT"]

    for symbol in symbols:
        print(f"Testing {symbol}:")
        print(get_stock_summary(symbol))
        print("-" * 60)


if __name__ == "__main__":
    main()