import os
import argparse
from typing import List, Tuple
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.embeddings.base import Embeddings
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

INDEX_DIR = os.environ.get("INDEX_DIR", "backend/db")

class RAGPipeline:
    def __init__(self, embed_model: Embeddings):
        self.embed_model = embed_model
        self.vs = None
        self._load_or_init()

    def _load_or_init(self):
        os.makedirs(INDEX_DIR, exist_ok=True)
        try:
            self.vs = FAISS.load_local(INDEX_DIR, self.embed_model, allow_dangerous_deserialization=True)
        except Exception:
            # Create a dummy document to initialize FAISS properly
            from langchain.docstore.document import Document
            dummy_doc = Document(page_content="dummy", metadata={})
            self.vs = FAISS.from_documents([dummy_doc], self.embed_model)

    def save_index(self):
        self.vs.save_local(INDEX_DIR)

    def add_documents(self, chunks: List[Document], metadata: dict):
        docs = []
        for i, d in enumerate(chunks):
            md = {**(d.metadata or {}), **metadata, "section": d.metadata.get("section", f"chunk-{i}")}
            docs.append(Document(page_content=d.page_content, metadata=md))
        self.vs.add_documents(docs)

    def retrieve(self, query: str, top_k: int = 4) -> List[Document]:
        return self.vs.as_retriever(search_kwargs={"k": top_k}).get_relevant_documents(query)

    def generate(self, prompt: str) -> Tuple[str, float]:
        try:
            # Use Ollama with Llama 3.1 (best free model)
            from langchain_community.llms import Ollama
            
            llm = Ollama(
                model="llama3.1:8b",  # Llama 3.1 8B - excellent free model
                base_url="http://localhost:11434"
            )
            
            # Create a more sophisticated prompt for better responses
            system_prompt = """You are a helpful, empathetic customer support agent. 
            Use the provided context to answer questions accurately and helpfully. 
            If you don't know something, say so politely. Be concise but thorough."""
            
            full_prompt = f"{system_prompt}\n\nContext:\n{prompt}\n\nResponse:"
            
            response = llm.invoke(full_prompt)
            confidence = 0.8  # High confidence for local model
            return response.strip(), confidence
            
        except Exception as e:
            # Fallback to simple response if Ollama fails
            response = f"I understand your question. Based on the available information, I'd be happy to help you. (Note: AI model temporarily unavailable - {str(e)})"
            confidence = 0.5
            return response, confidence

def _build_from_data(embed_model: Embeddings, data_root: str = "data"):
    from backend.utils.file_loader import load_path_to_texts
    from backend.utils.chunker import chunk_text
    pipeline = RAGPipeline(embed_model)
    total = 0
    for filepath, text in load_path_to_texts(data_root):
        chunks = chunk_text(text)
        pipeline.add_documents(chunks, metadata={"filename": os.path.basename(filepath)})
        total += len(chunks)
    pipeline.save_index()
    print(f"Built FAISS with {total} chunks from {data_root}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build_index", action="store_true")
    parser.add_argument("--data_root", default="data")
    args = parser.parse_args()

    from backend.core.embeddings import get_embed_model
    embed = get_embed_model()
    if args.build_index:
        _build_from_data(embed, data_root=args.data_root)


