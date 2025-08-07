import json
from pathlib import Path
from typing import List, Dict

FILE_PATH = Path("applications.json")

def load_applications() -> List[Dict]:
    if not FILE_PATH.exists():
        return []
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_applications(apps: List[Dict]):
    with open(FILE_PATH, "w") as f:
        json.dump(apps, f, indent=4)

