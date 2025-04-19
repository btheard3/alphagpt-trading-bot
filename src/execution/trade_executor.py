import json
from datetime import datetime
from pathlib import Path

def simulate_trade(strategy: dict, ticker: str, entry_price: float, dte: int, target_pct: float, stop_pct: float):
    """
    Simulate a paper trade using the selected strategy and parameters.
    """
    trade = {
        "timestamp": datetime.now().isoformat(),
        "ticker": ticker.upper(),
        "strategy_name": strategy.get("strategy_name", "Unknown Strategy"),
        "description": strategy.get("description", strategy.get("reason", "No description provided")),
        "entry_price": entry_price,
        "dte": dte,
        "target_pct": target_pct,
        "stop_pct": stop_pct,
        "status": "OPEN"
    }

    # Save to trade_log.json
    log_path = Path("data/trade_log.json")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    if log_path.exists():
        with open(log_path, "r") as f:
            try:
                existing = json.load(f)
            except json.JSONDecodeError:
                existing = []
    else:
        existing = []

    existing.append(trade)

    with open(log_path, "w") as f:
        json.dump(existing, f, indent=2)

    print("📥 Trade logged!")
    return trade

