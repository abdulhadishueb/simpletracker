import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "users": [],
            "projects": [],
            "tasks": [],
            "counters": {"user": 0, "project": 0, "task": 0}
        }

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def next_id(data, key):
    data["counters"][key] += 1
    return data["counters"][key]