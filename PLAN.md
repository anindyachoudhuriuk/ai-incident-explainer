# Incident Processing Architecture Plan

Live Logs
   ↓
Kafka Stream
   ↓
Sliding Window Engine
   ↓
Incident Detection
   ↓
LLM Reasoning Layer
        ↑
        │
   RAG Context Layer (optional enrichment)
        │
   Runbooks + Docs + Incident History
   ↓
Agent Decision Layer
   ↓
Actions
   ↓
Feedback Loop
