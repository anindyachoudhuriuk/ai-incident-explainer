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

## Current implementation notes
- `src/evaluate.py` runs model evaluation across candidate models and writes a leaderboard to `outputs/leaderboards/latest.json`.
- `src/main.py` consumes the selected best model and processes incidents into `outputs/sample_run.json`.
- The architecture separates model selection and incident processing, letting evaluation inform the live analysis path.

## Next actions
- Add an LLM judge layer after incident detection to validate, score, or enrich incident summaries and root cause analysis.
- Implement live log classification from the Kafka stream to produce structured log records before incident detection.
- Use the structured logs as input to the LLM reasoning layer, enabling better consistency and more reliable downstream analysis.
- Build drift measurement metrics to monitor model performance and incident output consistency over time.
