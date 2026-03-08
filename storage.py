import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path("orders.json")


def read_orders() -> List[Dict]:

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def write_orders(data: List[Dict]) -> None:

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)