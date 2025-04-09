import os
import pandas as pd
from src.strategies.trade_scanner import scan_calendar_spreads

def load_market_tickers(source="sp500"):
    """
    Loads a list of tickers for 'auto' mode.
    Default = S&P 500 (from CSV or hardcoded fallback)
    """
    default = ["SPY", "AAPL", "TSLA", "NVDA", "QQQ", "MSFT", "GOOGL", "AMZN"]

    try:
        df = pd.read_csv("data/market_tickers.csv")  # Create this file with your list
        return df["ticker"].dropna().unique().tolist()
    except Exception as e:
        print(f"⚠️ Could not load market tickers: {e}\nUsing default list.")
        return default


def get_trade_ideas(tickers="SPY", days_out=30, verbose=True):
    """
    Master scanner function. Supports:
    - Single ticker: string
    - Multiple tickers: list
    - Auto mode: 'auto' (loads tickers from file)
    """
    if isinstance(tickers, str) and tickers.lower() == "auto":
        tickers = load_market_tickers()

    if isinstance(tickers, str):
        tickers = [tickers]

    all_ideas = []

    for t in tickers:
        try:
            ideas = scan_calendar_spreads(t, days_out=days_out)
            if ideas:
                all_ideas.extend(ideas)
                if verbose:
                    print(f"✅ {t}: {len(ideas)} ideas found")
            else:
                if verbose:
                    print(f"⚪ {t}: No ideas")
        except Exception as e:
            print(f"❌ {t}: Failed to scan - {e}")

    print(f"\n📈 Total trade ideas: {len(all_ideas)}")
    return all_ideas
