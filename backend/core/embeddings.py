import os
from langchain_huggingface import HuggingFaceEmbeddings

def get_embed_model():
    # Use free Hugging Face embeddings instead of OpenAI
    model_name = os.environ.get("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},  # Use CPU to avoid GPU requirements
        encode_kwargs={'normalize_embeddings': True}
    )


