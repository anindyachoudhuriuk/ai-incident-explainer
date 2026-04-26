# Incident Processing Architecture Plan

## Vision
Build a lightweight incident explainer that separates:
- model benchmarking and selection,
- live incident reasoning,
- optional human review and observability,
while keeping the hot path fast and cost-aware.

## Target architecture
Live Logs
   ↓
Log Ingestion / Normalization
   ↓
Classification / Routing
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
Evaluation / Judge Layer (model selection + sampled validation)
   ↓
Agent Decision Layer
   ↓
Actions
   ↓
Feedback Loop

## Project structure (aligned with README)
- `README.md` — repository overview, quick start, and layout.
- `requirements.txt` — Python dependency list.
- `data/` — source incident data, sample inputs, and optional embeddings cache.
- `outputs/` — generated sample run outputs and model leaderboards.
- `review_queue/` — HITL queue for pending human review.
- `src/main.py` — runtime entry point for live incident analysis.
- `src/evaluate.py` — benchmarking and leaderboard generation.
- `src/config/` — configuration loader and model settings.
- `src/llms/` — LLM prompt building, client integration, and incident processing.
- `src/ingestion/` — planned log loader, parser, normalizer.
- `src/classification/` — planned routing layer for rules, embeddings, and LLM classification.
- `src/evaluation/` — metrics, scoring, and judge logic.
- `src/benchmarking/` — planned model comparison runner and experiments.
- `src/hitl/` — planned reviewer queue and labeling workflow.
- `src/observability/` — planned drift detection and performance tracking.
- `src/models/` — Pydantic schemas for config, responses, logs, and evaluation.
- `src/utils/` — utility helpers for JSON, leaderboard persistence, and shared helpers.
- `tests/` — unit tests for processor, classification, and evaluation.

## Current implementation notes
- `src/evaluate.py` runs candidate model evaluation and writes `outputs/leaderboards/latest.json`.
- `src/main.py` loads the best model from `outputs/leaderboards/latest.json` and produces `outputs/sample_run.json`.
- `src/llms/processor.py` orchestrates incident prompt creation and LLM calls.
- `src/evaluation/judge.py` and `src/evaluation/evaluator.py` implement the judge layer used in evaluation.
- `src/config/config_loader.py` reads model settings from `src/config/config.yaml`.
- The live path currently executes incident reasoning with the selected best model, while evaluation remains a separate benchmark path.

## Updated plan
### Implemented
- Model benchmarking and leaderboard generation via `src/evaluate.py`.
- Live incident analysis entrypoint in `src/main.py`.
- LLM response orchestration in `src/llms/processor.py`.
- Judge-layer evaluation scoring logic in `src/evaluation/judge.py` and `src/evaluation/evaluator.py`.

### Next actions
- Add log ingestion and normalization in `src/ingestion/` to prepare raw logs for incident detection.
- Build classification/routing in `src/classification/` to select between fast rules, semantic embeddings, or LLM routing.
- Implement drift detection and monitoring in `src/observability/` to track model output consistency over time.
- Add a curated HITL review queue in `review_queue/` and `src/hitl/` for manual validation of edge-case incidents.
- Keep the live path lightweight by using the judge layer for model selection and sampled validation only, avoiding full per-incident post-detection judge calls unless needed for high-risk events.
