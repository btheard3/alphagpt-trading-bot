import json
from datetime import datetime
from pathlib import Path


def log_trade(trade: dict, explanation: str, reflections: dict = None, journal_path: str = "data/journal.json"):

    """
    Logs a trade idea with explanation and optional reflections to a JSON journal.
    Creates the journal file and folder if they don't exist.
    
    Args:
        trade (dict): Dictionary with trade details (ticker, strike, strategy, etc.)
        explanation (str): GPT or human-readable explanation of the trade
        reflections (dict, optional): Mark Douglas-style journaling input
        journal_path (str): Path to the journal file
    """

    # Ensure parent folder exists
    Path(journal_path).parent.mkdir(parents=True, exist_ok=True)

    # Build log entry
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "trade": trade,
        "explanation": explanation,
        "reflections": reflections or {}
    }

    # Load existing journal or start new
    if Path(journal_path).exists():
        with open(journal_path, "r") as f:
            journal = json.load(f)
    else:
        journal = []

    # Add and save entry
    journal.append(entry)

    with open(journal_path, "w") as f:
        json.dump(journal, f, indent=4)

    print(f"✅ Trade logged at {entry['timestamp']}")

