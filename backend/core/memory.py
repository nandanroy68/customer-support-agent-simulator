import os
import json
import redis
from typing import List, Dict

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

class RedisMemory:
    def __init__(self):
        self.r = redis.from_url(REDIS_URL, decode_responses=True)
        self.ttl = int(os.environ.get("MEMORY_TTL", "86400"))
        self.max_history = int(os.environ.get("MAX_HISTORY", "50"))

    def _key(self, session_id: str) -> str:
        return f"session:{session_id}:history"

    def get_recent(self, session_id: str, k: int = 6) -> List[Dict]:
        items = self.r.lrange(self._key(session_id), -k, -1)
        return [json.loads(i) for i in items] if items else []

    def append(self, session_id: str, role: str, content: str):
        entry = {"role": role, "content": content}
        key = self._key(session_id)
        self.r.rpush(key, json.dumps(entry))
        self.r.ltrim(key, -self.max_history, -1)
        self.r.expire(key, self.ttl)

    def clear_session(self, session_id: str):
        self.r.delete(self._key(session_id))


