from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from backend.utils.file_loader import load_to_text
from backend.utils.chunker import chunk_text
from backend.core.embeddings import get_embed_model
from backend.core.rag_pipeline import RAGPipeline

router = APIRouter()

_embed = get_embed_model()
_rag = RAGPipeline(embed_model=_embed)

@router.post("")
async def ingest(files: List[UploadFile] = File(...)):
    try:
        added = 0
        for f in files:
            raw_bytes = await f.read()
            text = load_to_text(raw_bytes, filename=f.filename)
            chunks = chunk_text(text)
            _rag.add_documents(chunks, metadata={"filename": f.filename})
            added += len(chunks)
        _rag.save_index()
        return {"status": "ok", "chunks_added": added}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

