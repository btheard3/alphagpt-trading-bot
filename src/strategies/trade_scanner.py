# src/strategies/trade_scanner.py

import yfinance as yf
from datetime import datetime, timedelta

def get_options_dates(ticker, days_out=30):
    """
    Fetches upcoming expiration dates within the next `days_out` days.
    """
    stock = yf.Ticker(ticker)
    all_dates = stock.options
    today = datetime.today()

    valid_dates = [
        d for d in all_dates
        if today < datetime.strptime(d, "%Y-%m-%d") <= today + timedelta(days=days_out)
    ]

    return valid_dates

def scan_calendar_spreads(ticker="SPY", days_out=30):
    """
    Finds potential calendar spreads for a given ticker within the next 30 days.
    Returns a list of dictionaries with short/long leg info.
    """
    stock = yf.Ticker(ticker)
    dates = get_options_dates(ticker, days_out)

    if len(dates) < 2:
        print("Not enough expiration dates to build a calendar spread.")
        return []

    short_exp = dates[0]
    long_exp = dates[1]

    short_chain = stock.option_chain(short_exp).calls
    long_chain = stock.option_chain(long_exp).calls

    trade_ideas = []

    # Match strike prices that exist in both chains
    matching_strikes = set(short_chain['strike']).intersection(set(long_chain['strike']))

    for strike in sorted(matching_strikes):
        short_leg = short_chain[short_chain['strike'] == strike].iloc[0]
        long_leg = long_chain[long_chain['strike'] == strike].iloc[0]

        calendar = {
            "ticker": ticker,
            "strategy": "calendar_call",
            "strike": strike,
            "short_exp": short_exp,
            "short_price": short_leg["lastPrice"],
            "long_exp": long_exp,
            "long_price": long_leg["lastPrice"],
            "net_debit": round(long_leg["lastPrice"] - short_leg["lastPrice"], 2)
        }

        trade_ideas.append(calendar)

    return trade_ideas
