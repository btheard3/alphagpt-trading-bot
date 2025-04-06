# src/llm/explain_trade.py
import openai
import os
from dotenv import load_dotenv
load_dotenv()


# Set your API key (or load from .env)
openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_calendar_trade(trade: dict):
    prompt = f"""
You are an expert options strategist. Please explain the following calendar spread trade idea to a beginner:

Ticker: {trade['ticker']}
Strategy: {trade['strategy']}
Strike Price: {trade['strike']}
Short Expiration: {trade['short_exp']} @ {trade['short_price']}
Long Expiration: {trade['long_exp']} @ {trade['long_price']}
Net Debit: {trade['net_debit']}

Explain the profit potential, risks, and market conditions this trade works best in.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a trading mentor who explains complex ideas in simple terms."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
