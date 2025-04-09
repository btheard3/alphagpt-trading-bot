import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rank_trades_with_gpt(strategy_text: str) -> str:
    prompt = f"""
    You are a senior trading strategist. Analyze and rank these options strategies based on:
    1. Profit potential
    2. Fit for a trader who favors calendar spreads
    3. Risk management flexibility

    Return the ranked list and a short explanation for each.

    {strategy_text}
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a trading mentor and strategy optimizer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

