import os
import json
from datetime import datetime
from backend.models.schemas import TurnLog

LOG_DIR = os.path.join("backend", "db", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "conversations.jsonl")

def write_log(entry: TurnLog):
    record = entry.dict()
    record["ts"] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


