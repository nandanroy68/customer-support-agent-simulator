from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str
    confidence: str
    sources: List[str]
    sentiment: str
    escalated: bool


