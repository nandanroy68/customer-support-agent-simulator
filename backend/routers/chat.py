from fastapi import APIRouter, HTTPException
from backend.models.chat_models import ChatRequest, ChatResponse
from backend.core.rag_pipeline import RAGPipeline
from backend.core.memory import RedisMemory
from backend.core.sentiment import SentimentDetector
from backend.core.escalation import should_escalate, detect_keywords
from backend.core.prompt_template import build_rag_prompt
from backend.core.embeddings import get_embed_model
from backend.models.schemas import TurnLog
from backend.utils.logger import write_log

router = APIRouter()

_embed = get_embed_model()
_rag = RAGPipeline(embed_model=_embed)
_memory = RedisMemory()
_sentiment = SentimentDetector()

@router.post("", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        history = _memory.get_recent(req.session_id, k=6)
        senti = _sentiment.analyze(req.message)
        retrieved = _rag.retrieve(req.message, top_k=4)
        context_blocks = []
        sources = []
        for d in retrieved:
            context_blocks.append(f"[{d.metadata.get('filename','unknown')} | section={d.metadata.get('section','')}] {d.page_content}")
            sources.append(d.metadata.get("filename","unknown"))
        prompt = build_rag_prompt(
            query=req.message,
            history=history,
            context="\n\n".join(context_blocks),
            k=4
        )
        answer, model_conf = _rag.generate(prompt)

        if senti.label in ["negative", "angry", "frustrated"]:
            answer = f"I'm really sorry you’re experiencing this. {answer}"

        conf_label = "High" if model_conf >= 0.8 else "Medium" if model_conf >= 0.6 else "Low"

        kw = detect_keywords(req.message)
        escalate = should_escalate(model_conf, senti.label, kw)

        _memory.append(req.session_id, role="user", content=req.message)
        _memory.append(req.session_id, role="assistant", content=answer)

        log_entry = TurnLog(
            session_id=req.session_id,
            user_message=req.message,
            assistant_message=answer,
            model_confidence=model_conf,
            sentiment=senti.label,
            sentiment_score=senti.score,
            sources=list(dict.fromkeys(sources)),
            escalated=escalate
        )
        write_log(log_entry)

        return ChatResponse(
            response=answer,
            confidence=conf_label,
            sources=list(dict.fromkeys(sources)),
            sentiment=senti.label,
            escalated=escalate
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

