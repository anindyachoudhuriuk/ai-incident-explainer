# AI Incident Explainer — Key Concepts

## Project purpose
- Convert incident logs into structured incident analysis using a local LLM.
- Provide a proof-of-concept pipeline for LLM-driven incident summaries, root cause extraction, and evaluation.

## Core architecture
- `src/main.py`: application entry point.
  - Loads incidents from `data/incident_logs.json`.
  - Reads the latest best model from `outputs/leaderboards/latest.json`.
  - Processes incidents with `src/llms.processor.process_incident()`.
  - Saves final results to `outputs/sample_run.json`.
- `src/evaluate.py`: model evaluation driver.
  - Loads model candidates from `src/config/config.yaml`.
  - Scores each model across all incidents.
  - Writes a leaderboard to `outputs/leaderboards/latest.json`.
- `src/llms/processor.py`: prompt building and response parsing.
  - Loads prompt assets from `src/llms/prompt_loader.py`.
  - Sends each incident prompt to the LLM and returns a normalized result.
- `src/llms/llm_client.py`: Ollama client.
  - Posts prompt payloads to `http://localhost:11434/api/generate`.
  - Validates the response using `src/models/response_models.py`.
- `src/evaluation/`:
  - `evaluator.py` builds evaluation metrics from each output.
  - `scorer.py` converts metrics into a final score.
- `src/models/`:
  - `config_models.py` defines the config model structure.
  - `response_models.py` defines the expected LLM response schema.
  - `evaluation_models.py` defines scoring outputs.
- `src/utils/utils.py`:
  - JSON helpers and leaderboard persistence.
  - Contains `save_versioned_leaderboard()` and `load_latest_leaderboard()`.

## Data and prompts
- `data/incident_logs.json`: sample incident records.
- `src/prompts/system_prompt.txt`: system-level instructions for the LLM.
- `src/prompts/incident_prompt_template.txt`: incident-specific prompt template.

## Configuration
- `src/config/config.yaml` defines:
  - `models`: candidate model list for evaluation.
  - `model.name`: default model name.
  - `llm.temperature`, `llm.max_tokens`, and other request options.
- Current setup uses Ollama locally and a `llama3.2:1b` model.

## Technical notes
- `src/utils/utils.py` currently writes `outputs/sample_run.json` in append mode, which can lead to invalid JSON if the file already exists.
- The LLM response is validated with Pydantic, but the processor still includes placeholder fields such as `summary`.
- The evaluation pipeline is simple and designed for experimentation rather than production-grade scoring.

## Improvement areas
- Replace dummy summary and root cause logic with direct schema extraction.
- Add stronger JSON persistence and file overwrite behavior.
- Extend scoring to support human-in-the-loop validation or LLM-based judges.
- Add unit tests for `src/llms.processor`, prompt loading, and leaderboard selection.

## Current flow
1. Candidate models are evaluated via `src/evaluate.py`.
2. The best model is selected from `outputs/leaderboards/latest.json`.
3. `src/main.py` processes incidents through that best model.
4. Evaluated results are written to `outputs/sample_run.json`.
