import json
from pathlib import Path

PRICING_FILE = Path(__file__).resolve().parent.parent / "data" / "model_pricing.json"


def load_pricing():
    if not PRICING_FILE.exists():
        raise FileNotFoundError(
            f"Pricing file not found: {PRICING_FILE}"
        )

    with open(PRICING_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["models"]


def get_model_pricing(model_id):
    models = load_pricing()

    if model_id not in models:
        raise ValueError(f"Model '{model_id}' not found.")

    return models[model_id]