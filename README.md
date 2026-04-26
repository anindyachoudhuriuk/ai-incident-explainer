# AI Incident Explainer

A lightweight prototype that converts incident logs into structured incident analysis using a local LLM and a simple evaluation pipeline.

## Quick Start

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Generate the model leaderboard before analysis (if needed):
   ```bash
   python -m src.evaluate
   ```
3. Run incident analysis:
   ```bash
   python -m src.main
   ```

## Repository Layout

```text
ai-incident-explainer/
├── README.md
├── explainer.md
├── PLAN.md
├── requirements.txt
│
├── data/
│   ├── incident_logs.json
│   ├── sample_inputs.txt
│   └── embeddings_cache.pkl              👈 NEW (performance optimization)
│
├── outputs/
│   ├── sample_run.json
│   └── leaderboards/
│       ├── latest.json
│       └── leaderboard_<timestamp>.json
│
├── review_queue/                          👈 NEW (HITL layer)
│   └── pending_reviews.json
│
├── src/
│   ├── main.py
│   ├── evaluate.py
│
│   ├── config/
│   │   ├── config_loader.py
│   │   └── config.yaml
│
│   ├── llms/
│   │   ├── llm_client.py
│   │   ├── processor.py
│   │   └── prompt_loader.py
│
│   ├── ingestion/                         👈 NEW (log layer)
│   │   ├── log_loader.py
│   │   ├── parser.py
│   │   └── normalizer.py
│
│   ├── classification/                    👈 NEW (routing layer)
│   │   ├── rules.py                       # fast keyword rules
│   │   ├── embeddings.py                  # semantic classification
│   │   ├── router.py                     # decides rules vs embeddings vs LLM
│   │   └── pipeline.py
│
│   ├── evaluation/
│   │   ├── evaluator.py
│   │   ├── metrics.py
│   │   ├── scorer.py
│   │   └── llm_judge.py                   👈 NEW (LLM-as-a-judge)
│
│   ├── benchmarking/                      👈 NEW (model comparison)
│   │   ├── runner.py
│   │   ├── leaderboard.py
│   │   └── experiments.py
│
│   ├── hitl/                              👈 NEW (human-in-the-loop)
│   │   ├── reviewer.py
│   │   ├── labels.py
│   │   └── queue_manager.py
│
│   ├── observability/                     👈 NEW (drift + monitoring)
│   │   ├── drift_detector.py
│   │   ├── metrics_store.py
│   │   └── performance_tracker.py
│
│   ├── models/
│   │   ├── config_models.py
│   │   ├── evaluation_models.py
│   │   ├── response_models.py
│   │   ├── log_models.py                  👈 NEW
│   │   └── classification_models.py       👈 NEW
│
│   └── utils/
│       └── utils.py
│
└── tests/
    ├── test_processor.py
    ├── test_classification.py             👈 NEW
    └── test_evaluation.py                 👈 NEW
```

- `data/incident_logs.json` — sample incident records used by the application.
- `src/main.py` — entry point that processes incidents with the current best model and writes `outputs/sample_run.json`.
- `src/evaluate.py` — evaluates configured models, generates a leaderboard, and writes `outputs/leaderboards/latest.json`.
- `src/config/config_loader.py` — loads model and LLM settings from `src/config/config.yaml`.
- `src/llms/processor.py` — builds prompts and orchestrates per-incident LLM calls.
- `src/llms/llm_client.py` — sends requests to Ollama and validates the LLM response schema.
- `src/llms/prompt_loader.py` — reads the system prompt and incident prompt template.
- `src/evaluation/` — evaluation metrics and scoring logic.
- `src/models/` — Pydantic models for config, response schema, and evaluation metrics.
- `src/utils/utils.py` — JSON loading, saving, and leaderboard persistence helpers.
- `outputs/` — generated outputs, including `sample_run.json` and `leaderboards/`.
- `tests/` — tests for processor behavior.

## What It Does

1. `src/main.py` loads incidents and selects the `best_model` from `outputs/leaderboards/latest.json`.
   - If `latest.json` is missing, run `python -m src.evaluate` first to generate the leaderboard.
2. `src/llms.processor.process_incident()` builds a prompt from `src/prompts/system_prompt.txt` and `src/prompts/incident_prompt_template.txt`.
3. The prompt is sent to Ollama via `src/llms/llm_client.py`.
4. The response is validated against `src/models/response_models.py`.
5. Each result is evaluated with `src/evaluation/evaluator.py` and scored by `src/evaluation/scorer.py`.
6. Results are saved to `outputs/sample_run.json`.

## Configuration

- `src/config/config.yaml` contains the model provider, model name, model list, temperature, token settings, and output options.
- The repository currently targets a local Ollama server at `http://localhost:11434/api/generate`.

## Notes

- The evaluation path is separate: `src/evaluate.py` compares models and populates `outputs/leaderboards/latest.json`.
- `src/utils/utils.py` currently writes `outputs/sample_run.json` using append mode, so repeated runs may require cleaning the file first.
- The prompt and evaluation pipeline are intentionally minimal and can be extended with stronger schema validation, richer scoring, or more robust model selection.
- Next development step: add drift measurement metrics to the evaluation path to detect changes in model performance and output consistency across leaderboard snapshots.

