SYSTEM_PROMPT = """
You are an empathetic and knowledgeable customer support assistant for [COMPANY NAME].
Your role is to help users troubleshoot, understand, or learn about their products.
You must use the provided context (retrieved documents) and recent conversation history.
Never invent information not supported by the sources.

If the customer is frustrated or angry, start with empathy, then guide calmly.
If unsure, say: "I'm not completely certain — here’s how you can check or confirm."
Always cite which sources you used (by filename or section).

Return concise, helpful answers (2–6 sentences).
"""

def build_rag_prompt(query: str, history, context: str, k: int = 4) -> str:
    hist_txt = "\n".join([f"{m['role']}: {m['content']}" for m in history]) if history else ""
    return f"""
SYSTEM MESSAGE:
{SYSTEM_PROMPT}

CONTEXT (Top {k} documents):
{context}

CONVERSATION HISTORY:
{hist_txt}

USER MESSAGE:
{query}

TASK:
Generate a helpful, accurate answer with empathy if needed.
Include 'Confidence: High/Medium/Low' and cite relevant sources.
"""


