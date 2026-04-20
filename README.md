# AI Incident Explainer

A lightweight prototype that converts incident logs into structured incident analysis using a local LLM and a simple evaluation pipeline.

## Quick Start

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Run incident analysis:
   ```bash
   python -m src.main
   ```
3. Run model evaluation and leaderboard generation:
   ```bash
   python -m src.evaluate
   ```

## Repository Layout

```text
ai-incident-explainer/
├── README.md
├── explainer.md
├── PLAN.md
├── requirements.txt
├── data/
│   ├── incident_logs.json
│   └── sample_inputs.txt
├── outputs/
│   ├── sample_run.json
│   └── leaderboards/
│       ├── latest.json
│       └── leaderboard_<timestamp>.json
├── src/
│   ├── main.py
│   ├── evaluate.py
│   ├── config/
│   │   ├── config_loader.py
│   │   └── config.yaml
│   ├── llms/
│   │   ├── llm_client.py
│   │   ├── processor.py
│   │   └── prompt_loader.py
│   ├── evaluation/
│   │   ├── evaluator.py
│   │   ├── metrics.py
│   │   └── scorer.py
│   ├── models/
│   │   ├── config_models.py
│   │   ├── evaluation_models.py
│   │   └── response_models.py
│   └── utils/
│       └── utils.py
└── tests/
    └── test_processor.py
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

