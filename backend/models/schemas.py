from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class RetrievedDoc(BaseModel):
    text: str
    source: str
    section: Optional[str] = None

class TurnLog(BaseModel):
    session_id: str
    user_message: str
    assistant_message: str
    model_confidence: float
    sentiment: str
    sentiment_score: float
    sources: List[str]
    escalated: bool

class IngestResponse(BaseModel):
    status: str
    files_processed: int
    total_chunks: int
    processed_files: List[Dict[str, Any]]
    errors: List[str]


