from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.chat import router as chat_router
from backend.routers.ingest import router as ingest_router

app = FastAPI(title="Customer Support Agent Simulator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/chat", tags=["chat"])
app.include_router(ingest_router, prefix="/api/ingest", tags=["ingest"])

@app.get("/api/health")
def health():
    return {"status": "ok"}


