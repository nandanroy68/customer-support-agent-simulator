**🚀 Customer Support Agent Simulator
*Retrieval-Augmented AI Support Agent with Sentiment Analysis, Escalation Logic & Multi-Turn Memory*

*This project is a production-ready GenAI-powered customer support system that uses:

Retrieval-Augmented Generation (RAG)

LangChain
FAISS vector search
FastAPI backend
Redis conversation memory
Sentiment analysis (Transformers)
Escalation triggers
React (Vite) frontend

It simulates a real-world AI support agent capable of answering customer queries using uploaded PDFs, FAQs, and manuals — with human-like empathy and safe fallback behaviors.

**⭐ Features**
**🔍 RAG-Based Question Answering**

Uses FAISS + OpenAI embeddings + LangChain retrieval pipeline to fetch relevant chunks from manuals, FAQs, resumes, etc.

**🧠 Multi-Turn Memory (Redis)**

Every user session maintains context across messages to enable coherent conversation.

**😊 Sentiment-Aware Responses**

Detects:

positive, neutral, negative, frustrated, angry

Adjusts tone automatically based on emotion.

**🚨 Automatic Escalation**

Triggers when:

confidence < threshold

negative/frustrated/angry sentiment

refund/return/complaint keywords appear

**📄 Document Ingestion System**

Upload PDFs, DOCX, TXT, MD → automatically chunked, embedded, and indexed into FAISS.

**💬 Next.js with TypeScript and Tailwind CSS**

Modern chat UI with:

real-time messages

confidence scores

source citations

sentiment badges

escalation warnings

file ingestion page

**🐳 Dockerized Deployment**

docker-compose up --build launches:

API

Redis

Frontend
