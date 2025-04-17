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
        "strategy_name": strategy["strategy_name"],
        "description": strategy["description"],
        "entry_price": entry_price,
        "target_price": round(entry_price * (1 + target_pct), 2),
        "stop_price": round(entry_price * (1 - stop_pct), 2),
        "dte": dte,
        "status": "PENDING",
        "notes": "Simulated trade generated from ranked strategy.",
    }

    # Save to trade_log.json
    log_path = Path("data/trade_log.json")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    if log_path.exists():
        with open(log_path, "r") as f:
            log = json.load(f)
    else:
        log = []

    log.append(trade)

    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)

    return trade
